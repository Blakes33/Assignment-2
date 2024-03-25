import winsound  # For playing sound effects

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            # Play sound effect for swap with varying pitch
            winsound.Beep(500 + 50 * k, 100) 

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print("Merging:", arr)

# Function to accept array input from the user
def get_array_input():
    n = int(input("Enter the number of elements: "))
    arr = []
    print("Enter the elements:")
    for _ in range(n):
        arr.append(int(input()))
    return arr

# Main function
def main():
    arr = get_array_input()
    print("Original array:", arr)
    merge_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()