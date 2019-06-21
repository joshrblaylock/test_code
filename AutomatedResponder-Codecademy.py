# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:04:27 2019

@author: Black Monkey
"""

name = input("What is your name? ")
print(name)


def cs_service_bot():
    print("Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer? \n[1] New Customer \n[2] Existing Customer\n")
    response_one = input("Please enter the number corresponding to your choice, fool!\n")
    if response_one == "1":
        new_customer()
    elif response_one == "2":
        existing_customer()
    else:
        print("Sorry, we didn't understand your selection.\n")
        cs_service_bot()   
        
def existing_customer():
    print("\nWhat kind of support do you need? \n[1] Television Support \n[2] Internet Support \n[3] Speak to a support representative. \n")
    response = input("Please enter the number corresponding to your choice.\n")
    if response == "1":
        television_support()
    elif response == "2":
        internet_support()
    elif response == "3":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.\n")
        existing_customer()
        
def new_customer():
    print("\nWe're excited to have you join the DNS family, how can we help you? \n[1] Sign up for service. \n[2] Schedule a home visit. \n[3] Speak to a sales representative.\n")
    response_two = input("Please select a number corresponding to your answer.\n")
    if response_two == "1":
        sign_up()
    elif response_two == "2":
        home_visit()
    elif response_two == "3":
        live_rep("sales")
    else:
        print("Bitch, why you fuckin round.  Provide a valid answer or go the hell home!\n")
        new_customer()
        
def television_support():
    print("\nWhat is the nature of your problem?: \n[1] I can't access certain channels. \n[2] My picture is blurry. \n[3] I keep losing service. \n[4] Other issues.")
    tv_response = input("Please select the number most closely corresponding to your tv service issue.\n")
    if tv_response == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.\n")
        did_that_help()
    elif tv_response == "2":
        print("Try adjusting the antenna above your television set.\n")
        did_that_help()
    elif tv_response == "3":
        print("Is it raining outside? If so, wait until it is not raining and then try again.\n")
        did_that_help()
    elif tv_response == "4":
        live_rep("support")
    else:
        print("WTF man?  You only have like 4 choices... how hard can it be?!?  Make a damn valid selection already!\n")
        television_support()
        
def internet_support():
    print("\nWhat is the nature of your Internet problem? \n[1] I can't connect to the internet. \n[2] My connection is very slow. \n[3] I can't access certain sites. \n[4] Other Issues \n")
    response = input("Please choose the number that corresponds most closely to your Internet issue.\n")
    if response == "1":
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.\n")
        did_that_help()
    elif response == "2":
        print("Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.\n")
        did_that_help()
    elif response == "3":
        print("Move to a different region or install a VPN. Some areas block certain sites.\n")
        did_that_help()
    elif response == "4":
        live_rep("support")
    else:
        print("Dude... are you like technologically stunted or something?!?  There are only 4 choices... make one!\n")
        internet_support()

def did_that_help():
    help_response = input("Did the solution provided solve your problem?  (Please enter [1] for 'Yes' or [2] for 'No')\n")
    if help_response == "1":
        print("Great!  Thank you for using the automated system to resolve your problem.\n")
    elif help_response == "2":
        print("Would you like to pursue this issue further? If so, please enter the number for your preferred option below: \n[1] Talk to a live representative. \n[2]Schedule a home visit.\n")
        next_step = input("Enter your choice now.\n")
        if next_step == "1":
            live_rep("support")
        elif next_step == "2":
            home_visit("support")
        else:
            print("You have choosen poorly my son.  Please try again to pick between the two numbers, and use your brain this time.\n")
            did_that_help()
    else:
        print("This is a simple Yes or No question, and you can't even answer it?  Come on... try again Mofo!\n")
        did_that_help()
        
def sign_up():
    print("Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for. \n[1] Bundle Deal (Internet + Cable) \n[2] Internet \n[3] Cable\n")
    sl_response = input("Please select the number for the service level you desire.\n")
    if sl_response == "1":
        print("You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.\n")
        home_visit("new install")
    elif sl_response == "2":
        print("You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.\n")
        home_visit("new install")
    elif sl_response == "3":
        print("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.\n")
        home_visit("new install")
    else:
        print("You AssClown!  There are only 3 choices here.  Pick one!  You do not have the option of not signing up at this point.  We are coming to your house.\n")
        sign_up()
        
def home_visit(purpose="none"):
    if purpose == "none":
        print("what is the purpose of your our visit? \n[1] New Service Installation. \n[2] Existing Service Repair. \n[3] Location scouting for unserviced region.\n")
        visit_response = input("Please select the number most closely correlating to the reason for our visit. \n")
        if visit_response == "1":
            home_visit("new install")
        elif visit_response == "2":
            home_visit("support")
        elif visit_response == "3":
            home_visit("scout")
        else:
            print("Why the #*$% can't you give me a valid response?  I need to know why you want us to come over.  Tell me!\n")
            home_visit()       
    if purpose == "new install":
        visit_date = input("Please enter a date below when you are available for a technician to come to your home and install your spanking new service.\n")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.\n")
        return visit_date
    if purpose == "support":
        visit_date = input("Please enter a date below when you are available for a technician to come to your home and provide you with ample emotional support.\n")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.\n")
        return visit_date
    if purpose == "scout":
        visit_date = input("Please enter a date below when you are available for a technician to come to your home and carefully scout it out.\n")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.\n")
        return visit_date
    
def live_rep(purpose):
    if purpose == "sales":
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.\n")
    elif purpose == "support":
        print("Please hold while we connect you with a live support representative. The wait time will be between two minutes and six hours. We thank you for your patience.\n")

cs_service_bot()        



tictactoe = [ ['X', 'O', 'X'],
              [ 'O', ' ', 'X'],
              ['X','O','O']]

for row in tictactoe:
    for column in row:
        print(column + " ", end='')
    print()