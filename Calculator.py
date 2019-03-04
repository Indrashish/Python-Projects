# Python script to implement the basic functionality of a scientific calculator

# Below methods defining the following functionality respectively
# 1.Add 2.Subtract 3.Multiply 4.Divide

class Calculator:
    # Add
    def add(self, num1, num2):
        return num1 + num2
    # Subtract
    def sub(self, num1, num2):
        return num1 - num2

    # Multiply
    def mul(self, num1, num2):
        return num1 * num2

    # Divide
    def div(self, num1, num2):
        try:
            return num1 / num2
        except Exception as err:
            raise Exception("Division by zero not possible!")
            return 0

    # performoperation: Method which performs operation as per user input
    def performoperation(self, option, num1, num2):
        print("Option =", option)
        if option == 1:
            print("Ready to add")
            print(self.add(self, num1, num2))
        elif option == 2:
            print("Ready to subtract")
            print(self.sub(self, num1, num2))
        elif option == 3:
            print("Ready to multiply")
            print(self.mul(self, num1, num2))
        elif option == 4:
            print("Ready to divide")
            print(self.div(self, num1, num2))
        else:
            print("Operation not valid")

    # Main function
    def main(self):
        while True:
            num1 = int(input("Enter 1st number: "))
            num2 = int(input("Enter 2nd number: "))

            option = int(input("What do you want to do? 1. Add 2. Subtract 3. Multiply 4. Divide. Enter your choice: "))
            self.performoperation(self, option, num1, num2)

            # We ask user if they want to use the calculator further
            user_input = int(input("Do you want to continue? 1. Yes 2. No"))

            if(user_input != 1):
                print("Exiting Calculator.....")
                break


cal = Calculator
Calculator.main(cal)

#main()
#if __name__ == '__main__':
#    main()
