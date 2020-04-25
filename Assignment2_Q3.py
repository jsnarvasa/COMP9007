def split_array(array):
    '''
    Splits the array into n subarrays
    Takes O(n) time complexity, due to the iteration within the input array "array"
    This is more efficient than conducting a recursive split of the array until length becomes one,
    since that will take O(nlog(n))
    '''

    splitted_array = [[num] for num in array]
    return splitted_array

def get_closest_neightbour(left_array, right_array,
    left_array_left, left_array_right, 
    right_array_left, right_array_right):
    
    # Get the closest higher neighbour to the left, for right array
    left_array_index = len(left_array)-1 # start from the right-most of the left array, knowing that you can keep following the index to the highest number on your left

    for index, value in enumerate(right_array):
        if right_array_left[index] != None:
            right_array_left[index] += len(left_array)
            continue

        while left_array_index != None and value > left_array[left_array_index]:
            ''' while the value of the current number we're in on the right array is greater than
            the value of left_array[left_array_index], then let's keep following the left_array_left
            since we know it will always go to a bigger closest neighbour to the left'''
            left_array_index = left_array_left[left_array_index]

        if left_array_index == None: # since we reached None in left_array_left, it means that we no longer have a bigger number required
            continue

        right_array_left[index] = left_array_index

    # Get the closest higher neighbour to the right, for the left array
    right_array_index = 0 # start from teh left-most of the right array, knowing that you can keep following the index to the highest number on your right

    for index, value in enumerate(reversed(left_array)): # start from the right-most of the left array
        if left_array_right[index] != None:
            continue

        while right_array_index != None and value > right_array[right_array_index]:
            right_array_index = right_array_right[right_array_index]
        
        if right_array_index == None:
            continue

        left_array_right[index] = right_array_index + len(left_array)

    right_array_right = list(map(lambda num: num+len(left_array) if num!= None else None, right_array_right))

    combined_left = left_array_left + right_array_left
    combined_right = left_array_right + right_array_right
    combined_numbers = left_array + right_array
    output = [combined_numbers, combined_left, combined_right]
    return output

print(get_closest_neightbour([5,2,6,8],[1,4,3,9],[None,0, None, None],[2,2,3,None], [None,None,1,None], [1,3,3,None]))

'''
a = [1,2,3,4,5,6]

arrays = split_array(a)
print(arrays)


for i in range(len(arrays)):
    left_array_left = [None for num in arrays[i]]
    left_array_right = [None for num in arrays[i]]
    right_array_left = [None for num in arrays[i]]
    right_array_right = [None for num in arrays[i]]
    get_closest_neightbour(arrays[i], arrays[i+1],
        left_array_left, left_array_right,
        right_array_left, right_array_right)
'''