#!/usr/bin/env python3
"""
Build script to compile the Next.js UI and integrate it with the Flask backend.
"""

import os
import subprocess
import sys
import shutil
from pathlib import Path

def run_command(command, cwd=None):
    """Run a shell command and return the result."""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(f"Error output: {result.stderr}")
        return False
    print(f"Success: {result.stdout}")
    return True

def main():
    """Main build process."""
    print("Starting UI build process...")
    
    # Get the project root directory
    project_root = Path(__file__).parent
    ui_dir = project_root / "UI" / "ayurveda-phytochemicals-animated-nexus-main"
    
    if not ui_dir.exists():
        print(f"UI directory not found: {ui_dir}")
        return False
    
    print(f"UI directory: {ui_dir}")
    
    # Check if Node.js is installed
    if not run_command("node --version"):
        print("Node.js is not installed. Please install Node.js first.")
        return False
    
    # Check if npm is available
    if not run_command("npm --version"):
        print("npm is not installed. Please install npm first.")
        return False
    
    # Install dependencies
    print("Installing dependencies...")
    if not run_command("npm install --legacy-peer-deps", cwd=ui_dir):
        print("Failed to install dependencies")
        return False
    
    # Build the Next.js app
    print("Building Next.js app...")
    if not run_command("npm run build", cwd=ui_dir):
        print("Failed to build Next.js app")
        return False
    
    # The build output should be in the 'out' directory
    build_output = ui_dir / "out"
    if not build_output.exists():
        print("Build output directory not found")
        return False
    
    print("UI build completed successfully!")
    print(f"Build output: {build_output}")
    
    # Verify the build
    index_file = build_output / "index.html"
    if not index_file.exists():
        print("index.html not found in build output")
        return False
    
    print("Build verification successful!")
    print("\nUI integration complete!")
    print("You can now run the Flask backend with: python run.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
