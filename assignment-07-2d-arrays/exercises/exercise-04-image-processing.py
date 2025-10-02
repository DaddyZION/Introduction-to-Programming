"""
Assignment 7 - Exercise 4: Simple Image Processing
Difficulty: 🟡 Intermediate

TODO: Implement basic image processing operations on 2D grids.

Requirements:
1. Represent images as 2D arrays of pixel values (0-255)
2. Apply filters and transformations
3. Perform basic image manipulations
"""

# ==================== FUNCTION 1: Create Grayscale Image ====================
def create_grayscale_image(rows, cols, pattern='gradient'):
    """
    Create a grayscale image (2D array of 0-255 values).
    
    Patterns:
    - 'solid': all one value (128)
    - 'gradient': horizontal gradient from 0 to 255
    - 'random': random values
    - 'checkerboard': alternating 0 and 255
    
    Returns: 2D list of integers
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Display Image ====================
def display_image(image, use_ascii=True):
    """
    Display image using ASCII characters.
    
    If use_ascii:
    - Map pixel values to ASCII characters
    - 0-63: ' '
    - 64-127: '.'
    - 128-191: '+'
    - 192-255: '#'
    
    Otherwise, display numeric values
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Invert Image ====================
def invert_image(image):
    """
    Invert image colors (255 - pixel_value for each pixel).
    
    Example: 0 → 255, 128 → 127, 255 → 0
    
    Returns: new inverted image
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Flip Image ====================
def flip_image(image, direction='horizontal'):
    """
    Flip image horizontally or vertically.
    
    Parameters:
    - image: 2D array
    - direction: 'horizontal' or 'vertical'
    
    Returns: flipped image
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 5: Rotate Image ====================
def rotate_image_90(image, clockwise=True):
    """
    Rotate image 90 degrees.
    
    Parameters:
    - image: 2D array
    - clockwise: True for clockwise, False for counter-clockwise
    
    Returns: rotated image
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 6: Brighten/Darken ====================
def adjust_brightness(image, amount):
    """
    Adjust brightness of image.
    
    Parameters:
    - image: 2D array
    - amount: positive to brighten, negative to darken
    
    Ensure values stay in 0-255 range (clamp values).
    
    Returns: adjusted image
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 7: Apply Threshold ====================
def apply_threshold(image, threshold=128):
    """
    Convert to binary image (black and white only).
    
    Pixels >= threshold become 255 (white)
    Pixels < threshold become 0 (black)
    
    Returns: thresholded image
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 8: Blur Filter ====================
def apply_blur(image):
    """
    Apply simple blur filter (average of neighboring pixels).
    
    For each pixel, average it with its 8 neighbors (or fewer at edges).
    
    Returns: blurred image
    """
    # TODO: Implement this function (CHALLENGE!)
    pass


# ==================== FUNCTION 9: Edge Detection ====================
def detect_edges(image):
    """
    Simple edge detection filter.
    
    Calculate difference between each pixel and its neighbors.
    Large differences indicate edges.
    
    Returns: edge-detected image
    """
    # TODO: Implement this function (CHALLENGE!)
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing Image Processing ===\n")
    
    # Create test image
    print("Test 1: Create Images")
    # gradient = create_grayscale_image(10, 20, 'gradient')
    # checker = create_grayscale_image(10, 10, 'checkerboard')
    # print("Gradient image:")
    # display_image(gradient)
    # print("\nCheckerboard image:")
    # display_image(checker)
    
    print("\nTest 2: Invert")
    # inverted = invert_image(gradient)
    # display_image(inverted)
    
    print("\nTest 3: Flip")
    # flipped_h = flip_image(checker, 'horizontal')
    # flipped_v = flip_image(checker, 'vertical')
    # print("Horizontal flip:")
    # display_image(flipped_h)
    # print("\nVertical flip:")
    # display_image(flipped_v)
    
    print("\nTest 4: Rotate")
    # rotated = rotate_image_90(checker)
    # display_image(rotated)
    
    print("\nTest 5: Brightness")
    # brighter = adjust_brightness(gradient, 50)
    # darker = adjust_brightness(gradient, -50)
    # print("Brighter:")
    # display_image(brighter)
    # print("\nDarker:")
    # display_image(darker)
    
    print("\nTest 6: Threshold")
    # binary = apply_threshold(gradient, 128)
    # display_image(binary)
    
    print("\nTest 7: Blur (if implemented)")
    # blurred = apply_blur(checker)
    # display_image(blurred)
