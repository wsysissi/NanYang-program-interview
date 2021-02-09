The working of my code is based on a rule that if a point is in a polygon, draw a radial from this point, if the radial intersects the polygon with an odd number of points, then the point is inside the polygon. If there are an even number of points, then it is outside the polygon.

Above is the general rule, there are some special circumstances that needs to discuss separately.
1.	the point is on the polygon
just regard it as in
2.	the radial intersects with the vertex of polygon
2.1	the 2 neighbor vertex is at same side of the radial
regard it as not intersect
2.2	the 2 neighbor vertex is at different sides of the radial
regard as intersect for once
3.	the radial go through the edge of polygon
3.1	the 2 neighbor vertex of the edge is at same side of the radial
regard it as not intersect
3.2	the 2 neighbor vertex of the edge is at different sides of the radial
regard as intersect for once
