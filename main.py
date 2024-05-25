import time

MAX_SIZE = 100
HASH_TABLE_SIZE = 100

# Linked list node
class ListNode:
    def _init_(self, data):
        self.data = data
        self.next = None

# Linked list
class LinkedList:
    def _init_(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            print("Index out of range.")
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Queue
class Queue:
    def _init_(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.items) == 0

# Stack
class Stack:
    def _init_(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.items) == 0

# Hash Table
class HashTable:
    def _init_(self):
        self.table = [None] * HASH_TABLE_SIZE

    def insert(self, key, value):
        index = key % HASH_TABLE_SIZE
        self.table[index] = (key, value)

    def get(self, key):
        index = key % HASH_TABLE_SIZE
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        else:
            return -1

    def delete(self, key):
        index = key % HASH_TABLE_SIZE
        if self.table[index] and self.table[index][0] == key:
            self.table[index] = None

# Graph
class Graph:
    def _init_(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        self.adjacency_matrix[src][dest] = 1
        self.adjacency_matrix[dest][src] = 1

    def display(self):
        for row in self.adjacency_matrix:
            print(row)


def print_menu():
    print("\nMenu:")
    print("1. Add Data")
    print("2. Linear Search")
    print("3. Binary Search")
    print("4. Bubble Sort")
    print("5. Selection Sort")
    print("6. Insertion Sort")
    print("7. Merge Sort")
    print("8. Quick Sort")
    print("9. Radix Sort")
    print("10. Exit")
    print("11. Linked List")
    print("12. Queue")
    print("13. Stack")
    print("14. Remove from Linked List")
    print("15. Dequeue from Queue")
    print("16. Pop from Stack")
    print("17. Insert into Hash Table")
    print("18. Get value from Hash Table")
    print("19. Delete from Hash Table")
    print("20. Graph")
    print("21. Print Graph")


def add_data(arr):
    if len(arr) < MAX_SIZE:
        data = int(input("Enter data to add: "))
        arr.append(data)
    else:
        print("Array is full. Cannot add more elements.")


def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            print(f"Element found at index {i}.")
            return
    print("Element not found in the array.")


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            print(f"Element found at index {mid}.")
            return
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("Element not found in the array.")


def bubble_sort(arr):
    n = len(arr)
    for i in range (n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


def main():
    arr = []
    ll = LinkedList()
    q = Queue()
    s = Stack()
    ht = HashTable()
    g = Graph(5)

    while True:
        print_menu()
        try:
            choice = int(input("Enter your choice: "))
        except EOFError:
            print("Reached end of input. Exiting...")
            break

        if choice == 1:
            add_data(arr)
        elif choice == 2:
            target = int(input("Enter the element to search: "))
            linear_search(arr, target)
        elif choice == 3:
            target = int(input("Enter the element to search: "))
            arr.sort()
            binary_search(arr, target)
        elif choice == 4:
            bubble_sort(arr)
            print("Sorted array:", arr)
        elif choice == 5:
            selection_sort(arr)
            print("Sorted array:", arr)
        elif choice == 6:
            insertion_sort(arr)
            print("Sorted array:", arr)
        elif choice == 7:
            merge_sort(arr)
            print("Sorted array:", arr)
        elif choice == 8:
            quick_sort(arr, 0, len(arr) - 1)
            print("Sorted array:", arr)
        elif choice == 9:
            radix_sort(arr)
            print("Sorted array:", arr)
        elif choice == 10:
            print("Exiting...")
            break
        elif choice == 11:
            ll.display()
        elif choice == 12:
            if not q.is_empty():
                print("Dequeued item:", q.dequeue())
            else:
                print("Queue is empty.")
        elif choice == 13:
            if not s.is_empty():
                print("Popped item:", s.pop())
            else:
                print("Stack is empty.")
        elif choice == 14:
            index = int(input("Enter the index to remove: "))
            ll.remove(index)
        elif choice == 15:
            if not q.is_empty():
                print("Dequeued item:", q.dequeue())
            else:
                print("Queue is empty.")
        elif choice == 16:
            if not s.is_empty():
                print("Popped item:", s.pop())
            else:
                print("Stack is empty.")
        elif choice == 17:
            key = int(input("Enter key: "))
            value = int(input("Enter value: "))
            ht.insert(key, value)
        elif choice == 18:
            key = int(input("Enter key: "))
            print("Value:", ht.get(key))
        elif choice == 19:
            key = int(input("Enter key: "))
            ht.delete(key)
        elif choice == 20:
            print("Adding edges to the graph...")
            g.add_edge(0, 1)
            g.add_edge(0, 2)
            g.add_edge(1, 2)
            g.add_edge(2, 3)
            g.add_edge(3, 4)
            g.add_edge(4, 0)
        elif choice == 21:
            g.display()
        else:
            print("Invalid choice. Please try again.")


if _name_ == "_main_":
    main()
