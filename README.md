# chess-game-generator

This repository contains Python code for generating multiple games of chess using the Stockfish chess engine, and storing the resulting moves in a Pandas DataFrame which is then saved to a CSV file. The main script includes two functions: **generate_game** which generates a single game with a specified time limit per move, and **generate_games** which generates multiple games and returns a DataFrame with the game index and the list of moves. The resulting CSV file can be used for further analysis or machine learning tasks.

## Usage

To use this code, simply clone the repository and run the ``chess_engine.py`` script using a Python interpreter. You can customize the number of games and the time limit per move by editing the parameters in the **generate_games** function call. By default, the generated games are saved to a CSV file named ``chess_games.csv`` in the same directory as the script.

If you prefer to run the code in a Jupyter Notebook environment, you can also use the provided ``chess_engine.ipynb`` notebook. This notebook includes sample code for loading the generated CSV file into a Pandas DataFrame and visualizing some basic statistics of the games.


## Google Colab

There is also a **Google Colab notebook** available for this code. This notebook allows you to run the code in a cloud-based environment without having to install any software locally. Simply open the notebook in your browser and follow the instructions. Note that you will need to have a Google account to use Google Colab.


## Requirements

This code requires the following Python packages:

    chess
    chess.engine
    pandas

You also need to have the Stockfish chess engine installed on your system. You can download Stockfish from the official website: https://stockfishchess.org/download/


## License

This code is released under the **MIT License**. Feel free to use, modify, and distribute the code as you wish. If you find this code useful, I would appreciate it if you could give credit by citing this repository in your work.
