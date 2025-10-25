import requests
import time
from typing import Dict, List, Optional, Any
import logging

logger = logging.getLogger(__name__)

class PubChemService:
    BASE_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
    RATE_LIMIT = 0.2  # 5 requests per second = 0.2 seconds between requests
    
    def __init__(self):
        self.session = requests.Session()
        self.last_request_time = 0
    
    def _rate_limit(self):
        """Enforce rate limiting."""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.RATE_LIMIT:
            time.sleep(self.RATE_LIMIT - elapsed)
        self.last_request_time = time.time()
    
    def search_compound(self, compound_name: str) -> Optional[int]:
        """Search for compound and return CID."""
        self._rate_limit()
        
        url = f"{self.BASE_URL}/compound/name/{compound_name}/cids/JSON"
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'IdentifierList' in data:
                cid = data['IdentifierList']['CID'][0]
                logger.info(f"Found CID {cid} for {compound_name}")
                return cid
            
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"PubChem API error for {compound_name}: {e}")
            return None
    
    def get_compound_properties(self, cid: int) -> Dict[str, Any]:
        """Get compound properties by CID."""
        self._rate_limit()
        
        url = (f"{self.BASE_URL}/compound/cid/{cid}/"
               f"property/MolecularFormula,MolecularWeight,"
               f"CanonicalSMILES/JSON")
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'PropertyTable' in data:
                props = data['PropertyTable']['Properties'][0]
                return {
                    'cid': props['CID'],
                    'molecular_formula': props.get('MolecularFormula'),
                    'molecular_weight': props.get('MolecularWeight'),
                    'smiles': props.get('CanonicalSMILES')
                }
            
            return {}
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting properties for CID {cid}: {e}")
            return {}
    
    def search_herb_compounds(self, herb_name: str) -> List[Dict[str, Any]]:
        """Search for common compounds in an herb."""
        # For MVP, you might have a hardcoded mapping
        # or use a simple search strategy
        compound_mappings = {
            'ashwagandha': ['withaferin', 'withanolide'],
            'turmeric': ['curcumin'],
            'tulsi': ['eugenol', 'ursolic acid'],
            'ginger': ['gingerol', 'shogaol'],
            'black pepper': ['piperine'],
            'neem': ['azadirachtin', 'nimbin'],
            'amla': ['vitamin c', 'ellagic acid'],
            'brahmi': ['bacosides'],
            'guduchi': ['berberine', 'tinosporin'],
            'cardamom': ['cineole', 'limonene'],
            'cinnamon': ['cinnamaldehyde', 'eugenol'],
            'cumin': ['cuminaldehyde'],
            'coriander': ['linalool'],
            'fennel': ['anethole'],
            'clove': ['eugenol'],
            'garlic': ['allicin'],
            'licorice': ['glycyrrhizin'],
            'saffron': ['crocin', 'crocetin']
        }
        
        herb_lower = herb_name.lower()
        compounds = []
        
        if herb_lower in compound_mappings:
            for compound_name in compound_mappings[herb_lower]:
                cid = self.search_compound(compound_name)
                if cid:
                    props = self.get_compound_properties(cid)
                    props['source_herb'] = herb_name
                    compounds.append(props)
        
        return compounds
    
    def get_compound_synonyms(self, compound_name: str) -> List[str]:
        """Get synonyms for a compound from PubChem."""
        self._rate_limit()
        
        try:
            url = f"{self.BASE_URL}/compound/name/{compound_name}/synonyms/JSON"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'InformationList' in data and 'Information' in data['InformationList']:
                synonyms = data['InformationList']['Information'][0].get('Synonym', [])
                return synonyms[:10]  # Return first 10 synonyms
            
            return []
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching synonyms for {compound_name}: {e}")
            return []
    
    def get_bioactivity_data(self, compound_name: str) -> Dict[str, Any]:
        """Get bioactivity data for a compound (simplified version)."""
        self._rate_limit()
        
        try:
            url = f"{self.BASE_URL}/compound/name/{compound_name}/property/MolecularWeight,LogP/JSON"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'PropertyTable' in data and 'Properties' in data['PropertyTable']:
                properties = data['PropertyTable']['Properties'][0]
                return {
                    'molecular_weight': properties.get('MolecularWeight'),
                    'logp': properties.get('LogP'),
                    'bioactivity_available': True
                }
            
            return {'bioactivity_available': False}
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching bioactivity data for {compound_name}: {e}")
            return {'bioactivity_available': False}
