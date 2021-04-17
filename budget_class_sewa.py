#create class budget
#different budget categories
#create functions : 1. deposit funds to each category 2. withdraw funds fromm each category 3. compute category balance 4. transfer balance amounts btw categories



class Budget:
    """
    Create a budget class
    """
    budget_balance = [0,0,0]
    budget_category = ["Food", "Vacation", "Rent" ]

    """
    create list for the balance and the category
    """

    def __init__(self, category): #using the constructor function to create parameters
        self.category = category - 1
        

    """
    Below are functions defined for budget operations
    Operations such as withdrawal, deposit, balance checking etc.
    """
    def budget_operation(self): #a func. defined to cater for different budgets operations and options
        selectedOption = int(input("What would you like to do? 1. deposit 2. withdrawal 3. Compute category balance 4. Transfer balance amount \n"))
        if selectedOption == 1:
            self.deposit()
        elif selectedOption == 2:
            self.withdrawal()
        elif selectedOption == 3:
            self.balance()
        elif selectedOption == 4:
            self.transfer()
        else: 
            print("invalid input")
            self.another_operation()

    def deposit(self): #deposit function created showing current amount, and other deposit transaction
        print(f"Your current {self.budget_category[self.category]} budget : {self.budget_balance[self.category]} naira")
        amount_deposit = int(input("How much would you like to deposit? \n"))
        self.budget_balance[self.category] += amount_deposit
        print(f"Your current {self.budget_category[self.category]} budget : {self.budget_balance[self.category]} naira")
        self.another_operation()
               

    def withdrawal(self): #withdrawal function created showing current amount, and other withdrawal transaction and also actions for invalid options selected
        print(f"Your current {self.budget_category[self.category]} budget : {self.budget_balance[self.category]} naira")
        amount = int(input("How much would you like to withdraw? \n"))
        if amount > self.budget_balance[self.category]:
            another_option = input("You have insufficient funds. To withdraw a lower amount, PRESS (Y) Yes or (N) No.")
            if another_option == "Y":
                self.withdrawal()
                self.another_operation()
            elif another_option == "N":
                withdrawal_amount = int(input("Would you like to withdraw a different amount or log out? (1) Yes or (2) No \n"))
                if withdrawal_amount == 1:
                    self.withdrawal()
                else:
                    self.another_operation()
        else:
            print("Your transaction is processing...")
            self.budget_balance[self.category] -= amount
            print(f"Your transaction has been completed, current balance : {self.budget_balance[self.category]} naira")
            self.another_operation()
        
    def balance(self): #function computing balance
        print("Processing Transaction......")
        print(f"Your {self.budget_category[self.category]} budget is: {self.budget_balance[self.category]}")
        print("Transaction completed")
        self.another_operation()

    def transfer(self): #function to transfer funds
        print("Choose budget to transfer to: ")
        print("1. Food")
        print("2. Vacation")
        print("3. Rent")
        selection = int(input(": "))

        if(selection <= 3):
            selection -= 1
            
            print("Processing Transfer...")
            amount = int(input("Enter amount to transfer: \n"))
                    
            if(selection == self.category):
                print("Cannot transfer funds, same budget fund selected. \nTransaction failed!")
                self.another_operation()

            elif(self.budget_balance[selection] != 0 or amount > self.budget_balance[selection]):
                print("Processing Transaction...")
                self.budget_balance[selection] -= amount
                self.budget_balance[(self.category - 1)] += amount                        
                print("Transaction Completed!")
                self.another_operation()
            else:
                print("Insufficient Funds!")
                self.another_operation()

        else:

            print("Invalid input")
            self.another_operation()
    

    def another_operation(self): # a sort of loop function created in place of a while loop
        option = int(input("Would you like to perform another operation? (1) Yes or (2) No\n"))
        if option == 1:
            self.budget_operation()
        else:
            print("Invalid option, read carefully before selecting.")
            self.another_operation()


def init(): #an init function used to call instances of the budget class and methods
    selection = input("Kindly select the budget you'd like to work on today. (1) Food (2) Vacation (3) Rent \n")

    if (selection == "1"):
        budget = Budget(1)
        budget.budget_operation()
    elif(selection == "2"):
        budget = Budget(2)
        budget.budget_operation()
    elif(selection == "3"):
        budget = Budget(3)
        budget.budget_operation()
    else:
        print("Invalid input")
        budget.another_operation()

init() #activing the budget class so user can operate as they see fit
