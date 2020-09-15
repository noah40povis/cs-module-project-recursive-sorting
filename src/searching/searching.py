# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    #check base case 
    if end>= start: 
        #create midpoint 
        midpoint = (end+start) // 2
         #if midpoint equals target then return midpoint 
        if arr[midpoint] == target:
            return midpoint
        #if midpoint is greater than target go to the left side and run recursive 
        elif arr[midpoint] > target:
            return binary_search(arr, target, start, midpoint-1) 
        else:
        # if midpoint is less than target go to right side and run recursive 
            return binary_search(arr, target, midpoint+1, end) 
    else: 
        # element is not present in the array 
        return -1         

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

# def agnostic_binary_search(arr, target):
#     # Your code here

