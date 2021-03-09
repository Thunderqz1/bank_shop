import textwrap
import time
import sys

groceries = {'fruit' : 40, 'veggies': 50, 'petfood': 100, 'King' : 'priceless'}
local_bank = [] # making arrays for numbers
sub_main_bank = []
deposit_dict = ["amount","description"]
dummy_list = []




print("******** WELCOME TO FOOD KING ************")
print("\n")


class Category:





        
    def shopping(self):

        
         
        print(textwrap.dedent("""
            What would you like?
            Fruit - $40
            Veggies - $50
            Petfood - $100
            King
            write 'done' to exit
            

        """))

        while True:
            
            user_shop = input("What would you like > ")
            
            

            
            if user_shop == "fruit" or user_shop == "Fruit":
                fruity = sub_main_bank[0] - 40
                sub_main_bank.clear()
                sub_main_bank.append(fruity)
                print("You have pruchased fruit for $", groceries['fruit'] )
                continue
                
                
            elif user_shop == "Veggies" or user_shop == "veggies":
                veggie = sub_main_bank[0] - 50
                sub_main_bank.clear()
                sub_main_bank.append(veggie)
                print("You have purchased fruit for $", groceries['veggies'] )
                continue
                
                
            elif user_shop == "Petfood" or user_shop == "petfood":
                petfoods = sub_main_bank[0] - 100
                sub_main_bank.clear()
                sub_main_bank.append(petfoods)
                print("You have purchased fruit for $", groceries['petfood'] )
                continue
            
                    
                    
                
            elif user_shop == "King" or user_shop == "king":
                print("Congrats! You have activated the secret self destruct code")
                cheatcode = (textwrap.dedent("""
                1
                2
                3
                Goodbye :)
                """))
                for c in cheatcode:
                    sys.stdout.write(c)
                    time.sleep(0.2)
                quit()
            
            elif user_shop == "done" or user_shop == "Done":
                self.main()
            

            else:
                print("Not enough funds, please deposit more")
                print("*" * 52)
                print ("*YOU ARE NOW BEING TAKEN TO DEPOSIT* \n")
                print("\n")
                return self.deposit_amount()
    

    def deposit_amount(self):
        print("Enter Deposit amount below: - write 'done' to finish deposit")
        print("Your bank total is", sub_main_bank)
        

        
        while True:

            user_deposit = input("Deposit: ")
            totald = sum(local_bank)
            # jaj = sum(sub_main_bank)

            if user_deposit == 'done':
                # total = sum(local_bank)
                print("Your added amounts were", local_bank)
                print("Total amount added",totald)
                # ftotal = sum(local_bank)
                # banktotal = ftotal
                sub_main_bank.append(totald)
                local_bank.clear()
                adding_it = sum(sub_main_bank)
                sub_main_bank.clear()
                sub_main_bank.append(adding_it)
                print(sub_main_bank, "********* TEST*******")
                self.main()
            

            try:
                floatting = float(user_deposit)
                local_bank.append(floatting)
                print("Transfering  amount", floatting, "to main wallet")
                print("*" * 50)

                 
            except:
                print("Sorry, that is not a number")
    
    def withdraw_amount(self):
        print("Enter Deposit amount below: - write 'done' to finish deposit")
        print("Your bank total is", sub_main_bank)

        while True:
            user_withdraw = input("Withdraw: ")
            totalw = sum(local_bank)



            if user_withdraw == 'done':
                print("Your withdrawn amounts were", local_bank)
                print("Total amount taken",totalw)
                local_bank.clear()
                print(sub_main_bank, "********* TEST*******")
                self.main()

            
                
    
            
            try:
                floater = float(user_withdraw)
                local_bank.append(floater)
                add_to_sub = sum(local_bank)
                print("You took out",totalw)
                print("*" * 50)
                subtract = sub_main_bank[0] - add_to_sub

                if sub_main_bank[0] == 0 or sub_main_bank[0] < floater:
                    print("Sorry you have to add more")
                print("Your new total is",subtract)
                sub_main_bank.clear()
                sub_main_bank.append(subtract)

                

            except:
                print("Sorry, can't do that")


            


    
    
    def main(self):
        print("Please choose if you want to 'shop', 'deposit', or 'withdraw'") # has to be inside a method so it reverts back to this
        print("*" * 50)
        print("write 'quit' to quit")
        print("\n")
        
        print(">>>>", sub_main_bank)
        user = input(">")        
        if user == 'deposit' or user == 'Deposit':
            self.deposit_amount()
        
        elif user == "withdraw" or user == "Withdraw":
            self.withdraw_amount()
        
        elif user == "shop" or user == "Shop":
            self.shopping()
        
        elif user == 'quit' or user == 'Quit':
            quit()
        else:
            print("Sorry that's not a choice, please try again \n ")
            self.main()
    
        

a = Category()
a.main()


