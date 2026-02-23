# starting of day two
 # we know what is vertual environment in python 

#  how to create vartual environ ment in Python
  
#   type python after that version  to crarte environment of that specific version

# and file name of envrion ment 

# Syntax: 
     
#      Python3.14 -m venv env 

# to activate vertual environment 
#     syantax:
#       source env/bin/activate 
 

#  using this command you can activate the vertual environment for that project  
# activate env on folder that folder conatin env file wich we create during envronment creation


# after that we move to data strcture 

# 4 types of data structure in Python

# 1)list
# 2)Dictonary
# 3)set
# 4)Tuple 

# syntax of list 
 
# cloud =list()  # this is a first type to careate list

# print(type(cloud))

a =["aws",100,200.9,34] # this is second type of create list

print(a)

a.append("ganesh") # you can append the data in to the list you can use this 
     
    #  with the help of append we can append data  from the last 
    # list index starts from 0 we can add hetrogenious types of data into the list 

a.append("rushabh")

a.append("kaivalya")

print(a)



clouds = list()

clouds.append("AWS")

clouds.append("gcp")

clouds.append("Utho")

clouds .append("IBM")

clouds .append("azure")

# print(cloud)


for cloud in clouds:
    if cloud == "AWS" :
        print(f"{cloud} Master of the cloud in cloud industry")
    elif cloud == "gcp" or clouds =="azure":
        print(f"{cloud} This will cover in the course ")
    else :
        print(f"{cloud} this will not cover in the course")
        

    # print(cloud[0])    

