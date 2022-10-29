# -*- coding: utf-8 -*-


# Finds the set of possible next moves, given the current of the game.
def next_moves(state):
    # define a list to contain the new moves
    new = []
    
    # loop over all the possible moves
    for i in range(1,10):
        # Check if this would be a valid move. So it is not in the previous moves
        # of this player or it is not the previous move of the other player.
        if (i not in state[(len(state)%2)::2]) and (i != state[len(state)-1]):
            # Append the new move to new
            new.append(state + [i,])
            
    return new

# Returns a boolean value for the statement that there is a three in a row
def check_3_row(state):
    # Make a list of the squares that have been taken by both players
    os = [i * int(state.count(i) == 2) for i in range(1,10)]
    
    # if the middle square has been taken
    if 5 in os:
        # Compute the absolute relative positions of all the filled squares
        os5 = [abs(s - 5) for s in os]
        
        # Loop over all the possible relative positions
        for i in range(1,5):
            # Check if there are two filled squares with this absolute relative
            # position. This would mean that there would be a three in a row
            # around the middle square. If so return True.
            if os5.count(i) == 2:
                return True
    
    # Return a boolean value for if there are three in a rows on the horizontal 
    # and vertical side edges.
    return ((((1 in os) and (2 in os)) or ((6 in os) and (9 in os))) and (3 in os)) or \
        ((((1 in os) and (4 in os)) or ((8 in os) and (9 in os))) and (7 in os))

# Return the value of the given state.
# 0 means that no one has won yet
# 1 means that player 2 has won
# 2 means a draw
# 3 means that player 1 has won
def value(state):
    # Check if there is 3-in-a-row. If so the game is over and the value should
    # not be zero
    if check_3_row(state):
        # If there is a 3-in-a-row and player 1 has just played, player 1 wins.
        # This can be seen from the fact that there is an uneven number of turns
        # played if player 1 has just played.
        if len(state)%2 == 1:
            return 3 # win for starting player
        # Otherwise player 2 won
        else:
            return 1 # lose for starting player
    # If there is no 3-in-a-row, but the board is full, there is a draw
    elif len(state) == 18:
        return 2 # draw
    # If non of these things are the case, the came has not ended yet.
    else:
        return 0 # no outcome yet

# Recursive function to check what the outcome will be if both players play the
# best they can and with full knowledge of all the options given a certain 
# situation on the board. Basically, we check if there is a winning strategy
# given a certain board situation.
def recursive(state):
    # If the game is decided, we just return the value of this board situation.
    if v := value(state):
        return v
    
    # Find all the next moves from this board situation.
    new_moves = next_moves(state)
    # Make a list with all the outcomes of these moves. Would we win or lose 
    # if we did this.
    outcomes = []
    
    # The script which finds the outcome of every possible move.
    # If player 1 would have the turn
    if len(state)%2 == 0:
        # We loop over all the possible moves
        for move in new_moves:
            # Find the outcome of this move by applying this function
            outcome = recursive(move)
            # if the outcome of this move would be that player 1 would win
            # the game, he will certainly choose this or a better option. Either
            # way he will be able to make a move that will lead him to victory.
            # So given this situation he will win. That is what we return.
            if outcome == 3:
                return 3
            # If not we just add the outcome to the outcomes list
            outcomes.append(outcome)
        
        # Since player 1 plays optimally he will make the best move for him. That
        # will thus be the outcome of this situation. 
        return max(outcomes)
    
    # If the player 2 would have the turn
    # We loop over all the possible moves
    for move in new_moves:
        # Find the outcome of this move by applying this function
        outcome = recursive(move)
        # if the outcome of this move would be that player 2 would win
        # the game, player 2 will certainly choose this or a better option. Either
        # way player 2 will be able to make a move that will lead him to victory.
        # So given this situation player 2 will win. That is what we return.
        if outcome == 1:
            return 1
        # If not we just add the outcome to the outcomes list
        outcomes.append(outcome)
    
    # Since player 2 plays optimally he will make the best move for him. That
    # will thus be the outcome of this situation. 
    return min(outcomes)
    




