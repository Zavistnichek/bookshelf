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


input_1 = input('Enter the elements of the first'
                'tuple separated by spaces: ')
input_2 = input('Enter the elements of the second'
                'tuple separated by spaces: ')
tuple_1, tuple_2 = (tuple(parse_element(e) for e in input_1.split()),
                    tuple(parse_element(e) for e in input_2.split()))
union_tuple = tuple_1 + tuple_2
print('Union tuple:', union_tuple)
