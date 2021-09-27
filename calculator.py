#!usr/bin/python3

def check_user_input(number):
    try:
        return float(number)
    except ValueError:
        return None


def additon(number1, number2):
    return number1 + number2


def substrction(number1, number2):
    return number1 - number2

    
def division(number1, number2):
    if number2 == 0:
        return "Can't divide by 0."
    return number1 / number2


def multiplication(number1, number2):
    return number1 * number2


def display_result(result):
    print(f'Result : {result}')


def welcome():
    print('\n-------------------------------------------------')
    print('welcome to Python calculator\n')
    print("""This is a well written calculator in python.\n
    **Please don't use a-z or A-Z for number inputs.""")
    print('-------------------------------------------------\n')


def operation_function():
    is_quit = True
    operations = ['+', '-', '/', '*']
    is_error = False

    while is_quit:

        number1 = check_user_input(input('Enter a number : '))
        if number1 is None:
            print('Error - Please enter numeric value to calculate.')
            is_error = True
        else:
            operation = input('Enter operation : ')
            if operation not in operations:
                print("Error - Please select a operation form '+', '-', '/', '*'.")
                is_error = True
            else:
                number2 = check_user_input(input('Enter second number : '))
                if number2 is None:
                    print('Error - Please enter numeric value to calculate.')
                    is_error = True
            
        if is_error:
            is_error = False
            print('Start again your calculation.\n')
            operation_function()

        if operation == operations[0]:
            display_result(additon(number1, number2))
        elif operation == operations[1]:
            display_result(substrction(number1, number2))
        elif operation == operations[2]:
            display_result(division(number1, number2))
        elif operation == operations[3]:
            display_result(multiplication(number1, number2))

        print('\n')
    else:
        print('you are quitting, Bay')


# main function
def main():
    welcome()
    operation_function()


# main function call
if __name__ == "__main__":
    main()
