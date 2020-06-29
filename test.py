from tictactoe import initial_state, player, actions, result, winner, minimax

board = result(initial_state(), (0, 0))

print(minimax(board))