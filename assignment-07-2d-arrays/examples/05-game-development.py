"""
Assignment 7 - Example 5: Game Development with 2D Arrays
=========================================================

This program demonstrates how 2D arrays are essential for game development,
from simple grid-based games to complex game mechanics. 2D arrays provide
the foundation for game boards, maps, collision detection, and state management.

Key Concepts Demonstrated:
- Game board representation and management
- Player movement and collision detection
- Enemy AI and pathfinding in games
- Game physics simulation
- Level design and procedural generation
- Turn-based and real-time game mechanics
"""

import random
import time
from collections import deque

print("=== GAME DEVELOPMENT WITH 2D ARRAYS ===")
print()

print("2D arrays are fundamental to game development:")
print("• Game boards: Tic-tac-toe, chess, checkers")
print("• Level maps: Platformers, RPGs, strategy games")
print("• Collision detection: Tile-based collision systems")
print("• Pathfinding: AI movement in grid-based worlds")
print("• Game state: Track objects, resources, territories")
print("• Procedural generation: Random level creation")
print()

# BASIC GAME BOARD IMPLEMENTATION
print("=== BASIC GAME BOARD IMPLEMENTATION ===")
print()

class GameBoard:
    """Generic game board class for grid-based games."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.turn_count = 0
        
        # Define cell types
        self.EMPTY = 0
        self.PLAYER = 1
        self.ENEMY = 2
        self.WALL = 3
        self.TREASURE = 4
        self.TRAP = 5
    
    def is_valid_position(self, row, col):
        """Check if position is within board bounds."""
        return 0 <= row < self.height and 0 <= col < self.width
    
    def get_cell(self, row, col):
        """Get cell value at position."""
        if self.is_valid_position(row, col):
            return self.board[row][col]
        return None
    
    def set_cell(self, row, col, value):
        """Set cell value at position."""
        if self.is_valid_position(row, col):
            self.board[row][col] = value
            return True
        return False
    
    def is_empty(self, row, col):
        """Check if cell is empty."""
        return self.get_cell(row, col) == self.EMPTY
    
    def clear_board(self):
        """Clear all cells to empty."""
        for row in range(self.height):
            for col in range(self.width):
                self.board[row][col] = self.EMPTY
        self.turn_count = 0
    
    def count_cells(self, cell_type):
        """Count cells of specific type."""
        count = 0
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == cell_type:
                    count += 1
        return count
    
    def find_cells(self, cell_type):
        """Find all cells of specific type."""
        cells = []
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == cell_type:
                    cells.append((row, col))
        return cells
    
    def display(self, symbols=None):
        """Display the board."""
        if symbols is None:
            symbols = {
                self.EMPTY: '.',
                self.PLAYER: 'P',
                self.ENEMY: 'E',
                self.WALL: '█',
                self.TREASURE: '$',
                self.TRAP: 'X'
            }
        
        print("  ", end="")
        for col in range(self.width):
            print(f"{col % 10}", end="")
        print()
        
        for row in range(self.height):
            print(f"{row % 10} ", end="")
            for col in range(self.width):
                cell_value = self.board[row][col]
                symbol = symbols.get(cell_value, '?')
                print(symbol, end="")
            print()
        print()

# Demonstrate basic board operations
print("Game Board Operations:")
game_board = GameBoard(10, 8)

# Add some game elements
game_board.set_cell(3, 4, game_board.PLAYER)
game_board.set_cell(1, 2, game_board.ENEMY)
game_board.set_cell(6, 7, game_board.TREASURE)
game_board.set_cell(4, 4, game_board.WALL)
game_board.set_cell(2, 6, game_board.TRAP)

print("Sample game board:")
game_board.display()

# TIC-TAC-TOE GAME
print("=== TIC-TAC-TOE GAME ===")
print()

class TicTacToe:
    """Complete Tic-Tac-Toe game implementation."""
    
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
    
    def display_board(self):
        """Display the tic-tac-toe board."""
        print("  0 1 2")
        for row in range(3):
            print(f"{row} ", end="")
            for col in range(3):
                print(self.board[row][col], end="")
                if col < 2:
                    print("|", end="")
            print()
            if row < 2:
                print("  -----")
        print()
    
    def make_move(self, row, col):
        """Make a move if position is valid."""
        if (0 <= row < 3 and 0 <= col < 3 and 
            self.board[row][col] == ' ' and not self.game_over):
            
            self.board[row][col] = self.current_player
            
            if self.check_winner():
                self.game_over = True
                self.winner = self.current_player
            elif self.is_board_full():
                self.game_over = True
                self.winner = 'Tie'
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            
            return True
        return False
    
    def check_winner(self):
        """Check if current player has won."""
        player = self.current_player
        
        # Check rows
        for row in range(3):
            if all(self.board[row][col] == player for col in range(3)):
                return True
        
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
        
        return False
    
    def is_board_full(self):
        """Check if board is full."""
        return all(self.board[row][col] != ' ' 
                  for row in range(3) for col in range(3))
    
    def get_available_moves(self):
        """Get list of available moves."""
        moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    moves.append((row, col))
        return moves
    
    def evaluate_position(self):
        """Evaluate position for AI (simple heuristic)."""
        if self.check_winner():
            return 10 if self.current_player == 'O' else -10
        return 0
    
    def ai_move_random(self):
        """Make random AI move."""
        available = self.get_available_moves()
        if available:
            row, col = random.choice(available)
            return self.make_move(row, col)
        return False
    
    def ai_move_strategic(self):
        """Make strategic AI move (basic strategy)."""
        # Check for winning move
        for row, col in self.get_available_moves():
            # Try move
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.board[row][col] = ' '  # Undo
                return self.make_move(row, col)
            self.board[row][col] = ' '  # Undo
        
        # Check for blocking opponent's winning move
        opponent = 'X' if self.current_player == 'O' else 'O'
        for row, col in self.get_available_moves():
            # Try opponent's move
            self.board[row][col] = opponent
            temp_player = self.current_player
            self.current_player = opponent
            if self.check_winner():
                self.current_player = temp_player
                self.board[row][col] = ' '  # Undo
                return self.make_move(row, col)
            self.current_player = temp_player
            self.board[row][col] = ' '  # Undo
        
        # Take center if available
        if self.board[1][1] == ' ':
            return self.make_move(1, 1)
        
        # Take corner
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        available_corners = [pos for pos in corners if self.board[pos[0]][pos[1]] == ' ']
        if available_corners:
            row, col = random.choice(available_corners)
            return self.make_move(row, col)
        
        # Make any available move
        return self.ai_move_random()

# Demonstrate Tic-Tac-Toe game
print("Tic-Tac-Toe Game Simulation:")
ttt_game = TicTacToe()

# Simulate a game with AI moves
moves_sequence = [(1, 1), (0, 0), (0, 1), (2, 2), (2, 1)]  # Predetermined moves for demo

print("Game progression:")
ttt_game.display_board()

for i, (row, col) in enumerate(moves_sequence):
    if not ttt_game.game_over:
        print(f"Player {ttt_game.current_player} moves to ({row}, {col}):")
        ttt_game.make_move(row, col)
        ttt_game.display_board()
        
        if ttt_game.game_over:
            if ttt_game.winner == 'Tie':
                print("Game ended in a tie!")
            else:
                print(f"Player {ttt_game.winner} wins!")
            break

# MAZE RUNNER GAME
print("=== MAZE RUNNER GAME ===")
print()

class MazeRunner:
    """Maze runner game with player movement and goal collection."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[0 for _ in range(width)] for _ in range(height)]
        
        # Game elements
        self.EMPTY = 0
        self.WALL = 1
        self.PLAYER = 2
        self.GOAL = 3
        self.VISITED = 4
        
        # Player state
        self.player_row = 1
        self.player_col = 1
        self.goals_collected = 0
        self.total_goals = 0
        self.moves = 0
        self.visited_cells = set()
        
        self.generate_maze()
        self.place_goals()
    
    def generate_maze(self):
        """Generate a simple maze."""
        # Initialize with walls
        for row in range(self.height):
            for col in range(self.width):
                if row == 0 or row == self.height - 1 or col == 0 or col == self.width - 1:
                    self.maze[row][col] = self.WALL
                elif row % 2 == 0 and col % 2 == 0:
                    self.maze[row][col] = self.WALL
                else:
                    self.maze[row][col] = self.EMPTY
        
        # Add some internal walls randomly
        for _ in range(self.width + self.height):
            row = random.randint(1, self.height - 2)
            col = random.randint(1, self.width - 2)
            if (row, col) != (1, 1):  # Don't block starting position
                self.maze[row][col] = self.WALL
        
        # Ensure starting position is clear
        self.maze[1][1] = self.EMPTY
    
    def place_goals(self):
        """Place goals randomly in the maze."""
        goal_count = max(3, self.width * self.height // 20)
        placed = 0
        
        while placed < goal_count:
            row = random.randint(1, self.height - 2)
            col = random.randint(1, self.width - 2)
            
            if (self.maze[row][col] == self.EMPTY and 
                (row, col) != (self.player_row, self.player_col)):
                self.maze[row][col] = self.GOAL
                placed += 1
        
        self.total_goals = placed
    
    def display_maze(self):
        """Display the current maze state."""
        symbols = {
            self.EMPTY: '.',
            self.WALL: '█',
            self.PLAYER: 'P',
            self.GOAL: '$',
            self.VISITED: '°'
        }
        
        print(f"Moves: {self.moves}, Goals: {self.goals_collected}/{self.total_goals}")
        print("  ", end="")
        for col in range(self.width):
            print(f"{col % 10}", end="")
        print()
        
        for row in range(self.height):
            print(f"{row % 10} ", end="")
            for col in range(self.width):
                if row == self.player_row and col == self.player_col:
                    print('P', end="")
                elif (row, col) in self.visited_cells and self.maze[row][col] == self.EMPTY:
                    print('°', end="")
                else:
                    cell_value = self.maze[row][col]
                    symbol = symbols.get(cell_value, '?')
                    print(symbol, end="")
            print()
        print()
    
    def move_player(self, direction):
        """Move player in specified direction."""
        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        
        if direction not in directions:
            return False
        
        dr, dc = directions[direction]
        new_row = self.player_row + dr
        new_col = self.player_col + dc
        
        # Check bounds and walls
        if (0 <= new_row < self.height and 0 <= new_col < self.width and
            self.maze[new_row][new_col] != self.WALL):
            
            # Mark current position as visited
            self.visited_cells.add((self.player_row, self.player_col))
            
            # Check for goal collection
            if self.maze[new_row][new_col] == self.GOAL:
                self.goals_collected += 1
                self.maze[new_row][new_col] = self.EMPTY
            
            # Move player
            self.player_row = new_row
            self.player_col = new_col
            self.moves += 1
            
            return True
        
        return False
    
    def is_game_complete(self):
        """Check if all goals have been collected."""
        return self.goals_collected >= self.total_goals
    
    def get_shortest_path_to_goal(self):
        """Find shortest path to nearest goal using BFS."""
        if self.goals_collected >= self.total_goals:
            return []
        
        # Find all remaining goals
        goals = []
        for row in range(self.height):
            for col in range(self.width):
                if self.maze[row][col] == self.GOAL:
                    goals.append((row, col))
        
        if not goals:
            return []
        
        # BFS to find shortest path to any goal
        queue = deque([(self.player_row, self.player_col, [])])
        visited = set()
        visited.add((self.player_row, self.player_col))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direction_names = ['up', 'down', 'left', 'right']
        
        while queue:
            row, col, path = queue.popleft()
            
            # Check if we reached a goal
            if (row, col) in goals:
                return path
            
            # Explore neighbors
            for i, (dr, dc) in enumerate(directions):
                new_row, new_col = row + dr, col + dc
                
                if ((0 <= new_row < self.height and 0 <= new_col < self.width) and
                    (new_row, new_col) not in visited and
                    self.maze[new_row][new_col] != self.WALL):
                    
                    visited.add((new_row, new_col))
                    new_path = path + [direction_names[i]]
                    queue.append((new_row, new_col, new_path))
        
        return []  # No path found

# Demonstrate Maze Runner game
print("Maze Runner Game:")
random.seed(42)  # For reproducible maze
maze_game = MazeRunner(15, 10)

print("Initial maze:")
maze_game.display_maze()

# Simulate some moves
print("Auto-solving using shortest path algorithm...")
step = 0
max_steps = 50

while not maze_game.is_game_complete() and step < max_steps:
    path = maze_game.get_shortest_path_to_goal()
    
    if path:
        # Take first move from optimal path
        next_move = path[0]
        if maze_game.move_player(next_move):
            step += 1
            if step % 5 == 0 or maze_game.is_game_complete():  # Show progress every 5 moves
                print(f"After {maze_game.moves} moves:")
                maze_game.display_maze()
        else:
            break
    else:
        print("No path to goals found!")
        break

if maze_game.is_game_complete():
    print(f"🎉 Maze completed in {maze_game.moves} moves!")
else:
    print("Maze solving stopped - maximum steps reached.")

# SIMPLE RPG BATTLE SYSTEM
print("=== SIMPLE RPG BATTLE SYSTEM ===")
print()

class RPGBattleSystem:
    """Turn-based RPG battle system using 2D arrays for positioning."""
    
    def __init__(self):
        self.battle_grid = [[0 for _ in range(8)] for _ in range(6)]
        
        # Cell types
        self.EMPTY = 0
        self.PLAYER = 1
        self.ENEMY = 2
        self.OBSTACLE = 3
        self.EFFECT = 4
        
        # Game state
        self.turn = 0
        self.battle_over = False
        
        # Characters
        self.player = {
            'row': 2, 'col': 1,
            'hp': 100, 'max_hp': 100,
            'attack': 20, 'defense': 5,
            'speed': 8, 'alive': True
        }
        
        self.enemies = [
            {'row': 2, 'col': 6, 'hp': 60, 'max_hp': 60, 'attack': 15, 'defense': 3, 'speed': 6, 'alive': True, 'type': 'Orc'},
            {'row': 4, 'col': 5, 'hp': 40, 'max_hp': 40, 'attack': 12, 'defense': 2, 'speed': 9, 'type': 'Goblin', 'alive': True},
            {'row': 1, 'col': 7, 'hp': 80, 'max_hp': 80, 'attack': 18, 'defense': 4, 'speed': 5, 'type': 'Ogre', 'alive': True}
        ]
        
        self.setup_battlefield()
    
    def setup_battlefield(self):
        """Setup initial battlefield layout."""
        # Clear grid
        for row in range(len(self.battle_grid)):
            for col in range(len(self.battle_grid[0])):
                self.battle_grid[row][col] = self.EMPTY
        
        # Place obstacles
        obstacles = [(0, 3), (1, 4), (3, 2), (4, 6), (5, 3)]
        for row, col in obstacles:
            self.battle_grid[row][col] = self.OBSTACLE
        
        # Place characters
        self.battle_grid[self.player['row']][self.player['col']] = self.PLAYER
        
        for enemy in self.enemies:
            if enemy['alive']:
                self.battle_grid[enemy['row']][enemy['col']] = self.ENEMY
    
    def display_battlefield(self):
        """Display the current battlefield state."""
        symbols = {
            self.EMPTY: '.',
            self.PLAYER: 'P',
            self.ENEMY: 'E',
            self.OBSTACLE: '█',
            self.EFFECT: '*'
        }
        
        print(f"=== Turn {self.turn} ===")
        print("Battlefield:")
        print("  01234567")
        
        for row in range(len(self.battle_grid)):
            print(f"{row} ", end="")
            for col in range(len(self.battle_grid[0])):
                cell_value = self.battle_grid[row][col]
                symbol = symbols.get(cell_value, '?')
                print(symbol, end="")
            print()
        
        print(f"\nPlayer HP: {self.player['hp']}/{self.player['max_hp']}")
        print("Enemies:")
        for i, enemy in enumerate(self.enemies):
            if enemy['alive']:
                status = f"  {enemy['type']}: {enemy['hp']}/{enemy['max_hp']} HP at ({enemy['row']}, {enemy['col']})"
                print(status)
        print()
    
    def calculate_distance(self, pos1, pos2):
        """Calculate Manhattan distance between two positions."""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def get_valid_moves(self, character):
        """Get valid move positions for character."""
        moves = []
        current_row, current_col = character['row'], character['col']
        
        # Check all adjacent positions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current_row + dr, current_col + dc
            
            if (0 <= new_row < len(self.battle_grid) and 
                0 <= new_col < len(self.battle_grid[0]) and
                self.battle_grid[new_row][new_col] in [self.EMPTY, self.EFFECT]):
                moves.append((new_row, new_col))
        
        return moves
    
    def move_character(self, character, new_row, new_col):
        """Move character to new position."""
        old_row, old_col = character['row'], character['col']
        
        # Clear old position
        self.battle_grid[old_row][old_col] = self.EMPTY
        
        # Update character position
        character['row'] = new_row
        character['col'] = new_col
        
        # Set new position
        char_type = self.PLAYER if character == self.player else self.ENEMY
        self.battle_grid[new_row][new_col] = char_type
    
    def attack_target(self, attacker, target):
        """Perform attack between characters."""
        # Calculate damage
        base_damage = attacker['attack']
        defense = target['defense']
        damage = max(1, base_damage - defense + random.randint(-3, 3))
        
        # Apply damage
        target['hp'] = max(0, target['hp'] - damage)
        
        print(f"{attacker.get('type', 'Player')} attacks {target.get('type', 'Player')} for {damage} damage!")
        
        # Check if target is defeated
        if target['hp'] <= 0:
            target['alive'] = False
            self.battle_grid[target['row']][target['col']] = self.EMPTY
            defeated_type = target.get('type', 'Player')
            print(f"{defeated_type} is defeated!")
    
    def ai_turn(self, enemy):
        """Simple AI turn logic."""
        player_pos = (self.player['row'], self.player['col'])
        enemy_pos = (enemy['row'], enemy['col'])
        distance = self.calculate_distance(enemy_pos, player_pos)
        
        # If close enough to attack (adjacent), attack
        if distance == 1:
            self.attack_target(enemy, self.player)
        else:
            # Try to move closer to player
            valid_moves = self.get_valid_moves(enemy)
            
            if valid_moves:
                # Choose move that gets closest to player
                best_move = None
                best_distance = float('inf')
                
                for move_row, move_col in valid_moves:
                    move_distance = self.calculate_distance((move_row, move_col), player_pos)
                    if move_distance < best_distance:
                        best_distance = move_distance
                        best_move = (move_row, move_col)
                
                if best_move:
                    print(f"{enemy['type']} moves to {best_move}")
                    self.move_character(enemy, best_move[0], best_move[1])
    
    def player_turn(self):
        """Simulate player turn with simple strategy."""
        # Find closest alive enemy
        closest_enemy = None
        closest_distance = float('inf')
        
        for enemy in self.enemies:
            if enemy['alive']:
                distance = self.calculate_distance(
                    (self.player['row'], self.player['col']),
                    (enemy['row'], enemy['col'])
                )
                if distance < closest_distance:
                    closest_distance = distance
                    closest_enemy = enemy
        
        if closest_enemy:
            # If adjacent, attack
            if closest_distance == 1:
                self.attack_target(self.player, closest_enemy)
            else:
                # Move closer
                valid_moves = self.get_valid_moves(self.player)
                
                if valid_moves:
                    best_move = None
                    best_distance = float('inf')
                    
                    for move_row, move_col in valid_moves:
                        move_distance = self.calculate_distance(
                            (move_row, move_col),
                            (closest_enemy['row'], closest_enemy['col'])
                        )
                        if move_distance < best_distance:
                            best_distance = move_distance
                            best_move = (move_row, move_col)
                    
                    if best_move:
                        print(f"Player moves to {best_move}")
                        self.move_character(self.player, best_move[0], best_move[1])
    
    def check_battle_end(self):
        """Check if battle has ended."""
        if not self.player['alive']:
            print("💀 GAME OVER - Player defeated!")
            self.battle_over = True
            return True
        
        alive_enemies = sum(1 for enemy in self.enemies if enemy['alive'])
        if alive_enemies == 0:
            print("🎉 VICTORY - All enemies defeated!")
            self.battle_over = True
            return True
        
        return False
    
    def run_battle(self, max_turns=20):
        """Run the battle simulation."""
        print("🗡️ BATTLE BEGINS!")
        self.display_battlefield()
        
        while not self.battle_over and self.turn < max_turns:
            self.turn += 1
            
            # Create turn order based on speed
            all_characters = [self.player] + [e for e in self.enemies if e['alive']]
            turn_order = sorted(all_characters, key=lambda x: x['speed'], reverse=True)
            
            for character in turn_order:
                if not character['alive']:
                    continue
                
                if character == self.player:
                    self.player_turn()
                else:
                    self.ai_turn(character)
                
                if self.check_battle_end():
                    break
            
            if not self.battle_over:
                self.display_battlefield()
                time.sleep(0.5)  # Brief pause for readability
        
        if not self.battle_over:
            print(f"Battle ended after {max_turns} turns (time limit reached)")

# Demonstrate RPG Battle System
print("RPG Battle System Simulation:")
random.seed(123)  # For reproducible combat
battle = RPGBattleSystem()
battle.run_battle()

# CELLULAR AUTOMATA GAME (CONWAY'S GAME OF LIFE)
print("=== CELLULAR AUTOMATA (GAME OF LIFE) ===")
print()

class GameOfLife:
    """Conway's Game of Life implementation."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.generation = 0
        
        # 0 = dead, 1 = alive
        self.DEAD = 0
        self.ALIVE = 1
    
    def set_cell(self, row, col, state):
        """Set cell state."""
        if 0 <= row < self.height and 0 <= col < self.width:
            self.grid[row][col] = state
    
    def get_cell(self, row, col):
        """Get cell state (returns 0 for out-of-bounds)."""
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.grid[row][col]
        return 0
    
    def count_neighbors(self, row, col):
        """Count living neighbors around a cell."""
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:  # Skip the cell itself
                    continue
                count += self.get_cell(row + dr, col + dc)
        return count
    
    def next_generation(self):
        """Calculate next generation based on Game of Life rules."""
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        
        for row in range(self.height):
            for col in range(self.width):
                neighbors = self.count_neighbors(row, col)
                current_state = self.grid[row][col]
                
                # Apply Game of Life rules:
                # 1. Live cell with 2-3 neighbors survives
                # 2. Dead cell with exactly 3 neighbors becomes alive
                # 3. All other cells die or stay dead
                
                if current_state == self.ALIVE:
                    if neighbors == 2 or neighbors == 3:
                        new_grid[row][col] = self.ALIVE
                else:  # current_state == DEAD
                    if neighbors == 3:
                        new_grid[row][col] = self.ALIVE
        
        self.grid = new_grid
        self.generation += 1
    
    def display(self):
        """Display the current grid."""
        print(f"Generation {self.generation}:")
        for row in self.grid:
            line = ""
            for cell in row:
                line += "█" if cell == self.ALIVE else "."
            print(line)
        print()
    
    def count_living_cells(self):
        """Count total living cells."""
        return sum(sum(row) for row in self.grid)
    
    def add_pattern(self, pattern, start_row, start_col):
        """Add a predefined pattern to the grid."""
        for r, pattern_row in enumerate(pattern):
            for c, cell in enumerate(pattern_row):
                self.set_cell(start_row + r, start_col + c, cell)
    
    def randomize(self, probability=0.3):
        """Randomly populate grid."""
        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col] = 1 if random.random() < probability else 0

# Common Game of Life patterns
def get_glider_pattern():
    """Returns the classic glider pattern."""
    return [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]

def get_blinker_pattern():
    """Returns the blinker oscillator pattern."""
    return [
        [1, 1, 1]
    ]

def get_block_pattern():
    """Returns the block still life pattern."""
    return [
        [1, 1],
        [1, 1]
    ]

# Demonstrate Game of Life
print("Conway's Game of Life Simulation:")
life = GameOfLife(20, 15)

# Add some interesting patterns
life.add_pattern(get_glider_pattern(), 2, 2)
life.add_pattern(get_blinker_pattern(), 8, 10)
life.add_pattern(get_block_pattern(), 12, 15)

# Add some random cells
random.seed(456)
for _ in range(15):
    row = random.randint(0, life.height - 1)
    col = random.randint(0, life.width - 1)
    life.set_cell(row, col, 1)

# Run simulation for several generations
print("Initial state:")
life.display()

for generation in range(5):
    life.next_generation()
    print(f"Living cells: {life.count_living_cells()}")
    life.display()

print("=== SUMMARY ===")
print()
print("Game Development with 2D Arrays Summary:")
print("1. 2D arrays provide natural game board representations")
print("2. Grid-based games are excellent starting projects")
print("3. Game state management requires careful array manipulation")
print("4. AI pathfinding algorithms work well with 2D grids")
print("5. Turn-based systems can be implemented with array iterations")
print("6. Cellular automata demonstrate emergent behavior from simple rules")
print("7. Real-time games require efficient array operations")
print("8. Game development teaches practical programming concepts")

"""
KEY TAKEAWAYS:
==============
1. 2D arrays are fundamental for grid-based game development
2. Game state can be efficiently represented using numeric codes
3. Movement and collision detection are array boundary checks
4. AI behavior can be implemented with pathfinding algorithms
5. Turn-based systems require careful state management
6. Cellular automata show how complex patterns emerge from simple rules
7. Visual representation enhances gameplay understanding
8. Game development combines multiple programming concepts

GAME TYPES USING 2D ARRAYS:
============================
• Board games: Chess, checkers, Go, tic-tac-toe
• Puzzle games: Sliding puzzles, match-3, Tetris
• RPGs: Turn-based combat, dungeon exploration
• Strategy games: Real-time strategy, tower defense
• Simulation games: Conway's Game of Life, cellular automata
• Platform games: Tile-based collision, level design

CORE GAME MECHANICS:
====================
• Movement: Position validation, boundary checking
• Collision: Occupancy testing, response handling
• AI: Pathfinding, decision trees, state machines
• Physics: Simple movement, gravity simulation
• Game loop: Update, render, input handling
• State: Score tracking, level progression

PATHFINDING IN GAMES:
=====================
• A*: Optimal pathfinding with heuristics
• BFS: Shortest path in unweighted grids
• DFS: Simple exploration (may not be optimal)
• Dijkstra: Weighted pathfinding
• Flow fields: Pre-computed movement directions
• Jump point search: Optimized A* for grids

OPTIMIZATION TECHNIQUES:
========================
• Spatial partitioning: Divide world into regions
• Dirty rectangles: Only update changed areas
• Object pooling: Reuse objects to avoid allocation
• Level-of-detail: Reduce complexity for distant objects
• Culling: Skip processing for non-visible elements
• Delta compression: Store only changes between states

REAL-WORLD APPLICATIONS:
========================
• Educational games: Teach programming concepts
• Mobile games: Tile-matching, puzzle solving
• Board game implementations: Digital versions of classics
• Simulation software: Conway's Game of Life variations
• Strategy games: Resource management, tactical combat
• Prototyping: Quick game concept validation

ADVANCED CONCEPTS:
==================
• Multi-layered grids: Separate collision, graphics, AI layers
• Hexagonal grids: Six-direction movement systems
• Infinite grids: Procedurally generated worlds
• Networked games: Synchronized game state
• Save systems: Serializing game state to disk
• Animation: Smooth movement between discrete positions

NEXT STEP:
Go to 06-data-analysis.py to explore statistical analysis with 2D arrays!
"""