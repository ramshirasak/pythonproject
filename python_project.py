import json
class Bank_account:
    acc_no = ''
    name = ''
    branch = ''
    acc_type = ''
    mail_id = ''
    phn_no = ''
    balance = 0
    userid = ''
    password = ''
    c_accno = ''
    personal_list_name = []

    def account_create(self):
       choice = ''
       self.acc_no = input(str("Enter Account Number: "))
       with open("bankdetailssaver.py","r")as file1:
           if(self.acc_no in file1.read()):
               print("Account already exists..Do you want to login?: ")
               self.login()

       if ((len(self.acc_no) > 11) or (len(self.acc_no) < 11)):
           print("Wrong... Account number should contain 11 digits")
           self.acc_no = input(str("Enter Account Number: "))
           with open("bankdetailssaver.py","r") as file1:
              if (self.acc_no) in file1.readlines():
                  print("The account already exist.....Please login!! ")
                  bank.login()
       self.name = input(str("Enter the account holder name: "))
       self.branch = input(str("Enter the branch: "))
       self.acc_type = input(str("Enter the account type(s/d): "))
       self.mail_id = input(str("Enter your mail id: "))
       self.phn_no = input(str("Enter your 10 digit mobile number: "))
       if(len(self.phn_no)!=10):
            print("Invalid mobile number")
            self.phn_no = input(str("Enter your 10 digit mobile number: "))
       self.balance = float(input("Enter the initial amount(savings account(>=500) and current account(>=1000): "))
       self.userid = str(input("Enter your user id: "))
       self.password = str(input("Enter Password: "))
       self.personal_list_name.append(self.acc_no)
       self.personal_list_name.append(self.name)
       self.personal_list_name.append(self.branch)
       self.personal_list_name.append(self.acc_type)
       self.personal_list_name.append(self.mail_id)
       self.personal_list_name.append(self.phn_no)
       self.personal_list_name.append(self.balance)
       self.personal_list_name.append(self.userid)
       self.personal_list_name.append(self.password)


       with open("bankdetailssaver.py", "a") as file1:
           file1.write(json.dumps(self.personal_list_name))

       print("Account created Successfully...")
       log = input("press 0 for login!! ")
       if(log == '0'):
           bank.login()

    def login(self):
        self.c_accno = str(input("Pls Confirm your account number: "))
        with open("bankdetailssaver.py","r")as file1:
            if(self.c_accno not in self.personal_list_name):
                print("Account not existing")
            else:
               c_userid = str(input("Enter your user id: "))
               c_password = str(input("Enter Password: "))
               with open("bankdetailssaver.py","r")as file1:
                    if(self.c_accno in file1.read()) :
                        if(self.c_accno==self.acc_no):
                           if((self.userid==c_userid) and (self.password==c_password)):
                              c = input("Do you want to continue?(Y/N)")
                              if (c == 'y' or c == 'Y'):
                                print("Successfully login")
                                while True:
                                   print("\t\tWelcome to the banking system")
                                   print("\t\t*****************************")
                                   print("1.1) Display")
                                   print("2.2) Deposit")
                                   print("3.3) Withdraw")
                                   print("4.4) Balance")
                                   print("5.5) Exit")
                                   choice = float(input("Enter your option: "))
                                   if (choice == 1.1):
                                      bank.display()
                                   if (choice == 2.2):
                                      deposit_amt = float(input("Enter the amount to be deposited : "))
                                      bank.deposit(deposit_amt)
                                   if (choice == 3.3):
                                      amount = float(input("Enter the amount you want to withdraw: "))
                                      bank.withdraw(amount)
                                   if (choice == 4.4):
                                      print("The current balance is ", self.balance)
                                   if (choice == 5.5):
                                      print("Thank you for using our services")
                                      break
                           else:
                               print("Incorrect login details")


    def withdraw(self,amount):
        try:

              if (amount > self.balance):
                print(f"Only {self.balance} in your account")
              else:
                self.balance -= amount
                self.personal_list_name[6] = self.balance
                print(f"Transaction Successfully completed...\nYour current balance is {self.balance}")
                with open("bankdetailssaver.py", "r+") as f:
                  f.truncate()
                with open("bankdetailssaver.py", "a") as file1:
                  file1.write(json.dumps(self.personal_list_name))
        except:
            print("Something wrong! Try again")
            bank.withdraw(amount)

    def deposit(self,deposit_amt):
        self.balance += deposit_amt
        self.personal_list_name[6] = self.balance
        with open("bankdetailssaver.py", "r+") as f:
            f.truncate()
        with open("bankdetailssaver.py", "a") as file1:
             file1.write(json.dumps(self.personal_list_name))
    def display(self):
        with open("bankdetailssaver.py", "r") as file1:
           if (self.personal_list_name[0]==self.c_accno):
                  print(self.personal_list_name[1])
                  print(self.personal_list_name[2])
                  print(self.personal_list_name[3])
                  print(self.personal_list_name[4])
                  print(self.personal_list_name[5])
                  print(self.personal_list_name[6])

    def exit(self):
          print("Thank you for using our banking system")

bank=Bank_account()

while True:
        print("\t\t\t\tBANK MANAGEMENT SYSTEM")
        print("\t\t\t\t**********************")
        print("\t\t1.Account Create")
        print("\t\t2.Login")
        print("\t\t3.Exit")
        choice = float(input("Enter your option: "))
        if (choice == 1):
            bank.account_create()
        if (choice == 2):
            bank.login()
        if (choice == 3):
            bank.exit()
        if (choice > 3):
            print("Wrong Choice......")
