from libs import point, origin
from time import sleep

while True:
    secim = input("""\n
                  Please, choose an option from the list bellow.\n
                  1. Distance between two points.\n
                  2. Perimeter of a triangle.\n
                  3. Area of a triangle.\n
                  >> 
                  """)
    match secim:
        case "1":
            cords1 = input("\nPlease enter the x any y values of the first point seperated with a semicolon (;)\n>>").strip().split(";")
            cords2 = input("\nPlease enter the x any y values of the second point seperated with a semicolon (;)\n>>").strip().split(";")
            
            for i in range(2):
                cords1[i] = int(cords1[i])
                cords2[i] = int(cords2[i])
                
            nokta1 = point(cords1[0], cords1[1])
            nokta2 = point(cords2[0], cords2[1])
            
            dist, calc_dist = nokta1.distance(nokta2)
            print("Distance between the points is the square root of {} which is {}".format(dist, calc_dist))
            sleep(2)
            
        case "2":
            cords1 = input("\nPlease enter the x any y values of the first corner seperated with a semicolon (;)\n>>").strip().split(";")
            cords2 = input("\nPlease enter the x any y values of the second corner seperated with a semicolon (;)\n>>").strip().split(";")
            cords3 = input("\nPlease enter the x any y values of the third corner seperated with a semicolon (;)\n>> ").strip().split(";")
            
            for i in range(2):
                cords1[i] = int(cords1[i])
                cords2[i] = int(cords2[i])
                cords3[i] = int(cords3[i])
                
            nokta1 = point(cords1[0], cords1[1])
            nokta2 = point(cords2[0], cords2[1])
            nokta3 = point(cords3[0], cords3[1])
            
            perimeter = nokta1.triangle_perimeter(nokta2, nokta3)
            print("\nPerimeter is " + str(perimeter))
            sleep(2)
            
        case "3":
            cords1 = input("\nPlease enter the x any y values of the first corner seperated with a semicolon (;)\n>>").strip().split(";")
            cords2 = input("\nPlease enter the x any y values of the second corner seperated with a semicolon (;)\n>>").strip().split(";")
            cords3 = input("\nPlease enter the x any y values of the third corner seperated with a semicolon (;)\n>> ").strip().split(";")
            
            for i in range(2):
                cords1[i] = int(cords1[i])
                cords2[i] = int(cords2[i])
                cords3[i] = int(cords3[i])
            
            nokta1 = point(cords1[0], cords1[1])
            nokta2 = point(cords2[0], cords2[1])
            nokta3 = point(cords3[0], cords3[1])
            
            area = nokta1.triangle_area(nokta2, nokta3)
            print("The area is " + str(area))
            sleep(2)
        
        case _:
                print("Invalid Value!")
                