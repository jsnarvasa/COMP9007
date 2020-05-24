def no_cut_tile(bathroom_array):
    '''
    Function is able to determine if a given n x m layout will mean that a 2x1 tile needs to be cut
    Input will be the room layout as a two-dimenional array, depicting RC
    Output will be TRUE or FALSE depending if a tile will need to be cut
    '''

    stack = []

    # starting at the first available tile - i.e. not FALSE
    for r_index, row in enumerate(bathroom_array):
        for c_index, column in enumerate(row):
            if column==False:
                continue
            current_tile = [r_index, c_index]
            while current_tile:
                current_row = current_tile[0]
                current_column = current_tile[1]
                stack.append([current_row, current_column]) # add to our stack the current location, so we can use for backtracking
                bathroom_array[current_row][current_column] = False # set our current location as false so it doesn't get detected later
                # check surrounding for other True tiles
                if current_row > 0 and bathroom_array[current_row-1][current_column] == True: # check north
                    current_tile = [current_row-1, current_column]
                elif current_row < len(bathroom_array)-1 and bathroom_array[current_row+1][current_column] == True: # check south
                    current_tile = [current_row+1, current_column]
                elif current_column > 0 and bathroom_array[current_row][current_column-1] == True: # check east
                    current_tile = [current_row, current_column-1]
                elif current_column < len(row)-1 and bathroom_array[current_row][current_column+1] == True: # check west
                    current_tile = [current_row, current_column+1]
                else:
                    current_tile = False
                print(f"currently at {current_row}, {current_column}")
            # we've reached the end of the path, now time to backtrack
            # break the stack as well, but checking first if the length is divisible by 2.


    print(stack)

no_cut_tile([[True,True,True],
                [True, False, True],
                [False, True, True],
                [True, False, False]])