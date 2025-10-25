# Ayurvedic Knowledge Graph
# Maps herbs to their traditional Ayurvedic properties

KNOWLEDGE_GRAPH = {
    'Turmeric': {
        'rasa': ['bitter', 'pungent', 'astringent'],
        'guna': ['light', 'dry', 'sharp'],
        'vipaka': ['pungent'],
        'virya': ['hot'],
        'prabhava': ['anti-inflammatory', 'antioxidant', 'hepatoprotective'],
        'dosha': ['pacifies kapha and pitta'],
        'therapeutic_actions': ['anti-inflammatory', 'antioxidant', 'hepatoprotective', 'wound healing'],
        'modern_compounds': ['curcumin', 'demethoxycurcumin', 'bisdemethoxycurcumin']
    },
    'Black Pepper': {
        'rasa': ['pungent'],
        'guna': ['light', 'dry', 'sharp'],
        'vipaka': ['pungent'],
        'virya': ['hot'],
        'prabhava': ['bioavailability enhancer', 'digestive stimulant'],
        'dosha': ['pacifies kapha and vata'],
        'therapeutic_actions': ['digestive', 'carminative', 'expectorant', 'bioavailability enhancer'],
        'modern_compounds': ['piperine', 'piperidine', 'chavicine']
    },
    'Ginger': {
        'rasa': ['pungent'],
        'guna': ['light', 'dry', 'sharp'],
        'vipaka': ['sweet'],
        'virya': ['hot'],
        'prabhava': ['digestive stimulant', 'anti-nausea'],
        'dosha': ['pacifies kapha and vata'],
        'therapeutic_actions': ['digestive', 'carminative', 'anti-nausea', 'anti-inflammatory'],
        'modern_compounds': ['gingerol', 'shogaol', 'paradol', 'zingiberene']
    },
    'Ashwagandha': {
        'rasa': ['bitter', 'astringent'],
        'guna': ['heavy', 'oily'],
        'vipaka': ['sweet'],
        'virya': ['hot'],
        'prabhava': ['adaptogenic', 'rejuvenative'],
        'dosha': ['pacifies vata and kapha'],
        'therapeutic_actions': ['adaptogenic', 'anti-stress', 'immunomodulatory', 'neuroprotective'],
        'modern_compounds': ['withanolides', 'withaferin A', 'withanoside']
    },
    'Tulsi': {
        'rasa': ['bitter', 'pungent'],
        'guna': ['light', 'dry', 'sharp'],
        'vipaka': ['pungent'],
        'virya': ['hot'],
        'prabhava': ['immunomodulatory', 'antimicrobial'],
        'dosha': ['pacifies kapha and vata'],
        'therapeutic_actions': ['immunomodulatory', 'antimicrobial', 'antioxidant', 'adaptogenic'],
        'modern_compounds': ['eugenol', 'ursolic acid', 'rosmarinic acid', 'caryophyllene']
    },
    'Neem': {
        'rasa': ['bitter'],
        'guna': ['light', 'dry', 'sharp'],
        'vipaka': ['pungent'],
        'virya': ['cold'],
        'prabhava': ['antimicrobial', 'blood purifier'],
        'dosha': ['pacifies pitta and kapha'],
        'therapeutic_actions': ['antimicrobial', 'antifungal', 'blood purifier', 'anti-inflammatory'],
        'modern_compounds': ['azadirachtin', 'nimbin', 'nimbidin', 'quercetin']
    },
    'Amla': {
        'rasa': ['sour', 'bitter', 'astringent', 'sweet', 'pungent'],
        'guna': ['heavy', 'dry'],
        'vipaka': ['sweet'],
        'virya': ['cold'],
        'prabhava': ['rejuvenative', 'antioxidant'],
        'dosha': ['pacifies all three doshas'],
        'therapeutic_actions': ['antioxidant', 'rejuvenative', 'immunomodulatory', 'hepatoprotective'],
        'modern_compounds': ['vitamin C', 'ellagic acid', 'gallic acid', 'emblicanin']
    },
    'Brahmi': {
        'rasa': ['bitter'],
        'guna': ['light', 'dry'],
        'vipaka': ['sweet'],
        'virya': ['cold'],
        'prabhava': ['memory enhancer', 'nervine tonic'],
        'dosha': ['pacifies pitta and kapha'],
        'therapeutic_actions': ['memory enhancement', 'neuroprotective', 'anxiolytic', 'adaptogenic'],
        'modern_compounds': ['bacosides', 'bacopaside', 'bacosaponin']
    },
    'Shankhpushpi': {
        'rasa': ['bitter', 'astringent'],
        'guna': ['light', 'dry'],
        'vipaka': ['sweet'],
        'virya': ['cold'],
        'prabhava': ['memory enhancer', 'nervine tonic'],
        'dosha': ['pacifies pitta and kapha'],
        'therapeutic_actions': ['memory enhancement', 'neuroprotective', 'anxiolytic', 'cognitive'],
        'modern_compounds': ['scopoletin', 'scopolin', 'convolvulin']
    },
    'Guduchi': {
        'rasa': ['bitter', 'astringent'],
        'guna': ['heavy', 'dry'],
        'vipaka': ['sweet'],
        'virya': ['hot'],
        'prabhava': ['immunomodulatory', 'rejuvenative'],
        'dosha': ['pacifies all three doshas'],
        'therapeutic_actions': ['immunomodulatory', 'antipyretic', 'hepatoprotective', 'antioxidant'],
        'modern_compounds': ['berberine', 'tinosporin', 'cordioside', 'tinosporaside']
    },
    'Triphala': {
        'rasa': ['sour', 'bitter', 'astringent', 'sweet', 'pungent'],
        'guna': ['heavy', 'dry'],
        'vipaka': ['sweet'],
        'virya': ['cold'],
        'prabhava': ['rejuvenative', 'digestive'],
        'dosha': ['pacifies all three doshas'],
        'therapeutic_actions': ['rejuvenative', 'digestive', 'antioxidant', 'immunomodulatory'],
        'modern_compounds': ['vitamin C', 'ellagic acid', 'gallic acid', 'chebulinic acid']
    },
    'Cardamom': {
        'rasa': ['pungent', 'sweet'],
        'guna': ['light', 'dry', 'sharp'],
        'vipaka': ['sweet'],
        'virya': ['cold'],
        'prabhava': ['digestive stimulant', 'carminative'],
        'dosha': ['pacifies kapha and vata'],
        'therapeutic_actions': ['digestive', 'carminative', 'expectorant', 'antimicrobial'],
        'modern_compounds': ['cineole', 'limonene', 'terpinolene', 'alpha-terpineol']
    },
    'Cinnamon': {
        'rasa': ['pungent', 'sweet', 'bitter'],
        'guna': ['heavy', 'dry', 'sharp'],
        'vipaka': ['sweet'],
        'virya': ['hot'],
        'prabhava': ['digestive stimulant', 'warming'],
        'dosha': ['pacifies kapha and vata'],
        'therapeutic_actions': ['digestive', 'warming', 'antimicrobial', 'hypoglycemic'],
        'modern_compounds': ['cinnamaldehyde', 'eugenol', 'cinnamyl acetate', 'coumarin']
    },
    'Cumin': {
        'rasa': ['pungent', 'bitter'],
        'guna': ['light', 'dry', 'sharp'],
        'vipaka': ['pungent'],
        'virya': ['hot'],
        'prabhava': ['digestive stimulant', 'carminative'],
        'dosha': ['pacifies kapha and vata'],
        'therapeutic_actions': ['digestive', 'carminative', 'antimicrobial', 'antioxidant'],
        'modern_compounds': ['cuminaldehyde', 'cuminol', 'p-cymene', 'terpinene']
    },
    'Coriander': {
        'rasa': ['sweet', 'bitter', 'pungent'],
        'guna': ['light', 'dry'],
        'vipaka': ['sweet'],
        'virya': ['cold'],
        'prabhava': ['digestive', 'cooling'],
        'dosha': ['pacifies pitta'],
        'therapeutic_actions': ['digestive', 'cooling', 'antimicrobial', 'antioxidant'],
        'modern_compounds': ['linalool', 'geraniol', 'borneol', 'camphor']
    },
    'Fennel': {
        'rasa': ['sweet', 'pungent'],
        'guna': ['light', 'dry', 'sharp'],
        'vipaka': ['sweet'],
        'virya': ['cold'],
        'prabhava': ['digestive', 'carminative'],
        'dosha': ['pacifies kapha and pitta'],
        'therapeutic_actions': ['digestive', 'carminative', 'expectorant', 'antimicrobial'],
        'modern_compounds': ['anethole', 'fenchone', 'estragole', 'limonene']
    },
    'Clove': {
        'rasa': ['pungent', 'bitter'],
        'guna': ['light', 'dry', 'sharp'],
        'vipaka': ['pungent'],
        'virya': ['hot'],
        'prabhava': ['antimicrobial', 'analgesic'],
        'dosha': ['pacifies kapha and vata'],
        'therapeutic_actions': ['antimicrobial', 'analgesic', 'carminative', 'expectorant'],
        'modern_compounds': ['eugenol', 'eugenyl acetate', 'caryophyllene', 'alpha-humulene']
    },
    'Garlic': {
        'rasa': ['pungent'],
        'guna': ['heavy', 'oily', 'sharp'],
        'vipaka': ['sweet'],
        'virya': ['hot'],
        'prabhava': ['antimicrobial', 'cardioprotective'],
        'dosha': ['pacifies kapha and vata'],
        'therapeutic_actions': ['antimicrobial', 'cardioprotective', 'hypolipidemic', 'immunomodulatory'],
        'modern_compounds': ['allicin', 'diallyl disulfide', 'ajoene', 's-allyl cysteine']
    },
    'Licorice': {
        'rasa': ['sweet', 'bitter'],
        'guna': ['heavy', 'oily', 'smooth'],
        'vipaka': ['sweet'],
        'virya': ['cold'],
        'prabhava': ['demulcent', 'expectorant'],
        'dosha': ['pacifies pitta and vata'],
        'therapeutic_actions': ['demulcent', 'expectorant', 'anti-inflammatory', 'hepatoprotective'],
        'modern_compounds': ['glycyrrhizin', 'glycyrrhetinic acid', 'liquiritin', 'glabridin']
    },
    'Saffron': {
        'rasa': ['bitter', 'pungent'],
        'guna': ['light', 'dry', 'sharp'],
        'vipaka': ['sweet'],
        'virya': ['hot'],
        'prabhava': ['rejuvenative', 'antidepressant'],
        'dosha': ['pacifies kapha and vata'],
        'therapeutic_actions': ['rejuvenative', 'antidepressant', 'antioxidant', 'neuroprotective'],
        'modern_compounds': ['crocin', 'crocetin', 'safranal', 'picrocrocin']
    }
}

def get_herb_properties(herb_name):
    """
    Get Ayurvedic properties for a given herb
    """
    herb_key = herb_name.title()
    return KNOWLEDGE_GRAPH.get(herb_key, None)

def get_all_herbs():
    """
    Get list of all herbs in the knowledge graph
    """
    return list(KNOWLEDGE_GRAPH.keys())

def search_herbs_by_property(property_type, property_value):
    """
    Search herbs by specific Ayurvedic property
    """
    matching_herbs = []
    for herb, properties in KNOWLEDGE_GRAPH.items():
        if property_type in properties and property_value in properties[property_type]:
            matching_herbs.append(herb)
    return matching_herbs

def get_herbs_by_dosha(dosha):
    """
    Get herbs that pacify a specific dosha
    """
    matching_herbs = []
    for herb, properties in KNOWLEDGE_GRAPH.items():
        if 'dosha' in properties and dosha.lower() in properties['dosha'].lower():
            matching_herbs.append(herb)
    return matching_herbs

def get_synergistic_herbs(herb_name):
    """
    Get herbs that work synergistically with the given herb
    """
    herb_properties = get_herb_properties(herb_name)
    if not herb_properties:
        return []
    
    synergistic = []
    herb_dosha = herb_properties.get('dosha', '')
    
    for other_herb, properties in KNOWLEDGE_GRAPH.items():
        if other_herb != herb_name:
            other_dosha = properties.get('dosha', '')
            # Herbs that pacify similar doshas often work synergistically
            if herb_dosha and other_dosha and any(d in other_dosha for d in herb_dosha.split()):
                synergistic.append(other_herb)
    
    return synergistic[:5]  # Return top 5 synergistic herbs
