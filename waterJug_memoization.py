from collections import defaultdict
from math import gcd

jug1 = int(input("Enter Jug 1 Capacity : "))
jug2 = int(input("Enter Jug 2 Capacity : "))
aim = int(input("Enter Target : "))
visited = defaultdict(lambda: False)
def waterJug(amt1, amt2):
    
     if aim > max(jug1, jug2) or aim % gcd(jug1, jug2) != 0:
        print("No possible solution")
        return
    
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1,amt2)
        return True

    if visited[(amt1,amt2)] == False:
        print(amt1,amt2)
        visited[(amt1,amt2)] = True
        return(waterJug(amt1,0)
               or waterJug(0,amt2)
               or waterJug(jug1,amt2)
               or waterJug(amt1,jug2)
               or waterJug(amt1 + min(amt2,jug1-amt1),amt2 - min(amt2,jug1-amt1))
                or waterJug(amt1-min(amt1,jug2-amt2),amt2+min(amt1,jug2-amt2)))
    else:
        return False
print("Steps : ")
waterJug(0,0)
