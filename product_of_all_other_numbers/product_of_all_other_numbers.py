'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    # [0] * size
    product_list = [] # how to give size without filling up with zeroes?
    for i in range(0, len(arr)):
        print(f"i = {i}")
        print(f"arr = {arr}")
        others = list(arr) # doing others = arr messed things up? was modifying arr
        # if i == 0:
        #     others.pop(i)
        others.pop(i)
        print(f"others = {others}")
        # forgot how to do this ^ in 1 line
        count = 1
        for num in others:
            count *= num
        product_list.append(count)
        print(f"all multiplied now")
        print(f"END of {i} loop")

    return product_list

# what does this do exactly?
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
