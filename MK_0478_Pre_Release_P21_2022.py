#CMG
#Task 1
# Membership sign up

FirstNameList =[]
LastNameList =[]
ListOfJoinDates =[]
PaidFeeList =[]
ListOfVolunteers=[]

print("==============================")
print("WELCOME TO SEAVIEW PIER")
print("===============================\n")

repetition = ""
while repetition !="q":
    print("=========================")
    print("APPLYING FOR A MEMBERSHIP:")
    print("=========================\n")
    print("Please input all relevant details for the new member:")
    print("=================================\n")
    FirstName = input("Enter first name:\n")
    LastName = input("Enter last name:\n")
    JoinDate = input("Enter today's date in the format DD/MM/YYYY:\n")
    PaidFee =input("Did you pay the fee? Answer in the format y/n:\n")

    PaidFee =input("Did you pay fee? Enter y/n:\n")
    while PaidFee != "y" and PaidFee != "n":      #validation
        PaidFee =input("Did you pay fee? Input y/n:\n")

print("VOLUNTEER DETAILS")
print("==================\n")
print("Enter one of the following options\n")  
print("0 - Not a volunteer member")
print("1 - For pier entrance gate")
print("2 - Gift shop")
print("3 - Painting and decoration")

Volunteers = int(input("Enter code 0-3:\n"))
while Volunteers < 0 or Volunteers > 3:        #validating
    Volunteers = int(input("Enter code 0-3:\n"))

    Volunteers = int(input("Enter code 0-3:\n"))

FirstNameList.append(FirstName)
LastNameList.append(LastName)
ListOfJoinDates.append(JoinDate)
PaidFeeList.append(PaidFee)
ListOfVolunteers.append(Volunteers)

repetition = input("Enter 'q' to quit or press any key to register another member\n")

#check the lists
for i in range (0,len(FirstNameList)):
    print("MEMBERSHIP DETAILS")
    print (FirstNameList[i],LastNameList[i],"date of joining:",ListOfJoinDates[i])
    print("Fee paid:",PaidFeeList[i],"Volunteer Code:",ListOfVolunteers[i])

    print("\n")

print("=========================")
print("SPONSORING WOODEN PLANK(S)")
print("=========================\n")

MembersPlaque = input("Would you like to kindly sponsor plank? Enter y/n:\n")
while MembersPlaque != "y" and MembersPlaque != "n":   
    #validation
    MembersPlaque = input("Would you like to kindly sponsor plank? Input y/n:\n")

    if MembersPlaque == "y":
        NamePlaque = input("Enter first and last name to appear on the plaque: \n")
        MessagePlaque = input("Please enter the short message that you would like to be written on the plaque, MAX 100 characters:\n")
        while len(MembersPlaque)>100:
            MessagePlaque = input("Please enter the short message that you would like to be written on the plaque, MAX 100 characters:\n")
    else:
        NamePlaque = "NA"
        MessagePlaque = "NA"
         
    print("\n")
    print("==================")
    print("CHECK OF MEMBER DATA")
    print("==================")

    print("First name:", FirstName)
    print("Last name::", LastName)
    print("Join Date:", DateOfJoining)
    print("Fee paid:", PaidFee)
    print("Volunteer code:", Volunteers)
    print("Plaque Name:",NamePlaque)
    print("Plaque Message:",MessagePlaque)
    print("\n")
    
    Confirm = input("Enter 'y' to confirm all details are correct or 'n' to re-enter:\n")
    if Confirm == "y":
        FirstNameList.append(FirstName)
        LastNameList.append(LastName)
        ListOfJoinDates.append(JoinDate)
        PaidFeeList.append(PaidFee)
        ListOfVolunteers.append(Volunteers)
        PlaqueNameList.append(NamePlaque)
        PlaqueMessageList.append(MessagePlaque)

for i in range (0,len(FirstNameList)):
    print("==================")
    print("CONFIRMATION DETAILS")
    print("==================")
    print("We will confirm these details by email")
    print("Name:",FirstNameList[i],LastNameList[i],"joindate:",DateOfJoining[i])
    print("Fee paid:",PaidFeeList[i],"Volunteer Code:",ListOfVolunteers[i])
    print("Plaque details\n")
    print("Name on plaque:", PlaqueNameList[i])
    print("Message on Plaque",PlaqueMessageList[i])
    if MembersPlaque =="y":
        print("Please pay $200 for the plaque using the email link")
    print("Many thanks from SEAVIEW PIER")

    
   
repetition2 = ""
while repetition2 != "q":

    print("===========================")
    print("MEMBERSHIP SEARCH")
    print("===========================\n")

    print("MENU")
    print("Enter 1 for list of members")
    print("Enter 2 for members who are not volunteering")
    print("Enter 3 for volunteering members at pier entrance gate")
    print("Enter 4 for volunteering members in the gift shop")
    print("Enter 5 for volunteering members who are participating in painting and decorating")
    print("Enter 6 for members whose membership has expired")
    print("Enter 7 for members who have not paid yet")

ChoiceForSearch = int(input("Enter number between 1-7\n"))
while ChoiceForSearch <1 or ChoiceForSearch >7:
    ChoiceForSearch = int(input("Enter a number in the range 1-7\n"))

    for i in range(0,len(FirstNameList)):
        if ChoiceForSearch == 1:
            print(FirstNameList[i],LastNameList[i])
        elif ChoiceForSearch == 2:
            if ListOfVolunteers[i] == 0:
                print(FirstNameList[i],LastNameList[i])
        elif ChoiceForSearch == 3:
            if ListOfVolunteers[i] == 1:
                print(FirstNameList[i],LastNameList[i])                  
        elif ChoiceForSearch == 4:
            if ListOfVolunteers[i] == 2:
                print(FirstNameList[i],LastNameList[i])
        elif ChoiceForSearch == 5:
            if ListOfVolunteers[i] == 3:
                print(FirstNameList[i],LastNameList[i])
        elif ChoiceForSearch == 6:
            Year = ListOfJoinDates[i]
            if Year[6:10] != "2021":
                print(FirstNameList[i],LastNameList[i])
        elif SearchChoice == 7:
            if PaidFeeList[i] == "n":
                print(FirstNameList[i],LastNameList[i])
        else:
            print("ERROR")

    Repeat2 = input("Enter 'q' to quit press any key to search again\n")

print("Membership search exited")






                      
                      
               
