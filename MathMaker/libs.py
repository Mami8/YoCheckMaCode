import math


class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
                
        self.coords = (x, y)


    def distance(self, target):
        """Calculates distance between two points

        Args:
            target (point object): Point object

        Returns:
            tuple: The distance squared and the distance itself
        """
        dist = (target.x-self.x)**2 + (target.y-self.y)**2
        calc_dist = math.sqrt(dist)
        return (dist, calc_dist)


    def triangle_perimeter(self, kose1, kose2):
        """Calculates the preimeter of the triangle formed by the given dots

        Args:
            kose1 (point object): One of the corners of the triangle
            kose2 (point object): One of the corners of the triangle

        Returns:
            float: The perimeter of the triangle
        """
        ab = math.dist(self.coords, kose1.coords)[1]
        bc = math.dist(self.coords, kose2.coords)[1]
        ac = math.dist(kose1.coords, kose2.coords)[1]
        perimeter = ab + ac + bc
        return perimeter


    def triangle_area(self, kose1, kose2):
        """Calculates the area of the triangle formed by the given dots

        Args:
            kose1 (point object): One of the corners of the triangle
            kose2 (point object): One of the corners of the triangle

        Args:
            kose1 (point object): One of the corners of the triangle
            kose2 (point object): One of the corners of the triangle

        Returns:
            float: The area of the triangle
        """        
        r1 = self.x * kose1.y
        r2 = kose1.x * kose2.y
        r3 = kose2.x * self.y
        
        l1 = self.y * kose1.x
        l2 = kose1.y * kose2.x
        l3 = kose2.y * self.x
        
        r = r1 + r2 + r3
        l = l1 + l2 + l3
        alan = (abs(r-l))/2
        return alan


    def __repr__(self) -> str:
        return "x: %f, y: %f" % (self.x, self.y)
    

origin = point(0, 0)
