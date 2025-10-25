import requests
import json
import time
from typing import Dict, List, Optional

# PubChem API base URL
PUBCHEM_BASE_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

# Known compound mappings for common herbs
HERB_COMPOUND_MAPPING = {
    'turmeric': ['curcumin', 'demethoxycurcumin', 'bisdemethoxycurcumin'],
    'black pepper': ['piperine', 'piperidine', 'chavicine'],
    'ginger': ['gingerol', 'shogaol', 'paradol', 'zingiberene'],
    'ashwagandha': ['withanolides', 'withaferin A', 'withanoside'],
    'tulsi': ['eugenol', 'ursolic acid', 'rosmarinic acid', 'caryophyllene'],
    'neem': ['azadirachtin', 'nimbin', 'nimbidin', 'quercetin'],
    'amla': ['vitamin C', 'ellagic acid', 'gallic acid', 'emblicanin'],
    'brahmi': ['bacosides', 'bacopaside', 'bacosaponin'],
    'guduchi': ['berberine', 'tinosporin', 'cordioside', 'tinosporaside'],
    'cardamom': ['cineole', 'limonene', 'terpinolene', 'alpha-terpineol'],
    'cinnamon': ['cinnamaldehyde', 'eugenol', 'cinnamyl acetate', 'coumarin'],
    'cumin': ['cuminaldehyde', 'cuminol', 'p-cymene', 'terpinene'],
    'coriander': ['linalool', 'geraniol', 'borneol', 'camphor'],
    'fennel': ['anethole', 'fenchone', 'estragole', 'limonene'],
    'clove': ['eugenol', 'eugenyl acetate', 'caryophyllene', 'alpha-humulene'],
    'garlic': ['allicin', 'diallyl disulfide', 'ajoene', 's-allyl cysteine'],
    'licorice': ['glycyrrhizin', 'glycyrrhetinic acid', 'liquiritin', 'glabridin'],
    'saffron': ['crocin', 'crocetin', 'safranal', 'picrocrocin']
}

def call_pubchem_api(herb_name: str) -> Dict[str, List[Dict]]:
    """
    Call PubChem API to get compound information for a herb
    """
    herb_lower = herb_name.lower()
    
    # First try to get compounds from our mapping
    known_compounds = HERB_COMPOUND_MAPPING.get(herb_lower, [])
    
    compounds_data = {}
    
    for compound_name in known_compounds:
        try:
            # Search for compound by name
            search_url = f"{PUBCHEM_BASE_URL}/compound/name/{compound_name}/property/MolecularFormula,MolecularWeight,IUPACName,CanonicalSMILES/json"
            
            response = requests.get(search_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if 'PropertyTable' in data and 'Properties' in data['PropertyTable']:
                    properties = data['PropertyTable']['Properties'][0]
                    
                    compounds_data[compound_name] = {
                        'molecular_formula': properties.get('MolecularFormula', 'N/A'),
                        'molecular_weight': properties.get('MolecularWeight', 'N/A'),
                        'iupac_name': properties.get('IUPACName', 'N/A'),
                        'canonical_smiles': properties.get('CanonicalSMILES', 'N/A'),
                        'pubchem_id': data.get('PropertyTable', {}).get('CID', 'N/A')
                    }
            
            # Add delay to avoid rate limiting
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error fetching data for {compound_name}: {str(e)}")
            # Provide fallback data
            compounds_data[compound_name] = {
                'molecular_formula': 'N/A',
                'molecular_weight': 'N/A',
                'iupac_name': compound_name,
                'canonical_smiles': 'N/A',
                'pubchem_id': 'N/A',
                'error': str(e)
            }
    
    # If no known compounds, try a general search
    if not compounds_data:
        try:
            search_url = f"{PUBCHEM_BASE_URL}/compound/name/{herb_name}/property/MolecularFormula,MolecularWeight,IUPACName,CanonicalSMILES/json"
            response = requests.get(search_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if 'PropertyTable' in data and 'Properties' in data['PropertyTable']:
                    properties = data['PropertyTable']['Properties'][0]
                    
                    compounds_data[herb_name] = {
                        'molecular_formula': properties.get('MolecularFormula', 'N/A'),
                        'molecular_weight': properties.get('MolecularWeight', 'N/A'),
                        'iupac_name': properties.get('IUPACName', 'N/A'),
                        'canonical_smiles': properties.get('CanonicalSMILES', 'N/A'),
                        'pubchem_id': data.get('PropertyTable', {}).get('CID', 'N/A')
                    }
        except Exception as e:
            print(f"Error in general search for {herb_name}: {str(e)}")
    
    return compounds_data

def get_compound_synonyms(compound_name: str) -> List[str]:
    """
    Get synonyms for a compound from PubChem
    """
    try:
        search_url = f"{PUBCHEM_BASE_URL}/compound/name/{compound_name}/synonyms/json"
        response = requests.get(search_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'InformationList' in data and 'Information' in data['InformationList']:
                synonyms = data['InformationList']['Information'][0].get('Synonym', [])
                return synonyms[:10]  # Return first 10 synonyms
        
        time.sleep(0.5)
    except Exception as e:
        print(f"Error fetching synonyms for {compound_name}: {str(e)}")
    
    return []

def get_compound_properties(compound_name: str) -> Dict:
    """
    Get detailed properties for a specific compound
    """
    try:
        search_url = f"{PUBCHEM_BASE_URL}/compound/name/{compound_name}/property/MolecularFormula,MolecularWeight,IUPACName,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,ExactMass,TopologicalPolarSurfaceArea,HeavyAtomCount,FormalCharge,Complexity/json"
        
        response = requests.get(search_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'PropertyTable' in data and 'Properties' in data['PropertyTable']:
                properties = data['PropertyTable']['Properties'][0]
                
                return {
                    'molecular_formula': properties.get('MolecularFormula', 'N/A'),
                    'molecular_weight': properties.get('MolecularWeight', 'N/A'),
                    'iupac_name': properties.get('IUPACName', 'N/A'),
                    'canonical_smiles': properties.get('CanonicalSMILES', 'N/A'),
                    'isomeric_smiles': properties.get('IsomericSMILES', 'N/A'),
                    'inchi': properties.get('InChI', 'N/A'),
                    'inchi_key': properties.get('InChIKey', 'N/A'),
                    'exact_mass': properties.get('ExactMass', 'N/A'),
                    'tpsa': properties.get('TopologicalPolarSurfaceArea', 'N/A'),
                    'heavy_atom_count': properties.get('HeavyAtomCount', 'N/A'),
                    'formal_charge': properties.get('FormalCharge', 'N/A'),
                    'complexity': properties.get('Complexity', 'N/A')
                }
        
        time.sleep(0.5)
    except Exception as e:
        print(f"Error fetching detailed properties for {compound_name}: {str(e)}")
    
    return {}

def search_compounds_by_property(property_name: str, property_value: str) -> List[Dict]:
    """
    Search compounds by specific property value
    """
    try:
        search_url = f"{PUBCHEM_BASE_URL}/compound/property/{property_name}/{property_value}/cids/json"
        response = requests.get(search_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'IdentifierList' in data and 'CID' in data['IdentifierList']:
                cids = data['IdentifierList']['CID']
                return cids[:20]  # Return first 20 results
        
        time.sleep(0.5)
    except Exception as e:
        print(f"Error searching compounds by property: {str(e)}")
    
    return []

def get_bioactivity_data(compound_name: str) -> Dict:
    """
    Get bioactivity data for a compound (if available)
    """
    try:
        # This is a simplified version - in practice, you'd need to query
        # ChEMBL or other bioactivity databases
        search_url = f"{PUBCHEM_BASE_URL}/compound/name/{compound_name}/property/MolecularWeight,LogP/json"
        response = requests.get(search_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'PropertyTable' in data and 'Properties' in data['PropertyTable']:
                properties = data['PropertyTable']['Properties'][0]
                
                return {
                    'molecular_weight': properties.get('MolecularWeight', 'N/A'),
                    'logp': properties.get('LogP', 'N/A'),
                    'bioactivity_available': True
                }
        
        time.sleep(0.5)
    except Exception as e:
        print(f"Error fetching bioactivity data for {compound_name}: {str(e)}")
    
    return {'bioactivity_available': False}

# Fallback data for demo purposes
FALLBACK_COMPOUND_DATA = {
    'turmeric': {
        'curcumin': {
            'molecular_formula': 'C21H20O6',
            'molecular_weight': 368.38,
            'iupac_name': '(1E,6E)-1,7-bis(4-hydroxy-3-methoxyphenyl)-1,6-heptadiene-3,5-dione',
            'canonical_smiles': 'COc1cc(ccc1O)C=CC(=O)CC(=O)C=Cc2ccc(O)c(OC)c2',
            'pubchem_id': '969516'
        }
    },
    'black pepper': {
        'piperine': {
            'molecular_formula': 'C17H19NO3',
            'molecular_weight': 285.34,
            'iupac_name': '(2E,4E)-5-(1,3-benzodioxol-5-yl)-1-(piperidin-1-yl)penta-2,4-dien-1-one',
            'canonical_smiles': 'O=C(N1CCCCC1)C=CC=CC2=CC3=C(OCO3)C=C2',
            'pubchem_id': '638024'
        }
    }
}

def get_fallback_compound_data(herb_name: str) -> Dict:
    """
    Get fallback compound data when API calls fail
    """
    herb_lower = herb_name.lower()
    return FALLBACK_COMPOUND_DATA.get(herb_lower, {})
