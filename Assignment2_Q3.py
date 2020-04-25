import math

def v2(array):
    if len(array) == 1:
        return {'left': [None], 'right': [None]}

    mid_point = math.floor(len(array)/2)
    left_array = array[:mid_point]
    right_array = array[mid_point:]

    left_array_output = v2(left_array)
    right_array_output = v2(right_array)

    # fill up the right array looking left
    # in this case, we start on the left-hand side of the right array because we know that the biggest None will be on the right side,
    # since it is looking at left, otherwise it would have been filled already
    left_array_index = len(left_array)-1

    for index, value in enumerate(right_array):
        if right_array_output['left'][index] != None:
            right_array_output['left'][index] += len(left_array)
            continue

        while left_array_index != None and value > left_array[left_array_index]:
            '''
            while the value of the current number we're in on the right array is greater than
            the value of left_array[left_array_index], then let's keep following the left_array_left
            since we know it will always go to a bigger closest neighbour to the left
            '''
            left_array_index = left_array_output['left'][left_array_index]

        if left_array_index == None: # since we reached None in left_array_output['left'], it means that we no longer have a bigger number required
            right_array_output['left'][index] = None
            continue

        right_array_output['left'][index] = left_array_index

    combined_left = left_array_output['left'] + right_array_output['left']


    # fill up the left array, looking right
    # for this one, need to start from the right side of the left array, because we know that the biggest None looking right
    # will be on the left-hand side, otherwise, it would have already been populated
    right_array_index = 0

    for left_counter in reversed(range(len(left_array))): # start from the right-most of the left array
        if left_array_output['right'][left_counter] != None:
            continue

        while right_array_index != None and left_array[left_counter] > right_array[right_array_index]:
            right_array_index = right_array_output['right'][right_array_index]
        
        if right_array_index == None:
            left_array_output['right'][left_counter] = None
            continue

        left_array_output['right'][left_counter] = right_array_index + len(left_array)

    right_array_output['right'] = list(map(lambda num: num+len(left_array) if num!= None else None, right_array_output['right']))

    combined_right = left_array_output['right'] + right_array_output['right']

    return {'left': combined_left, 'right': combined_right}

A = [5,2,6,8,1,4,3,9]

results = v2(A)
for side in results:
    results[side] = list(map(str, results[side]))
    print(','.join(results[side]))
