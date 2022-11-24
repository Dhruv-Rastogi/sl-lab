lists = []

n = int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(0, n):
    element = int(input())
    lists.append(element)
print(lists)

while True:
    print("MAIN MENU")
    print("1. Determine Minimum element in the list")
    print("2. Determine Maximum element in the list")
    print("3. Insert a new element into the list")
    print("4. Delete an element from the list")
    print("5. Determine if an element is present in the list")
    print("6. Print the list")
    print("7. Exit the program")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Minimum element in the list: " + str(min(lists)))
    if choice == 2:
        print("Minimum element in the list: " + str(max(lists)))
    if choice == 3:
        ele = int(input("Enter the element to insert into the list: "))
        ind = int(input("Enter the index to insert" + str(ele) + " : "))
        lists.insert(ind, ele)
    if choice == 4:
        ele = int(input("Enter the element to be deleted: "))
        ind = lists.index(ele)
        lists.pop(ind)
        print(str(ele) + " deleted from the list.")
    if choice == 5:
        ele = int(input("Enter the element to be determined: "))
        if ele in lists:
            x = lists.index(ele)
            print("Element is present at index : " + str(x))
        else:
            print("Element is not present.")
    if choice == 6:
        print(lists)
    if choice == 7:
        break
