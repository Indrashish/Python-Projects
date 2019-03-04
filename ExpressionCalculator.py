# Python script to implement parsing of an expression using the basic functionality of a scientific calculator

# Take input expression from user
# Parse the expression
# Calculate the expression and print out the final answer

# Import Stack file for using the basic features of the stack class
from Stack import Stack

class ExpressionCalculator:

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
    def performoperation(self, operator, num1, num2):
        if operator == "+":
            # print("Ready to add")
            return self.add(float(num1), float(num2))
        elif operator == "-":
            # print("Ready to subtract")
            return self.sub(float(num1), float(num2))
        elif operator == "*":
            # print("Ready to multiply")
            return self.mul(float(num1), float(num2))
        elif operator == "/":
            # print("Ready to divide")
            return self.div(float(num1), float(num2))

    def isnumber(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    # infixtopostfix: method which parses the regular character by character as per operands, operator and parenthesis
    def infixtopostfix(self, exp):
        priority_dict = {"-": 1, "+": 1, "*": 2, "/": 2}
        result = []
        infixtopostfixstack = Stack()
        tokenlist = exp.split()
        for token in tokenlist:
            if self.isnumber(token):
                result.append(token)
            elif token == "(":
                infixtopostfixstack.push(token)
            elif token == ")":
                while not infixtopostfixstack.isempty():
                    # print(stack1.peek() + " is the current top")
                    if infixtopostfixstack.peek() == "(":
                        break
                    result.append(infixtopostfixstack.peek())
                    infixtopostfixstack.pop()
                infixtopostfixstack.pop() # Popping the "("
            elif token in ["+", "-", "*", "/"]:
                # print(token + " detected")
                while not infixtopostfixstack.isempty():
                    # print(stack1.peek() + " is the current top :" + priority_dict[token] + " is the priority of the operator")
                    if infixtopostfixstack.peek() == "(":
                        break
                    if priority_dict[infixtopostfixstack.peek()] >= priority_dict[token]:
                        result.append(infixtopostfixstack.peek())
                        infixtopostfixstack.pop()
                    else:
                        break
                infixtopostfixstack.push(token)
            else:
                raise Exception("Input character not supported")

        # Print out the result list
        while not infixtopostfixstack.isempty():
            if infixtopostfixstack.peek() in ["+", "-", "*", "/"]:
                result.append(infixtopostfixstack.peek())
                infixtopostfixstack.pop()
        # print(result)
        return result

    # evalpostfix: this method evaluates the list, then calculate and return the final answer
    def evalpostfix(self, after_postfix_list):
        evalstack = Stack()
        for index in range(len(after_postfix_list)):
            # if not evalstack.isempty():
            #    print("Stack top is : " + evalstack.peek())
            # print("Index = ", index, " Value at index =  ", after_postfix_list[index])
            if after_postfix_list[index] in ["+", "-", "*", "/"]:
                num2 = evalstack.pop()
                num1 = evalstack.pop()
                result = str(self.performoperation(after_postfix_list[index], num1, num2))
                evalstack.push(result)
            else:
                evalstack.push(after_postfix_list[index])
        return evalstack.pop()

    # Main function
    def main(self):
        while True:
            expression = input("Please enter the expression: ")
            result_list = self.infixtopostfix(expression)
            print(result_list)
            result = self.evalpostfix(result_list)
            print("Final Value: ", result)

            # We ask user if they want to use the calculator further
            user_input = int(input("Do you want to continue? 1. Yes 2. No"))

            if (user_input != 1):
                print("Exiting Calculator.....")
                break


cal = ExpressionCalculator()
# ExpressionCalculator.main(cal)
cal.main()