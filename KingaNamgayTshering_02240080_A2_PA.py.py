student_ids = [2001, 2004, 2002, 2007, 2010, 2003, 2005, 2006, 2008, 2009,
               2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

scores_sorted = [32, 40, 45, 50, 55, 60, 62, 65, 70, 72,
                 75, 80, 82, 85, 87, 90, 92, 95, 98, 100]


def linear_search(lst, target):
    comparisons = 0
    for index, value in enumerate(lst):
        comparisons += 1
        if value == target:
            return index + 1, comparisons
    return None, comparisons


def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if lst[mid] == target:
            return mid + 1, comparisons
        elif target < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None, comparisons


while True:
    print("\n=== Searching Algorithms Menu ===")
    print("Select a search operation (1-3):")
    print("1. Linear Search - Find Student ID")
    print("2. Binary Search - Find Score")
    print("3. Exit program")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Searching in the list:", student_ids)
        target = int(input("Enter Student ID to search: "))
        pos, comp = linear_search(student_ids, target)
        if pos:
            print(f"Result: Student ID {target} found at position {pos} Comparisons made: {comp}")
        else:
            print(f"Result: Student ID {target} not found. Comparisons made: {comp}")

    elif choice == '2':
        print("Sorted scores:", scores_sorted)
        target = int(input("Enter score to search: "))
        pos, comp = binary_search(scores_sorted, target)
        if pos:
            print(f"Result: Score {target} found at position {pos} Comparisons made: {comp}")
        else:
            print(f"Result: Score {target} not found. Comparisons made: {comp}")

    elif choice == '3':
        print("Thank you for using the search program!")
        break

    else:
        print("Invalid choice! Please select 1-3.")

    again = input("Would you like to perform another search? (y/n): ")
    if again.lower() != 'y':
        print("Thank you for using the search program!")
        break

