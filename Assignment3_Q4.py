longest_sequence_memo = {}

def winning_sequence(num_array, colour_array, current_pos):
    '''
    INPUT: array of numbers for the board,
        corresponding array denoting colour for each number on the board,
        the current index position that we're looking to obtain the max increasing sequence for
    OUTPUT: integer of the longest increasing sequence at this index within the array
    '''

    if current_pos in longest_sequence_memo:
        return longest_sequence_memo[current_pos]["seq_num"]

    max_increasing_sequence = 0
    max_increasing_sequence_index = None

    # checking to the left of our current position - meaning we only look for x[j] < x[current_pos] to our left which are GREEN
    for index, num in enumerate(num_array[:current_pos]):
        if num < num_array[current_pos] and colour_array[index] == "g":
            # check if we already have the value in our memoization dict else, try to find out what the longest sequence is for that index by checking against the other candidates
            if index not in longest_sequence_memo:
                # we'll need to store this value for future reference if it's not in our memoization dict already
                sequence_num, prev_index = winning_sequence(num_array, colour_array, index)
                longest_sequence_memo[index] = {}
                longest_sequence_memo[index]["seq_num"] = sequence_num
                longest_sequence_memo[index]["prev_index"] = prev_index
            # we just compare and look for the highest increasing sequence
            if longest_sequence_memo[index]["seq_num"] > max_increasing_sequence:
                max_increasing_sequence = longest_sequence_memo[index]["seq_num"]
                max_increasing_sequence_index = index
    
    # checking to the right of our current position - meaning we only look for x[j] < x[current_pos] to our right which are RED
    for index, num in enumerate(num_array[current_pos:]):
        if num < num_array[current_pos] and colour_array[index+current_pos] == "r":
            if index+current_pos not in longest_sequence_memo:
                sequence_num, prev_index = winning_sequence(num_array, colour_array, index+current_pos)
                longest_sequence_memo[index+current_pos] = {}
                longest_sequence_memo[index+current_pos]["seq_num"] = sequence_num
                longest_sequence_memo[index+current_pos]["prev_index"] = prev_index
            if longest_sequence_memo[index+current_pos]["seq_num"] > max_increasing_sequence:
                max_increasing_sequence = longest_sequence_memo[index+current_pos]["seq_num"]
                max_increasing_sequence_index = index+current_pos

    # if we're not able to find an index in the board which has a lower number, then that means our current_pos is at the lowest pos
    # this is our base case where longest_increasing_sequence will be 1
    if max_increasing_sequence == 0:
        longest_sequence_memo[current_pos] = {}
        longest_sequence_memo[current_pos]["seq_num"] = 1
        # setting this twice on purpose. When we reach sequence 1 via recursion we return a tuple
        # but, if the num_array given does not create a recursion, each index will need to be set with prev_index = None at this stage
        longest_sequence_memo[current_pos]["prev_index"] = None 
        return (longest_sequence_memo[current_pos]["seq_num"], None)

    # just an additional if statement, to make sure the very first iteration of the recursion is included in the memo dictionary
    # otherwise its value will just be returned but not included in our dictionary
    if current_pos not in longest_sequence_memo:
        longest_sequence_memo[current_pos] = {}
        longest_sequence_memo[current_pos]["seq_num"] = max_increasing_sequence+1
        longest_sequence_memo[current_pos]["prev_index"] = max_increasing_sequence_index

    return (max_increasing_sequence+1, max_increasing_sequence_index)


def wrapper_function(num_array, colour_array):
    '''
    A wrapper array for the actual recursion function.
    We'll use this to extract the winning indices and transform it to the array - which is the expected output
    '''

    # This loop ensures that all parts of the board is considered
    # i.e. we check all the indices within the array, to make sure we have the longest increasing sequence num for each index
    for index in range(len(num_array)):
        if index not in longest_sequence_memo:
            winning_sequence(num_array, colour_array, index)

    # Here, we are looking for the index that has the highest sequence number
    # We need to find the ending first (the last move of the longest increasing sequence) - since we will backtrack from here
    highest_sequence_number = 0
    highest_sequence_index = None
    for key in longest_sequence_memo:
        if longest_sequence_memo[key]["seq_num"] > highest_sequence_number:
            highest_sequence_number = longest_sequence_memo[key]["seq_num"]
            highest_sequence_index = key

    # Instantiating the array which will hold our winning steps (from the first move to the last move)
    winning_moves = []
    winning_moves.append(highest_sequence_index) # this is the very last move - we'll reverse the index later, so right now it's last to first move

    # Now start back-tracking
    index_to_visit = longest_sequence_memo[highest_sequence_index]["prev_index"]
    while index_to_visit != None:
        winning_moves.append(index_to_visit)
        index_to_visit = longest_sequence_memo[index_to_visit]["prev_index"]

    winning_moves = reversed(winning_moves)
    output = ','.join([str(index) for index in winning_moves])
    print(output)

print("Test Case 1")
longest_sequence_memo.clear()
wrapper_function([9,6,9,3,8,9,2,0,4,12],
                ["r","g","r","g","r","g","r","r","r","g"])


print("Test Case 2")
longest_sequence_memo.clear()
wrapper_function([1, 2, 3, 4, 5, 6, 7, 10],
                ["r","r","r","r","r","r","r","r"])

print("Test Case 3")
longest_sequence_memo.clear()
wrapper_function([5, 3, 2, 0, 24, 9, 20],
                ["g","g","g","g","r","r","g"])
