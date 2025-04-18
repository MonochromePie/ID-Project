# import numpy as np
# import math

# def find_bool_path(matrix, path):
#     """Create a boolean matrix of valid path nodes"""
#     bool_path_matrix = np.zeros([15, 15], dtype=bool)
#     for i in range(15):
#         for j in range(15):
#             bool_path_matrix[i, j] = matrix[i, j] == path
#     return bool_path_matrix

# def matrix_dis(current, destination, matrix):
#     """Calculate Euclidean distance between two points in the matrix"""
#     a = np.where(matrix == destination)
#     diff = np.array(current) - np.array([a[0][0], a[1][0]])
#     return np.sqrt(diff[0]**2 + diff[1]**2)

# def get_neighbors(pos, matrix, path_check):
#     """Get valid neighboring positions"""
#     neighbors = [
#         (pos[0] - 1, pos[1]),  # Up
#         (pos[0] + 1, pos[1]),  # Down
#         (pos[0], pos[1] + 1),  # Right
#         (pos[0], pos[1] - 1)   # Left
#     ]
    
#     # Filter valid neighbors within matrix bounds and allowed path
#     valid_neighbors = []
#     for neighbor in neighbors:
#         x, y = neighbor
#         if (0 <= x < matrix.shape[0] and 
#             0 <= y < matrix.shape[1] and 
#             path_check[x, y]):
#             valid_neighbors.append(neighbor)
    
#     return valid_neighbors

# def reconstruct_path(came_from, current):
#     """Reconstruct the path from start to end"""
#     path = [current]
#     while current in came_from:
#         current = came_from[current]
#         path.append(current)
#     return path[::-1]

# def aStar(matrix, path, start, end, verbose=False):
#     """A* pathfinding algorithm implementation with debugging"""
#     # Create a boolean matrix of valid path nodes
#     path_check = find_bool_path(matrix, path)
    
#     # Find start and end locations as tuples
#     start_locations = list(zip(*np.where(matrix == start)))
#     end_locations = list(zip(*np.where(matrix == end)))
    
#     # Verbose debugging
#     if verbose:
#         print("Start locations:", start_locations)
#         print("End locations:", end_locations)
#         print("Path check matrix:\n", path_check)
    
#     # Return None if no start or end locations found
#     if not start_locations or not end_locations:
#         print("No start or end locations found!")
#         return None
    
#     # Multiple possible start and end points, try all combinations
#     for start_location in start_locations:
#         for end_location in end_locations:
#             # Reset sets and dictionaries for each attempt
#             open_set = {start_location}
#             closed_set = set()
            
#             # Cost dictionaries
#             g_score = {start_location: 0}
#             f_score = {start_location: matrix_dis(start_location, end, matrix)}
            
#             # Track path
#             came_from = {}
            
#             while open_set:
#                 # Get node with lowest f_score
#                 current = min(open_set, key=lambda x: f_score.get(x, float('inf')))
                
#                 # Check if reached end
#                 if current == end_location:
#                     path = reconstruct_path(came_from, current)
#                     if verbose:
#                         print(f"Path found from {start_location} to {end_location}")
#                     return path
                
#                 # Move current from open to closed set
#                 open_set.remove(current)
#                 closed_set.add(current)
                
#                 # Check neighbors
#                 for neighbor in get_neighbors(current, matrix, path_check):
#                     # Skip if already evaluated
#                     if neighbor in closed_set:
#                         continue
                    
#                     # Tentative g_score
#                     tentative_g_score = g_score[current] + 1
                    
#                     # Discover a new node or find a better path
#                     if neighbor not in open_set:
#                         open_set.add(neighbor)
#                     elif tentative_g_score >= g_score.get(neighbor, float('inf')):
#                         continue
                    
#                     # This path is the best until now. Record it!
#                     came_from[neighbor] = current
#                     g_score[neighbor] = tentative_g_score
#                     f_score[neighbor] = g_score[neighbor] + matrix_dis(neighbor, end, matrix)
    
#     # No path found
#     print("No path found between start and end locations!")
#     return None

# # Example usage
# QR_matrix = np.array([
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ])

# # Run with verbose debugging
# path = aStar(QR_matrix, 1, 2, 3, verbose=True)
# if path:
#     print("Path found:", path)

import numpy as np

def debug_grid(grid):
    """Print grid for visual inspection"""
    print("Grid Contents:")
    for row in grid:
        print(' '.join(str(cell) for cell in row))

def find_marker_locations(grid):
    """Find locations of all string markers"""
    # Find unique string markers in the grid
    locations = {}
    for marker in np.unique(grid):
        if isinstance(marker, str):
            # Find all locations of this marker
            coords = np.where(grid == marker)
            locations[marker] = list(zip(coords[0], coords[1]))
    return locations

def are_markers_connected(grid, start_marker, end_marker):
    """Check if markers are connected via paths of only letters"""
    rows, cols = grid.shape
    
    # Find locations of start and end markers
    start_locs = np.where(grid == start_marker)
    end_locs = np.where(grid == end_marker)
    
    # If no locations found, return False
    if len(start_locs[0]) == 0 or len(end_locs[0]) == 0:
        return False
    
    # Take first location for each marker
    start = (start_locs[0][0], start_locs[1][0])
    end = (end_locs[0][0], end_locs[1][0])
    
    # Visited set to track explored cells
    visited = set()
    
    def depth_first_search(x, y):
        # Check bounds and valid moves
        if (x, y) == end:
            return True
        
        # Strict condition: only allow letter traversal
        if (x < 0 or x >= rows or 
            y < 0 or y >= cols or 
            grid[x, y] != start_marker or 
            (x, y) in visited):
            return False
        
        visited.add((x, y))
        
        # Check 4 directions: right, down, left, up
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if depth_first_search(next_x, next_y):
                return True
        
        return False
    
    return depth_first_search(start[0], start[1])

def find_all_marker_connections(grid):
    """Find connections between all markers"""
    # Find all markers
    unique_markers = [marker for marker in np.unique(grid) if isinstance(marker, str)]
    
    # Check connections between all pairs of markers
    connections = {}
    
    for i in range(len(unique_markers)):
        for j in range(i+1, len(unique_markers)):
            start = unique_markers[i]
            end = unique_markers[j]
            
            connected = are_markers_connected(grid, start, end)
            connections[f"{start}-{end}"] = connected
    
    return connections

# Example grid
QR_matrix = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, "a", 1, 1, 1, 1, 1, 1, 1, 1, "b", 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

# Debug and run
debug_grid(QR_matrix)
print("\nMarker Locations:")
print(find_marker_locations(QR_matrix))
print("\nMarker Connections:")
connections = find_all_marker_connections(QR_matrix)
for connection, is_connected in connections.items():
    print(f"{connection}: {'Connected' if is_connected else 'Not Connected'}")