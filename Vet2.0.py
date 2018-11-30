import time 
import random

#CREATE CLASS - CUSTOMER, OWNER NAME, PHONE NUMBER, PET NAME, DOG OR CAT
class Customer:
    def __init__(self, owner_name, dog_cat, pet_name='fido', phone_number=555-5555):
        """Purpose - define owner name, phone number, pet name and dog/cat to associate to customer"""
        self.owner_name = owner_name
        self.dog_cat = dog_cat
        self.pet_name = pet_name
        self.phone_number = phone_number


#MAIN MENU - ALLOWS CUSTOMERS TO CHECK IN, CHECK OUT OR ADMINS TO VIEW ROOMS
def vet_menu():
    #CREATE EMPTY ROOMS LIST TO REPRESENT BEGINNING OF DAY WITH NO CUSTOMERS YET
    rooms = []
    while len(rooms) < 1000:
        print("What can we help you with today?")
        time.sleep(1)
        print("1. Check In", "2. Check Out", "3. View Rooms - Admin Only", sep="\n")
        vet_menu_selected = input("Please enter the desired number: ")
        if vet_menu_selected == '1':
            check_in(rooms)
        if vet_menu_selected == '2':
            check_out(rooms)
        if vet_menu_selected == '3':
            view_rooms(rooms)

#DEFINE CHECK IN FUNCTION
def check_in(rooms):
    if len(rooms) == 5:
            print("We're full!")
    elif len(rooms) <6:
        #import pdb; pdb.set_trace()
        owner_name = input("First things first, what is your name? ")
        print ("Thanks! We'll be sure to send the bill to you at the end.")
        dog_cat = input("Dog or Cat? " )
        pet_name = input("What is your pet's name? ")
        phone_number = input("I know we just met, but can we get your number? ")
        print ("You are ready to be seen") 
        rooms.append(Customer(owner_name, dog_cat, pet_name, phone_number))
    

#DEFINE CHECK OUT FUNCTION
def check_out(rooms):
    input("Type your name to check out: ")
    del rooms[0]

#DEFINE ADMIN ONLY - VIEW ROOMS FUNCITON
def view_rooms(rooms):
    input("You are attempting to access restricted content, please enter your password: ")
    time.sleep(1)
    print("Great! Generating rooms list")
    time.sleep(1)
    for i in rooms[0:-1]:
        print(i, end=', ')    
    time.sleep(1)
    vet_menu()


#WELCOME MESSAGE TO USER
#import pdb; pdb.set_trace()
print("Welcome to rewardStyle's vet clinic! Only pets with over 100K+ Instagram Followers will be seen by Dr. Blair.")
time.sleep(1)

#DISPLAY MAIN MENU
vet_menu()



