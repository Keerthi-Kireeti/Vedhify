import pytest
from app.services.nlp_service import AyurvedicNLPService

def test_herb_extraction():
    nlp_service = AyurvedicNLPService()
    
    sample_text = """
    Ashwagandha (Withania somnifera) has a bitter (tikta) and 
    astringent (kashaya) taste with heating (ushna) potency.
    It is used for strength and vitality.
    """
    
    herbs = nlp_service.extract_herbs(sample_text)
    
    assert len(herbs) > 0
    assert any('Ashwagandha' in h['name'] for h in herbs)

def test_ayurvedic_properties_extraction():
    nlp_service = AyurvedicNLPService()
    
    sample_text = """
    Turmeric has bitter, pungent, and astringent taste (rasa).
    It has light, dry, and sharp qualities (guna).
    It has hot potency (virya).
    """
    
    properties = nlp_service.extract_ayurvedic_properties(sample_text)
    
    assert 'tikta' in properties['rasa']  # bitter
    assert 'katu' in properties['rasa']   # pungent
    assert 'kashaya' in properties['rasa'] # astringent
    assert 'ushna' in properties['virya']  # hot
