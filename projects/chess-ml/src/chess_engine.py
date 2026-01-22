import chess
import random

def main():
    """
    Main entry point for the chess engine.
    Initializes the board and plays a short game using random legal moves.
    This serves as a baseline before introducing evaluation functions and ML.
    """

    # Initialize a standard chess board in the starting position
    board = chess.Board()

    # Print the initial board state
    print("Initial Board:")
    print(board)
    print("\n")

    move_count = 0  # Track number of moves played

    # Play until the game ends or a move limit is reached
    while not board.is_game_over() and move_count < 20:

        # Generate all legal moves from the current board state
        legal_moves = list(board.legal_moves)

        # Select a random move (baseline policy)
        move = random.choice(legal_moves)

        # Apply the move to the board
        board.push(move)
        move_count += 1

        # Print move information and updated board
        print(f"Move {move_count}: {move}")
        print(board)
        print("\n")

    # Print final game result (win, loss, or draw)
    print("Game over:", board.result())


# Run main() only if this file is executed directly
if __name__ == "__main__":
    main()
