## Session 13 - Sequence Types I

**A regular strictly convex polygon is a polygon that has the following characteristics:**
1. all interior angles are less than 180
2. all sides have equal length
 
**For a regular strictly convex polygon with:**
* n edges (=n vertices)
* R circumradius
* interiorAngle=(n−2)⋅180n
* edgeLength,s=2⋅R⋅sin(πn)
* apothem,a=R⋅cos(πn)
* area=12⋅n⋅s⋅a
* perimeter=n⋅s

**Objective 1 :**

1. Create a Polygon Class: where initializer takes in:
    * number of edges/vertices
    * circumradius

    that can provide these properties:
    * edges
    * vertices
    * interior angle
    * edge length
    * apothem
    * area
    * perimeter
    
    that has these functionalities:
    * a proper __repr__ function
    * implements equality (==) based on # vertices and circumradius (__eq__)
    * implements > based on number of vertices only (__gt__)
    
**Objective 2 : **

1. Implement a Custom Polygon sequence type:where initializer takes in:

    * number of vertices for largest polygon in the sequence
    * common circumradius for all polygons

   that can provide these properties:
   
   * max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
   
   that has these functionalities:
   * functions as a sequence type (__getitem__)
   * supports the len() function (__len__)
   * has a proper representation (__repr__)
   
2. Results:
    1. Implement these 2 classes as a separate module. Access these modules in a jupyter-notebook (or Google Colab or Deep Note)
    2. Run Objective 1 module to show that the functionalities are implemented properly
    3. Run Objective 2 module and show which polygon is efficient for n = 25
    4. You are submitting link to your GitHub repo, where we can find the 2 modules and your notebook in which you have called and tested them


## Polygon 

**Usage**

```python
p = Polygon(10, 10) # no of edges , circumradius
p.num_edges
p.perimeter
p.area

```

## Polygon_Sequence

**Usage**

```python
p = Polygon_Sequence(num_edges = 10,  circumradius = 10) 

#for getting the each Polygon through index
p[3]

#slicing
p[3:10]

#length
len(p)

#max efficinecy polygon
p.max_efficiency_polygon


```
