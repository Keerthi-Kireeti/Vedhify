from flask import Blueprint, request, jsonify
from app.services.nlp_service import AyurvedicNLPService
from app.services.kg_service import KnowledgeGraphService
from app.services.pubchem_service import PubChemService
from app.services.hypothesis_service import HypothesisEngine
from app.config import Config
import logging

logger = logging.getLogger(__name__)

api_bp = Blueprint('api', __name__)

# Initialize services
nlp_service = AyurvedicNLPService()
kg_service = KnowledgeGraphService(
    Config.NEO4J_URI,
    Config.NEO4J_USER,
    Config.NEO4J_PASSWORD
)
pubchem_service = PubChemService()
hypothesis_engine = HypothesisEngine()

@api_bp.route('/analyze', methods=['POST'])
def analyze_text():
    """Analyze Ayurvedic text and generate insights."""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Step 1: Extract herbs using NLP
        herbs = nlp_service.extract_herbs(text)
        logger.info(f"Extracted {len(herbs)} herbs")
        
        results = []
        
        for herb in herbs:
            herb_name = herb['name']
            
            # Step 2: Add to knowledge graph
            kg_service.add_herb(herb_name, {
                'rasa': ','.join(herb.get('rasa', [])),
                'virya': herb.get('virya', 'unknown'),
                'guna': ','.join(herb.get('guna', []))
            })
            
            # Add properties to graph
            for rasa in herb.get('rasa', []):
                kg_service.add_rasa_property(herb_name, rasa)
            
            for guna in herb.get('guna', []):
                kg_service.add_guna_property(herb_name, guna)
            
            if herb.get('virya') != 'unknown':
                kg_service.add_virya_property(herb_name, herb['virya'])
            
            # Step 3: Search PubChem for compounds
            compounds = pubchem_service.search_herb_compounds(herb_name)
            
            # Step 4: Link compounds to graph
            for compound in compounds:
                if 'cid' in compound:
                    kg_service.link_herb_to_compound(
                        herb_name,
                        compound['cid'],
                        compound.get('molecular_formula', 'Unknown')
                    )
            
            # Step 5: Generate hypotheses
            hypotheses = hypothesis_engine.generate_hypotheses(herb, compounds)
            
            results.append({
                'herb': herb,
                'compounds': compounds,
                'hypotheses': hypotheses
            })
        
        return jsonify({
            'success': True,
            'results': results
        }), 200
        
    except Exception as e:
        logger.error(f"Error analyzing text: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500

@api_bp.route('/graph/<herb_name>', methods=['GET'])
def get_herb_graph(herb_name):
    """Get knowledge graph for a specific herb."""
    try:
        graph_data = kg_service.get_herb_graph(herb_name)
        return jsonify(graph_data), 200
    except Exception as e:
        logger.error(f"Error fetching graph: {e}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/herbs', methods=['GET'])
def get_all_herbs():
    """Get all herbs in the knowledge graph."""
    try:
        herbs = kg_service.get_all_herbs()
        return jsonify({'herbs': herbs}), 200
    except Exception as e:
        logger.error(f"Error fetching herbs: {e}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/search', methods=['GET'])
def search_herbs():
    """Search herbs by property."""
    try:
        property_type = request.args.get('property_type')
        property_value = request.args.get('property_value')
        
        if not property_type or not property_value:
            return jsonify({'error': 'property_type and property_value required'}), 400
        
        herbs = kg_service.search_herbs_by_property(property_type, property_value)
        return jsonify({'herbs': herbs}), 200
    except Exception as e:
        logger.error(f"Error searching herbs: {e}")
        return jsonify({'error': str(e)}), 500

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'}), 200
