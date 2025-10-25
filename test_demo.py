#!/usr/bin/env python3
"""
Demo script for Ayurvedic AI Analyzer
Tests the complete analysis pipeline as specified in the requirements
"""

import requests
import json
import time

def test_demo_flow():
    """Test the complete demo flow as specified"""
    
    print("=" * 60)
    print("AYURVEDIC AI ANALYZER - DEMO FLOW TEST")
    print("=" * 60)
    
    # Demo text as specified
    demo_text = "Turmeric (Curcuma longa) combined with black pepper (Piper nigrum) enhances bioavailability. The hot property of these herbs aids in digestion and reduces inflammation."
    
    print(f"\nDemo Text: {demo_text}")
    print("\n" + "=" * 60)
    
    # Test the demo endpoint
    try:
        print("Testing demo endpoint...")
        response = requests.get('http://localhost:5000/demo')
        
        if response.status_code == 200:
            data = response.json()
            print("[SUCCESS] Demo endpoint successful!")
            
            # Display results
            print("\n" + "=" * 40)
            print("DEMO RESULTS")
            print("=" * 40)
            
            print(f"\n1. EXTRACTED HERBS:")
            for herb in data['herbs']:
                print(f"   - {herb}")
            
            print(f"\n2. AYURVEDIC PROPERTIES:")
            for herb, properties in data['ayurvedic_properties'].items():
                print(f"   {herb}:")
                if 'rasa' in properties:
                    print(f"     Rasa: {', '.join(properties['rasa'])}")
                if 'guna' in properties:
                    print(f"     Guna: {', '.join(properties['guna'])}")
                if 'virya' in properties:
                    print(f"     Virya: {', '.join(properties['virya'])}")
                if 'dosha' in properties:
                    print(f"     Dosha: {properties['dosha']}")
            
            print(f"\n3. MODERN COMPOUNDS:")
            for herb, compounds in data['modern_compounds'].items():
                print(f"   {herb}:")
                for compound, details in compounds.items():
                    print(f"     - {compound}")
                    if 'molecular_formula' in details:
                        print(f"       Formula: {details['molecular_formula']}")
                    if 'molecular_weight' in details:
                        print(f"       Weight: {details['molecular_weight']}")
            
            print(f"\n4. GENERATED HYPOTHESES:")
            for i, hypothesis in enumerate(data['hypotheses'], 1):
                print(f"   Hypothesis {i}: {hypothesis['title']}")
                print(f"   Summary: {hypothesis['summary']}")
                
                if 'synergies' in hypothesis:
                    for synergy in hypothesis['synergies']:
                        print(f"     - {synergy['type']}")
                        if 'mechanism' in synergy:
                            print(f"       Mechanism: {synergy['mechanism']}")
                        if 'evidence' in synergy:
                            print(f"       Evidence: {synergy['evidence']}")
                
                if 'correlations' in hypothesis:
                    for correlation in hypothesis['correlations']:
                        print(f"     - {correlation['type']}")
                        if 'correlations' in correlation:
                            for corr in correlation['correlations']:
                                if 'ancient_property' in corr:
                                    print(f"       {corr['ancient_property']}: {corr['modern_understanding']}")
            
            print("\n" + "=" * 60)
            print("DEMO FLOW COMPLETED SUCCESSFULLY!")
            print("=" * 60)
            
            return True
            
        else:
            print(f"[ERROR] Demo endpoint failed: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("[ERROR] Could not connect to server. Make sure the Flask app is running.")
        print("   Run: python app.py")
        return False
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        return False

def test_analysis_api():
    """Test the analysis API with custom text"""
    
    print("\n" + "=" * 60)
    print("TESTING ANALYSIS API")
    print("=" * 60)
    
    test_text = "Ashwagandha and Brahmi are excellent for memory enhancement and stress reduction."
    
    try:
        response = requests.post('http://localhost:5000/analyze', 
                              json={'text': test_text},
                              headers={'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            data = response.json()
            print("[SUCCESS] Analysis API successful!")
            print(f"Found herbs: {data['herbs']}")
            print(f"Generated {len(data['hypotheses'])} hypotheses")
            return True
        else:
            print(f"[ERROR] Analysis API failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        return False

def main():
    """Main test function"""
    
    print("Starting Ayurvedic AI Analyzer Tests...")
    print("Make sure the Flask app is running on http://localhost:5000")
    print("Run: python app.py")
    
    # Wait a moment for user to start the server
    time.sleep(2)
    
    # Test demo flow
    demo_success = test_demo_flow()
    
    # Test analysis API
    api_success = test_analysis_api()
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Demo Flow: {'[PASSED]' if demo_success else '[FAILED]'}")
    print(f"Analysis API: {'[PASSED]' if api_success else '[FAILED]'}")
    
    if demo_success and api_success:
        print("\n[SUCCESS] All tests passed! The Ayurvedic AI Analyzer is working correctly.")
    else:
        print("\n[WARNING] Some tests failed. Check the error messages above.")

if __name__ == "__main__":
    main()
