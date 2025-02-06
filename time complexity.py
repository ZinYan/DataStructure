'''
How to calculate: 
    1. Keep fastest growing term
    2. Drop constants
Why keep only fastest growing term and drop constants
    e.g.,
        time = 5*n^2 + 3*n + 20
        if n = 1000,
            time = 5*1000^2 + 3*1000 + 20
            time = 5000000 + 3020 
        3020 become insignificant even when n=1000 and Big O refers to very large value of n 
# Linear time complexity O(n)
Calculation 
    time = a*n+b
    1. Keep fastest growing term
        time = a*n
    2. Drop constants
        time = n
    time = O(n)
E.g.,
    Squaring numbers
    def squared_numbers(numbers):
        squared_nums = []
        for num in numbers:
            squared_nums.append(num*num)
        return squared_nums
    numbers = 4 -> iterations = 4 : grows linearly
# Constant time complexity O(1)
Calculation
    time = a
    1. time= a
    2. time = 1 
    time = O(1)
E.g.,
    square of a num
    def squared(num):
        squared_num = num*num
        return squared_num
# Quadratic time complexity O(n^2)
Calculation
    time = a*n^2+b
    1. time = a*n^2
    2. time = n^2
    time = O(n^2)
E.g.,
    Finding duplicates
    numbers = [3,6,2,4,3,6,8,9]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]==numbers[j]
                print(numbers[i],"has a duplicate.")
                break
    for i in range(len(numbers)):
        if numbers[i]==duplicate:
            print(i)
    1st block code : n^2 iterations
    3nd block : n iterations
    time = a*n^2 + b^n + c
    1. time = a*n^2
    2. time = n^2
    time = O(n^2)
# Logarithmic Time Complexity O(log n)
arr = [4,9,15,21,34,57,68,91]
Search for 68:
    normal search = O(n)
    Binary search = O(log n)
        Find mid element(21) compare with 68 and 21<68 so discard left half [Iteration 1 = n/2]
        Iteration 2 = (n/2)/2 = n/2^2
        Iteration 3 = ((n/2)/2)/2 = n/2^3
        Iteration k = n/2^k
        1 = n/2^k (1 because worst case)
        n = 2^k
        log2 n = log2 2^k
        log2 n = k*log2 2
        log n = k
        k = log n 
        k = O(log n)
        In this e.g., there are 8 elements in the array,
            k = log2 8 = log2 2^3 = 3*log2 2 = 3 iterations

'''