def filter_homogenous(arr):
    res = []
    for subarr in arr:
        if not subarr: 
            continue
#        first_type = type(subarr[0])
#        if all(type(item) == first_type for item in subarr):
 #           res.append(subarr)
    return res
inp_arr = [[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]
out_arr = filter_homogenous(inp_arr)
print(out_arr)
