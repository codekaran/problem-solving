"""Given an array of integers nums and an integer k, write a program to return the number of unique k-diff pairs in the array.
A k-diff pair is defined as an integer pair (nums[i], nums[j]), where the following conditions are true:

0≤i,j<length of nums and i≠j.

The absolute difference between the two numbers is exactly k, i.e., ∣nums[i]−nums[j]∣=k."""

# solution - we can sort the array and perform binary search to find the compliment
# things to keep in mind the binary search end condidition, when k=0 then

def get_pairs(arr,k):
    arr.sort()
    l = len(arr)
    sets = set()
    for i in arr:
        print('i=',i,'j=',i-k)   
        if bin_search(arr,i-k):
            sets.add((i,i-k))
    print(sets)

def bin_search(arr,v):
    beg = 0
    end = len(arr)-1
    while beg <= end:
        mid =(beg+end)//2
        print(mid)
        if v==arr[mid]:
            return True
        if v>arr[mid]:
            beg = mid+1   
        else:
            end = mid-1
        print(beg,end)
    return  False
# get_pairs([3,1,4,5,1],2)
print(bin_search([1,2,3,4,5],2))
11345