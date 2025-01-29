user_list = input("Enter a list of elements separated by spaces: ")
user_n = int(input("Enter the number n: "))
list_of_elements = user_list.split()

if len(list_of_elements) == 0:
    print("The list is empty")
else:
    n = user_n % len(list_of_elements)
    result = list_of_elements[-n:] + list_of_elements[:-n]
    print(result)
