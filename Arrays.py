'''
stock_prices = [298,305,320,301,292]
How they are stored on RAM:
                     Addresses(hex)
    stock_prices ->  0x00500        298
                     0x00504        305
                     0x00508        320
                     0x0050A        301
                     0x0050F        292
    In computer, numbers are stored in 0s and 1s
        298 in binary: 100101010
        Int are stored in 4 bytes(1byte=8bits):
            298 = 00000000 00000000 00000001 00101010
    How numbers are actually stored on RAM: 
    stock_prices -> 0x00500     00000000
                    0x00501     00000000
                    0x00502     00000001
                    0x00503     00101010
                    0x00504     00000000
                    0x00505     00000000
                    0x00506     00000001
                    0x00507     00110001
                    ......
Look up by index O(1)
    What was the price on day 3: stock_prices[2] = ?
    stock_prices[0] = 0x00500
    stock_prices[2] = 0x00500 + 2 * sizeof(integer)
    stock_prices[2] = 0x00500 + 2 * 4
    stock_prices[2] = 0x00508
Look up by value O(n)
    On what day the price was 301? 
    for i in range(len(stock_prices)):
        if stock_prices[i] == 301:
            return i
    # if you want to look for 292(big O worst case), have to go through all elements : O(n)
Array Traversal O(n)
    Print all prices
    for i in stock_prices:
        print(i)
Array Insertion O(n)
    Inserting new price 284 at index 1
    stock_prices.insert(1,284) 
        will shift all elements by one position 
Array Deletion O(n)
    Same with insertion 
    stock_prices.remove(298)
        will shift all elements by one position

In python, list is implemented as Dynamic Array.
In Java or C++, they have both Static & Dynamic Array
    Java:
        Static: int[] stock_prices = new int[5]
        Dynamic: ArrayList<Integer> stock_prices = new ArrayList<Integer>()
    C++
        Dynamic: std::vector

How Static and Dynamic Arrays work:
    Static Array
        - fixed size, will only allocate memory for that fixed size
    Dynamic Array
        - first, will allocate initial capacity(e.g., 10) in the memory
        - when you want to add new element and the capacity is full, it will allocate new memory area at a different location with additional capacity of original capacity*2(e.g., 10*2=20 -> total capacity = 30)
        - Then copied the original elements(10 elements) into the new space and add new element.
Python Arrays can store different data types together.
'''
# Ex 1
# jan, feb, mar, apr, may
monthly_expenses = [2200,2350,2600,2130,2190]
# dollars spent extra in Feb compare to Jan
print('In feb this much extra was spent compared to jan:',monthly_expenses[1]-monthly_expenses[0])
# total expenses in first quarter(3 months)
print("Expense for first quarter:",sum(monthly_expenses[:3]))
# if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any months?",2000 in monthly_expenses)
# Add june expense 1980 dollar
monthly_expenses.append(1980)
print('Expenses at the end of June:',monthly_expenses)
# April - refund 200
monthly_expenses[3] = monthly_expenses[3]-200
print('Expenses after 200$ return in April:',monthly_expenses)

# Ex 2
heros=['spider man','thor','hulk','iron man','captain america']
print("Length of list:",len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
heros[1:3] = ['doctor strange']
print(heros)
print(dir(heros))
heros.sort()
print(heros)

# Ex 3
x = int(input('Enter a max num: '))
odd_lst = [i for i in range(1,x+1) if i%2!=0]
print(odd_lst)