"""
Data models for Ayurvedic entities
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from datetime import datetime

@dataclass
class Property:
    """Ayurvedic property (Rasa, Guna, Virya, Vipaka)"""
    name: str
    value: str
    type: str  # 'rasa', 'guna', 'virya', 'vipaka'
    confidence: float = 1.0

@dataclass
class Compound:
    """Chemical compound from PubChem"""
    cid: str
    name: str
    molecular_formula: str
    molecular_weight: float
    synonyms: List[str] = field(default_factory=list)
    properties: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Herb:
    """Ayurvedic herb entity"""
    name: str
    scientific_name: Optional[str] = None
    properties: List[Property] = field(default_factory=list)
    compounds: List[Compound] = field(default_factory=list)
    description: Optional[str] = None
    uses: List[str] = field(default_factory=list)
    contraindications: List[str] = field(default_factory=list)

@dataclass
class AnalysisResult:
    """Result of text analysis"""
    text: str
    herbs: List[Herb] = field(default_factory=list)
    properties: List[Property] = field(default_factory=list)
    compounds: List[Compound] = field(default_factory=list)
    hypotheses: List[Dict[str, Any]] = field(default_factory=list)
    confidence_scores: Dict[str, float] = field(default_factory=dict)
    processing_time: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class Hypothesis:
    """Generated hypothesis connecting Ayurvedic and modern science"""
    title: str
    description: str
    ayurvedic_basis: str
    modern_evidence: str
    confidence: float
    supporting_compounds: List[str] = field(default_factory=list)
    references: List[str] = field(default_factory=list)