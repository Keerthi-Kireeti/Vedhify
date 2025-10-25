from neo4j import GraphDatabase
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

class KnowledgeGraphService:
    def __init__(self, uri: str, user: str, password: str):
        """Initialize Neo4j connection."""
        try:
            self.driver = GraphDatabase.driver(uri, auth=(user, password))
            self._create_constraints()
            logger.info("Neo4j connection established successfully")
        except Exception as e:
            logger.warning(f"Neo4j not available, using fallback mode: {e}")
            self.driver = None
    
    def close(self):
        """Close Neo4j connection."""
        if self.driver:
            self.driver.close()
    
    def _create_constraints(self):
        """Create unique constraints for nodes."""
        if not self.driver:
            return
            
        with self.driver.session() as session:
            session.run("CREATE CONSTRAINT herb_name IF NOT EXISTS "
                       "FOR (h:Herb) REQUIRE h.name IS UNIQUE")
            session.run("CREATE CONSTRAINT compound_id IF NOT EXISTS "
                       "FOR (c:Compound) REQUIRE c.cid IS UNIQUE")
    
    def add_herb(self, name: str, properties: Dict[str, Any]) -> None:
        """Add herb node to graph."""
        if not self.driver:
            logger.info(f"Fallback mode: Would add herb {name} with properties {properties}")
            return
            
        with self.driver.session() as session:
            session.run(
                "MERGE (h:Herb {name: $name}) "
                "SET h += $properties",
                name=name,
                properties=properties
            )
    
    def add_rasa_property(self, herb_name: str, rasa: str) -> None:
        """Link herb to rasa (taste) property."""
        if not self.driver:
            logger.info(f"Fallback mode: Would link {herb_name} to rasa {rasa}")
            return
            
        with self.driver.session() as session:
            session.run(
                "MATCH (h:Herb {name: $herb_name}) "
                "MERGE (r:Rasa {name: $rasa}) "
                "MERGE (h)-[:HAS_RASA]->(r)",
                herb_name=herb_name,
                rasa=rasa
            )
    
    def add_guna_property(self, herb_name: str, guna: str) -> None:
        """Link herb to guna (quality) property."""
        if not self.driver:
            logger.info(f"Fallback mode: Would link {herb_name} to guna {guna}")
            return
            
        with self.driver.session() as session:
            session.run(
                "MATCH (h:Herb {name: $herb_name}) "
                "MERGE (g:Guna {name: $guna}) "
                "MERGE (h)-[:HAS_GUNA]->(g)",
                herb_name=herb_name,
                guna=guna
            )
    
    def add_virya_property(self, herb_name: str, virya: str) -> None:
        """Link herb to virya (potency) property."""
        if not self.driver:
            logger.info(f"Fallback mode: Would link {herb_name} to virya {virya}")
            return
            
        with self.driver.session() as session:
            session.run(
                "MATCH (h:Herb {name: $herb_name}) "
                "MERGE (v:Virya {name: $virya}) "
                "MERGE (h)-[:HAS_VIRYA]->(v)",
                herb_name=herb_name,
                virya=virya
            )
    
    def link_herb_to_compound(self, herb_name: str, cid: int, 
                             compound_name: str) -> None:
        """Link herb to PubChem compound."""
        if not self.driver:
            logger.info(f"Fallback mode: Would link {herb_name} to compound {compound_name}")
            return
            
        with self.driver.session() as session:
            session.run(
                "MATCH (h:Herb {name: $herb_name}) "
                "MERGE (c:Compound {cid: $cid}) "
                "SET c.name = $compound_name "
                "MERGE (h)-[:CONTAINS_COMPOUND]->(c)",
                herb_name=herb_name,
                cid=cid,
                compound_name=compound_name
            )
    
    def get_herb_graph(self, herb_name: str) -> Dict[str, Any]:
        """Get full graph data for a herb."""
        if not self.driver:
            return {'nodes': [], 'relationships': []}
            
        with self.driver.session() as session:
            result = session.run(
                "MATCH (h:Herb {name: $herb_name})"
                "-[r]->(n) "
                "RETURN h, type(r) as rel, n",
                herb_name=herb_name
            )
            
            nodes = []
            relationships = []
            
            for record in result:
                nodes.append(dict(record['h']))
                nodes.append(dict(record['n']))
                relationships.append({
                    'type': record['rel'],
                    'source': record['h']['name'],
                    'target': record['n'].get('name', record['n'].get('cid'))
                })
            
            return {'nodes': nodes, 'relationships': relationships}
    
    def search_herbs_by_property(self, property_type: str, property_value: str) -> List[str]:
        """Search herbs by specific property."""
        if not self.driver:
            return []
            
        with self.driver.session() as session:
            result = session.run(
                f"MATCH (h:Herb)-[:HAS_{property_type.upper()}]->(p:{property_type.capitalize()} {{name: $value}}) "
                "RETURN h.name as herb_name",
                value=property_value
            )
            
            return [record['herb_name'] for record in result]
    
    def get_all_herbs(self) -> List[str]:
        """Get all herbs in the knowledge graph."""
        if not self.driver:
            return []
            
        with self.driver.session() as session:
            result = session.run("MATCH (h:Herb) RETURN h.name as herb_name")
            return [record['herb_name'] for record in result]
