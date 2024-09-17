# find minimum of three numbers

def find_minimum(a,b,c):
    minimum = None
    if a <= b and a <= c:
        minimum = a
    elif b <= c :
        minimum = b
    else:
        minimum = c
    print(f"minimum number is: {minimum}")

find_minimum(4,7,3)
find_minimum(2,3,1)
find_minimum(4,3,5)
find_minimum(3,2,1)
find_minimum(2,4,5)


