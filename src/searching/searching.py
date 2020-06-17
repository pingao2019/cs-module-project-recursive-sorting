# TO-DO: Implement a recursive implementation of binary search
#https://stackoverflow.com/questions/41283736/binary-search-using-recursion-goes-into-an-infinite-loop
def binary_search(arr, target, start, end):
    # Your code here
        # we're searching in between the low and high indices 
    low = 0
    high = len(arr) - 1
    if len(arr)==0:
        return False
    elif len(arr)==1 and arr[0]==target:
        return True
    else:
        mid= len(arr)/2 -1
        if target> arr[mid]:
            binary_search(arr[mid:], target)
        else:binary_search(arr[:mid].target)


      

# STRETCH: implement an order-agnostic binary search # This version of binary search should correctly find  # the target regardless of whether the input array is # sorted in ascending order or in descending order
# You can implement this function either recursively  # or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
     
   