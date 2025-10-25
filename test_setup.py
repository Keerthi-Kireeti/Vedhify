#!/usr/bin/env python3
"""
Test script to verify the MVP setup is working correctly.
Run this after installation to check all components.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        from app import create_app
        print("Flask app factory imported successfully")
    except ImportError as e:
        print(f"Flask app import failed: {e}")
        return False
    
    try:
        from app.services.nlp_service import AyurvedicNLPService
        print("NLP service imported successfully")
    except ImportError as e:
        print(f"NLP service import failed: {e}")
        return False
    
    try:
        from app.services.hypothesis_service import HypothesisEngine
        print("Hypothesis engine imported successfully")
    except ImportError as e:
        print(f"Hypothesis engine import failed: {e}")
        return False
    
    try:
        from app.services.pubchem_service import PubChemService
        print("PubChem service imported successfully")
    except ImportError as e:
        print(f"PubChem service import failed: {e}")
        return False
    
    return True

def test_nlp_service():
    """Test NLP service functionality."""
    print("\nTesting NLP service...")
    
    try:
        from app.services.nlp_service import AyurvedicNLPService
        nlp_service = AyurvedicNLPService()
        
        test_text = "Turmeric has bitter taste and hot potency"
        herbs = nlp_service.extract_herbs(test_text)
        properties = nlp_service.extract_ayurvedic_properties(test_text)
        
        print(f"Extracted herbs: {herbs}")
        print(f"Extracted properties: {properties}")
        return True
    except Exception as e:
        print(f"NLP service test failed: {e}")
        return False

def test_hypothesis_engine():
    """Test hypothesis engine functionality."""
    print("\nTesting hypothesis engine...")
    
    try:
        from app.services.hypothesis_service import HypothesisEngine
        engine = HypothesisEngine()
        
        herb_data = {
            'name': 'Turmeric',
            'rasa': ['tikta', 'katu'],
            'guna': ['laghu', 'ruksha'],
            'virya': 'ushna'
        }
        
        compound_data = [
            {'molecular_formula': 'C21H20O6', 'cid': 969516}
        ]
        
        hypotheses = engine.generate_hypotheses(herb_data, compound_data)
        print(f"Generated {len(hypotheses)} hypotheses")
        for i, hyp in enumerate(hypotheses, 1):
            print(f"   {i}. {hyp.get('ayurvedic_property', hyp.get('type', 'Unknown'))}")
        return True
    except Exception as e:
        print(f"Hypothesis engine test failed: {e}")
        return False

def test_flask_app():
    """Test Flask app creation."""
    print("\nTesting Flask app...")
    
    try:
        from app import create_app
        app = create_app('testing')
        
        with app.test_client() as client:
            response = client.get('/api/health')
            if response.status_code == 200:
                print("Flask app and health endpoint working")
                return True
            else:
                print(f"Health endpoint returned status {response.status_code}")
                return False
    except Exception as e:
        print(f"Flask app test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Ayurvedic Text Mining MVP - Setup Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_nlp_service,
        test_hypothesis_engine,
        test_flask_app
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! Your MVP setup is working correctly.")
        print("\nNext steps:")
        print("1. Set up Neo4j database")
        print("2. Configure .env file with Neo4j credentials")
        print("3. Run: python run.py")
        print("4. Open http://localhost:5000 in your browser")
    else:
        print("Some tests failed. Please check the errors above.")
        print("\nTroubleshooting:")
        print("1. Make sure all dependencies are installed: pip install -r requirements.txt")
        print("2. Download spaCy model: python -m spacy download en_core_web_sm")
        print("3. Check that all files are in the correct locations")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
