'''
called Bubble sort as bubble also pop up to the surface of water.
The algorithm also compare numbers side by side and largest number will pop up to the surface(rightmost)
38 9 29 7 2 15 28
1st loop:
    1st inner loop:
        (9 38) 29 7 2 15 18
    2nd inner loop:
        9 (29 38) 7 2 15 18
    Repeat this till 6th loop(N-1):
        9 29 7 2 15 (18 32) 
2nd loop:
    1st inner loop: 
        9 29 7 2 15 18 [32] 
    2nd inner loop:
        9 7 2 15 18 29 [32]
    no need to compare with 32(N-1-i)
...
6th loop(N-1):
    if all large elements are in place, first element(2) won't need to loop
    [2] 7 9 15 28 29 38

For efficiency,
If you don't end up swapping any element in your inner loop, you array is sorted
1 2 4 
1st loop:
    1st inner loop:
        (1 2) 4
    2nd inner loop:
        1 (2 4)
# nothing is swapped in 1st loop -> proof of already sorted array

'''
# Time Complexity : O(n^2)
# Space Complexity : O(1)
def Bubble_Sort(num_lst):
    N = len(num_lst)
    for i in range(N-1):
        # if list is sorted
        swapped = False
        for j in range(N-1-i):
            if num_lst[j]>num_lst[j+1]:
                # swap
                tmp = num_lst[j]
                num_lst[j] = num_lst[j+1]
                num_lst[j+1] = tmp
                # if list is sorted
                swapped = True
        # if list is sorted
        if not swapped:
            break

if __name__ == "__main__":
    #num_lst = [38,9,29,7,2,15,28]
    num_lst = [1,2,4]
    Bubble_Sort(num_lst)
    print(num_lst)

# E.x.
def Bubble_SortKey(num_lst,key):
    N = len(num_lst)
    for i in range(N-1):
        swapped = False
        for j in range(N-1-i):
            if elements[j][key]>elements[j+1][key]:
                elements[j],elements[j+1] = elements[j+1],elements[j]
                swapped = True
        if not swapped:
            break
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
#Bubble_SortKey(elements,key='transaction_amount')
Bubble_SortKey(elements,key='name')
print(elements)
