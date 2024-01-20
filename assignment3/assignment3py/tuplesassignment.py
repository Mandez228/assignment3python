print("#1 list creation")
fruits = []
for f in range(5):
    fruit = input("Enter favourite fruit: ")
    fruits.append(fruit)
print("List of fruits: ", fruits)
print("**********************")


print("#2 list slicing")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slicing = list1[2:7]
print("Middle five elements: ", slicing)
print("**********************")


print("#3 tuple conversion")
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
input3 = int(input("Enter third number: "))
numbers = (input1, input2, input3)
print(numbers)
print("**********************")


print("#4 list operations")
list_ex = list(map(int, input("Enter a list of nums separated by space: ").split()))
list_app = int(input("Enter a number to add in the end: "))
list_ex.append(list_app)
print("Added number in the end: ", list_ex)
list_ex.pop(0)
print("Removed first item: ", list_ex)
list_ex.sort()
print("Sorted list: ", list_ex)
print("**********************")


print("#5 element search")
list_f = list(map(int, input("Enter a list of nums separated by space: ").split()))
search = int(input("Enter a number to search in list: "))
if search in list_f:
    print(f"The number {search} is in the list")
else:
    print(f"The number {search} is not in the list")
print("**********************")


print("#5 list reversal")
list_r = list(map(int, input("Enter a list of nums separated by space: ").split()))
print("Entered list", list_r)
list_r.reverse()
print("Reversed list", list_r)
print("**********************")


print("#7 tuple unpacking")
tuple_u = tuple(map(int, input("Enter 4 numbers separated by space: ").split()))
print("Tuple:", tuple_u)
a, b, c, d = tuple_u
print("Unpacked elements of tuple:", a, b, c, d)
print("**********************")


print("8 maximum and minimum")
u_input = list(map(int, input("Enter the list of nums separated by space: ").split()))
max_num = max(u_input)
min_num = min(u_input)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
print("**********************")


print("#9 concatenate lists")
list1 = list(map(int, input("Enter the list of nums separated by space: ").split()))
list2 = list(map(int, input("Enter the list of nums separated by space: ").split()))
c_list = list1 + list2
print("Concatenated list:", c_list)
print("**********************")


print("#10 list to tuple")
user_input = list(map(int, input("Enter the list of nums separated by space: ").split()))
print(user_input)
user_tuple = tuple(user_input)
print("Converted tuple:", user_tuple)
print("**********************")
