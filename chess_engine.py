import chess
import chess.engine
import pandas as pd

# Function to generate a chess game
def generate_game(time_per_move):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish")
    board = chess.Board()
    
    moves = []

    while not board.is_game_over():

        result = engine.play(board, chess.engine.Limit(time=time_per_move))

        move = result.move
        board.push(move)

        moves.append(move)

    engine.quit()
    print(moves)
    return moves

# Function to generate multiple games and store the results in a DataFrame
def generate_games(num_games, time_per_move):
    df = pd.DataFrame(columns=["Game", "Moves"])

    for i in range(num_games):
        moves = generate_game(time_per_move)
        df = pd.concat([df, pd.DataFrame({"Game": [i], "Moves": [moves]})], ignore_index=True)
    df.to_csv("chess_games.csv", index=False)
    return df

# Example usage: generate 100 games with 1 second per move
df = generate_games(100, 1.0)
print(df)
