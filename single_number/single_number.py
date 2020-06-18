'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    for i in range(0, len(arr)):
        duplicate_count = 0
        for j in range(0, len(arr)):
            if arr[i] == arr[j]:
                duplicate_count += 1
        
        if duplicate_count < 2:
            return arr[i]

    # returns number that doesn't have duplicate
    return -1


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")