# higher-or-lower-game-
<pre>
📉 📈 Higher Lower Game - Python
A Python implementation of the popular "Higher Lower" game. Test your intuition by guessing which celebrity, brand, or entity has more Instagram followers!

📖 Description
This is a text-based strategy game where the player is presented with two random entities (e.g., "Cristiano Ronaldo" vs "Ariana Grande"). The goal is to guess if the first person has more followers than the second.

If you guess correctly, the second person moves to the top slot, and a new challenger appears. The game continues until you guess wrong.

I built this project to master:

Working with Data: Importing and accessing complex lists of dictionaries from external files (game_data.py).

Comparison Logic: Comparing integer values nested inside dictionaries.

Game Loop: Creating a continuous "streak" mechanic where the game only ends on a loss.

Function Decomposition: Breaking logic into small, reusable functions (check, choose).

⚡ Features
Real Data: Uses a dataset of popular figures and their actual follower counts.

Score Tracking: Keeps count of your winning streak.

Dynamic Gameplay: The winner of the previous round becomes the "champion" for the next round.

Randomization: Every game offers different matchups.

🎮 How to Play
Run the script.

You will see two names (e.g., A: Taylor Swift vs B: Kim Kardashian).

The program asks: Does A have more followers than B?

Type y (Yes) if you think A is higher.

Type n (No) if you think B is higher.

If you are correct, your score increases, and the game continues.

If you are wrong, the game ends and your final score is displayed.</pre>
