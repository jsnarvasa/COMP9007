def is_cut_required_v2(room_array):
    '''
    INPUT: double-sided array - which is the layout of the room with True or False values
    OUTPUT: True or False boolean - True if the room_array is such that a 2x1 tile will need to be cut, False if tile/s doesn't need to be cut
    '''

    # instantiating our adjacency list
    adjacency_list = {}

    # building the adjacency list, based on the neighbouring segments
    # this will help us determine if a segment has a neighbouring segment which can be tiled, which we'll use during matching later
    for r_index, row in enumerate(room_array):
        for c_index, column in enumerate(row):

            if column == True:
                adjacency_list[r_index, c_index] = {}
                adjacency_list[r_index, c_index]['neighbours'] = []
                adjacency_list[r_index, c_index]['num_neighbours'] = 0

            # check surrounding for other True tiles
                if r_index > 0 and room_array[r_index-1][c_index] == True: # check north
                    adjacency_list[r_index, c_index]['neighbours'].append([r_index-1, c_index])
                if r_index < len(room_array)-1 and room_array[r_index+1][c_index] == True: # check south
                    adjacency_list[r_index, c_index]['neighbours'].append([r_index+1, c_index])
                if c_index > 0 and room_array[r_index][c_index-1] == True: # check east
                    adjacency_list[r_index, c_index]['neighbours'].append([r_index, c_index-1])
                if c_index < len(row)-1 and room_array[r_index][c_index+1] == True: # check west
                    adjacency_list[r_index, c_index]['neighbours'].append([r_index, c_index+1])

    # We need to know how many neighbours each tileable segment has
    for segment in adjacency_list:
        adjacency_list[segment]['num_neighbours'] = len(adjacency_list[segment]['neighbours'])
            

    # Now, we keep this loop going, while there are still tileable segments that are not done
    while bool(adjacency_list):
        
         # 4 is the max number of neighbours a tile can have (not arbitrary num)
        smallest_neighbour_count = 4
        smallest_neighbour = tuple()
        for segment in adjacency_list:
            if adjacency_list[segment]['num_neighbours'] < smallest_neighbour_count:
                smallest_neighbour = tuple(segment)
                smallest_neighbour_count = adjacency_list[segment]['num_neighbours']

        # Starting from the segment that we know has the smallest num of neighbours

        # Return True because you found a tileable segment which DOES NOT have a tileable neighbour
        if smallest_neighbour_count == 0:
            return True
        
        # From the segment that we are in, look for one of it's adjacent segments that has the smallest num of other adjacent tiles
        smallest_other_neighbour_count = 4
        smallest_other_neighbour = tuple()
        for segment in adjacency_list[smallest_neighbour]['neighbours']:
            segment = tuple(segment)
            if segment in adjacency_list and adjacency_list[segment]['num_neighbours'] < smallest_other_neighbour_count:
                smallest_other_neighbour = segment
                smallest_other_neighbour_count = adjacency_list[segment]['num_neighbours']
        
        # If not able to find an AVAILABLE adjacent segment (meaning a tileable neighbour - not already tiled), then means we have an isolated segment
        if bool(smallest_other_neighbour) == False:
            return True

        # Now, we've found a segment that needs to be tile, as well as an adjacent segment to it - that has the least num of neighbours
        # We will pair the two with one tile.  But first need to update the num of tileable neighbours of the two segments, to reflect this change
        for adjacent_segments in adjacency_list[smallest_neighbour]['neighbours']:
            adjacent_segments = tuple(adjacent_segments)
            if adjacent_segments in adjacency_list:
                adjacency_list[adjacent_segments]['num_neighbours'] -= 1

        for adjacent_segments in adjacency_list[smallest_other_neighbour]['neighbours']:
            adjacent_segments = tuple(adjacent_segments)
            if adjacent_segments in adjacency_list:
                adjacency_list[adjacent_segments]['num_neighbours'] -= 1

        # Delete the two (just) tiled segments from our adjacency list
        adjacency_list.pop(smallest_neighbour)
        adjacency_list.pop(smallest_other_neighbour)

        # If we only have one tileable segment left, then it's not possible to pair it with another segment.  Need to cut tile.
        if len(adjacency_list) == 1:
            return True
    
    return False



print(is_cut_required_v2([[True,True,True],
                [True, False, True],
                [True, False, True],
                [True, False, True]]))