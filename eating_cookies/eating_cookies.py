'''
Input: an integer
Returns: an integer
'''

# Cookie Monster can eat either 1, 2, or 3 cookies at a time. 
# If he were given a jar of cookies with `n` cookies inside of it,
#  how many ways could he eat all `n` cookies in the cookie jar?
#  Implement a function `eating_cookies` that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar. 

# For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

#  1. He can eat 1 cookie at a time 3 times
#  2. He can eat 1 cookie, then 2 cookies 
#  3. He can eat 2 cookies, then 1 cookie
#  4. He can eat 3 cookies all at once. 

# Thus, `eating_cookies(3)` should return an answer of 4.
#  self.assertEqual(eating_cookies(0), 1)
#     self.assertEqual(eating_cookies(1), 1)
#     self.assertEqual(eating_cookies(2), 2)
#     self.assertEqual(eating_cookies(5), 13)
#     self.assertEqual(eating_cookies(10), 274)
# Can you implement a solution that runs fast enough to pass the large input test?

def eating_cookies(n, cache={}):
    # Your code here

    if n < 0:
        return 0

    if n == 0:
        return 1

    # if we've already done this before, get result from cache
    if cache and cache[n] > 0:
        return cache[n]

    else:
        # make a cache for our first run with  n's
        if not cache:
            # make a cache with n keys, and values start as 0
            cache = {i: 0 for i in range(n+1)}
        # store result in cache that we pass back
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    # print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

print(eating_cookies(3))