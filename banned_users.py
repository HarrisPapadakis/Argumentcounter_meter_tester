banned_users = ["toilet_duck", "archiblame", "nightstalker", "blamer"] #create the list with given values
user = "melanie" # name of user that is not in the list

if user not in banned_users: #check the condition with boolean
    print(f"{user.title()} , you are authorized and you have permition to write if you wish") #print response
