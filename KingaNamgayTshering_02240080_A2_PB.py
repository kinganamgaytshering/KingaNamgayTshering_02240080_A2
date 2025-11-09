student_names = ["Sonam", "Karma", "Leki", "Tshering", "Yeshey", "Tashi", "Nima", "Dema", "Thinley", "Pema",
                 "Jigme", "Dorji", "Wangmo", "Ugyen", "Sangay"]

test_scores = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 76, 85, 48, 93, 71, 89, 57, 80, 69, 62]

book_prices = [450, 230, 678, 125, 890, 560, 330, 150, 770, 980,
               210, 300, 410, 650, 720]


def bubble_sort(lst):
    n = len(lst)
    arr = lst.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(lst):
    arr = lst.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


recursive_calls = 0
def quick_sort(arr):
    global recursive_calls
    recursive_calls += 1
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


while True:
    print("\n=== Sorting Algorithms Menu ===")
    print("Select a sorting operation (1-4):")
    print("1. Bubble Sort - Sort Student Names")
    print("2. Insertion Sort - Sort Test Scores")
    print("3. Quick Sort - Sort Book Prices")
    print("4. Exit program")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Original names:", student_names)
        result = bubble_sort(student_names)
        print("Sorted names:", result)

    elif choice == '2':
        print("Original scores:", test_scores)
        result = insertion_sort(test_scores)
        print("Sorted scores:", result)
        print("\nTop 5 Scores:")
        top5 = sorted(result, reverse=True)[:5]
        for i, val in enumerate(top5, start=1):
            print(f"{i}. {val}")

    elif choice == '3':
        print("Original prices:", book_prices)
        recursive_calls = 0
        result = quick_sort(book_prices.copy())
        print("Sorted prices:", result)
        print("Recursive calls made:", recursive_calls)

    elif choice == '4':
        print("Thank you for using the sorting program!")
        break

    else:
        print("Invalid choice! Please select 1-4.")

    again = input("Would you like to perform another sort? (y/n): ")
    if again.lower() != 'y':
        print("Thank you for using the sorting program!")
        break
