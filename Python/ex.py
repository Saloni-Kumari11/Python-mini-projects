def search_value_in_list(value, lst):
    for index in range(len(lst)):
        if lst[index] == value:
            return index  
    return -1  

numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers.split()]

value_to_search = int(input("Enter the value to search for: "))


index = search_value_in_list(value_to_search, numbers_list)


if index != -1:
    print(f"Value {value_to_search} found at index {index}.")
else:
    print(f"Value {value_to_search} not found in the list.")