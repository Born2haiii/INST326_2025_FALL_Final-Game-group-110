# 326-Final-Game-group-110

# PyCraft - Minecraft-Inspired Crafting Game

## Project Overview: 
PyCraft is a console-based crafting game inspired by Minecraft's crafting system. Players use a 3x3 grid to combine materials (STONE, WOOD, STICK, DIAMOND) to craft various items like swords and pickaxes. The game tracks player efficiency and provides feedback on optimal crafting paths.

### `PyCraft.py` 
The main game file containing all game logic, including:
- **Recipe definitions**: Dictionaries storing all crafting recipes for swords and pickaxes
- **Gameboard class**: Manages the 3x3 crafting grid and tracks user actions
- **Pattern recognition**: `Crafting_check()` function validates when a recipe is completed
- **Path analysis**: `analyze_fastest_path()` compares user steps to optimal paths
- **Analysis helper**: `get_crafting_analysis()` used to feed the result from the checked item into the crafting function
- **User interface**: Console-based display and interaction system
- **Game loop**: `menu()` Main menu and gameplay flow

## How to use the Program

**NOTE** This program takes no command line arguments, instead it takes advantage of input statements


#### Starting the Game
1. When you run the program, you'll see the main menu:
    ```
    ==== PyCraft====
    
        1. Start Game 
        2. End Game 
    
    Please choose 1 or 2:
    ```
2. Enter `1` to start a new game or `2` to exit

#### Understanding the Board
- The game displays a 3x3 grid with coordinates and the goal is to fill those coordinates withthe correct path to craft the desired item.
- It loops until attempts have run out. Users get 9 attempts max. 
- Users can hit `Q` to quit

#### Placing Materials
- **Input format**: `COORDINATE,MATERIAL`
  - Example: `A1,STONE` places stone at position A1
  - Example: `B2,STICK` places a stick at position B2

- **Valid coordinates**: A1, A2, A3, B1, B2, B3, C1, C2, C3
- **Valid materials**: STONE, WOOD, STICK, DIAMOND


#### Success Message
    When you successfully craft an item the message below will be shown. Afterwards, the craft analysis will display to the user
    ```
    You have crafted a stone sword in 5 attempts!
    ```
**Understanding the metrics**:
- **Your steps**: Total placements you made
- **Optimal steps**: Minimum placements needed
- **Extra steps**: How many unnecessary placements you made
- **Efficiency**: Percentage score (100% = perfect)
- **Recommended optimal path**: The most efficient sequence for this recipe

## Annotated Bibliography

### Python Programming Resources

- **Real Python - Regular Expressions Tutorial**  
    https://realpython.com/regex-python/  
    Used to implement the regex pattern matching in `get_crafting_analysis()` to extract the crafted item name from success       messages. Specifically helped with understanding capture groups and the `re.search()` method.



## Attribution

| Method/Function | Primary Author | Techniques Demonstrated |
|----------------|----------------|------------------------|
| analyze_fastest_path | Ibukun Adenuga | Conditional expressions|
| get_crafting_analysis | Ibukun Adenuga | Regex|
| get_action_history | Ibukun Adenuga | None| 
| panel  | Yushen An  | comprehension, conditional expressions, key functions  |
| print_game  | Yushen An  | comprehension, conditional expressions  |


