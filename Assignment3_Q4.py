longest_sequence_memo = {}

def winning_sequence(num_array, colour_array, current_pos):
    '''
    INPUT: array of numbers for the board,
        corresponding array denoting colour for each number on the board,
        the current index position that we're looking to obtain the max increasing sequence for
    OUTPUT: array containing the index positions of the winning move for the given board
    '''

    if current_pos in longest_sequence_memo:
        return longest_sequence_memo[current_pos]

    max_increasing_sequence = 0
    max_increasing_sequence_index = None

    # checking to the left of our current position - meaning we only look for x[j] < x[current_pos] to our left which are GREEN
    for index, num in enumerate(num_array[:current_pos]):
        if num < num_array[current_pos] and colour_array[index] == "g":
            # check if we already have the value in our memoization dict else, try to find out what the longest sequence is for that index by checking against the other candidates
            if index not in longest_sequence_memo:
                # we'll need to store this value for future reference if it's not in our memoization dict already
                longest_sequence_memo[index] = winning_sequence(num_array, colour_array, index)
            # we just compare and look for the highest increasing sequence
            if longest_sequence_memo[index] > max_increasing_sequence:
                max_increasing_sequence = longest_sequence_memo[index]
                max_increasing_sequence_index = index
    
    # checking to the right of our current position - meaning we only look for x[j] < x[current_pos] to our right which are RED
    for index, num in enumerate(num_array[current_pos:]):
        if num < num_array[current_pos] and colour_array[index+current_pos] == "r":
            if index+current_pos not in longest_sequence_memo:
                longest_sequence_memo[index+current_pos] = winning_sequence(num_array, colour_array, index+current_pos)
            if longest_sequence_memo[index+current_pos] > max_increasing_sequence:
                max_increasing_sequence = longest_sequence_memo[index+current_pos]
                max_increasing_sequence_index = index+current_pos

    # if we're not able to find an index in the board which has a lower number, then that means our current_pos is at the lowest pos
    # this is our base case where longest_increasing_sequence will be 1
    if max_increasing_sequence == 0:
        longest_sequence_memo[current_pos] = 1
        return longest_sequence_memo[current_pos]

    # just an additional if statement, to make sure the very first iteration of the recursion is included in the memo dictionary
    # otherwise its value will just be returned but not included in our dictionary
    if current_pos not in longest_sequence_memo:
        longest_sequence_memo[current_pos] = max_increasing_sequence+1

    return max_increasing_sequence+1


def wrapper_function(num_array, colour_array, current_pos):
    '''
    A wrapper array for the actual recursion function.
    We'll use this to extract the winning indices and transform it to the array - which is the expected output
    '''

    winning_sequence(num_array, colour_array, current_pos)

    winning_moves = []
    for key in longest_sequence_memo:
        winning_moves.append([key, longest_sequence_memo[key]])

    winning_moves = sorted(winning_moves, key=lambda x: x[1], reverse=False)

    winning_moves_index = [turn[0] for turn in winning_moves]

    return winning_moves_index

print(wrapper_function([9,6,9,3,8,9,2,0,4,12],
                ["r","g","r","g","r","g","r","r","r","g"],
                0))