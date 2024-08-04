# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#           The username for Admin account is: Admin
#           The password for Admin account is: 11111

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# --This reads the text file and creates a list of objects--

with open('test.txt', 'r') as file:
    userlist = []
    info = file.readline().strip()
    while info != '':
        userdict = {"name": "", "pass": "", "balance": 0}
        userdict["name"] = info
        info = file.readline().strip()
        userdict["pass"] = info
        info = file.readline().strip()
        userdict["balance"] = int(info)
        userlist.append(userdict)
        info = file.readline().strip()
file.close()

# --This temp list will store all the contents of the original list so that they
# can be easily stored in the text file--

temp_list = []
user_number = len(userlist)

# --Start of program. Any invalid inputs will be highlighted--

choice1 = "0"
while (choice1 == "0") or (choice1 == "1") or (choice1 == "2"):
    choice1 = input("Enter 1 to login, 2 to signup, 3 to exit \n")

# --Login segment.--

    if choice1 == "1":
        user_name = input("Enter your name \n")
        user_pass = input("Enter your password \n")

# --Check statements for admin account, and logging in if it exists--

        if user_name == "Admin" and user_pass == "11111":
            choice3 = "0"
            while choice3 == "0" or choice3 == "1" or choice3 == "2":
                choice3 = input("Enter 1 to delete user, 2 to exit \n")
                if choice3 == "1":
                    delete_user = input("Which user do you want to delete \n")

# --Making sure that the admin does not delete the admin account--

                    while delete_user == "Admin":
                        delete_user = input("You cannot delete admin account! Enter again \n")

# --Checking if name exists in the text file and then deleting that account--
                    
                    name_found = any(item["name"] == delete_user for item in userlist)
                    if name_found:
                        userlist = [item for item in userlist if item["name"] != delete_user]
                        print(f"{delete_user} has been deleted.")
                    else:
                        print(f"{delete_user} not found in the list.")

# --Updating the user list since an account is deleted--

                    temp_list = []  # Reinitialize temp_list before updating it
                    user_number = len(userlist)
                    for k in range(user_number):
                        temp_list.append(userlist[k]["name"])
                        temp_list.append(userlist[k]["pass"])
                        temp_list.append(str(userlist[k]["balance"]))

# --Updating the text file with the new list of users--

                    with open('test.txt', 'w') as file2:
                        line = ''
                        for l in range(len(temp_list)):
                            line = line + temp_list[l] + "\n"
                        file2.write(line)
                    file2.close()
                    print(temp_list)
                    print(userlist)

# --Option to exit the code--

                elif choice3 == "2":
                    exit()

# --Code to highlight invalid input--

                else:
                    choice3 == "0"
                    print("Invalid input!")

# --Code for login for non-admin users--

        else:
            for i in range(user_number):
                x = userlist[i]
                user_name_check = x.get("name")
                user_pass_check = x.get("pass")

# --Checking if the username entered exists--

                if user_name == user_name_check:

# --Checking if the correct password is entered--

                    if user_pass == user_pass_check:
                        choice2 = 0

# --Displaying the account balance

                        user_balance = x.get("balance")
                        print("Your account balance is", {user_balance})

# --Presenting options to Deposit, Withdraw, Transfer, and Exit--

                        while (choice2 == 0) or (choice2 == 1) or (choice2 == 2) or (choice2 == 3) or (choice2 == 4):
                            choice2 = int(input("Enter 1 to Deposit, 2 to Withdraw, 3 to Transfer, 4 to Exit \n"))

# --Code for updating the text file before exiting--

                            if choice2 == 4:
                                temp_list = []  # Reinitialize temp_list before updating it
                                for k in range(user_number):
                                    temp_list.append(userlist[k]["name"])
                                    temp_list.append(userlist[k]["pass"])
                                    temp_list.append(str(userlist[k]["balance"]))
                                with open('test.txt', 'w') as file2:
                                    line = ''
                                    for l in range(len(temp_list)):
                                        line = line + temp_list[l] + "\n"
                                    file2.write(line)
                                file2.close()

# --Uncomment the following 2 lines if you want the list of users displayed--
                                # print(temp_list)
                                # print(userlist)

                                exit()

# --Option for Depositing money

                            elif choice2 == 1:
                                deposit_value = input("Enter your deposit value \n")

# --Checking if the user enters a valid value for depositing money--

                                if deposit_value.isdigit():

# --Updating the balance of the user, and printing it on-screen--

                                    user_balance = user_balance + int(deposit_value)
                                    print("Your balance is", {user_balance})
                                    userlist[i]["balance"] = user_balance

# --Code for giving an error if an invalid value for Deposit is entered--

                                else:
                                    print("Invalid input!")

# --Option for Withdrawing money

                            elif choice2 == 2:
                                withdraw_value = input("Enter the value you wish to withdraw \n")

# --Checking if the user enters a valid value for withdrawing money--

                                if withdraw_value.isdigit():
                                    if user_balance < int(withdraw_value):
                                        print("Insufficient funds in account")

# --Updating the balance of the user, and printing it on-screen--

                                    elif user_balance >= int(withdraw_value):
                                        user_balance = user_balance - int(withdraw_value)
                                        print("Your balance is", {user_balance})
                                        userlist[i]["balance"] = user_balance

# --Code for giving an error if an invalid value for Withdraw is entered--

                                else:
                                    print("Invalid input!")

# --Option for Transferring money to another account

                            elif choice2 == 3:
                                user_name_2 = input("Who do you wish to transfer money to? \n")

# --Making sure that the user does not transfer money to his own account--

                                while user_name_2 == user_name:
                                    user_name_2 = input("You cannot enter your own name! Enter again \n")

# --Checking if the users entered a correct username to transfer money to--

                                user_found = False  # Initialize user_found to False before the loop
                                for j in range(user_number):
                                    x = userlist[j]
                                    user_name_check = x.get("name")
                                    if user_name_2 == user_name_check:
                                        user_found = True  # Set user_found to True if a matching username is found

# --Taking input to transfer the money, checking if it is a valid input, then updating
# the balance of both accounts--

                                        transfer_value = input("How much money do you wish to transfer \n")
                                        if transfer_value.isdigit():
                                            if int(transfer_value) <= user_balance:
                                                userlist[i]["balance"] = userlist[i]["balance"] - int(transfer_value)
                                                userlist[j]["balance"] = userlist[j]["balance"] + int(transfer_value)
                                                print("Your balance is", userlist[i]["balance"])
                                                break
                                            else:
                                                print("Balance is insufficient")
                                        else:
                                            print("Invalid input!")
                                        break  # Exit the loop once the transfer is processed

                                if not user_found:
                                    print("Wrong username")
                            else:
                                print("Invalid input!")
                                choice2 = 0
                        break

# --Giving an error if the wrong password to the account was entered

                    else:
                        print("Wrong password")
                    break
                elif i == (user_number - 1):
                    print("Wrong username")

# --Code to create a new account

    elif choice1 == "2":
        user_name = input("Enter your name \n")

# --Checking it the username exists or not, and exiting if it does

        for i in range(user_number):
            x = userlist[i]
            user_name_check = x.get("name")
            if user_name == user_name_check:    
                print("This username already exists!")
                exit()

# --Checking if the correct password is entered both times--

        user_pass = input("Enter your password \n")
        user_pass_check = input("Confirm password \n")
        while user_pass != user_pass_check:
            print("The passwords do not match!")
            user_pass_check = input("Confirm password again \n")

# --Updating the user list with the new account, and setting default balance to zero--

        new_entry = {"name" : "" , "pass" : "" , "balance" : 0}
        new_entry["name"] = user_name
        new_entry["pass"] = user_pass
        userlist.append(new_entry)
        user_number = len(userlist)
        temp_list = []  # Reinitialize temp_list before updating it
        for k in range(user_number):
            temp_list.append(userlist[k]["name"])
            temp_list.append(userlist[k]["pass"])
            temp_list.append(str(userlist[k]["balance"]))

# --Updating the text file--

        with open('test.txt', 'w') as file2:
            line = ''
            for l in range(len(temp_list)):
                line = line + temp_list[l] + "\n"
            file2.write(line)
        file2.close()

# --Option to exit program--

    elif choice1 == "3":
        exit()

# --Printing error if invalid value is entered

    else:
        choice1 = "0"
        print("Invalid")
