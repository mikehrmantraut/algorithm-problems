def maxSubarrayValue(arr):
    l = list(enumerate(arr))
    even_index = list()
    odd_index = list()
    c = 0

    for i in l:
        if i[c] == 0 or i[c] % 2 == 0:
            even_index.append(i[c+1])
        else:
            odd_index.append(i[c+1])
        
    print((sum(even_index)-sum(odd_index))**2)

maxSubarrayValue([1,2,4,-1,-1])
