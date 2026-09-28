class Calculator:
    def subtraction(self,n):
        result = n[0]
        for i in n[1:]:
            result -= i
        return result
    def addition(self,n):
        result = 0
        for i in n:
            result += i
        return result
    def multiplication(self,n):
        result = 1
        for i in n:
            result *= i
        result = round(result, 4)
        return result  
    def division(self,n):
        try:
            result = n[0]
            for i in n[1:]:
                result /= i
            return result
        except ZeroDivisionError:
            a1="Division by zero is not possible"
            return a1
        except IndexError:
            a2="Please enter atleast two number to do operation"
            return a2
cal=Calculator()
add_history=[]
sub_history=[]
mul_history=[]
division_history=[]
import time
while True:
    print("\n=======================================================")
    print("\tWelcome to the Simple Math Calculator")
    print("=======================================================")
    print("Select the operation you want to perform:")
    print("1. Addition")                            
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. History")
    print("6. Exit")
    try:
       choice =int(input("Enter the choice 1-2-3-4-5-6 :"))
       if choice not in [1,2,3,4,5,6]:
           print("The given choice is not valid, Pleae select the valid choice ")
           continue
    except ValueError:
        a3="Invalid input. Please enter a number."
        print(a3)
        continue
    except IndexError:
        a4="Please enter the required number of values."
        print(a4)
        continue
    if choice == 6:
        print("--------------------------------")
        print("Exiting the calculator. Goodbye!")
        print("--------------------------------")
        time.sleep(2)
        break
    elif choice == 1:
        print(f"\nYou have selected chioice: {choice}")
        print("You have selected Addition Operation\n")
    elif choice == 2:
        print(f"\nYou have selected choice: {choice}")
        print("You have selected Subtraction Operation\n")
    elif choice == 3:
        print(f"\nYou have selected choice: {choice}")
        print("you have selected choice Multiplication Operation\n")
    elif choice == 4:
        print(f"\nYou have selected the choice: {choice}")
        print("You have selected the Divison Operation")
        print("=========")
        print("Please enter at least two numbers for division.")
        print("==========")
        print("If you enter only one number, the result will be the same as the input number.\n")
    elif choice == 5:
        print("\n--------------- HISTORY ---------------")
        print("\nAddition History:\n")
        if not add_history:
            print("\tNo addition history available.")
        for i in add_history:
            print(i)
        print("\nSubtraction History:\n")
        if not sub_history:
             print("\tNo subtraction history available.")
        for i in sub_history:
            print(i)
        print("\nMultiplication History:\n")
        if not mul_history:
            print("\tNo multiplication history available.")
        for i in mul_history:
            print(i)
        print("\nDivision History:\n")
        if not division_history:
            print("\tNo division history available.")
        for i in division_history:
            print(i)   
        print("\n----------------------------------------")
        continue
    try:
        a=input_numbers=list(map(float,input("Enter the numbers separated with \'-\' :").split('-')))
        if choice == 1:
            print("\n===============Addition Operation===============\n")        
            print("The numbers you have entered\n",str(a),end="\n\n")
            print("----------------------------------------------")
            print("The sum of the numbers is : ",cal.addition(a))
            print("----------------------------------------------")
            add_history.append(f"{a} = {cal.addition(a)}")
            print("================================================")
        elif choice == 2:
            print("\n===============Subtraction Operation===============\n")
            print("The numbers you have entered\n",str(a),end="\n\n")
            print("----------------------------------------------")
            print("The difference of the numbers is : ",cal.subtraction(a))
            print("----------------------------------------------")
            sub_history.append(f"{a} = {cal.subtraction(a)}")
            print("\n================================================")
        elif choice == 3:
            print("\n===============Multiplication Operation===============\n")
            print("The numbers you have entered\n",str(a),end="\n\n")
            print("----------------------------------------------")
            print("The product of the numbers is : ",cal.multiplication(a))
            print("----------------------------------------------")
            mul_history.append(f"{a} = {cal.multiplication(a)}")
            print("\n================================================")
        elif choice == 4:
            if len(a) < 2:
                a.append(1)
            print("\n===============Division Operation===============\n")
            print("The numbers you have entered\n",str(a),end="\n\n")
            print("----------------------------------------------")
            print("The quotient of the numbers is : ",cal.division(a))
            print("----------------------------------------------")
            division_history.append(f"{a} = {cal.division(a)}")
            print("\n================================================")
    except ValueError:
        a5="Invalid input. Please enter valid numbers separated by '-'."
        print(a5)    