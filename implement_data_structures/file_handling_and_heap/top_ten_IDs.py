
# open and read the file
# store IDs into a hash, key = ID, value = frequency of apperance

# use a heap to keep track of the top ten IDs as we are passing it into the hash

# otherwise, we could do one pass to store into the hash, 
# then iterate through all entries of the hash and keep track of highest values with a heap

# wrong stuff following
# or we could switch keys and values in the hash map and sort the keys, return the values mapping to the highest value keys
# THIS DOES NOT WORK FOR DUPLICATE VALUES. DON'T DO THIS. 
# new_d = {value:key for key,value in d.iteritems()}
# dictionary comprehension

# import heap_module


# overall O(nlogn) with sorting 
# would be O(logn) with a heap

def top_ten(f):
    f = open(f)
    id_list = [x.strip() for x in f]
    f.close()

    # print ID_list

    d = {}
    for item in id_list:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1

    reverse_d = {}
    for key, value in d.iteritems():
        if value in reverse_d:
            reverse_d[value].append(key)
        else:
            reverse_d[value] = [key]

    print reverse_d

    # O(nlogn)
    # sorted_keys = sorted(reverse_d.keys())[::-1]
    sorted_keys = sorted(reverse_d.keys(), reverse = True)

    print sorted_keys

    returned_keys = 0
    top_ten = []

    # while returned_keys < 10:
    # hah. What was I thinking. 

    for value in sorted_keys:

            for ID in reverse_d[value]:
                top_ten.append(ID)
                returned_keys += 1

                # once you reach ten keys, return those keys
                # how to handle ties for the tenth place? discuss. 
                if returned_keys >= 10:
                    return top_ten


print top_ten('IDs.txt')

"""expect
['88889213', '30957835', '59783821', '869702-1', '67920000', '34567915', '20598361', '94010-57', '69878301', '87950231']
"""

# print d
# print len(d)

# min heap
# top_ten = heap_module.Heap()

# for key in d:
#     frequency = d[key]
#     if top_ten.size < 10:
#         top_ten.insert(key)
#     else: # already have ten things in the heap
        
#         min_id_in_heap = top_ten.heap[1]
#         min_frequency_in_heap = d[min_id_in_heap]

#         if min_frequency_in_heap < frequency:
#             top_ten.heap.popMin()
#             top_ten.insert(key)

#             # need to fix heap implementation if we want to do this. bah! 
#             # currently, this heap only handles integers
#             # I wanted to only store keys in the heap, and then look up keys in the dictionary
#             # to see their frequency value.


