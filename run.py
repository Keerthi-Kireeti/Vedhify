from app import create_app
import os

app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    print("Starting Ayurvedic AI Analyzer...")
    print("Available endpoints:")
    print("- http://localhost:5000/ (Main interface)")
    print("- http://localhost:5000/api/analyze (Analysis API)")
    print("- http://localhost:5000/api/health (Health check)")
    print("- http://localhost:5000/demo (Demo data)")
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )

