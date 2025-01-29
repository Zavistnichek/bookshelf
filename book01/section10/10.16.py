def sum_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length!")
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result


list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
result_list = sum_lists(list_a, list_b)

print(f"Sum result: {result_list}")
