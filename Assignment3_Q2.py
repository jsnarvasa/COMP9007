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
                adjacency_list[r_index, c_index] = []

            # check surrounding for other True tiles
                if r_index > 0 and room_array[r_index-1][c_index] == True: # check north
                    adjacency_list[r_index, c_index].append([r_index-1, c_index])
                if r_index < len(room_array)-1 and room_array[r_index+1][c_index] == True: # check south
                    adjacency_list[r_index, c_index].append([r_index+1, c_index])
                if c_index > 0 and room_array[r_index][c_index-1] == True: # check east
                    adjacency_list[r_index, c_index].append([r_index, c_index-1])
                if c_index < len(row)-1 and room_array[r_index][c_index+1] == True: # check west
                    adjacency_list[r_index, c_index].append([r_index, c_index+1])

    # We need to know how many neighbours each tileable segment has
    num_tile_neighbours = []
    for tileable in adjacency_list:
        num_neighbours = len(adjacency_list[tileable])
        num_tile_neighbours.append([tileable, num_neighbours])

    # now iterate through the list containing the num of neighbours
    while num_tile_neighbours:
        # Now sort it from smallest to largest num of neighbours
        num_tile_neighbours = sorted(num_tile_neighbours, key=lambda x: x[1], reverse=False)

        # Return True because you found a tileable segment which DOES NOT have a tileable neighbour
        # We will hit this point either at the very start of the iteration - where there is an isolated tileable segment
        # Middle or at the very end where teh remaining tile has no more available segment
        if num_tile_neighbours[0][1] == 0:
            return True
        
        # Now we are guaranteed to have the first array which has number of neighbours as 1 (since it's sorted in ASC order)
        # There will always be a tile which only has one tileable neighbour, we start with this
        segment_2_visit = num_tile_neighbours[0][0]

        paired_segment = tuple()
        # Need to make sure to pair with the neighbour with the least number of neighbours
        for index, val in enumerate(num_tile_neighbours):
            if index == 0:
                continue # skip the first index since you are looking for a tile to match this with

            if list(val[0]) in adjacency_list[segment_2_visit]:
                paired_segment = tuple(val[0])
                break

        # Here, we are reducing the number of tileable neighbours for the two segments by 1 - because the two are now tiled by 1 tile
        num_tile_neighbours[0][1] -=1
        for index, segment in enumerate(num_tile_neighbours):
            if segment[0] == paired_segment:
                num_tile_neighbours[index][1] -= 1
                break
        
        # Note, we don't need to update our adjacency_list - because, when choosing for the paired_segment, we choose from
        # the smallest segment in num_tile_neighbours.  Therefore, even though a segment may already have been paired with another tile
        # but we keep that segment within our adjacency_list, it will never be selected because we choose on what's num_tile_neighbours
        # which is always updated

        # Remove the index array if it reaches 0 - which it should.  This allows us to keep just looking at index 0 throughout the whole while loop
        # we only need to check the first two - it is impossible to get 3 indexes to turn 0 in one turn (since we only reduce by 1 for two items above)
        # First is segment_2_visit and second is paired_segment - if we do delete two here, that means we finished and no tiles needs to be cut
        for index in range(2):
            if num_tile_neighbours[0][1] == 0:
                print(f"deleted {num_tile_neighbours[0]}")
                del num_tile_neighbours[0]

    return False



print(is_cut_required_v2([[True,True,True],
                [True, False, True],
                [True, False, True],
                [False, False, True]]))