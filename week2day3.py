#code one 
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    
p1=person("sara",20)
print(f"name is {p1.name} and age is {p1.age}")
#code two 
class student:
    def __init__(self,name,age,major):
        self.name=name
        self.age =age 
        self.major=major
s1=student("Ali",20,"cs")
s2=student("Bilal",22,"It")
print(f"name is {s1.name} and age is {s1.age} and major is {s1.major}")        
print(f"name is {s2.name} and age is {s2.age} and major is {s2.major}")        
