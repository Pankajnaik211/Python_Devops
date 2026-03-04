# API Methods 
# 1)GET : 
#   GEt Mainly used for read data on the server when you wants to read the data 
#   on server you can used GET method 

# 2)POST :

#    POST mainly used for send data to server 
#       eg. when you  book tickit on the application you need to fill form means your sending
#           your information to server to send the information,data to server 
#          POST method will be used 

#  3)DELETE :
#      Delete used to delete the record from the server 
#      e.g  you wants to remove your profile  picture from the instagram 
#      what you will do you will send the delete request to instagram  that this api method used 

# 4) UPDATE :
#    Update  used to update record on server 
#          e.g you wants to update your date of birth on server that time update method will be used  
# 
# # 📘 Life Status Codes – Personal Notes


# ## 200 : OK

# **Meaning:** Everything is working.
# **Life Note:** I am stable. I am progressing slowly but correctly.
# **My Notes:** ____________________________________________

# ---

# ## 201 : Created

# **Meaning:** Something new has started.
# **Life Note:** New habit, new skill, new opportunity created.
# **My Notes:** ____________________________________________

# ---

# ## 204 : No Content

# **Meaning:** No visible results yet.
# **Life Note:** Efforts are happening silently. Results will come later.
# **My Notes:** ____________________________________________

# ---

# ## 301 : Redirect

# **Meaning:** Direction changed.
# **Life Note:** Career shift, mindset shift, new path.
# **My Notes:** ____________________________________________

# ---

# ## 400 : Bad Request

# **Meaning:** Wrong decision taken.
# **Life Note:** I made a mistake. Learn and adjust.
# **My Notes:** ____________________________________________

# ---

# ## 401 : Unauthorized

# **Meaning:** Access denied.
# **Life Note:** Not everyone deserves access to my time or energy.
# **My Notes:** ________________

# # 
#   

import requests

url = "https://fake-store-api.mock.beeceptor.com/products/1"

response=requests.get(url=url)

# print(response)

print(response.json)

# print(response.text)

# Video day2  2:30:09