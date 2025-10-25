from flask import Blueprint, render_template, request, jsonify, send_from_directory, send_file
import logging
import os

logger = logging.getLogger(__name__)

web_bp = Blueprint('web', __name__)

# Path to the Next.js build directory
NEXTJS_BUILD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'UI', 'ayurveda-phytochemicals-animated-nexus-main', 'out')

# Ensure the build directory exists
if not os.path.exists(NEXTJS_BUILD_DIR):
    logger.warning(f"Next.js build directory not found: {NEXTJS_BUILD_DIR}")
    logger.warning("Please run: python build_ui.py to build the UI")

@web_bp.route('/')
def index():
    """Main web interface - serve Next.js app."""
    try:
        return send_file(os.path.join(NEXTJS_BUILD_DIR, 'index.html'))
    except FileNotFoundError:
        # Fallback to Flask template if Next.js build not available
        return render_template('index.html')

@web_bp.route('/<path:path>')
def serve_nextjs(path):
    """Serve Next.js static files."""
    try:
        return send_from_directory(NEXTJS_BUILD_DIR, path)
    except FileNotFoundError:
        # If file doesn't exist, serve index.html for client-side routing
        return send_file(os.path.join(NEXTJS_BUILD_DIR, 'index.html'))

@web_bp.route('/graph/<herb_name>')
def graph_view(herb_name):
    """Knowledge graph visualization page."""
    return render_template('graph.html', herb_name=herb_name)

@web_bp.route('/demo')
def demo():
    """Demo endpoint for testing."""
    demo_text = "Turmeric (Curcuma longa) combined with black pepper (Piper nigrum) enhances bioavailability. The hot property of these herbs aids in digestion and reduces inflammation."
    
    try:
        # This would normally call the services, but for demo we'll return static data
        return jsonify({
            'text': demo_text,
            'herbs': ['Turmeric', 'Black Pepper'],
            'ayurvedic_properties': {
                'Turmeric': {
                    'rasa': ['bitter', 'pungent', 'astringent'],
                    'guna': ['light', 'dry', 'sharp'],
                    'virya': ['hot']
                },
                'Black Pepper': {
                    'rasa': ['pungent'],
                    'guna': ['light', 'dry', 'sharp'],
                    'virya': ['hot']
                }
            },
            'modern_compounds': {
                'Turmeric': {
                    'curcumin': {
                        'molecular_formula': 'C21H20O6',
                        'molecular_weight': 368.38
                    }
                },
                'Black Pepper': {
                    'piperine': {
                        'molecular_formula': 'C17H19NO3',
                        'molecular_weight': 285.34
                    }
                }
            },
            'hypotheses': [
                {
                    'title': 'Bioavailability Enhancement',
                    'summary': 'Piperine enhances curcumin bioavailability by inhibiting glucuronidation',
                    'confidence': 'high'
                }
            ],
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        })
