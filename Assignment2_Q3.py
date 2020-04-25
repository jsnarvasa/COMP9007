import math


def get_higher_neighbour(array):
    '''
    Returns a dictionary of two arrays, containing the closest higher neighbour of n (where n is a member of array "array"),
    where the key 'LEFT' returns array of the closest neighbour that is higher when looking to the left
    and key 'RIGHT' returns array of the closest neighbour that is higher when looking to the right
    '''
    # accounting for the base case where length of array is 1
    if len(array) == 1:
        return {'left': [None], 'right': [None]}

    # find the mid point of the array and split into two arrays
    mid_point = math.floor(len(array)/2)
    left_array = array[:mid_point]
    right_array = array[mid_point:]

    # make recursive calls, solving for each half of the array and then merging the results
    left_array_output = get_higher_neighbour(left_array)
    right_array_output = get_higher_neighbour(right_array)


    # For the right array, find the closest higher neighbour, looking to the LEFT (against the left array)
    # We start the search from the left-hand side of the right array, only filling the ones which are left as None
    # We know that the indexes which are left as None (no highest left neighbour), will only increase as we move the counter from left to right of the right_array
    left_array_index = len(left_array)-1

    for index, value in enumerate(right_array):
        if right_array_output['left'][index] != None:
            # if we already found the closest higher neighbour for an index in an array, just need to increment it
            # so the index it refers to remains valid after we combine the two arrays/lists
            right_array_output['left'][index] += len(left_array)
            continue

        while left_array_index != None and value > left_array[left_array_index]:
            '''
            while the value of the current number in the right array is greater than the value of left_array[left_array_index],
            then follow the value of left_array[left_array_index], so we get the index of the next higher value of the left_array,
            since we know it will always go to a bigger closest neighbour to the left
            '''
            left_array_index = left_array_output['left'][left_array_index]

        if left_array_index == None:
            # since we reached None in left_array_output['left'], it means that we no longer have a bigger number required
            # we need to continue to the next one, but we DON'T BREAK - because we still need to increment the values in the array
            # which already has a value (need to ensure the index remains true after merging the two arrays)
            right_array_output['left'][index] = None
            continue

        right_array_output['left'][index] = left_array_index

    combined_left = left_array_output['left'] + right_array_output['left']


    # For the left array, find the closest higher neighbour, looking to the RIGHT (against the right array)
    # Need to start from the right side of the left array, because we know that as we move from right to left of left_array_output[right]
    # where the indices remain with value None, the value required for those to be filled (with a higher num) increases
    right_array_index = 0

    for left_counter in reversed(range(len(left_array))):
        # start from the right-most of the left array, and using a counter since we need the reversed index position and enumerate with index isn't sufficient
        if left_array_output['right'][left_counter] != None:
            continue

        while right_array_index != None and left_array[left_counter] > right_array[right_array_index]:
            right_array_index = right_array_output['right'][right_array_index]
        
        if right_array_index == None:
            left_array_output['right'][left_counter] = None
            continue

        left_array_output['right'][left_counter] = right_array_index + len(left_array)

    # Since we don't iterate over all the values in the right array one-by-one, need to increment those which are not none
    # in order to ensure the index it refers to after we merge the two lists remains correct
    # this is not required for left_array_output since we are filling the right array there which refers to the left array and no increment is required
    right_array_output['right'] = list(map(lambda num: num+len(left_array) if num!= None else None, right_array_output['right']))

    combined_right = left_array_output['right'] + right_array_output['right']

    return {'left': combined_left, 'right': combined_right}


# Sample input
A = [5,2,6,8,1,4,3,9]

results = get_higher_neighbour(A)
for side in results:
    results[side] = list(map(str, results[side]))
    print(','.join(results[side]))
