class circle:
    def __init__(self, radius):
        self.radius=radius
        

    def area(self):
        a=3.14*self.radius**2
        print("The area is: ",a)

    def peri(self):
        p=3.14*2*self.radius
        print("The perimeter is: ",p)

d= circle(5)
d.area()
d.peri()
