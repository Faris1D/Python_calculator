
def my_calculator():
    num1 = float(input("Enter first num: "))
    oper = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Enter second num: "))

    if oper == '+':
        result = num1 + num2
        print(num1, '+', num2, '=', result)
    elif oper == '-':
        result = num1 - num2
        print(num1, '-', num2, '=', result)
    elif oper == '*':
        result = num1 * num2
        print(num1, '*', num2, '=', result)
    elif oper == '/':
        result = num1 / num2
        print(num1, '/', num2, '=', result)
    else:
        print('error')


def admin_login():
    my_data = ['faris', 'ahmed', 'khaled']
    user = input('username: ')
    password = input('password: ')

    if user == 'admin' and password == '123':
        print('welcome admin. your list:', my_data)
    else:
        print('error access')


print("Choose option:")
print("1 - my_Calculator")
print("2 - admin_Login")

choice = input("Enter your choice: ")

if choice == '1':
    my_calculator()
elif choice == '2':
    admin_login()
else:
    print("Invalid choice")
