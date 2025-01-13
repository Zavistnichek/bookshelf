number = int(input("Введите число: "))
original = str(number)
reversed_number = ""

for char in original:
    reversed_number =  char + reversed_number

if original == reversed_number:
    print("Число является палиндромом")
else:
    print("Число не является палиндромом")
