"""
Assignment 7 - Example 3: Grid Traversal and Pathfinding
========================================================

This program demonstrates advanced grid traversal techniques and pathfinding
algorithms essential for game development, robotics, and spatial analysis.
These techniques enable navigation through 2D spaces, finding optimal paths,
and solving complex spatial problems in various applications.

Key Concepts Demonstrated:
- Grid representation and navigation fundamentals
- Breadth-First Search (BFS) and Depth-First Search (DFS)
- A* pathfinding algorithm implementation
- Maze generation and solving algorithms
- Flood fill and connected component analysis
- Advanced traversal patterns and optimizations
"""

from collections import deque
import heapq
import random
import time

print("=== GRID TRAVERSAL AND PATHFINDING ===")
print()

print("Grid-based algorithms are fundamental to many applications:")
print("• Game development: Character movement, AI pathfinding")
print("• Robotics: Navigation planning, obstacle avoidance")
print("• Image processing: Connected component analysis, flood fill")
print("• Geographic systems: Route planning, area analysis")
print("• Network analysis: Graph traversal, connectivity")
print("• Puzzle solving: Maze solving, sliding puzzles")
print()

# GRID REPRESENTATION AND BASIC NAVIGATION
print("=== GRID REPRESENTATION AND BASIC NAVIGATION ===")
print()

class Grid:
    """Represents a 2D grid with various cell types and navigation capabilities."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        
        # Define cell types
        self.EMPTY = 0
        self.WALL = 1
        self.START = 2
        self.END = 3
        self.VISITED = 4
        self.PATH = 5
        
        # Define movement directions (4-directional)
        self.directions_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        self.direction_names_4 = ['Right', 'Down', 'Left', 'Up']
        
        # Define movement directions (8-directional)
        self.directions_8 = [
            (0, 1), (1, 0), (0, -1), (-1, 0),      # Cardinal
            (1, 1), (1, -1), (-1, 1), (-1, -1)     # Diagonal
        ]
        self.direction_names_8 = [
            'Right', 'Down', 'Left', 'Up',
            'Down-Right', 'Down-Left', 'Up-Right', 'Up-Left'
        ]
    
    def is_valid_position(self, row, col):
        """Check if position is within grid bounds."""
        return 0 <= row < self.height and 0 <= col < self.width
    
    def is_walkable(self, row, col):
        """Check if position is walkable (not a wall)."""
        if not self.is_valid_position(row, col):
            return False
        return self.grid[row][col] != self.WALL
    
    def get_neighbors(self, row, col, use_diagonal=False):
        """Get all valid neighboring positions."""
        neighbors = []
        directions = self.directions_8 if use_diagonal else self.directions_4
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_position(new_row, new_col):
                neighbors.append((new_row, new_col))
        
        return neighbors
    
    def get_walkable_neighbors(self, row, col, use_diagonal=False):
        """Get all valid walkable neighboring positions."""
        neighbors = self.get_neighbors(row, col, use_diagonal)
        return [(r, c) for r, c in neighbors if self.is_walkable(r, c)]
    
    def set_cell(self, row, col, cell_type):
        """Set cell type at specified position."""
        if self.is_valid_position(row, col):
            self.grid[row][col] = cell_type
    
    def get_cell(self, row, col):
        """Get cell type at specified position."""
        if self.is_valid_position(row, col):
            return self.grid[row][col]
        return None
    
    def clear_path_markers(self):
        """Clear visited and path markers from grid."""
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] in [self.VISITED, self.PATH]:
                    self.grid[row][col] = self.EMPTY
    
    def display(self, symbols=None):
        """Display the grid using specified symbols."""
        if symbols is None:
            symbols = {
                self.EMPTY: '.',
                self.WALL: '█',
                self.START: 'S',
                self.END: 'E',
                self.VISITED: '°',
                self.PATH: '*'
            }
        
        print("  ", end="")
        for col in range(self.width):
            print(f"{col % 10}", end="")
        print()
        
        for row in range(self.height):
            print(f"{row % 10} ", end="")
            for col in range(self.width):
                cell_type = self.grid[row][col]
                symbol = symbols.get(cell_type, '?')
                print(symbol, end="")
            print()

def create_sample_maze():
    """Create a sample maze for demonstration."""
    grid = Grid(15, 10)
    
    # Add walls to create a maze pattern
    walls = [
        # Outer walls
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14),
        (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14),
        # Left and right walls
        (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
        (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (6, 14), (7, 14), (8, 14),
        # Internal obstacles
        (2, 3), (2, 4), (2, 5),
        (4, 2), (4, 6), (4, 7), (4, 8),
        (6, 4), (6, 5), (6, 10), (6, 11), (6, 12),
        (7, 2), (7, 9),
        (3, 10), (3, 11), (3, 12),
        (5, 13)
    ]
    
    for row, col in walls:
        grid.set_cell(row, col, grid.WALL)
    
    # Set start and end positions
    grid.set_cell(1, 1, grid.START)
    grid.set_cell(8, 13, grid.END)
    
    return grid

# Demonstrate grid creation and display
print("Grid Creation and Display:")
sample_grid = create_sample_maze()
print("Sample maze:")
sample_grid.display()
print()

# BREADTH-FIRST SEARCH (BFS)
print("=== BREADTH-FIRST SEARCH (BFS) ===")
print()

def breadth_first_search(grid, start_pos, end_pos, use_diagonal=False):
    """
    Implement BFS pathfinding algorithm.
    Returns path if found, None otherwise.
    BFS guarantees shortest path in unweighted grids.
    Time Complexity: O(V + E) where V is cells, E is edges
    Space Complexity: O(V) for queue and visited set
    """
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    
    # Validate start and end positions
    if not grid.is_walkable(start_row, start_col) or not grid.is_walkable(end_row, end_col):
        return None
    
    # Initialize BFS
    queue = deque([(start_row, start_col, 0)])  # (row, col, distance)
    visited = set()
    parent = {}  # For path reconstruction
    visited.add((start_row, start_col))
    
    while queue:
        current_row, current_col, distance = queue.popleft()
        
        # Check if we reached the end
        if current_row == end_row and current_col == end_col:
            # Reconstruct path
            path = []
            current = (end_row, end_col)
            
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append((start_row, start_col))
            path.reverse()
            
            return path, distance
        
        # Mark as visited (for visualization)
        if (current_row, current_col) != (start_row, start_col):
            grid.set_cell(current_row, current_col, grid.VISITED)
        
        # Explore neighbors
        neighbors = grid.get_walkable_neighbors(current_row, current_col, use_diagonal)
        
        for neighbor_row, neighbor_col in neighbors:
            if (neighbor_row, neighbor_col) not in visited:
                visited.add((neighbor_row, neighbor_col))
                parent[(neighbor_row, neighbor_col)] = (current_row, current_col)
                queue.append((neighbor_row, neighbor_col, distance + 1))
    
    return None  # No path found

def bfs_flood_fill(grid, start_pos, target_value, new_value):
    """
    Use BFS to perform flood fill operation.
    Changes all connected cells of target_value to new_value.
    """
    start_row, start_col = start_pos
    
    if not grid.is_valid_position(start_row, start_col):
        return 0
    
    if grid.get_cell(start_row, start_col) != target_value:
        return 0
    
    queue = deque([(start_row, start_col)])
    visited = set()
    visited.add((start_row, start_col))
    filled_count = 0
    
    while queue:
        current_row, current_col = queue.popleft()
        
        # Fill current cell
        grid.set_cell(current_row, current_col, new_value)
        filled_count += 1
        
        # Check neighbors
        neighbors = grid.get_neighbors(current_row, current_col)
        
        for neighbor_row, neighbor_col in neighbors:
            if ((neighbor_row, neighbor_col) not in visited and 
                grid.is_valid_position(neighbor_row, neighbor_col) and
                grid.get_cell(neighbor_row, neighbor_col) == target_value):
                
                visited.add((neighbor_row, neighbor_col))
                queue.append((neighbor_row, neighbor_col))
    
    return filled_count

# Demonstrate BFS pathfinding
print("BFS Pathfinding Example:")
bfs_grid = create_sample_maze()
start = (1, 1)
end = (8, 13)

print("Finding path using BFS...")
result = breadth_first_search(bfs_grid, start, end)

if result:
    path, distance = result
    print(f"Path found! Distance: {distance} steps")
    
    # Mark path on grid
    for row, col in path:
        if bfs_grid.get_cell(row, col) not in [bfs_grid.START, bfs_grid.END]:
            bfs_grid.set_cell(row, col, bfs_grid.PATH)
    
    print("Grid with BFS solution:")
    bfs_grid.display()
    print(f"Path coordinates: {path}")
else:
    print("No path found!")
print()

# DEPTH-FIRST SEARCH (DFS)
print("=== DEPTH-FIRST SEARCH (DFS) ===")
print()

def depth_first_search(grid, start_pos, end_pos, use_diagonal=False):
    """
    Implement DFS pathfinding algorithm.
    Returns path if found, None otherwise.
    DFS does not guarantee shortest path but uses less memory.
    Time Complexity: O(V + E)
    Space Complexity: O(V) for recursion stack in worst case
    """
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    
    if not grid.is_walkable(start_row, start_col) or not grid.is_walkable(end_row, end_col):
        return None
    
    visited = set()
    path = []
    
    def dfs_recursive(row, col):
        # Mark as visited
        visited.add((row, col))
        path.append((row, col))
        
        # Mark on grid for visualization
        if (row, col) != (start_row, start_col) and (row, col) != (end_row, end_col):
            grid.set_cell(row, col, grid.VISITED)
        
        # Check if we reached the end
        if row == end_row and col == end_col:
            return True
        
        # Explore neighbors
        neighbors = grid.get_walkable_neighbors(row, col, use_diagonal)
        
        for neighbor_row, neighbor_col in neighbors:
            if (neighbor_row, neighbor_col) not in visited:
                if dfs_recursive(neighbor_row, neighbor_col):
                    return True
        
        # Backtrack
        path.pop()
        return False
    
    if dfs_recursive(start_row, start_col):
        return path
    else:
        return None

def dfs_connected_components(grid):
    """
    Find all connected components in the grid using DFS.
    Returns list of components, each containing cell coordinates.
    """
    visited = set()
    components = []
    
    def dfs_component(row, col, component):
        if ((row, col) in visited or 
            not grid.is_valid_position(row, col) or 
            not grid.is_walkable(row, col)):
            return
        
        visited.add((row, col))
        component.append((row, col))
        
        # Visit all neighbors
        neighbors = grid.get_neighbors(row, col)
        for neighbor_row, neighbor_col in neighbors:
            dfs_component(neighbor_row, neighbor_col, component)
    
    # Search entire grid for components
    for row in range(grid.height):
        for col in range(grid.width):
            if ((row, col) not in visited and 
                grid.is_walkable(row, col)):
                component = []
                dfs_component(row, col, component)
                if component:
                    components.append(component)
    
    return components

# Demonstrate DFS pathfinding
print("DFS Pathfinding Example:")
dfs_grid = create_sample_maze()

print("Finding path using DFS...")
dfs_path = depth_first_search(dfs_grid, start, end)

if dfs_path:
    print(f"Path found! Length: {len(dfs_path)} steps")
    
    # Mark path on grid
    for row, col in dfs_path:
        if dfs_grid.get_cell(row, col) not in [dfs_grid.START, dfs_grid.END]:
            dfs_grid.set_cell(row, col, dfs_grid.PATH)
    
    print("Grid with DFS solution:")
    dfs_grid.display()
else:
    print("No path found!")
print()

# A* PATHFINDING ALGORITHM
print("=== A* PATHFINDING ALGORITHM ===")
print()

def manhattan_distance(pos1, pos2):
    """Calculate Manhattan distance between two positions."""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def euclidean_distance(pos1, pos2):
    """Calculate Euclidean distance between two positions."""
    return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5

def a_star_search(grid, start_pos, end_pos, use_diagonal=False, heuristic='manhattan'):
    """
    Implement A* pathfinding algorithm.
    A* uses a heuristic to guide search toward the goal.
    Guarantees shortest path if heuristic is admissible.
    Time Complexity: O(b^d) where b is branching factor, d is depth
    Space Complexity: O(b^d) for storing nodes
    """
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    
    if not grid.is_walkable(start_row, start_col) or not grid.is_walkable(end_row, end_col):
        return None
    
    # Choose heuristic function
    if heuristic == 'euclidean':
        heuristic_func = euclidean_distance
    else:
        heuristic_func = manhattan_distance
    
    # Priority queue: (f_score, g_score, position)
    open_set = [(0, 0, start_pos)]
    heapq.heapify(open_set)
    
    # Track costs and paths
    g_score = {start_pos: 0}  # Cost from start to node
    f_score = {start_pos: heuristic_func(start_pos, end_pos)}  # g_score + heuristic
    parent = {}
    visited = set()
    
    while open_set:
        current_f, current_g, current_pos = heapq.heappop(open_set)
        current_row, current_col = current_pos
        
        # Skip if already processed
        if current_pos in visited:
            continue
        
        visited.add(current_pos)
        
        # Mark as visited (for visualization)
        if current_pos != start_pos and current_pos != end_pos:
            grid.set_cell(current_row, current_col, grid.VISITED)
        
        # Check if we reached the goal
        if current_pos == end_pos:
            # Reconstruct path
            path = []
            current = end_pos
            
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start_pos)
            path.reverse()
            
            return path, g_score[end_pos]
        
        # Explore neighbors
        neighbors = grid.get_walkable_neighbors(current_row, current_col, use_diagonal)
        
        for neighbor_row, neighbor_col in neighbors:
            neighbor_pos = (neighbor_row, neighbor_col)
            
            if neighbor_pos in visited:
                continue
            
            # Calculate movement cost
            if use_diagonal and abs(neighbor_row - current_row) + abs(neighbor_col - current_col) == 2:
                move_cost = 1.414  # Diagonal movement cost (√2)
            else:
                move_cost = 1  # Cardinal movement cost
            
            tentative_g = g_score[current_pos] + move_cost
            
            if neighbor_pos not in g_score or tentative_g < g_score[neighbor_pos]:
                # Better path found
                parent[neighbor_pos] = current_pos
                g_score[neighbor_pos] = tentative_g
                f_score[neighbor_pos] = tentative_g + heuristic_func(neighbor_pos, end_pos)
                
                heapq.heappush(open_set, (f_score[neighbor_pos], tentative_g, neighbor_pos))
    
    return None  # No path found

# Demonstrate A* pathfinding
print("A* Pathfinding Example:")
astar_grid = create_sample_maze()

print("Finding path using A* with Manhattan heuristic...")
astar_result = a_star_search(astar_grid, start, end)

if astar_result:
    astar_path, astar_cost = astar_result
    print(f"Path found! Cost: {astar_cost:.2f}")
    
    # Mark path on grid
    for row, col in astar_path:
        if astar_grid.get_cell(row, col) not in [astar_grid.START, astar_grid.END]:
            astar_grid.set_cell(row, col, astar_grid.PATH)
    
    print("Grid with A* solution:")
    astar_grid.display()
else:
    print("No path found!")
print()

# ADVANCED TRAVERSAL PATTERNS
print("=== ADVANCED TRAVERSAL PATTERNS ===")
print()

def spiral_traversal(grid):
    """Traverse grid in spiral pattern (clockwise from outside in)."""
    if not grid.grid:
        return []
    
    result = []
    top, bottom = 0, grid.height - 1
    left, right = 0, grid.width - 1
    
    while top <= bottom and left <= right:
        # Go right along top row
        for col in range(left, right + 1):
            result.append((top, col))
        top += 1
        
        # Go down along right column
        for row in range(top, bottom + 1):
            result.append((row, right))
        right -= 1
        
        # Go left along bottom row (if we still have rows)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append((bottom, col))
            bottom -= 1
        
        # Go up along left column (if we still have columns)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append((row, left))
            left += 1
    
    return result

def zigzag_traversal(grid):
    """Traverse grid in zigzag pattern (alternating left-right)."""
    result = []
    
    for row in range(grid.height):
        if row % 2 == 0:  # Even rows: left to right
            for col in range(grid.width):
                result.append((row, col))
        else:  # Odd rows: right to left
            for col in range(grid.width - 1, -1, -1):
                result.append((row, col))
    
    return result

def diagonal_traversal(grid):
    """Traverse grid along diagonals."""
    result = []
    
    # Traverse diagonals from top-left to bottom-right
    for diagonal in range(grid.height + grid.width - 1):
        if diagonal < grid.width:
            # Start from top row
            start_row, start_col = 0, diagonal
        else:
            # Start from left column
            start_row, start_col = diagonal - grid.width + 1, grid.width - 1
        
        # Traverse the diagonal
        row, col = start_row, start_col
        while row < grid.height and col >= 0:
            result.append((row, col))
            row += 1
            col -= 1
    
    return result

# Demonstrate advanced traversal patterns
print("Advanced Traversal Patterns:")
demo_grid = Grid(6, 4)

# Fill grid with numbers for visualization
counter = 0
for row in range(demo_grid.height):
    for col in range(demo_grid.width):
        demo_grid.set_cell(row, col, counter)
        counter += 1

print("Original grid (filled with sequential numbers):")
symbols = {i: str(i % 10) for i in range(24)}
demo_grid.display(symbols)
print()

# Show different traversal patterns
patterns = [
    ("Spiral", spiral_traversal),
    ("Zigzag", zigzag_traversal),
    ("Diagonal", diagonal_traversal)
]

for pattern_name, pattern_func in patterns:
    traversal_order = pattern_func(demo_grid)
    print(f"{pattern_name} traversal order:")
    values = [demo_grid.get_cell(row, col) for row, col in traversal_order]
    print(f"  Positions: {traversal_order[:12]}..." if len(traversal_order) > 12 else f"  Positions: {traversal_order}")
    print(f"  Values: {values}")
    print()

# MAZE GENERATION ALGORITHM
print("=== MAZE GENERATION ALGORITHM ===")
print()

def generate_maze_recursive_backtracking(width, height):
    """
    Generate a maze using recursive backtracking algorithm.
    Creates a perfect maze (no loops, exactly one path between any two points).
    """
    # Initialize maze with all walls
    maze = Grid(width, height)
    for row in range(height):
        for col in range(width):
            maze.set_cell(row, col, maze.WALL)
    
    # Stack for backtracking
    stack = []
    
    # Start from top-left corner (make it odd to ensure proper maze structure)
    start_row, start_col = 1, 1
    maze.set_cell(start_row, start_col, maze.EMPTY)
    stack.append((start_row, start_col))
    
    # Directions for maze generation (skip by 2 to maintain wall structure)
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    
    while stack:
        current_row, current_col = stack[-1]
        
        # Get unvisited neighbors
        unvisited_neighbors = []
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            
            if (maze.is_valid_position(new_row, new_col) and 
                maze.get_cell(new_row, new_col) == maze.WALL):
                unvisited_neighbors.append((new_row, new_col))
        
        if unvisited_neighbors:
            # Choose random unvisited neighbor
            next_row, next_col = random.choice(unvisited_neighbors)
            
            # Remove wall between current cell and chosen neighbor
            wall_row = (current_row + next_row) // 2
            wall_col = (current_col + next_col) // 2
            
            maze.set_cell(next_row, next_col, maze.EMPTY)
            maze.set_cell(wall_row, wall_col, maze.EMPTY)
            
            stack.append((next_row, next_col))
        else:
            # Backtrack
            stack.pop()
    
    return maze

# Demonstrate maze generation
print("Maze Generation Example:")
random.seed(42)  # For reproducible results
generated_maze = generate_maze_recursive_backtracking(21, 15)

print("Generated maze:")
generated_maze.display()
print()

# PERFORMANCE COMPARISON
print("=== PERFORMANCE COMPARISON ===")
print()

def compare_pathfinding_algorithms():
    """Compare performance of different pathfinding algorithms."""
    print("Pathfinding Algorithm Performance Comparison:")
    print(f"{'Algorithm':<12} {'Time (ms)':<12} {'Path Length':<12} {'Nodes Visited':<15}")
    print("-" * 60)
    
    # Create test grid
    test_grid_size = 20
    test_grid = Grid(test_grid_size, test_grid_size)
    
    # Add some obstacles
    for _ in range(test_grid_size * 2):
        row = random.randint(1, test_grid_size - 2)
        col = random.randint(1, test_grid_size - 2)
        test_grid.set_cell(row, col, test_grid.WALL)
    
    start_pos = (1, 1)
    end_pos = (test_grid_size - 2, test_grid_size - 2)
    
    algorithms = [
        ("BFS", lambda g: breadth_first_search(g, start_pos, end_pos)),
        ("DFS", lambda g: depth_first_search(g, start_pos, end_pos)),
        ("A* Manhattan", lambda g: a_star_search(g, start_pos, end_pos, False, 'manhattan')),
        ("A* Euclidean", lambda g: a_star_search(g, start_pos, end_pos, False, 'euclidean'))
    ]
    
    for name, algorithm in algorithms:
        # Create fresh copy of grid for each algorithm
        grid_copy = Grid(test_grid_size, test_grid_size)
        for row in range(test_grid_size):
            for col in range(test_grid_size):
                grid_copy.set_cell(row, col, test_grid.get_cell(row, col))
        
        # Time the algorithm
        start_time = time.time()
        result = algorithm(grid_copy)
        end_time = time.time()
        
        # Calculate metrics
        time_ms = (end_time - start_time) * 1000
        
        if result:
            if isinstance(result, tuple):
                path, _ = result
                path_length = len(path)
            else:
                path = result
                path_length = len(path)
            
            # Count visited nodes
            visited_count = 0
            for row in range(test_grid_size):
                for col in range(test_grid_size):
                    if grid_copy.get_cell(row, col) == grid_copy.VISITED:
                        visited_count += 1
            
            print(f"{name:<12} {time_ms:<12.3f} {path_length:<12} {visited_count:<15}")
        else:
            print(f"{name:<12} {time_ms:<12.3f} {'No Path':<12} {'N/A':<15}")

# Run performance comparison
compare_pathfinding_algorithms()
print()

print("=== SUMMARY ===")
print()
print("Grid Traversal and Pathfinding Summary:")
print("1. BFS guarantees shortest path in unweighted grids")
print("2. DFS uses less memory but may not find optimal paths")
print("3. A* provides optimal paths with better performance than BFS")
print("4. Different heuristics affect A* performance and behavior")
print("5. Grid representation choices impact algorithm efficiency")
print("6. Advanced traversal patterns enable specialized applications")
print("7. Maze generation creates interesting test environments")
print("8. Algorithm choice depends on specific requirements and constraints")

"""
KEY TAKEAWAYS:
==============
1. Grid-based algorithms are fundamental for spatial problem solving
2. Different search algorithms have trade-offs in optimality and performance
3. Heuristics can significantly improve search efficiency
4. Proper grid representation and validation are crucial
5. Visualization helps understand algorithm behavior
6. Performance characteristics vary based on problem structure
7. Real-world applications require careful algorithm selection

ALGORITHM CHARACTERISTICS:
==========================
• BFS: Guarantees shortest path, explores level by level
• DFS: Memory efficient, may find longer paths
• A*: Optimal with admissible heuristic, guided search
• Dijkstra: Handles weighted graphs (not shown here)

HEURISTIC FUNCTIONS:
====================
• Manhattan Distance: Sum of absolute differences (grid movement)
• Euclidean Distance: Straight-line distance (diagonal movement)
• Chebyshev Distance: Maximum of coordinate differences (8-directional)

OPTIMIZATION TECHNIQUES:
========================
• Jump Point Search: Skip redundant nodes
• Hierarchical Pathfinding: Multi-level path planning
• Flow Fields: Pre-compute movement directions
• Theta*: Any-angle pathfinding

APPLICATIONS:
=============
• Game AI: Character movement, strategy planning
• Robotics: Navigation, path planning
• Network Routing: Internet packet routing
• Image Processing: Connected component analysis
• GIS: Route optimization, area analysis

PERFORMANCE CONSIDERATIONS:
===========================
• Memory usage varies significantly between algorithms
• Heuristic choice affects A* performance
• Grid size and obstacle density impact all algorithms
• Preprocessing can improve repeated queries
• Parallel processing possible for some algorithms

NEXT STEP:
Go to 04-image-processing.py to learn about pixel manipulation and image filters!
"""