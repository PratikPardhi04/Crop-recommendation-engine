employees = [
    {"id": 105, "name": "John", "salary": 50000},
    {"id": 102, "name": "Alice", "salary": 70000},
    {"id": 110, "name": "Mark", "salary": 45000},
    {"id": 101, "name": "Sophia", "salary": 80000},
    {"id": 108, "name": "David", "salary": 60000},
    {"id": 103, "name": "Emma", "salary": 55000},
    {"id": 109, "name": "Chris", "salary": 65000},
    {"id": 107, "name": "Olivia", "salary": 72000},
    {"id": 104, "name": "Daniel", "salary": 47000},
    {"id": 106, "name": "Liam", "salary": 52000}
]

def quick_sort(arr, low, high, key):
    if low < high:
        p = partition(arr, low, high, key)
        quick_sort(arr, low, p-1, key)
        quick_sort(arr, p+1, high, key)

def partition(arr, low, high, key):
    pivot = arr[high][key]
    i = low - 1
    for j in range(low, high):
        if arr[j][key] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def merge_sort(arr, key):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L, key)
        merge_sort(R, key)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][key] <= R[j][key]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

emp_by_id = employees.copy()
quick_sort(emp_by_id, 0, len(emp_by_id)-1, "id")
print("\nEmployees sorted by ID (Quick Sort):")
for e in emp_by_id:
    print(e)

emp_by_name = employees.copy()
merge_sort(emp_by_name, "name")
print("\nEmployees sorted by Name (Merge Sort):")
for e in emp_by_name:
    print(e)

