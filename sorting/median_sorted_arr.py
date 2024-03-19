def median(nums1,nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    i=j=k=flag=flag1 =0
    if (l1+l2)%2 == 0:
        print('even')
        flag=1
    median_index = (l1+l2)//2
    print(median_index)
    prev=0
    med=0
    while  k <= median_index:
        
        print(i,j,k,med,prev)
        if nums1[i]<nums2[j]:
            prev = med
            med = nums1[i]
            if i<l1-1:
                i+=1
            else:
                flag1 =1
                break
            
        elif j<l2:
            prev = med
            med=nums2[j]
            if j<l2-1:
                j+=1
            else: 
                flag1=2
                break
        k+=1
    if flag1 != 0:
        while  k < median_index:
            if flag1 == 2:
                prev = med
                med = nums1[i]
                i+=1
            if flag1==1:
                prev = med
                med = nums2[j]
                j+=1
            k+=1
            print(i,j,k,med,prev)
    if flag ==1:
        print((med+prev)/2)
        return (med+prev)/2

    print(med)
    return med

median([1,2],[3,4])

1,2,3,4

