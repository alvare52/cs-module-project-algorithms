'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    cache = {}

    for num in arr:

        # if number isn't in cache, add it with 0 as value
        if num not in cache:
            cache[num] = 0

        # if it is already in cache (duplicate), then +1
        else:
            cache[num] += 1
    
    # check if there's a key with a value of 0 (means no duplicate)
    for key in cache:
        if cache[key] == 0:
            return key
    return -1

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")