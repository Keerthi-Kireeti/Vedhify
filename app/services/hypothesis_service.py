from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

class HypothesisEngine:
    def __init__(self):
        """Initialize rule-based hypothesis engine."""
        self._init_rules()
    
    def _init_rules(self):
        """Define simple correlation rules."""
        self.ayurveda_modern_mapping = {
            'tikta': {  # Bitter taste
                'likely_properties': ['anti-inflammatory', 'antimicrobial'],
                'mechanism': 'Bitter compounds often contain alkaloids and polyphenols'
            },
            'ushna': {  # Heating potency
                'likely_properties': ['metabolism-enhancing', 'circulation-improving'],
                'mechanism': 'Heating herbs typically contain thermogenic compounds'
            },
            'kashaya': {  # Astringent taste
                'likely_properties': ['antioxidant', 'wound-healing'],
                'mechanism': 'Astringent taste indicates presence of tannins'
            },
            'madhura': {  # Sweet taste
                'likely_properties': ['nutritive', 'tonic'],
                'mechanism': 'Sweet compounds often have nutritive and tonic properties'
            },
            'katu': {  # Pungent taste
                'likely_properties': ['digestive', 'antimicrobial'],
                'mechanism': 'Pungent compounds often have digestive and antimicrobial properties'
            },
            'amla': {  # Sour taste
                'likely_properties': ['antioxidant', 'digestive'],
                'mechanism': 'Sour compounds often contain organic acids with antioxidant properties'
            }
        }
        
        self.guna_modern_mapping = {
            'guru': {  # Heavy quality
                'likely_properties': ['nourishing', 'grounding'],
                'mechanism': 'Heavy compounds often have nutritive and grounding effects'
            },
            'laghu': {  # Light quality
                'likely_properties': ['digestive', 'metabolic'],
                'mechanism': 'Light compounds often enhance digestion and metabolism'
            },
            'snigdha': {  # Oily quality
                'likely_properties': ['lubricating', 'nourishing'],
                'mechanism': 'Oily compounds often provide lubrication and nourishment'
            },
            'ruksha': {  # Dry quality
                'likely_properties': ['astringent', 'absorbing'],
                'mechanism': 'Dry compounds often have astringent and absorbing properties'
            },
            'tiksna': {  # Sharp quality
                'likely_properties': ['penetrating', 'stimulating'],
                'mechanism': 'Sharp compounds often have penetrating and stimulating effects'
            },
            'manda': {  # Dull quality
                'likely_properties': ['calming', 'soothing'],
                'mechanism': 'Dull compounds often have calming and soothing effects'
            }
        }
    
    def generate_hypotheses(self, herb_data: Dict[str, Any],
                           compound_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate hypotheses linking Ayurvedic properties to compounds."""
        hypotheses = []
        
        herb_name = herb_data.get('name', 'Unknown')
        rasas = herb_data.get('rasa', [])
        gunas = herb_data.get('guna', [])
        virya = herb_data.get('virya', 'unknown')
        
        # Generate hypotheses based on rasa
        for rasa in rasas:
            if rasa in self.ayurveda_modern_mapping:
                mapping = self.ayurveda_modern_mapping[rasa]
                
                hypothesis = {
                    'herb': herb_name,
                    'ayurvedic_property': f"Rasa: {rasa}",
                    'predicted_bioactivity': mapping['likely_properties'],
                    'mechanism': mapping['mechanism'],
                    'confidence': 'medium',
                    'compounds_found': len(compound_data)
                }
                hypotheses.append(hypothesis)
        
        # Generate hypotheses based on guna
        for guna in gunas:
            if guna in self.guna_modern_mapping:
                mapping = self.guna_modern_mapping[guna]
                
                hypothesis = {
                    'herb': herb_name,
                    'ayurvedic_property': f"Guna: {guna}",
                    'predicted_bioactivity': mapping['likely_properties'],
                    'mechanism': mapping['mechanism'],
                    'confidence': 'medium',
                    'compounds_found': len(compound_data)
                }
                hypotheses.append(hypothesis)
        
        # Generate hypothesis based on virya
        if virya in self.ayurveda_modern_mapping:
            mapping = self.ayurveda_modern_mapping[virya]
            
            hypothesis = {
                'herb': herb_name,
                'ayurvedic_property': f"Virya: {virya}",
                'predicted_bioactivity': mapping['likely_properties'],
                'mechanism': mapping['mechanism'],
                'confidence': 'medium',
                'compounds_found': len(compound_data)
            }
            hypotheses.append(hypothesis)
        
        # Add compound-specific insights
        if compound_data:
            hypothesis = {
                'herb': herb_name,
                'type': 'phytochemical_analysis',
                'message': f"Identified {len(compound_data)} bioactive compounds",
                'compounds': [c.get('molecular_formula', 'Unknown') 
                            for c in compound_data[:3]],
                'confidence': 'high'
            }
            hypotheses.append(hypothesis)
        
        # Generate synergy hypotheses if multiple herbs
        if len(compound_data) > 1:
            synergy_hypothesis = self._generate_synergy_hypothesis(herb_name, compound_data)
            if synergy_hypothesis:
                hypotheses.append(synergy_hypothesis)
        
        return hypotheses
    
    def _generate_synergy_hypothesis(self, herb_name: str, compound_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate synergy hypothesis for multiple compounds."""
        if len(compound_data) < 2:
            return None
        
        # Known synergistic combinations
        known_synergies = {
            ('curcumin', 'piperine'): {
                'mechanism': 'Piperine enhances curcumin bioavailability by inhibiting glucuronidation',
                'evidence': 'Piperine increases curcumin absorption by up to 2000%',
                'clinical_significance': 'Enhanced anti-inflammatory and antioxidant effects'
            },
            ('gingerol', 'allicin'): {
                'mechanism': 'Combined anti-inflammatory and cardiovascular protective effects',
                'evidence': 'Synergistic reduction in inflammatory markers',
                'clinical_significance': 'Enhanced cardiovascular and immune system support'
            },
            ('withanolides', 'bacosides'): {
                'mechanism': 'Complementary adaptogenic and neuroprotective effects',
                'evidence': 'Enhanced stress reduction and cognitive function',
                'clinical_significance': 'Improved mental clarity and stress resilience'
            }
        }
        
        # Check for known synergies
        compound_names = [c.get('molecular_formula', '').lower() for c in compound_data]
        
        for combo, synergy_info in known_synergies.items():
            if all(any(comp in name for name in compound_names) for comp in combo):
                return {
                    'herb': herb_name,
                    'type': 'synergy_analysis',
                    'title': 'Compound Synergy Identified',
                    'compounds': list(combo),
                    'mechanism': synergy_info['mechanism'],
                    'evidence': synergy_info['evidence'],
                    'clinical_significance': synergy_info['clinical_significance'],
                    'confidence': 'high'
                }
        
        # Generic synergy hypothesis
        return {
            'herb': herb_name,
            'type': 'synergy_analysis',
            'title': 'Potential Compound Synergy',
            'message': f"Multiple bioactive compounds identified that may work synergistically",
            'compounds': [c.get('molecular_formula', 'Unknown') for c in compound_data[:3]],
            'confidence': 'medium'
        }
