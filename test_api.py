#!/usr/bin/env python3
"""
Test script to verify the API endpoints are working correctly.
"""

import requests
import json

def test_health():
    """Test health endpoint."""
    try:
        response = requests.get('http://localhost:5000/api/health')
        print(f"Health check: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_analyze():
    """Test analyze endpoint."""
    try:
        data = {"text": "Turmeric has bitter taste and hot potency"}
        response = requests.post(
            'http://localhost:5000/api/analyze',
            json=data,
            headers={'Content-Type': 'application/json'}
        )
        print(f"Analyze endpoint: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Success: {result.get('success', False)}")
            print(f"Results count: {len(result.get('results', []))}")
            for i, result_item in enumerate(result.get('results', []), 1):
                print(f"  Result {i}: {result_item.get('herb', {}).get('name', 'Unknown')}")
        else:
            print(f"Error: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Analyze test failed: {e}")
        return False

def test_demo():
    """Test demo endpoint."""
    try:
        response = requests.get('http://localhost:5000/demo')
        print(f"Demo endpoint: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Demo herbs: {result.get('herbs', [])}")
        return response.status_code == 200
    except Exception as e:
        print(f"Demo test failed: {e}")
        return False

def main():
    """Run all API tests."""
    print("API Testing")
    print("=" * 30)
    
    tests = [
        ("Health Check", test_health),
        ("Demo Endpoint", test_demo),
        ("Analyze Endpoint", test_analyze)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nTesting {test_name}...")
        if test_func():
            print(f"PASS: {test_name}")
            passed += 1
        else:
            print(f"FAIL: {test_name}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
