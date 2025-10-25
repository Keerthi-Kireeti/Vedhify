from typing import Dict, List, Tuple
import re
from knowledge_graph import KNOWLEDGE_GRAPH

def generate_hypothesis(herbs: List[str], ayurvedic_data: Dict, modern_compounds: Dict) -> List[Dict]:
    """
    Generate hypotheses about potential bioactive mechanisms and synergistic combinations
    """
    hypotheses = []
    
    # Hypothesis 1: Modern biochemical synergy
    synergy_hypothesis = find_biochemical_synergies(herbs, modern_compounds)
    if synergy_hypothesis:
        hypotheses.append(synergy_hypothesis)
    
    # Hypothesis 2: Ancient-to-modern correlations
    correlation_hypothesis = find_ancient_modern_correlations(herbs, ayurvedic_data, modern_compounds)
    if correlation_hypothesis:
        hypotheses.append(correlation_hypothesis)
    
    # Hypothesis 3: Dosha-based therapeutic potential
    dosha_hypothesis = analyze_dosha_therapeutic_potential(herbs, ayurvedic_data)
    if dosha_hypothesis:
        hypotheses.append(dosha_hypothesis)
    
    # Hypothesis 4: Rasa-Guna-Virya correlations
    rasa_hypothesis = analyze_rasa_guna_virya_correlations(herbs, ayurvedic_data)
    if rasa_hypothesis:
        hypotheses.append(rasa_hypothesis)
    
    return hypotheses

def find_biochemical_synergies(herbs: List[str], modern_compounds: Dict) -> Dict:
    """
    Find potential biochemical synergies between compounds
    """
    if len(herbs) < 2:
        return None
    
    synergies = []
    
    # Known synergistic combinations
    known_synergies = {
        ('turmeric', 'black pepper'): {
            'mechanism': 'Piperine enhances curcumin bioavailability by inhibiting glucuronidation',
            'evidence': 'Piperine increases curcumin absorption by up to 2000%',
            'clinical_significance': 'Enhanced anti-inflammatory and antioxidant effects'
        },
        ('ginger', 'garlic'): {
            'mechanism': 'Combined anti-inflammatory and cardiovascular protective effects',
            'evidence': 'Synergistic reduction in inflammatory markers',
            'clinical_significance': 'Enhanced cardiovascular and immune system support'
        },
        ('ashwagandha', 'brahmi'): {
            'mechanism': 'Complementary adaptogenic and neuroprotective effects',
            'evidence': 'Enhanced stress reduction and cognitive function',
            'clinical_significance': 'Improved mental clarity and stress resilience'
        }
    }
    
    # Check for known synergies
    herb_combinations = []
    for i in range(len(herbs)):
        for j in range(i+1, len(herbs)):
            herb_combinations.append((herbs[i].lower(), herbs[j].lower()))
    
    for combo in herb_combinations:
        if combo in known_synergies:
            synergies.append({
                'herbs': [combo[0].title(), combo[1].title()],
                'type': 'Known Biochemical Synergy',
                'mechanism': known_synergies[combo]['mechanism'],
                'evidence': known_synergies[combo]['evidence'],
                'clinical_significance': known_synergies[combo]['clinical_significance'],
                'confidence': 'High'
            })
    
    # Analyze compound interactions
    compound_interactions = analyze_compound_interactions(herbs, modern_compounds)
    synergies.extend(compound_interactions)
    
    if synergies:
        return {
            'type': 'Biochemical Synergy Analysis',
            'title': 'Modern Biochemical Synergies Identified',
            'synergies': synergies,
            'summary': f'Found {len(synergies)} potential synergistic interactions between the identified herbs'
        }
    
    return None

def analyze_compound_interactions(herbs: List[str], modern_compounds: Dict) -> List[Dict]:
    """
    Analyze potential interactions between compounds
    """
    interactions = []
    
    # Get all compounds
    all_compounds = []
    for herb, compounds in modern_compounds.items():
        for compound_name in compounds.keys():
            all_compounds.append((herb, compound_name))
    
    # Look for complementary mechanisms
    for i in range(len(all_compounds)):
        for j in range(i+1, len(all_compounds)):
            herb1, compound1 = all_compounds[i]
            herb2, compound2 = all_compounds[j]
            
            if herb1 != herb2:  # Different herbs
                interaction = analyze_compound_pair(compound1, compound2, herb1, herb2)
                if interaction:
                    interactions.append(interaction)
    
    return interactions

def analyze_compound_pair(compound1: str, compound2: str, herb1: str, herb2: str) -> Dict:
    """
    Analyze potential interaction between two compounds
    """
    # Known compound interactions
    compound_interactions = {
        ('curcumin', 'piperine'): {
            'mechanism': 'Bioavailability enhancement',
            'effect': 'Piperine inhibits curcumin metabolism, increasing absorption'
        },
        ('gingerol', 'allicin'): {
            'mechanism': 'Anti-inflammatory synergy',
            'effect': 'Combined COX-2 inhibition and antioxidant activity'
        },
        ('withanolides', 'bacosides'): {
            'mechanism': 'Neuroprotective synergy',
            'effect': 'Complementary stress reduction and cognitive enhancement'
        }
    }
    
    combo = (compound1.lower(), compound2.lower())
    reverse_combo = (compound2.lower(), compound1.lower())
    
    if combo in compound_interactions:
        return {
            'herbs': [herb1.title(), herb2.title()],
            'compounds': [compound1, compound2],
            'type': 'Compound Interaction',
            'mechanism': compound_interactions[combo]['mechanism'],
            'effect': compound_interactions[combo]['effect'],
            'confidence': 'Medium'
        }
    elif reverse_combo in compound_interactions:
        return {
            'herbs': [herb1.title(), herb2.title()],
            'compounds': [compound1, compound2],
            'type': 'Compound Interaction',
            'mechanism': compound_interactions[reverse_combo]['mechanism'],
            'effect': compound_interactions[reverse_combo]['effect'],
            'confidence': 'Medium'
        }
    
    return None

def find_ancient_modern_correlations(herbs: List[str], ayurvedic_data: Dict, modern_compounds: Dict) -> Dict:
    """
    Find correlations between ancient Ayurvedic descriptions and modern biochemical data
    """
    correlations = []
    
    for herb in herbs:
        herb_properties = ayurvedic_data.get(herb, {})
        herb_compounds = modern_compounds.get(herb, {})
        
        if herb_properties and herb_compounds:
            # Analyze rasa-virya correlations
            rasa_correlation = analyze_rasa_modern_correlation(herb, herb_properties, herb_compounds)
            if rasa_correlation:
                correlations.append(rasa_correlation)
            
            # Analyze guna correlations
            guna_correlation = analyze_guna_modern_correlation(herb, herb_properties, herb_compounds)
            if guna_correlation:
                correlations.append(guna_correlation)
            
            # Analyze therapeutic action correlations
            therapeutic_correlation = analyze_therapeutic_correlation(herb, herb_properties, herb_compounds)
            if therapeutic_correlation:
                correlations.append(therapeutic_correlation)
    
    if correlations:
        return {
            'type': 'Ancient-Modern Correlation',
            'title': 'Ancient Ayurvedic Properties Correlate with Modern Science',
            'correlations': correlations,
            'summary': f'Found {len(correlations)} correlations between ancient descriptions and modern biochemical understanding'
        }
    
    return None

def analyze_rasa_modern_correlation(herb: str, properties: Dict, compounds: Dict) -> Dict:
    """
    Analyze correlation between rasa (taste) and modern compounds
    """
    rasa = properties.get('rasa', [])
    if not rasa:
        return None
    
    # Known rasa-compound correlations
    rasa_compound_correlations = {
        'bitter': {
            'compounds': ['alkaloids', 'glycosides', 'terpenoids'],
            'modern_understanding': 'Bitter compounds often have strong pharmacological activity',
            'examples': ['curcumin', 'piperine', 'withanolides']
        },
        'pungent': {
            'compounds': ['volatile oils', 'phenolic compounds'],
            'modern_understanding': 'Pungent compounds often have antimicrobial and digestive properties',
            'examples': ['gingerol', 'piperine', 'eugenol']
        },
        'sweet': {
            'compounds': ['sugars', 'glycosides', 'triterpenes'],
            'modern_understanding': 'Sweet compounds often have nutritive and tonic properties',
            'examples': ['glycyrrhizin', 'saponins']
        }
    }
    
    correlations_found = []
    for taste in rasa:
        if taste in rasa_compound_correlations:
            correlations_found.append({
                'ancient_property': f'{taste} rasa',
                'modern_understanding': rasa_compound_correlations[taste]['modern_understanding'],
                'compounds': rasa_compound_correlations[taste]['compounds'],
                'examples': rasa_compound_correlations[taste]['examples']
            })
    
    if correlations_found:
        return {
            'herb': herb,
            'type': 'Rasa-Modern Correlation',
            'correlations': correlations_found,
            'significance': 'Ancient taste classification correlates with modern phytochemical understanding'
        }
    
    return None

def analyze_guna_modern_correlation(herb: str, properties: Dict, compounds: Dict) -> Dict:
    """
    Analyze correlation between guna (qualities) and modern compounds
    """
    guna = properties.get('guna', [])
    if not guna:
        return None
    
    # Known guna-compound correlations
    guna_correlations = {
        'hot': {
            'modern_understanding': 'Hot guna correlates with compounds that increase metabolism and circulation',
            'compounds': ['capsaicinoids', 'piperine', 'gingerol'],
            'mechanism': 'Thermogenic and vasodilatory effects'
        },
        'cold': {
            'modern_understanding': 'Cold guna correlates with compounds that have cooling and anti-inflammatory effects',
            'compounds': ['menthol', 'camphor', 'eugenol'],
            'mechanism': 'Anti-inflammatory and cooling effects'
        },
        'dry': {
            'modern_understanding': 'Dry guna correlates with compounds that have astringent properties',
            'compounds': ['tannins', 'phenolic compounds'],
            'mechanism': 'Astringent and tissue-drying effects'
        },
        'oily': {
            'modern_understanding': 'Oily guna correlates with lipid-soluble compounds',
            'compounds': ['fatty acids', 'terpenes', 'sterols'],
            'mechanism': 'Lipid-soluble absorption and tissue lubrication'
        }
    }
    
    correlations_found = []
    for quality in guna:
        if quality in guna_correlations:
            correlations_found.append({
                'ancient_property': f'{quality} guna',
                'modern_understanding': guna_correlations[quality]['modern_understanding'],
                'compounds': guna_correlations[quality]['compounds'],
                'mechanism': guna_correlations[quality]['mechanism']
            })
    
    if correlations_found:
        return {
            'herb': herb,
            'type': 'Guna-Modern Correlation',
            'correlations': correlations_found,
            'significance': 'Ancient quality classification correlates with modern pharmacological understanding'
        }
    
    return None

def analyze_therapeutic_correlation(herb: str, properties: Dict, compounds: Dict) -> Dict:
    """
    Analyze correlation between therapeutic actions and modern compounds
    """
    therapeutic_actions = properties.get('therapeutic_actions', [])
    if not therapeutic_actions:
        return None
    
    # Known therapeutic-compound correlations
    therapeutic_correlations = {
        'anti-inflammatory': {
            'modern_compounds': ['curcumin', 'gingerol', 'eugenol', 'ursolic acid'],
            'mechanism': 'COX-2 inhibition, NF-κB pathway modulation',
            'evidence': 'Well-documented anti-inflammatory activity in modern research'
        },
        'antioxidant': {
            'modern_compounds': ['curcumin', 'vitamin C', 'ellagic acid', 'rosmarinic acid'],
            'mechanism': 'Free radical scavenging, antioxidant enzyme induction',
            'evidence': 'Strong antioxidant activity demonstrated in vitro and in vivo'
        },
        'antimicrobial': {
            'modern_compounds': ['allicin', 'eugenol', 'azadirachtin', 'piperine'],
            'mechanism': 'Cell membrane disruption, enzyme inhibition',
            'evidence': 'Broad-spectrum antimicrobial activity against bacteria and fungi'
        },
        'adaptogenic': {
            'modern_compounds': ['withanolides', 'bacosides', 'ginsenosides'],
            'mechanism': 'HPA axis modulation, stress response regulation',
            'evidence': 'Stress-reducing and performance-enhancing effects'
        }
    }
    
    correlations_found = []
    for action in therapeutic_actions:
        if action in therapeutic_correlations:
            correlations_found.append({
                'ancient_action': action,
                'modern_compounds': therapeutic_correlations[action]['modern_compounds'],
                'mechanism': therapeutic_correlations[action]['mechanism'],
                'evidence': therapeutic_correlations[action]['evidence']
            })
    
    if correlations_found:
        return {
            'herb': herb,
            'type': 'Therapeutic-Modern Correlation',
            'correlations': correlations_found,
            'significance': 'Ancient therapeutic descriptions align with modern pharmacological research'
        }
    
    return None

def analyze_dosha_therapeutic_potential(herbs: List[str], ayurvedic_data: Dict) -> Dict:
    """
    Analyze therapeutic potential based on dosha balancing
    """
    dosha_analysis = {}
    
    for herb in herbs:
        herb_properties = ayurvedic_data.get(herb, {})
        if herb_properties and 'dosha' in herb_properties:
            dosha_info = herb_properties['dosha']
            dosha_analysis[herb] = {
                'dosha_effect': dosha_info,
                'therapeutic_potential': analyze_dosha_therapeutic_implications(dosha_info)
            }
    
    if dosha_analysis:
        return {
            'type': 'Dosha-Based Therapeutic Analysis',
            'title': 'Dosha Balancing and Therapeutic Potential',
            'analysis': dosha_analysis,
            'summary': 'Analysis of how herb combinations can balance doshas for optimal health'
        }
    
    return None

def analyze_dosha_therapeutic_implications(dosha_info: str) -> str:
    """
    Analyze therapeutic implications of dosha effects
    """
    dosha_implications = {
        'vata': 'Calming, grounding, stress reduction, nervous system support',
        'pitta': 'Cooling, anti-inflammatory, digestive support, liver health',
        'kapha': 'Stimulating, expectorant, metabolic enhancement, weight management',
        'all three doshas': 'Balancing, rejuvenative, comprehensive health support'
    }
    
    for dosha, implication in dosha_implications.items():
        if dosha in dosha_info.lower():
            return implication
    
    return 'General health support and balance'

def analyze_rasa_guna_virya_correlations(herbs: List[str], ayurvedic_data: Dict) -> Dict:
    """
    Analyze correlations between rasa, guna, and virya
    """
    correlations = []
    
    for herb in herbs:
        herb_properties = ayurvedic_data.get(herb, {})
        if herb_properties:
            rasa = herb_properties.get('rasa', [])
            guna = herb_properties.get('guna', [])
            virya = herb_properties.get('virya', [])
            
            if rasa and guna and virya:
                correlation = analyze_rgv_correlation(herb, rasa, guna, virya)
                if correlation:
                    correlations.append(correlation)
    
    if correlations:
        return {
            'type': 'Rasa-Guna-Virya Analysis',
            'title': 'Traditional Property Correlations',
            'correlations': correlations,
            'summary': 'Analysis of how traditional Ayurvedic properties work together'
        }
    
    return None

def analyze_rgv_correlation(herb: str, rasa: List[str], guna: List[str], virya: List[str]) -> Dict:
    """
    Analyze correlation between rasa, guna, and virya for a specific herb
    """
    # Known RGV correlations
    rgv_patterns = {
        'pungent-hot-sharp': {
            'pattern': ['pungent', 'hot', 'sharp'],
            'significance': 'Strong digestive and metabolic stimulation',
            'therapeutic_potential': 'Digestive disorders, respiratory conditions, circulation'
        },
        'bitter-cold-light': {
            'pattern': ['bitter', 'cold', 'light'],
            'significance': 'Cooling and detoxifying properties',
            'therapeutic_potential': 'Inflammation, fever, detoxification'
        },
        'sweet-heavy-cold': {
            'pattern': ['sweet', 'heavy', 'cold'],
            'significance': 'Nourishing and cooling properties',
            'therapeutic_potential': 'Debility, inflammation, nourishment'
        }
    }
    
    herb_properties = rasa + guna + virya
    
    for pattern_name, pattern_info in rgv_patterns.items():
        pattern_properties = pattern_info['pattern']
        if all(prop in herb_properties for prop in pattern_properties):
            return {
                'herb': herb,
                'pattern': pattern_name,
                'significance': pattern_info['significance'],
                'therapeutic_potential': pattern_info['therapeutic_potential'],
                'confidence': 'High'
            }
    
    return None
