
#trying out python Creating Functions 

import time


#for checking things further on in the code *Developer Option 

def lazykid():
    if input("1010,"+ " Press Enter") == "010":
       print("SOOOOO LAZY")
       time.sleep(1)
       questioning3()





#master Login

def questioning3():
    MUsername = "AsdInd"
    MPassword = "YeetoDeleto"
    print("Master LogIn... ")
    time.sleep(1)
    muser1 = str(input("Username:  "))
    if muser1 == MUsername:
        time.sleep(1.5)
        print("Welcome "+ MUsername + " Please Enter Your Password.. ")
        mpass = str(input("Password:  "))
        if mpass == MPassword:
            print("Welcome, Alphie.. ")
            quit()




        else:
            print("Incorrect Username Master Override Canceled ")
            time.sleep(1)
            print("....")
            time.sleep(1)
            questioning()
    elif muser1 == "Asd123":
        print("Unauthorised User Detected Transfering To Correct Department...")
        time.sleep(1)
        print("....")
        time.sleep(1)
        signin()


    else:
        print("Incorrect Password MAster Override Canceled ")
        time.sleep(1)
        print("....")
        time.sleep(1)
        questioning()



#couldnt get gamw to work

def pythongame():
    print("NO")
    questioning2()

#asking user if they wanna play with possibilty of master override

def questioning2():

    ans2=input("would You like to Play a Game...  ")
    if ans2 == "yes":
        pythongame()
    elif ans2 == "no":
        print("okay...")
        time.sleep(1)
        questioning2()
    elif ans2 == "$*Override ASDIndustries778":
        print("Processing OverRide")
        time.sleep(2)
        questioning3()

    else:
        print("Incorrect Input...")
        time.sleep(1)
        questioning2()

#asking user if they want to signin

def questioning():

    lazykid()
    print("Welcome To Program #1 ASD Industries")
    ans=input("Would You Like to Sign In.. ")
    if ans == "yes":
     signin()
    elif ans == "no":
     print("okay Goodbye... ")
     time.sleep(1)
     questioning()
    else:
     print("incorrect input ")
    time.sleep(1)
    questioning()


def signin():
#main signin
    correctusername = "Asd123"
    correctpassword = "asd"
    usernameattempt= input ("Hello They're Please Enter Your Username ")
    if usernameattempt == correctusername:
        passwordattempt=input("Welcome "+ correctusername + " Please Enter Your Password... ")
        if passwordattempt == correctpassword:
            print("Welcome... ")
            time.sleep(1)
            questioning2()
        else:
         print("incorrect Password")
        time.sleep(1)
        signin()


    else:
        print("Incorrect Username ")
        time.sleep(1)
        signin()









#the main program thats ran

questioning()




