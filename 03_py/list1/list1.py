'''
DISCO : An element in a list can be accesed in the form LISTNAME[INDEX]
'''
def first_last6(nums):
    return nums[0] == 6 or nums[len(nums)-1] == 6 #checks if either first or last in list is 6

print(first_last6([1, 2, 3]))
print("expecting: False\n")
print(first_last6([1, 2, 6]))
print("expecting: True\n")
print(first_last6([6, 2, 4, 3]))
print("expecting: True\n")
print("*****")

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[len(nums)-1] #checks if first and last in list are equal

print(first_last6([1, 2, 3]))
print("expecting: False\n")
print(first_last6([1, 2, 1]))
print("expecting: True\n")
print(first_last6([1, 2, 2, 3]))
print("expecting: False\n")
print("*****")

'''
DISCO : Creating a list just requires writing out the list with its desired elements.
'''
def make_pi():
    return [3,1,4] #list with first 3 digits of pi in sequence

print(make_pi())
print("expecting: [3, 1, 4]\n")
print("*****")

def common_end(a, b):
    return a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1] #checks if first element of list of a and b match or if the last element matches

print(common_end([1, 2, 3], [7, 3]))
print("expecting: True\n")
print(common_end([1, 2, 3], [7, 3, 2]))
print("expecting: False\n")
print(common_end([1, 2, 3], [1, 3]))
print("expecting: True\n")
print("*****")

def sum3(nums):
    sum = 0
    for e in nums: #goes through the list
        sum += e   #add each element in the list to the sum
    return sum

print(sum3([1, 2, 3]))
print("expecting: 6\n")
print(sum3([5, 11, 2]))
print("expecting: 18\n")
print(sum3([7, 0, 0]))
print("expecting: 7\n")
print("*****")

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]] #rearranges list so elements are rotated left once

print(rotate_left3([1, 2, 3]))
print("expecting: [2, 3, 1]\n")
print(rotate_left3([5, 11, 9]))
print("expecting: [11, 9, 5]\n")
print(rotate_left3([7, 0, 0]))
print("expecting: [0, 0, 7]\n")
print("*****")

def reverse3(nums):
    return [nums[2], nums[1], nums[0]] #arranges list in reverse order

print(rotate_left3([1, 2, 3]))
print("expecting: [3, 2, 1]\n")
print(rotate_left3([5, 11, 9]))
print("expecting: [9, 11, 5]\n")
print(rotate_left3([7, 0, 0]))
print("expecting: [0, 0, 7]\n")
print("*****")

'''
DISCO : max() is a built in python function that can return the greatest value of the given parameters.
'''
def max_end3(nums):
    m = max(nums[0], nums[2]) #takes greater of first and last element
    return [m,m,m] #returns list with all elements that are m

print(max_end3([1, 2, 3]))
print("expecting: [3, 3, 3]\n")
print(max_end3([11, 5, 9]))
print("expecting: [11, 11, 11]\n")
print(max_end3([2, 11, 3]))
print("expecting: [3, 3, 3]\n")
print("*****")

def sum2(nums):
    if len(nums) == 0:
        return 0 #returns 0 for list of length 0
    elif len(nums) < 2: 
        return nums[0] #returns sum of all elements for list of length 1
    return nums[0] + nums[1] #returns sum of first 2 elements for list of length >1

print(sum2([1, 2, 3, 4]))
print("expecting: 3\n")
print(sum2([1, 2]))
print("expecting: 3\n")
print(sum2([100]))
print("expecting: 100\n")
print(sum2([]))
print("expecting: 0\n")
print("*****")

def middle_way(a, b):
    return [a[1], b[1]] #returns new list with middle elements of list a and b

print(middle_way([1, 2, 3], [4, 5, 6]))
print("expecting: [2, 5]\n")
print(middle_way([7, 7, 7], [3, 8, 0]))
print("expecting: [7, 8]\n")
print(middle_way([5, 2, 9], [1, 4, 5]))
print("expecting: [2, 4]\n")
print("*****")

def make_ends(nums):
    return [nums[0], nums[len(nums) - 1]] #returns new list with first and last elements of original list

print(make_ends([1, 3]))
print("expecting: [1, 3]\n")
print(make_ends([7, 4, 6, 2]))
print("expecting: [7, 2]\n")
print(make_ends([100]))
print("expecting: [100, 100]\n")
print("*****")

def has23(nums):
    return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3 #checks if list contains a 2 or a 3

print(has23([2, 5]))
print("expecting: True\n")
print(has23([4, 3]))
print("expecting: True\n")
print(has23([4, 5]))
print("expecting: False\n")
