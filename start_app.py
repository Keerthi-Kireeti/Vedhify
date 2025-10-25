#!/usr/bin/env python3
"""
Start script for the Vedhify application.
This script will start the Flask backend which serves the Next.js UI.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_ui_build():
    """Check if the UI has been built."""
    ui_build_dir = Path("UI/ayurveda-phytochemicals-animated-nexus-main/out")
    if not ui_build_dir.exists():
        print("UI build not found. Please run: python build_ui.py")
        return False
    
    index_file = ui_build_dir / "index.html"
    if not index_file.exists():
        print("UI build incomplete. Please run: python build_ui.py")
        return False
    
    print("UI build found")
    return True

def main():
    """Start the application."""
    print("Starting Vedhify Application...")
    
    # Check if UI is built
    if not check_ui_build():
        return False
    
    # Set environment variables
    os.environ['FLASK_ENV'] = 'development'
    
    print("Starting Flask backend...")
    print("The application will be available at: http://localhost:5000")
    print("API endpoints available at: http://localhost:5000/api/")
    print("\nPress Ctrl+C to stop the server")
    
    try:
        # Start the Flask app
        from run import app
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Error starting application: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
