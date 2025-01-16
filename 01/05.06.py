def parse_element(element):
    element = element.strip()
    if element.isdigit():
        return int(element)
    try:
        return float(element)
    except ValueError:
        if element.lower() == 'true':
            return True
        elif element.lower() == 'false':
            return False
    return element


user_input = input('Enter the elements of the tuple separated by spaces: ')
user_index_1 = int(input('Enter the first index for slicing the tuple: '))
user_index_2 = int(input('Enter the second index for slicing the tuple: '))
user_tuple = tuple(parse_element(e) for e in user_input.split())
sliced = user_tuple[user_index_1:user_index_2]
print('Sliced tuple:', sliced)
