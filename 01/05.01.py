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
user_tuple = tuple(parse_element(e) for e in user_input.split())
print('Created tuple:', user_tuple)
