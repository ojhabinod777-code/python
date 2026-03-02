a=int(input("Enter 1st side of a triangle ;"))
b=int(input("Enter 2nd side of a triangle ;"))
c=int(input("Enter 3rd side of a triangle ;"))        
s=(a+b+c)/2
if a+b>c and b+c>a and c+a>b:
    ar=(s*(s-a)*(s-b)*(s-c))**(1/2)
    p=a+b+c
    print(f"the perimeter of a triangle is {p}")
    print(f"the area of a triangle is {ar}")
else:
    print("it is not a triangle ")

