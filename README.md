# Ayurvedic Text Mining System - MVP

A comprehensive system that bridges ancient Ayurvedic wisdom with modern science by extracting herbs, properties, and generating hypotheses from Ayurvedic texts using NLP, knowledge graphs, and PubChem integration.

## 🌿 Features

### Core MVP Features
- ✅ **Text Upload & NLP Extraction** - Extract herbs and Ayurvedic properties from text
- ✅ **Knowledge Graph Visualization** - Neo4j-based graph database for herb relationships
- ✅ **PubChem API Integration** - Modern compound identification and properties
- ✅ **Rule-based Hypothesis Generation** - Connect ancient properties to modern science
- ✅ **Modern Web Interface** - Beautiful, responsive UI with real-time analysis

### Technology Stack
- **Backend**: Flask 3.0+ with modular architecture
- **NLP**: spaCy 3.7+ with custom Ayurvedic patterns
- **Database**: Neo4j Community Edition for knowledge graph
- **API Integration**: PubChem REST API with rate limiting
- **Frontend**: HTML5, CSS3, JavaScript with Bootstrap 5
- **Visualization**: D3.js for interactive graph visualization

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Neo4j Community Edition
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ayurveda-nlp-mvp
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download spaCy model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **Set up Neo4j**
   - Download and install Neo4j Desktop
   - Create a new database named "ayurveda-kg"
   - Start the database
   - Note the connection details

5. **Configure environment**
   ```bash
   cp env.example .env
   # Edit .env with your Neo4j credentials
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

7. **Access the application**
   - Open http://localhost:5000 in your browser
   - Try the demo text or enter your own Ayurvedic text

## 📁 Project Structure

```
ayurveda-nlp-mvp/
├── .cursorrules                 # Cursor AI context file
├── .env                        # Environment variables
├── .gitignore
├── requirements.txt
├── README.md
├── run.py                      # Main application runner
├── app/
│   ├── __init__.py             # Flask app factory
│   ├── config.py               # Configuration management
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── api.py              # REST API endpoints
│   │   └── web.py              # Web routes
│   ├── services/
│   │   ├── __init__.py
│   │   ├── nlp_service.py      # spaCy NLP processing
│   │   ├── kg_service.py       # Neo4j knowledge graph
│   │   ├── pubchem_service.py  # PubChem API integration
│   │   └── hypothesis_service.py # Rule-based hypothesis
│   ├── models/
│   │   ├── __init__.py
│   │   └── entities.py         # Data models
│   └── utils/
│       ├── __init__.py
│       └── helpers.py          # Helper functions
├── templates/
│   ├── base.html               # Base template
│   ├── index.html              # Main interface
│   └── graph.html              # Graph visualization
├── tests/
│   ├── __init__.py
│   ├── test_nlp.py
│   └── test_api.py
└── static/                     # Static assets
```

## 🔧 API Endpoints

### Analysis
- `POST /api/analyze` - Analyze Ayurvedic text
- `GET /api/graph/<herb_name>` - Get knowledge graph for herb
- `GET /api/herbs` - Get all herbs in database
- `GET /api/search?property_type=X&property_value=Y` - Search herbs by property

### Web Interface
- `GET /` - Main analysis interface
- `GET /graph/<herb_name>` - Graph visualization
- `GET /demo` - Demo data endpoint

### Health
- `GET /api/health` - Health check

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

Run specific test files:
```bash
pytest tests/test_nlp.py
pytest tests/test_api.py
```

## 📊 Usage Examples

### Basic Text Analysis
```python
from app.services.nlp_service import AyurvedicNLPService

nlp_service = AyurvedicNLPService()
text = "Turmeric has bitter taste and hot potency"
herbs = nlp_service.extract_herbs(text)
properties = nlp_service.extract_ayurvedic_properties(text)
```

### Knowledge Graph Operations
```python
from app.services.kg_service import KnowledgeGraphService

kg_service = KnowledgeGraphService(uri, user, password)
kg_service.add_herb("Turmeric", {"rasa": "bitter", "virya": "hot"})
graph_data = kg_service.get_herb_graph("Turmeric")
```

### PubChem Integration
```python
from app.services.pubchem_service import PubChemService

pubchem_service = PubChemService()
compounds = pubchem_service.search_herb_compounds("Turmeric")
```

## 🌟 Key Features Explained

### 1. Ayurvedic Property Extraction
- **Rasa (Taste)**: 6 types - sweet, sour, salty, pungent, bitter, astringent
- **Guna (Qualities)**: Heavy/light, hot/cold, oily/dry, sharp/dull, etc.
- **Virya (Potency)**: Hot or cold
- **Vipaka (Post-digestive effect)**: Sweet, sour, or pungent

### 2. Knowledge Graph
- Nodes: Herbs, Compounds, Properties (Rasa, Guna, Virya)
- Relationships: Herb-HAS_RASA-Property, Herb-CONTAINS_COMPOUND-Compound
- Queries: Find herbs by property, get full herb relationships

### 3. Hypothesis Generation
- Rule-based correlation between Ayurvedic properties and modern compounds
- Synergy analysis for herb combinations
- Bioactivity predictions based on traditional properties

## 🔮 Future Enhancements

### Post-MVP Features
- [ ] OCR for manuscript digitization
- [ ] ML-based hypothesis generation
- [ ] ChEMBL integration for bioactivity data
- [ ] Multi-database synchronization
- [ ] Advanced graph algorithms
- [ ] User authentication/authorization
- [ ] Cloud deployment

### Advanced NLP
- [ ] Custom entity recognition models
- [ ] Sanskrit text processing
- [ ] Multi-language support
- [ ] Context-aware property extraction

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Ancient Ayurvedic texts and practitioners
- Modern scientific research on phytochemicals
- PubChem database for compound information
- Neo4j for graph database technology
- spaCy for NLP capabilities

## 📞 Support

For questions or support, please open an issue on GitHub or contact the development team.

---

**Note**: This is an MVP prototype for research and educational purposes. Always consult qualified healthcare professionals for medical advice.# Vedhify
# Vedhify
# Vedhify
