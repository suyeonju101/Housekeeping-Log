from pathlib import Path
from Exceptions import WrongInputError
import Tools
import Home
import Grocery
import Personal
import Uber
import Others
import HousekeepingLog


### Main.py


if __name__ == "__main__":
    HOME = Home.Home()
    GROCERY = Grocery.Grocery()
    PERSONAL = Personal.Personal()
    UBER = Uber.Uber()
    OTHERS = Others.Others()
    
    while True:
        try:
            user_input = input("HOME / GROCERY / PERSONAL / UBER / OTHERS / QUIT\nEnter your option: ")
            
            # CASE 1. QUIT
            if (user_input == "QUIT"):
                statistic = HousekeepingLog.analyzeHousekeepingLog(HousekeepingLog.gatherHousekeepingLog())
                Tools.printResult(statistic)
                print("Goodbye :)")
                break

            # CASE 2. HOME
            elif (user_input == "HOME"):
                while True:
                    try:
                        print("[MESSAGE] IN ORDER TO EXIT, ENTER E.")
                        print("[MESSAGE] IF NOT, ENTER C.")
                        user_input_check = input("[TYPEHERE] E | C : ")

                        if (user_input_check == "E"):
                            break
                        elif (user_input_check == "C"):
                            if Tools.checkFile(user_input):
                                user_input_product = input("Prdouct: ")
                                user_input_amount = float(input("Amount: "))

                                HOME.setProduct(user_input_product)
                                HOME.setAmount(user_input_amount)
                                HOME.updateTotalAmount()
                                print("----[DEBUGING] {}".format(HOME.getAmount()))
                                HOME.writeCSVFile()
                                print("[MESSAGE] Successfully Update the Log!")
                            else:
                                HOME.createCSVFile()
                                print("[MESSAGE] Successfully Create the Log!")
                        else:
                            raise WrongInputError

                    except WrongInputError:
                        print("[WARNING] WRONG INPUT")

            # CASE 3. GROCERY 
            elif (user_input == "GROCERY"):
                while True:
                    try:
                        print("[MESSAGE] IN ORDER TO EXIT, ENTER E.")
                        print("[MESSAGE] IF NOT, ENTER C.")
                        user_input_check = input("[TYPEHERE] E | C : ")

                        if (user_input_check == "E"):
                            break
                        elif (user_input_check == "C"):
                            if Tools.checkFile(user_input):
                                user_input_product = input("Prdouct: ")
                                user_input_amount = float(input("Amount: "))

                                GROCERY.setProduct(user_input_product)
                                GROCERY.setAmount(user_input_amount)
                                GROCERY.updateTotalAmount()

                                GROCERY.writeCSVFile()
                                print("[MESSAGE] Successfully Update the Log!")
                            else:
                                GROCERY.createCSVFile()
                                print("[MESSAGE] Successfully Create the Log!")
                        else:
                            raise WrongInputError

                    except WrongInputError:
                        print("[WARNING] WRONG INPUT")
                        
            # CASE 4. PERSONAL
            elif (user_input == "PERSONAL"):
                while True:
                    try:
                        print("[MESSAGE] IN ORDER TO EXIT, ENTER E.")
                        print("[MESSAGE] IF NOT, ENTER C.")
                        user_input_check = input("[TYPEHERE] E | C : ")

                        if (user_input_check == "E"):
                            break
                        elif (user_input_check == "C"):
                            if Tools.checkFile(user_input):
                                user_input_product = input("Prdouct: ")
                                user_input_amount = float(input("Amount: "))

                                PERSONAL.setProduct(user_input_product)
                                PERSONAL.setAmount(user_input_amount)
                                PERSONAL.updateTotalAmount()

                                PERSONAL.writeCSVFile()
                                print("[MESSAGE] Successfully Update the Log!")
                            else:
                                PERSONAL.createCSVFile()
                                print("[MESSAGE] Successfully Create the Log!")
                        else:
                            raise WrongInputError
                        
                    except WrongInputError:
                        print("[WARNING] WRONG INPUT")

            # CASE 5. UBER
            elif (user_input == "UBER"):
                while True:
                    try:
                        print("[MESSAGE] IN ORDER TO EXIT, ENTER E.")
                        print("[MESSAGE] IF NOT, ENTER C.")
                        user_input_check = input("[TYPEHERE] E | C : ")

                        if (user_input_check == "E"):
                            break
                        elif (user_input_check == "C"):
                            if Tools.checkFile(user_input):
                                user_input_trip = input("Trip: ")
                                user_input_amount = float(input("Amount: "))

                                UBER.setTrip(user_input_trip)
                                UBER.setAmount(user_input_amount)
                                UBER.updateTotalAmount()

                                UBER.writeCSVFile()
                                print("[MESSAGE] Successfully Update the Log!")
                            else:
                                UBER.createCSVFile()
                                print("[MESSAGE] Successfully Create the Log!")
                        else:
                            raise WrongInputError
                        
                    except WrongInputError:
                        print("[WARNING] WRONG INPUT")

            # CASE 6. OTHERS     
            elif (user_input == "OTHERS"):
                while True:
                    try:
                        print("[MESSAGE] IN ORDER TO EXIT, ENTER E.")
                        print("[MESSAGE] IF NOT, ENTER C.")
                        user_input_check = input("[TYPEHERE] E | C : ")

                        if (user_input_check == "E"):
                            break
                        elif (user_input_check == "C"):
                            if Tools.checkFile(user_input):
                                user_input_product = input("Prdouct: ")
                                user_input_amount = float(input("Amount: "))

                                OTHERS.setProduct(user_input_product)
                                OTHERS.setAmount(user_input_amount)
                                OTHERS.updateTotalAmount()

                                OTHERS.writeCSVFile()
                                print("[MESSAGE] Successfully Update the Log!")
                            else:
                                OTHERS.createCSVFile()
                                print("[MESSAGE] Successfully Create the Log!")
                        else:
                            raise WrongInputError

                    except WrongInputError:
                        print("[WARNING] WRONG INPUT")

            HousekeepingLog.createHousekeepingLog(HousekeepingLog.gatherHousekeepingLog())

        except WrongInputError:
            print("[WARNING] WRONG INPUT")
        
            
