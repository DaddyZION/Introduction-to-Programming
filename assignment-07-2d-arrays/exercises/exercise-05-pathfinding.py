"""
Assignment 7 - Exercise 5: Basic Pathfinding (Grid Navigation)
Difficulty: 🟠 Advanced

TODO: Implement basic pathfinding and grid traversal algorithms.

Requirements:
1. Navigate through a grid maze
2. Find paths from start to end
3. Avoid obstacles
4. Track visited cells
"""

# Grid values:
# 0 = walkable path
# 1 = wall/obstacle
# 2 = start position
# 3 = end/goal position
# 4 = visited cell


# ==================== FUNCTION 1: Create Simple Maze ====================
def create_maze(rows, cols, walls=None):
    """
    Create a maze grid.
    
    Parameters:
    - rows, cols: dimensions
    - walls: list of (row, col) tuples for wall positions
    
    Returns: 2D grid (0 for path, 1 for wall)
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Display Maze ====================
def display_maze(maze, path=None):
    """
    Display maze with symbols.
    
    Symbols:
    0 (path): ' . '
    1 (wall): '###'
    2 (start): ' S '
    3 (goal): ' G '
    4 (visited): ' * '
    
    If path provided, mark path cells with 'o'
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Is Valid Move ====================
def is_valid_move(maze, row, col):
    """
    Check if a move to (row, col) is valid.
    
    Valid if:
    - Within grid bounds
    - Not a wall (value != 1)
    
    Returns: boolean
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Get Neighbors ====================
def get_neighbors(row, col, maze):
    """
    Get all valid neighboring cells (up, down, left, right).
    
    Returns: list of (row, col) tuples
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 5: Find Path (BFS) ====================
def find_path_bfs(maze, start, goal):
    """
    Find shortest path using Breadth-First Search.
    
    Parameters:
    - maze: 2D grid
    - start: (row, col) tuple
    - goal: (row, col) tuple
    
    Returns: list of (row, col) tuples representing path
             Returns [] if no path exists
    
    Algorithm:
    1. Use a queue for BFS
    2. Keep track of visited cells
    3. Store parent of each cell to reconstruct path
    4. Return path from start to goal
    """
    # TODO: Implement this function
    # Hint: Use a list as queue, append() to add, pop(0) to remove
    pass


# ==================== FUNCTION 6: Mark Path on Maze ====================
def mark_path_on_maze(maze, path):
    """
    Create a copy of maze with path marked.
    
    Mark path cells with value 4 (visited marker).
    
    Returns: new maze with path marked
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 7: Count Reachable Cells ====================
def count_reachable_cells(maze, start):
    """
    Count how many cells are reachable from start position.
    
    Use flood fill algorithm (similar to BFS).
    
    Returns: integer count
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 8: Find All Paths ====================
def find_all_paths(maze, start, goal, max_length=100):
    """
    Find all possible paths from start to goal.
    
    Uses recursive depth-first search.
    
    Parameters:
    - max_length: maximum path length to prevent infinite loops
    
    Returns: list of paths (each path is a list of tuples)
    """
    # TODO: Implement this function (CHALLENGE!)
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing Pathfinding ===\n")
    
    # Create simple maze
    walls = [
        (1, 1), (1, 2), (1, 3),
        (3, 1), (3, 2), (3, 3),
        (2, 5), (3, 5), (4, 5)
    ]
    
    print("Test 1: Create Maze")
    # maze = create_maze(6, 8, walls)
    # maze[0][0] = 2  # Start
    # maze[5][7] = 3  # Goal
    # display_maze(maze)
    
    print("\nTest 2: Is Valid Move")
    # print(f"  (0, 0): {is_valid_move(maze, 0, 0)}")
    # print(f"  (1, 1): {is_valid_move(maze, 1, 1)}")
    # print(f"  (10, 10): {is_valid_move(maze, 10, 10)}")
    
    print("\nTest 3: Get Neighbors")
    # neighbors = get_neighbors(2, 2, maze)
    # print(f"  Neighbors of (2, 2): {neighbors}")
    
    print("\nTest 4: Find Path (BFS)")
    # start = (0, 0)
    # goal = (5, 7)
    # path = find_path_bfs(maze, start, goal)
    # print(f"  Path found: {len(path)} steps")
    # if path:
    #     print(f"  Path: {path}")
    #     marked_maze = mark_path_on_maze(maze, path)
    #     display_maze(marked_maze, path)
    
    print("\nTest 5: Count Reachable Cells")
    # count = count_reachable_cells(maze, (0, 0))
    # print(f"  Reachable cells from start: {count}")
    
    print("\nTest 6: Find All Paths (if implemented)")
    # all_paths = find_all_paths(maze, start, goal)
    # print(f"  Total paths found: {len(all_paths)}")
