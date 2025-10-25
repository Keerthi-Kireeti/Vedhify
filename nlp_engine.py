import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Note: spaCy is optional for this demo
nlp = None

# Common Ayurvedic herbs database
AYURVEDIC_HERBS = {
    'turmeric': ['curcumin', 'curcuma longa', 'haldi'],
    'black pepper': ['piper nigrum', 'piperine', 'kali mirch'],
    'ginger': ['zingiber officinale', 'adrak', 'shunthi'],
    'ashwagandha': ['withania somnifera', 'winter cherry'],
    'tulsi': ['ocimum sanctum', 'holy basil', 'basil'],
    'neem': ['azadirachta indica', 'margosa'],
    'amla': ['emblica officinalis', 'indian gooseberry'],
    'brahmi': ['bacopa monnieri', 'water hyssop'],
    'shankhpushpi': ['convolvulus pluricaulis'],
    'guduchi': ['tinospora cordifolia', 'giloy'],
    'triphala': ['three fruits', 'amla', 'haritaki', 'bibhitaki'],
    'haritaki': ['terminalia chebula'],
    'bibhitaki': ['terminalia bellirica'],
    'cardamom': ['elaichi', 'ela'],
    'cinnamon': ['dalchini', 'cinnamomum'],
    'cumin': ['jeera', 'cumin seed'],
    'coriander': ['dhaniya', 'cilantro'],
    'fennel': ['saunf', 'fennel seed'],
    'clove': ['laung', 'syzygium aromaticum'],
    'garlic': ['lahsun', 'allium sativum'],
    'onion': ['pyaz', 'allium cepa'],
    'mustard': ['sarson', 'brassica'],
    'sesame': ['til', 'sesamum indicum'],
    'coconut': ['nariyal', 'cocos nucifera'],
    'mint': ['pudina', 'mentha'],
    'lemongrass': ['lemon grass', 'cymbopogon'],
    'sandalwood': ['chandan', 'santalum'],
    'saffron': ['kesar', 'crocus sativus'],
    'licorice': ['mulethi', 'glycyrrhiza glabra'],
    'aloe vera': ['aloe', 'kumari'],
    'castor oil': ['arandi', 'ricinus communis'],
    'fenugreek': ['methi', 'trigonella foenum-graecum'],
    'jaggery': ['gur', 'unrefined sugar'],
    'honey': ['shahad', 'madhu'],
    'ghee': ['clarified butter', 'ghrit'],
    'milk': ['dudh', 'ksheer'],
    'yogurt': ['dahi', 'curd'],
    'rice': ['chawal', 'oryza sativa'],
    'wheat': ['gehun', 'triticum'],
    'barley': ['jau', 'hordeum vulgare'],
    'mung bean': ['moong', 'vigna radiata'],
    'chickpea': ['chana', 'cicer arietinum'],
    'lentil': ['dal', 'lens culinaris']
}

def find_herbs_in_text(text):
    """
    Extract herb names from text using NLP and pattern matching
    """
    if not text:
        return []
    
    found_herbs = []
    text_lower = text.lower()
    
    # Direct pattern matching for known herbs
    for herb, variations in AYURVEDIC_HERBS.items():
        if herb in text_lower:
            found_herbs.append(herb.title())
        else:
            for variation in variations:
                if variation in text_lower:
                    found_herbs.append(herb.title())
                    break
    
    # Use spaCy for additional entity recognition if available
    if nlp:
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ in ['PLANT', 'ORG', 'PERSON']:  # Plants might be tagged as ORG
                ent_text = ent.text.lower()
                for herb, variations in AYURVEDIC_HERBS.items():
                    if herb in ent_text or any(var in ent_text for var in variations):
                        if herb.title() not in found_herbs:
                            found_herbs.append(herb.title())
    
    # Remove duplicates and return
    return list(set(found_herbs))

def extract_ayurvedic_properties(text):
    """
    Extract Ayurvedic properties like rasa, guna, vipaka, virya from text
    """
    properties = {
        'rasa': [],
        'guna': [],
        'vipaka': [],
        'virya': [],
        'prabhava': []
    }
    
    # Rasa (taste) patterns
    rasa_patterns = {
        'rasa': ['sweet', 'bitter', 'pungent', 'astringent', 'sour', 'salty'],
        'guna': ['heavy', 'light', 'hot', 'cold', 'oily', 'dry', 'smooth', 'rough', 'sharp', 'dull', 'stable', 'mobile', 'soft', 'hard', 'clear', 'cloudy', 'gross', 'subtle'],
        'vipaka': ['sweet', 'sour', 'pungent'],
        'virya': ['hot', 'cold', 'warm', 'cool'],
        'prabhava': ['special action', 'unique effect', 'specific property']
    }
    
    text_lower = text.lower()
    
    for prop_type, patterns in rasa_patterns.items():
        for pattern in patterns:
            if pattern in text_lower:
                properties[prop_type].append(pattern)
    
    return properties

def extract_preparation_methods(text):
    """
    Extract preparation methods from text
    """
    methods = []
    preparation_keywords = [
        'decoction', 'infusion', 'powder', 'paste', 'oil', 'ghee',
        'juice', 'extract', 'tincture', 'tablet', 'capsule', 'syrup',
        'churna', 'kwath', 'avaleha', 'ghrit', 'taila', 'bhasma',
        'rasayana', 'leha', 'gutika', 'vati', 'modaka'
    ]
    
    text_lower = text.lower()
    for method in preparation_keywords:
        if method in text_lower:
            methods.append(method)
    
    return methods

def extract_therapeutic_properties(text):
    """
    Extract therapeutic properties and indications
    """
    therapeutic_keywords = [
        'anti-inflammatory', 'antioxidant', 'antimicrobial', 'antiviral',
        'antibacterial', 'antifungal', 'immunomodulatory', 'adaptogenic',
        'digestive', 'carminative', 'expectorant', 'bronchodilator',
        'hypoglycemic', 'hypolipidemic', 'cardioprotective', 'hepatoprotective',
        'nephroprotective', 'neuroprotective', 'analgesic', 'antipyretic',
        'anti-cancer', 'anti-tumor', 'wound healing', 'anti-aging',
        'memory enhancement', 'cognitive', 'stress relief', 'anxiety',
        'depression', 'sleep', 'insomnia', 'fatigue', 'energy',
        'vitality', 'strength', 'endurance', 'recovery'
    ]
    
    text_lower = text.lower()
    found_properties = []
    
    for prop in therapeutic_keywords:
        if prop in text_lower:
            found_properties.append(prop)
    
    return found_properties
