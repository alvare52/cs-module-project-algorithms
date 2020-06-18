'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here (move zeroes to end of list?)
    # maybe loop once just to get future size of each list?
    non_zero_list = []
    zero_list = []
    for num in arr:
        if num != 0:
            non_zero_list.append(num)
        else:
            zero_list.append(num)
    return non_zero_list + zero_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")