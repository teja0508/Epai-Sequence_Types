# Polygon.py
import math

class Polygon :
    
    """
    Implementation of a regular Polygon which takes num_eges and circumradius as input
    It can give num_eges, num_vertices,interior angle,edge length,apothem,area,perimeter
    
    """
    
    def __init__(self, num_edges : int, circumradius : float) -> None:
    
        self.num_edges =  num_edges
        self.circumradius = circumradius
        
    @property
    def num_edges(self):
       
 
        return self._num_edges
    
    @num_edges.setter
    def num_edges(self, value):
   
        if(value < 3):
            raise ValueError("Polygon should have atleast 3 edges")
            
        self._num_edges = value
    
    @property
    def num_vertices(self):

        
        return self._num_edges
    
    @num_vertices.setter
    def num_vertices(self, value):
        
        if(value < 3):
            raise ValueError("Polygon should have atleast 3 vertices")
            
        self._num_edges = value
        
    @property    
    def circumradius(self):
        
        return self._circumradius
    
    @circumradius.setter
    def circumradius(self, value):
        
        if(value < 0) : 
            raise ValueError(" Radius should be greater than 0")
        self._circumradius = value

    @property  
    def interior_angle(self):
        
        return (self.num_edges - 2) * 180 / self.num_edges
    
    @property  
    def edge_length(self):
        
        return 2 * self.circumradius * math.sin(math.pi/ self.num_edges)
    
    @property  
    def apothem(self):
        
        return self.circumradius * math.cos(math.pi/ self.num_edges)
    
    @property  
    def area(self):
        return 1/2 * self.num_edges * self.edge_length * self.apothem
    
    @property  
    def perimeter(self):
        return self.num_edges * self.edge_length
    
    def __repr__(self) : 
        return f"Regular Convex Polygon with edges : {self.num_edges} and circumradius : {self.circumradius} "
    
    def __eq__(self, other):
        
        return self.num_edges == other.num_edges and self.circumradius == other.circumradius
    
    def __gt__(self, other) :
        
        return self.num_vertices > other.num_vertices