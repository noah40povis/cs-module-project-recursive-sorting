# TO-DO: complete the helper function below to merge 2 sorted arrays
#putting it back together 
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    j = 0 #starting index for arrA
    i = 0 #starting index for arrb 
    k = 0 #merged index 
    while j < len(arrA) and i < len(arrB):
        if arrA[j] < arrB[i]: #compares first element of two arrays 
            merged_arr[k] = arrA[j] #makes the first element of merged array from A if smaller 
            j += 1 #raises the arrA index so will point to next element 
        else: 
            merged_arr[k] = arrB[i]  #makes first element of the merged array from B if smaller 
            i += 1 #raises the arrb index so will point to the next element 
        k += 1 #outside the IF, this raises the merged Index. 
    while j < len(arrA): #continues while the arrA index is less than the length of arrA (only occurs if B goes first)
        merged_arr[k] = arrA[j] #adds next element from A to merged. 
        k += 1 #raises merged index
        j += 1 #raises arrA index 
    while i < len(arrB): #continues while arrB index is less than the length of arrB (only occurs if A goes first)
        merged_arr[k] = arrB[i] #adds next element from B to merged 
        k += 1 #raises merged index 
        i += 1 #raises arrb index 
    return merged_arr




#splitting it up 
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1: #checks that array is more than single item 
        right = len(arr)#high
        left = 0 #low 
        middle = (right+ left) // 2 #middle 
        left_merge_arr = merge_sort(arr[:middle]) #recursively breaks array into two parts
        right_merge_arr = merge_sort(arr[middle:]) #recursively breaks array into two parts
        final_arr = merge(left_merge_arr, right_merge_arr) #runs helper function on array broken into two parts
        return final_arr #returns final product 
    return arr #returns if rarry is single element 

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

