def layered_matrix(m, n):
    # Create empty 2D matrix filled with 0s
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    
    # Calculate number of layers (min of half of width or height)
    layers = (min(m, n) + 1) // 2
    
    for layer in range(layers):
        # Determine the value to fill this layer
        value = layer + 1
        
        # Loop through the rectangle boundaries for this layer
        for i in range(layer, n - layer):
            for j in range(layer, m - layer):
                matrix[i][j] = value
                
    return matrix
from pprint import pprint

#output
# pprint(layered_matrix(5, 8))
# [[1, 1, 1, 1, 1],
#  [1, 2, 2, 2, 1],
#  [1, 2, 3, 2, 1],
#  [1, 2, 3, 2, 1],
#  [1, 2, 3, 2, 1],
#  [1, 2, 3, 2, 1],
#  [1, 2, 2, 2, 1],
#  [1, 1, 1, 1, 1]]


# This function generates a 2D matrix of size n rows × m columns, 
# where each element's value corresponds to how deep it is in a "layered" 
# structure starting from the outer edges.
# Each "layer" is like a frame or border around the matrix:
# Layer 1: outermost
# Layer 2: one step inside
# Layer 3: further in
# … and so on.

#Step 1: Create an empty matrix
#Creates a 2D list of size n × m, filled with zeros.
#Step 2: Determine number of layers
#The number of layers is half of the smaller of m or n (rounded up), 
# because we can't have more layers than the center allows.

# Step 3: Loop through each layer and fill it
#For each layer:
#It fills a rectangle starting at (layer, layer) and ending at (n - layer - 1,
#  m - layer - 1)
#This fills the entire area of that layer with value = layer + 1

#Example: layered_matrix(5, 8)
# Input: m = 5 columns, n = 8 rows
# Let’s draw how this happens step-by-step:
# Layer 0 (value = 1):
# Fills whole matrix:

#Layer 2 (value = 3):
#Fills from (2,2) to (5,2):