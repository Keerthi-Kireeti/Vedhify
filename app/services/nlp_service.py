from typing import List, Dict, Any
import re
import logging

logger = logging.getLogger(__name__)

class AyurvedicNLPService:
    def __init__(self):
        """Initialize Ayurvedic patterns (spaCy optional)."""
        try:
            import spacy
            self.nlp = spacy.load("en_core_web_sm")
            logger.info("spaCy model loaded successfully")
        except Exception as e:
            logger.warning(f"spaCy not available, using fallback NLP: {e}")
            self.nlp = None
        
        self._init_ayurvedic_patterns()
    
    def _init_ayurvedic_patterns(self):
        """Define regex patterns for Ayurvedic properties."""
        self.rasa_patterns = {
            'madhura': r'\b(sweet|madhura)\b',
            'amla': r'\b(sour|amla)\b',
            'lavana': r'\b(salty|lavana)\b',
            'katu': r'\b(pungent|katu)\b',
            'tikta': r'\b(bitter|tikta)\b',
            'kashaya': r'\b(astringent|kashaya)\b'
        }
        
        self.virya_patterns = {
            'ushna': r'\b(hot|heating|ushna)\b',
            'shita': r'\b(cold|cooling|shita)\b'
        }
        
        self.guna_patterns = {
            'guru': r'\b(heavy|guru)\b',
            'laghu': r'\b(light|laghu)\b',
            'snigdha': r'\b(oily|snigdha)\b',
            'ruksha': r'\b(dry|ruksha)\b',
            'tiksna': r'\b(sharp|tiksna)\b',
            'manda': r'\b(dull|manda)\b',
            'sita': r'\b(cold|sita)\b',
            'ushna': r'\b(hot|ushna)\b'
        }
    
    def extract_herbs(self, text: str) -> List[Dict[str, Any]]:
        """Extract herb names and their properties from text."""
        herbs = []
        
        # Use spaCy if available
        if self.nlp:
            doc = self.nlp(text)
            # Extract entities that might be herbs
            for ent in doc.ents:
                if ent.label_ in ['PRODUCT', 'SUBSTANCE', 'ORG']:  # Adjust labels
                    herb_info = {
                        'name': ent.text,
                        'rasa': self._extract_rasa(text, ent.text),
                        'virya': self._extract_virya(text, ent.text),
                        'guna': self._extract_guna(text, ent.text)
                    }
                    herbs.append(herb_info)
        
        # Also check for known Ayurvedic herbs using pattern matching
        known_herbs = self._extract_known_herbs(text)
        for herb in known_herbs:
            if not any(h['name'].lower() == herb.lower() for h in herbs):
                herb_info = {
                    'name': herb,
                    'rasa': self._extract_rasa(text, herb),
                    'virya': self._extract_virya(text, herb),
                    'guna': self._extract_guna(text, herb)
                }
                herbs.append(herb_info)
        
        return herbs
    
    def _extract_known_herbs(self, text: str) -> List[str]:
        """Extract known Ayurvedic herbs from text."""
        known_herbs = [
            'turmeric', 'curcumin', 'curcuma longa', 'haldi',
            'black pepper', 'piper nigrum', 'piperine', 'kali mirch',
            'ginger', 'zingiber officinale', 'adrak', 'shunthi',
            'ashwagandha', 'withania somnifera', 'winter cherry',
            'tulsi', 'ocimum sanctum', 'holy basil', 'basil',
            'neem', 'azadirachta indica', 'margosa',
            'amla', 'emblica officinalis', 'indian gooseberry',
            'brahmi', 'bacopa monnieri', 'water hyssop',
            'shankhpushpi', 'convolvulus pluricaulis',
            'guduchi', 'tinospora cordifolia', 'giloy',
            'triphala', 'haritaki', 'terminalia chebula',
            'bibhitaki', 'terminalia bellirica',
            'cardamom', 'elaichi', 'ela',
            'cinnamon', 'dalchini', 'cinnamomum',
            'cumin', 'jeera', 'cumin seed',
            'coriander', 'dhaniya', 'cilantro',
            'fennel', 'saunf', 'fennel seed',
            'clove', 'laung', 'syzygium aromaticum',
            'garlic', 'lahsun', 'allium sativum',
            'onion', 'pyaz', 'allium cepa',
            'mustard', 'sarson', 'brassica',
            'sesame', 'til', 'sesamum indicum',
            'coconut', 'nariyal', 'cocos nucifera',
            'mint', 'pudina', 'mentha',
            'lemongrass', 'lemon grass', 'cymbopogon',
            'sandalwood', 'chandan', 'santalum',
            'saffron', 'kesar', 'crocus sativus',
            'licorice', 'mulethi', 'glycyrrhiza glabra',
            'aloe vera', 'aloe', 'kumari',
            'castor oil', 'arandi', 'ricinus communis',
            'fenugreek', 'methi', 'trigonella foenum-graecum'
        ]
        
        found_herbs = []
        text_lower = text.lower()
        
        for herb in known_herbs:
            if herb in text_lower:
                # Find the original case version
                pattern = re.compile(re.escape(herb), re.IGNORECASE)
                match = pattern.search(text)
                if match:
                    found_herbs.append(match.group())
        
        return list(set(found_herbs))
    
    def _extract_rasa(self, text: str, herb_name: str) -> List[str]:
        """Extract rasa (taste) properties near herb mention."""
        # Simple context window approach
        rasas = []
        for rasa, pattern in self.rasa_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                rasas.append(rasa)
        return rasas
    
    def _extract_virya(self, text: str, herb_name: str) -> str:
        """Extract virya (potency) property."""
        for virya, pattern in self.virya_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                return virya
        return 'unknown'
    
    def _extract_guna(self, text: str, herb_name: str) -> List[str]:
        """Extract guna (qualities) properties."""
        gunas = []
        for guna, pattern in self.guna_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                gunas.append(guna)
        return gunas
    
    def extract_ayurvedic_properties(self, text: str) -> Dict[str, List[str]]:
        """Extract all Ayurvedic properties from text."""
        properties = {
            'rasa': [],
            'guna': [],
            'vipaka': [],
            'virya': [],
            'prabhava': []
        }
        
        # Extract rasa
        for rasa, pattern in self.rasa_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                properties['rasa'].append(rasa)
        
        # Extract guna
        for guna, pattern in self.guna_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                properties['guna'].append(guna)
        
        # Extract virya
        for virya, pattern in self.virya_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                properties['virya'].append(virya)
        
        return properties
