#Set Items. Set items are unordered, unchangeable, and do not allow duplicate values.
s={2,5,3,2,3,5}
print(s)
print(type(s))
sagar=set()
print(type(sagar))
info={"new, 4, 6, False, 5.5,19"}
print(info)

for value in info:
    print(value)

#set in union and intersection
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

# example of union and intersection
cities1={"Azamgarh","Lucknow","varanasi","Delhi"}
cities2={"Azamgarh","Mumbai","Noida","Lucknow"}
cities3=cities1.union(cities2)
print(cities3)

#intersection function in common cities in both set
cities3=cities1.intersection(cities2)
print(cities3)
#set 1 set 2 common cities in set 
cities3=cities1.symmetric_difference(cities2)
print(cities3)
#set 1 in varansi and delhi
cities3=cities1.difference(cities2)
print(cities3)

#azamgarh and lucknow is common in set the output given false
cities3=cities1.isdisjoint(cities2)
print(cities3)

# cities chack in set 1 and set2 cities name not common then output given false
cities1={"Azamgarh","Lucknow","varanasi","Delhi"}
cities2={"Azamgarh","Lucknow"}
print(cities1.issuperset(cities2))

#Add method in set
cities1={"Azamgarh","Lucknow","varanasi","Delhi"}
cities1.add("Mehnagar")
print(cities1)

#remove metode in set 
cities1={"Azamgarh","Lucknow","varanasi","Delhi"}
cities1.remove("Delhi")
print(cities1)

#pop method in set
cities1={"Azamgarh","Lucknow","varanasi","Delhi"}
item=cities1.pop()
print(cities1)
print(item)

#if and else mothod from delete set
info={"Azamgarh",50,"False",6.2}
if "Azamgarh" in info:
    print("Azamgarh is prasent")
else:
    print("Azamgarh is not prasent")




