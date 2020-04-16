"""Given an array (a list in Python) of integers and an integer n, find all occurrences of n in the given array
and return another array containing all the index positions of n in the given array.

If n is not in the given array, return an empty array [].

Assume that n and all values in the given array will always be integers.

Example:
find_all([6, 9, 3, 4, 3, 82, 11], 3) > [2, 4]"""

#FINISHED!

def find_all(array, n):
    array_2 = []
    for i, e in enumerate(array):
        if e == n:
            #print(i) #for controling purposes
            array_2.append(i)
    return array_2

print(find_all([3,4,5,6,10,12,3,11,12,1,3],3))

array = [6,9,3,4,4,82,11]
print(find_all(array,4))
#print(array.index(3))