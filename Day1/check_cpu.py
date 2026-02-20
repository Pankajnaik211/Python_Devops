import psutil  # import the labrary for get cpu utilization from the script 

def cpu_utilization():
    thrash_hold= int(input("Enter your thrash hold"))# take user input of the trshhold to compare with cpu usages
    current_cpu= psutil.cpu_percent(interval=1)   # to get Current cpu utilzation syntax of get psutil lbrary

    if current_cpu > thrash_hold:  #use conditional statement for compare the condition  
        print("Cpu alet mail has been send to user")
    else :
        print("Cpu is in safe state")   

cpu_utilization()   #call the function
