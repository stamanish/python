a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

print('1. Add\n2. Subtract\n3. Divide')
c = int(input('Choose operation (1/2/3): '))

if c == 1:
    print(f'Result: {a + b}')
elif c == 2:
    print(f'Result: {a - b}')
elif c == 3:
    print(f'Result: {a / b if b != 0 else "Division by zero error"}')
else:
    print('Invalid input')
