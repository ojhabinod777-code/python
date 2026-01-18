# intermediate level code
a = input("Enter anything: ")

try:
    a = int(a)
except ValueError:
    try:
        a = float(a)
    except ValueError:
        pass

print(type(a))
# to get there first basic to know

a=123 # it is a integer
b=1.2 #it is a float
c=(5>3) # it is a booleans


