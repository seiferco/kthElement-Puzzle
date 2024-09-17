# This is a function that finds the kth element in 2 sorted sub arrays. It uses divide and conquer technique to do so. 
# Since the main array is already split into 2 sub arrays and sorted, the first two steps of this process are already taken care of for us.
# All that is left for this algorithm to do is the merge portion of divide and conquer 
# CONSTRAINT: Assume k is within range of lenghths of sub arrays combined
def kthElement(arr1, arr2, k):
    start1 = 0 # used to track the comparison value of arr1
    start2 = 0 # used to track the comparison value of arr2
    idx = 0 # used to tell algorithm when to stop (when idx = k we found the kth Element in ans)
    ans = -1 # used to track current kth element
    while(idx < k):
        # check if index of start1 is in range of arr1
        #if not set ans to arr2[start2] (no more elements in arr1 to check)
        if(start1 >= len(arr1)):
            ans = arr2[start2]
            start2 += 1

        # check if index of start2 is in range of arr2
        #if not set ans to arr1[start1] (no more elements in arr2 to check)
        elif(start2 >=len(arr2)):
            ans = arr1[start1]
            start1 += 1

        # if arr1's curr val is less than arr2, set ans to arr1's curr val
        elif(arr1[start1] < arr2[start2]):
            ans = arr1[start1]
            start1 += 1

        # otherwise set ans to arr2's curr val
        else:
            ans = arr2[start2]
            start2 += 1

        idx += 1

    return ans

def main():

    #1,2,3,3,4,4,5,5,6,6,7
    arr1 = [1,2,3,4,5,6]
    arr2 = [3,4,5,6,7]

    ans = kthElement(arr1, arr2, 5) #5th element
    print(f"5th element: {ans}")

main()

