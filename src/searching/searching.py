# TO-DO: Implement a recursive implementation of binary search
#https://stackoverflow.com/questions/41283736/binary-search-using-recursion-goes-into-an-infinite-loop
def binary_search(arr, target, low, high):
    # Your code here
        # we're searching in between the low and high indices 
     
    if low> high:
        return -1
    else:
        mid= (low+high)//2 
        if arr[mid]==target:
            return mid
        if target< arr[mid]:
            return binary_search(arr, target, low, mid-1)
        else:
            return binary_search(arr,target, mid+1, high)


      

# STRETCH: implement an order-agnostic binary search # This version of binary search should correctly find  # the target regardless of whether the input array is # sorted in ascending order or in descending order
# You can implement this function either recursively  # or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here
     
   