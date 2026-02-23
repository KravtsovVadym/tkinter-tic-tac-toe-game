## Tic-Tac-Toe Game / (GUI, AI opponent, tkinter)

### This is a simple tic-tac-toe game with a graphical interface, designed to consolidate practical experience in Python, implementing game logic, and basic artificial intelligence algorithms.

![Screen game](images/Screen_game.jpg)

### In this project, the following were implemented:
- Game logic for tic-tac-toe with win/draw detection
- Graphical interface using tkinter
- AI opponent with smart move prioritization
- Player choice: play as X or O (first or second move)
- Game restart functionality
- Visual game board with clickable cells
- Image handling using Pillow (PIL)

### Start-up instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/KravtsovVadym/tkinter-tic-tac-toe-game
    ```
    ```bash
    cd <tic-tac-toe-folder>
    ```
    ```bash
    python -m venv .venv
    ```
    ```bash
    source .venv/bin/activate # On Windows: .venv\Scripts\activate
    ```
    ```bash
    pip install -r requirements.txt
    ```
2. **Run the game:**
   ```bash
   python run.py
   ```
3. **How to play:**
   - Choose whether you want to play first (X) or second (O)
   - Click on cells to make your moves
   - AI will automatically make its moves
   - After game ends, click restart to play again
