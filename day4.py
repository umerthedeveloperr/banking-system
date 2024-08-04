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

temp_list = []
user_number = len(userlist)

choice1 = "0"
while (choice1 == "0") or (choice1 == "1") or (choice1 == "2"):
    choice1 = input("Enter 1 to login, 2 to signup, 3 to exit")
    if choice1 == "1":
        user_name = input("Enter your name")
        user_pass = input("Enter your password")
        if user_name == "Admin" and user_pass == "11111":
            choice3 = "0"
            while choice3 == "0" or choice3 == "1" or choice3 == "2":
                choice3 = input("Enter 1 to delete user, 2 to exit")
                if choice3 == "1":
                    delete_user = input("Which user do you want to delete")
                    while delete_user == "Admin":
                        delete_user = input("You cannot deelete admin account! Enter again")
                    name_found = any(item["name"] == delete_user for item in userlist)
                    if name_found:
                        userlist = [item for item in userlist if item["name"] != delete_user]
                        print(f"{delete_user} has been deleted.")
                    else:
                        print(f"{delete_user} not found in the list.")
                    user_number = len(userlist)
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
                    print(temp_list)
                    print(userlist)
                elif choice3 == "2":
                    exit()
                else:
                    choice3 == "0"
                    print("Invalid input!")
        else:
            for i in range(user_number):
                x = userlist[i]
                user_name_check = x.get("name")
                user_pass_check = x.get("pass")
                if user_name == user_name_check:
                    if user_pass == user_pass_check:
                        choice2 = 0
                        user_balance = x.get("balance")
                        print("Your account balance is" , {user_balance})
                        while (choice2 == 0) or (choice2 == 1) or (choice2 == 2) or (choice2 == 3) or (choice2 == 4):
                            choice2 = int(input("Enter 1 to Deposit, 2 to Withdraw, 3 to Transfer, 4 to Exit"))
                            if choice2 == 4:
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
                                print(temp_list)
                                print(userlist)
                                exit()
                            elif choice2 == 1:
                                deposit_value = input("Enter your deposit value")
                                if deposit_value.isdigit():
                                    user_balance = user_balance + int(deposit_value)
                                    print("Your balance is" , {user_balance})
                                    userlist[i]["balance"] = user_balance
                                else:
                                    print("Invalid input!")
                            elif choice2 == 2:
                                withdraw_value = input("Enter the value you wish to withdraw")
                                if withdraw_value.isdigit():
                                    if user_balance < int(withdraw_value):
                                        print("Insufficient funds in account")
                                    elif user_balance >= int(withdraw_value):
                                        user_balance = user_balance - int(withdraw_value)
                                        print("Your balance is" , {user_balance})
                                        userlist[i]["balance"] = user_balance
                                else:
                                    print("Invalid input!")
                            elif choice2 == 3:
                                user_name_2 = input("Who do you wish to transfer money to?")
                                while user_name_2 == user_name:
                                    user_name_2 = input("You cannot enter your own name! Enter again")
                                for j in range(user_number):
                                    x = userlist[j]
                                    user_name_check = x.get("name")
                                    if user_name_2 == user_name_check:
                                        user_found = True
                                        transfer_value = input("How much money do you wish to transfer")
                                        if transfer_value.isdigit():
                                            if int(transfer_value) <= user_balance:
                                                userlist[i]["balance"] = userlist[i]["balance"] - int(transfer_value)
                                                userlist[j]["balance"] = userlist[j]["balance"] + int(transfer_value)
                                                print("Your balance is" , {userlist[i]["balance"]})
                                                break
                                            else:
                                                print("Balance is insufficient")
                                        else:
                                            print("Invalid input!")
                                    else:
                                        user_found = False
                                if not user_found:
                                    print("Wrong username")
                            else:
                                print("Invalid input!")
                                choice2 = 0
                        break
                    else:
                        print("Wrong password")
                    break
                elif i == (user_number - 1):
                    print("Wrong username")
    elif choice1 == "2":
        user_name = input("Enter your name")
        for i in range(user_number):
            x = userlist[i]
            user_name_check = x.get("name")
            if user_name == user_name_check:    
                print("This username already exists!")
                exit()
        user_pass = input("Enter your password")
        user_pass_check = input("Confirm password")
        while user_pass != user_pass_check:
            print("The passwords donot match!")
            user_pass_check = input("Confirm password again")
        new_entry = {"name" : "" , "pass" : "" , "balance" : 0}
        new_entry["name"] = user_name
        new_entry["pass"] = user_pass
        userlist.append(new_entry)
        user_number = len(userlist)
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
    elif choice1 == "3":
        exit()
    else:
        choice1 = "0"
        print("Invalid")
