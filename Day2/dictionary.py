info ={
    "name" : "Pankaj Naik",
    "Mobile NO" : 9370883109,
    "Adress" : "Gajanan Vasahat snagmnear road shrirampur",
    "age" : 25,
    "slaery" : 4.5,
    "married" : False,
    "qualification" : "MCA"
}

print(info)

print("i like to enter in the city to solve",info["Adress"])

print("My qulification is",info["qualification"])

print("My qulification is",info.get("dress","not found"))

info.update({"Fevraits" : ["cricket","Singing"]})

print (dir(info)) 


print(info.update.__doc__)


for key,value in info.items():
    print(key,value)

