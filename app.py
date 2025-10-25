from flask import Flask, render_template, request, jsonify
import json
import requests
import pandas as pd
import time
from nlp_engine import find_herbs_in_text, extract_ayurvedic_properties
from knowledge_graph import KNOWLEDGE_GRAPH, get_herb_properties
from pubchem_integration import call_pubchem_api, get_fallback_compound_data
from hypothesis_engine import generate_hypothesis

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        text = request.json.get('text', '')
        
        print(f"Analyzing text: {text[:100]}...")
        
        # Step 1: NLP Engine - Extract herbs
        print("Step 1: Running NLP Engine...")
        herbs = find_herbs_in_text(text)
        print(f"Found herbs: {herbs}")
        
        # Step 2: Knowledge Graph - Get Ayurvedic properties
        print("Step 2: Querying Knowledge Graph...")
        ayurvedic_data = {}
        for herb in herbs:
            properties = get_herb_properties(herb)
            if properties:
                ayurvedic_data[herb] = properties
        print(f"Retrieved properties for: {list(ayurvedic_data.keys())}")
        
        # Step 3: PubChem API - Get modern compounds
        print("Step 3: Calling PubChem API...")
        modern_compounds = {}
        for herb in herbs:
            try:
                compounds = call_pubchem_api(herb)
                if compounds:
                    modern_compounds[herb] = compounds
                else:
                    # Use fallback data for demo
                    fallback_data = get_fallback_compound_data(herb)
                    if fallback_data:
                        modern_compounds[herb] = fallback_data
            except Exception as e:
                print(f"Error calling PubChem for {herb}: {e}")
                # Use fallback data
                fallback_data = get_fallback_compound_data(herb)
                if fallback_data:
                    modern_compounds[herb] = fallback_data
        
        print(f"Retrieved compounds for: {list(modern_compounds.keys())}")
        
        # Step 4: Hypothesis Engine - Generate correlations
        print("Step 4: Generating hypotheses...")
        hypotheses = generate_hypothesis(herbs, ayurvedic_data, modern_compounds)
        print(f"Generated {len(hypotheses)} hypotheses")
        
        return jsonify({
            'herbs': herbs,
            'ayurvedic_properties': ayurvedic_data,
            'modern_compounds': modern_compounds,
            'hypotheses': hypotheses,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        })

@app.route('/demo')
def demo():
    """Demo endpoint for testing"""
    demo_text = "Turmeric (Curcuma longa) combined with black pepper (Piper nigrum) enhances bioavailability. The hot property of these herbs aids in digestion and reduces inflammation."
    
    try:
        # Step 1: NLP Engine - Extract herbs
        herbs = find_herbs_in_text(demo_text)
        
        # Step 2: Knowledge Graph - Get Ayurvedic properties
        ayurvedic_data = {}
        for herb in herbs:
            properties = get_herb_properties(herb)
            if properties:
                ayurvedic_data[herb] = properties
        
        # Step 3: PubChem API - Get modern compounds
        modern_compounds = {}
        for herb in herbs:
            fallback_data = get_fallback_compound_data(herb)
            if fallback_data:
                modern_compounds[herb] = fallback_data
        
        # Step 4: Hypothesis Engine - Generate correlations
        hypotheses = generate_hypothesis(herbs, ayurvedic_data, modern_compounds)
        
        return jsonify({
            'text': demo_text,
            'herbs': herbs,
            'ayurvedic_properties': ayurvedic_data,
            'modern_compounds': modern_compounds,
            'hypotheses': hypotheses,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        })

if __name__ == '__main__':
    print("Starting Ayurvedic AI Analyzer...")
    print("Available endpoints:")
    print("- http://localhost:5000/ (Main interface)")
    print("- http://localhost:5000/analyze (Analysis API)")
    print("- http://localhost:5000/demo (Demo data)")
    app.run(debug=True, host='0.0.0.0', port=5000)
