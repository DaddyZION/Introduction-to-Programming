"""
Assignment 7 - Example 4: Image Processing with 2D Arrays
=========================================================

This program demonstrates how 2D arrays are used in image processing and
computer vision applications. Images are represented as 2D arrays of pixels,
making them perfect examples of practical 2D array manipulation.

Key Concepts Demonstrated:
- Image representation as 2D arrays
- Pixel manipulation and color models
- Image filtering and convolution operations
- Edge detection and feature extraction
- Morphological operations
- Image transformations and geometric operations
"""

import numpy as np
import random
import math

print("=== IMAGE PROCESSING WITH 2D ARRAYS ===")
print()

print("Images are natural applications of 2D arrays:")
print("• Each pixel is represented by intensity values")
print("• Grayscale images: Single value per pixel (0-255)")
print("• Color images: Multiple values (RGB, HSV, etc.)")
print("• Image processing operations are array manipulations")
print("• Filters and transformations use neighborhood operations")
print("• Computer vision algorithms analyze pixel patterns")
print()

# IMAGE REPRESENTATION AND BASIC OPERATIONS
print("=== IMAGE REPRESENTATION AND BASIC OPERATIONS ===")
print()

class SimpleImage:
    """Simple image class for demonstrating 2D array operations."""
    
    def __init__(self, width, height, channels=1):
        """Initialize image with specified dimensions and channels."""
        self.width = width
        self.height = height
        self.channels = channels
        
        if channels == 1:  # Grayscale
            self.data = [[0 for _ in range(width)] for _ in range(height)]
        else:  # Color (RGB)
            self.data = [[[0 for _ in range(channels)] for _ in range(width)] for _ in range(height)]
    
    def get_pixel(self, row, col, channel=0):
        """Get pixel value at specified position."""
        if not (0 <= row < self.height and 0 <= col < self.width):
            return 0  # Return black for out-of-bounds
        
        if self.channels == 1:
            return self.data[row][col]
        else:
            return self.data[row][col][channel]
    
    def set_pixel(self, row, col, value, channel=0):
        """Set pixel value at specified position."""
        if not (0 <= row < self.height and 0 <= col < self.width):
            return
        
        if self.channels == 1:
            self.data[row][col] = max(0, min(255, int(value)))
        else:
            self.data[row][col][channel] = max(0, min(255, int(value)))
    
    def get_rgb_pixel(self, row, col):
        """Get RGB values as tuple."""
        if self.channels < 3:
            gray = self.get_pixel(row, col)
            return (gray, gray, gray)
        return (
            self.get_pixel(row, col, 0),
            self.get_pixel(row, col, 1),
            self.get_pixel(row, col, 2)
        )
    
    def set_rgb_pixel(self, row, col, r, g, b):
        """Set RGB values."""
        if self.channels >= 3:
            self.set_pixel(row, col, r, 0)
            self.set_pixel(row, col, g, 1)
            self.set_pixel(row, col, b, 2)
    
    def display_ascii(self, chars=" .:-=+*#%@"):
        """Display image using ASCII characters based on intensity."""
        if self.channels == 1:
            print("Grayscale Image (ASCII representation):")
            for row in range(self.height):
                line = ""
                for col in range(self.width):
                    intensity = self.get_pixel(row, col)
                    char_index = int(intensity * (len(chars) - 1) / 255)
                    line += chars[char_index]
                print(line)
        else:
            print("Color Image (ASCII representation - using luminance):")
            for row in range(self.height):
                line = ""
                for col in range(self.width):
                    r, g, b = self.get_rgb_pixel(row, col)
                    # Calculate luminance (perceived brightness)
                    luminance = int(0.299 * r + 0.587 * g + 0.114 * b)
                    char_index = int(luminance * (len(chars) - 1) / 255)
                    line += chars[char_index]
                print(line)
        print()
    
    def copy(self):
        """Create a copy of the image."""
        new_image = SimpleImage(self.width, self.height, self.channels)
        
        if self.channels == 1:
            for row in range(self.height):
                for col in range(self.width):
                    new_image.set_pixel(row, col, self.get_pixel(row, col))
        else:
            for row in range(self.height):
                for col in range(self.width):
                    for channel in range(self.channels):
                        new_image.set_pixel(row, col, self.get_pixel(row, col, channel), channel)
        
        return new_image

def create_test_image():
    """Create a test image with various patterns."""
    image = SimpleImage(32, 20)
    
    # Create different regions with patterns
    for row in range(image.height):
        for col in range(image.width):
            # Gradient pattern
            if col < 8:
                intensity = int(255 * col / 7)
            # Checkerboard pattern
            elif col < 16:
                if (row // 2 + col // 2) % 2 == 0:
                    intensity = 255
                else:
                    intensity = 0
            # Circular pattern
            elif col < 24:
                center_row, center_col = 10, 20
                distance = ((row - center_row)**2 + (col - center_col)**2)**0.5
                intensity = int(255 * max(0, 1 - distance / 8))
            # Noise pattern
            else:
                intensity = random.randint(0, 255)
            
            image.set_pixel(row, col, intensity)
    
    return image

def create_color_test_image():
    """Create a color test image."""
    image = SimpleImage(24, 16, 3)
    
    for row in range(image.height):
        for col in range(image.width):
            # Create color regions
            if col < 8:  # Red gradient
                r = int(255 * col / 7)
                g = 0
                b = 0
            elif col < 16:  # Green gradient
                r = 0
                g = int(255 * (col - 8) / 7)
                b = 0
            else:  # Blue gradient
                r = 0
                g = 0
                b = int(255 * (col - 16) / 7)
            
            # Add row-based variation
            factor = row / (image.height - 1)
            r = int(r * factor)
            g = int(g * factor)
            b = int(b * factor)
            
            image.set_rgb_pixel(row, col, r, g, b)
    
    return image

# Demonstrate image creation and display
print("Image Creation and Display:")
test_image = create_test_image()
print("Test image with various patterns:")
test_image.display_ascii()

color_image = create_color_test_image()
print("Color test image:")
color_image.display_ascii()

# BASIC IMAGE TRANSFORMATIONS
print("=== BASIC IMAGE TRANSFORMATIONS ===")
print()

def adjust_brightness(image, delta):
    """Adjust image brightness by adding delta to all pixels."""
    result = image.copy()
    
    for row in range(image.height):
        for col in range(image.width):
            if image.channels == 1:
                old_value = image.get_pixel(row, col)
                new_value = old_value + delta
                result.set_pixel(row, col, new_value)
            else:
                for channel in range(image.channels):
                    old_value = image.get_pixel(row, col, channel)
                    new_value = old_value + delta
                    result.set_pixel(row, col, new_value, channel)
    
    return result

def adjust_contrast(image, factor):
    """Adjust image contrast by multiplying all pixels by factor."""
    result = image.copy()
    
    for row in range(image.height):
        for col in range(image.width):
            if image.channels == 1:
                old_value = image.get_pixel(row, col)
                new_value = int((old_value - 127) * factor + 127)
                result.set_pixel(row, col, new_value)
            else:
                for channel in range(image.channels):
                    old_value = image.get_pixel(row, col, channel)
                    new_value = int((old_value - 127) * factor + 127)
                    result.set_pixel(row, col, new_value, channel)
    
    return result

def invert_image(image):
    """Invert image colors (negative)."""
    result = image.copy()
    
    for row in range(image.height):
        for col in range(image.width):
            if image.channels == 1:
                old_value = image.get_pixel(row, col)
                new_value = 255 - old_value
                result.set_pixel(row, col, new_value)
            else:
                for channel in range(image.channels):
                    old_value = image.get_pixel(row, col, channel)
                    new_value = 255 - old_value
                    result.set_pixel(row, col, new_value, channel)
    
    return result

def threshold_image(image, threshold=128):
    """Apply threshold to create binary image."""
    result = image.copy()
    
    for row in range(image.height):
        for col in range(image.width):
            if image.channels == 1:
                old_value = image.get_pixel(row, col)
                new_value = 255 if old_value >= threshold else 0
                result.set_pixel(row, col, new_value)
            else:
                # Convert to grayscale first, then threshold
                r, g, b = image.get_rgb_pixel(row, col)
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                new_value = 255 if gray >= threshold else 0
                result.set_rgb_pixel(row, col, new_value, new_value, new_value)
    
    return result

# Demonstrate basic transformations
print("Basic Image Transformations:")

# Brightness adjustment
bright_image = adjust_brightness(test_image, 50)
print("Brightness increased (+50):")
bright_image.display_ascii()

# Contrast adjustment
contrast_image = adjust_contrast(test_image, 1.5)
print("Contrast increased (×1.5):")
contrast_image.display_ascii()

# Inversion
inverted_image = invert_image(test_image)
print("Inverted (negative):")
inverted_image.display_ascii()

# Thresholding
binary_image = threshold_image(test_image, 128)
print("Binary threshold (128):")
binary_image.display_ascii()

# IMAGE FILTERING AND CONVOLUTION
print("=== IMAGE FILTERING AND CONVOLUTION ===")
print()

def apply_kernel(image, kernel, normalize=True):
    """
    Apply convolution kernel to image.
    Kernel is a 2D list representing the filter.
    """
    kernel_height = len(kernel)
    kernel_width = len(kernel[0])
    kernel_center_row = kernel_height // 2
    kernel_center_col = kernel_width // 2
    
    result = image.copy()
    
    # Calculate kernel sum for normalization
    kernel_sum = sum(sum(row) for row in kernel)
    if kernel_sum == 0:
        kernel_sum = 1
    
    for row in range(image.height):
        for col in range(image.width):
            if image.channels == 1:
                # Apply kernel to grayscale image
                pixel_sum = 0
                
                for kr in range(kernel_height):
                    for kc in range(kernel_width):
                        img_row = row + kr - kernel_center_row
                        img_col = col + kc - kernel_center_col
                        pixel_value = image.get_pixel(img_row, img_col)  # Returns 0 for out-of-bounds
                        pixel_sum += pixel_value * kernel[kr][kc]
                
                if normalize and kernel_sum != 0:
                    pixel_sum = pixel_sum // kernel_sum
                
                result.set_pixel(row, col, pixel_sum)
            else:
                # Apply kernel to each channel separately
                for channel in range(image.channels):
                    pixel_sum = 0
                    
                    for kr in range(kernel_height):
                        for kc in range(kernel_width):
                            img_row = row + kr - kernel_center_row
                            img_col = col + kc - kernel_center_col
                            pixel_value = image.get_pixel(img_row, img_col, channel)
                            pixel_sum += pixel_value * kernel[kr][kc]
                    
                    if normalize and kernel_sum != 0:
                        pixel_sum = pixel_sum // kernel_sum
                    
                    result.set_pixel(row, col, pixel_sum, channel)
    
    return result

# Define common kernels
def get_blur_kernel(size=3):
    """Get blur (box filter) kernel."""
    value = 1.0 / (size * size)
    return [[value for _ in range(size)] for _ in range(size)]

def get_gaussian_kernel():
    """Get 3x3 Gaussian blur kernel."""
    return [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]

def get_sharpen_kernel():
    """Get sharpening kernel."""
    return [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]

def get_edge_detection_kernels():
    """Get various edge detection kernels."""
    sobel_x = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]
    
    sobel_y = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]
    
    laplacian = [
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ]
    
    return sobel_x, sobel_y, laplacian

def detect_edges(image):
    """Detect edges using Sobel operators."""
    sobel_x, sobel_y, _ = get_edge_detection_kernels()
    
    # Apply Sobel X and Y kernels
    edges_x = apply_kernel(image, sobel_x, normalize=False)
    edges_y = apply_kernel(image, sobel_y, normalize=False)
    
    # Combine edge magnitudes
    result = image.copy()
    
    for row in range(image.height):
        for col in range(image.width):
            if image.channels == 1:
                gx = edges_x.get_pixel(row, col)
                gy = edges_y.get_pixel(row, col)
                magnitude = int((gx**2 + gy**2)**0.5)
                result.set_pixel(row, col, magnitude)
            else:
                # Process each channel
                for channel in range(image.channels):
                    gx = edges_x.get_pixel(row, col, channel)
                    gy = edges_y.get_pixel(row, col, channel)
                    magnitude = int((gx**2 + gy**2)**0.5)
                    result.set_pixel(row, col, magnitude, channel)
    
    return result

# Demonstrate filtering operations
print("Image Filtering Examples:")

# Gaussian blur
gaussian_kernel = get_gaussian_kernel()
blurred_image = apply_kernel(test_image, gaussian_kernel)
print("Gaussian blur applied:")
blurred_image.display_ascii()

# Sharpening
sharpen_kernel = get_sharpen_kernel()
sharpened_image = apply_kernel(test_image, sharpen_kernel, normalize=False)
print("Sharpening filter applied:")
sharpened_image.display_ascii()

# Edge detection
edges_image = detect_edges(test_image)
print("Edge detection (Sobel):")
edges_image.display_ascii()

# MORPHOLOGICAL OPERATIONS
print("=== MORPHOLOGICAL OPERATIONS ===")
print()

def erode_image(image, kernel_size=3):
    """
    Morphological erosion - shrinks white regions.
    Useful for removing noise and separating connected objects.
    """
    result = image.copy()
    offset = kernel_size // 2
    
    for row in range(image.height):
        for col in range(image.width):
            # Check if all pixels in neighborhood are white (255)
            min_value = 255
            
            for kr in range(-offset, offset + 1):
                for kc in range(-offset, offset + 1):
                    pixel_value = image.get_pixel(row + kr, col + kc)
                    min_value = min(min_value, pixel_value)
            
            result.set_pixel(row, col, min_value)
    
    return result

def dilate_image(image, kernel_size=3):
    """
    Morphological dilation - expands white regions.
    Useful for filling holes and connecting nearby objects.
    """
    result = image.copy()
    offset = kernel_size // 2
    
    for row in range(image.height):
        for col in range(image.width):
            # Check if any pixel in neighborhood is white (255)
            max_value = 0
            
            for kr in range(-offset, offset + 1):
                for kc in range(-offset, offset + 1):
                    pixel_value = image.get_pixel(row + kr, col + kc)
                    max_value = max(max_value, pixel_value)
            
            result.set_pixel(row, col, max_value)
    
    return result

def opening_operation(image, kernel_size=3):
    """
    Morphological opening (erosion followed by dilation).
    Removes noise while preserving shape.
    """
    eroded = erode_image(image, kernel_size)
    return dilate_image(eroded, kernel_size)

def closing_operation(image, kernel_size=3):
    """
    Morphological closing (dilation followed by erosion).
    Fills holes while preserving shape.
    """
    dilated = dilate_image(image, kernel_size)
    return erode_image(dilated, kernel_size)

# Demonstrate morphological operations
print("Morphological Operations:")

# Create binary image for morphological operations
morph_test = threshold_image(test_image, 100)
print("Original binary image:")
morph_test.display_ascii()

# Erosion
eroded = erode_image(morph_test)
print("After erosion:")
eroded.display_ascii()

# Dilation
dilated = dilate_image(morph_test)
print("After dilation:")
dilated.display_ascii()

# Opening
opened = opening_operation(morph_test)
print("After opening (erosion + dilation):")
opened.display_ascii()

# GEOMETRIC TRANSFORMATIONS
print("=== GEOMETRIC TRANSFORMATIONS ===")
print()

def rotate_image_90(image, clockwise=True):
    """Rotate image 90 degrees."""
    if clockwise:
        result = SimpleImage(image.height, image.width, image.channels)
        for row in range(image.height):
            for col in range(image.width):
                new_row = col
                new_col = image.height - 1 - row
                
                if image.channels == 1:
                    value = image.get_pixel(row, col)
                    result.set_pixel(new_row, new_col, value)
                else:
                    for channel in range(image.channels):
                        value = image.get_pixel(row, col, channel)
                        result.set_pixel(new_row, new_col, value, channel)
    else:
        result = SimpleImage(image.height, image.width, image.channels)
        for row in range(image.height):
            for col in range(image.width):
                new_row = image.width - 1 - col
                new_col = row
                
                if image.channels == 1:
                    value = image.get_pixel(row, col)
                    result.set_pixel(new_row, new_col, value)
                else:
                    for channel in range(image.channels):
                        value = image.get_pixel(row, col, channel)
                        result.set_pixel(new_row, new_col, value, channel)
    
    return result

def flip_horizontal(image):
    """Flip image horizontally (mirror)."""
    result = image.copy()
    
    for row in range(image.height):
        for col in range(image.width):
            new_col = image.width - 1 - col
            
            if image.channels == 1:
                value = image.get_pixel(row, col)
                result.set_pixel(row, new_col, value)
            else:
                for channel in range(image.channels):
                    value = image.get_pixel(row, col, channel)
                    result.set_pixel(row, new_col, value, channel)
    
    return result

def flip_vertical(image):
    """Flip image vertically."""
    result = image.copy()
    
    for row in range(image.height):
        for col in range(image.width):
            new_row = image.height - 1 - row
            
            if image.channels == 1:
                value = image.get_pixel(row, col)
                result.set_pixel(new_row, col, value)
            else:
                for channel in range(image.channels):
                    value = image.get_pixel(row, col, channel)
                    result.set_pixel(new_row, col, value, channel)
    
    return result

def scale_image_nearest(image, scale_factor):
    """Scale image using nearest neighbor interpolation."""
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    result = SimpleImage(new_width, new_height, image.channels)
    
    for new_row in range(new_height):
        for new_col in range(new_width):
            # Map new coordinates to original coordinates
            orig_row = int(new_row / scale_factor)
            orig_col = int(new_col / scale_factor)
            
            # Clamp to image bounds
            orig_row = min(orig_row, image.height - 1)
            orig_col = min(orig_col, image.width - 1)
            
            if image.channels == 1:
                value = image.get_pixel(orig_row, orig_col)
                result.set_pixel(new_row, new_col, value)
            else:
                for channel in range(image.channels):
                    value = image.get_pixel(orig_row, orig_col, channel)
                    result.set_pixel(new_row, new_col, value, channel)
    
    return result

# Demonstrate geometric transformations
print("Geometric Transformations:")

# Create smaller test image for transformations
small_image = SimpleImage(12, 8)
for row in range(small_image.height):
    for col in range(small_image.width):
        if col < 4:
            intensity = 255 if row < 4 else 128
        elif col < 8:
            intensity = 64 if (row + col) % 2 == 0 else 192
        else:
            intensity = min(255, row * col * 8)
        small_image.set_pixel(row, col, intensity)

print("Original small image:")
small_image.display_ascii()

# Rotation
rotated_cw = rotate_image_90(small_image, clockwise=True)
print("Rotated 90° clockwise:")
rotated_cw.display_ascii()

# Horizontal flip
flipped_h = flip_horizontal(small_image)
print("Flipped horizontally:")
flipped_h.display_ascii()

# Vertical flip
flipped_v = flip_vertical(small_image)
print("Flipped vertically:")
flipped_v.display_ascii()

# HISTOGRAM AND STATISTICAL ANALYSIS
print("=== HISTOGRAM AND STATISTICAL ANALYSIS ===")
print()

def calculate_histogram(image, channel=0):
    """Calculate histogram of pixel intensities."""
    histogram = [0] * 256
    
    for row in range(image.height):
        for col in range(image.width):
            if image.channels == 1:
                intensity = image.get_pixel(row, col)
            else:
                intensity = image.get_pixel(row, col, channel)
            histogram[intensity] += 1
    
    return histogram

def calculate_image_statistics(image, channel=0):
    """Calculate basic statistical measures for image."""
    pixels = []
    
    for row in range(image.height):
        for col in range(image.width):
            if image.channels == 1:
                intensity = image.get_pixel(row, col)
            else:
                intensity = image.get_pixel(row, col, channel)
            pixels.append(intensity)
    
    # Calculate statistics
    total_pixels = len(pixels)
    mean = sum(pixels) / total_pixels
    
    variance = sum((p - mean) ** 2 for p in pixels) / total_pixels
    std_dev = variance ** 0.5
    
    min_val = min(pixels)
    max_val = max(pixels)
    
    # Calculate median
    sorted_pixels = sorted(pixels)
    if total_pixels % 2 == 0:
        median = (sorted_pixels[total_pixels // 2 - 1] + sorted_pixels[total_pixels // 2]) / 2
    else:
        median = sorted_pixels[total_pixels // 2]
    
    return {
        'mean': mean,
        'median': median,
        'std_dev': std_dev,
        'variance': variance,
        'min': min_val,
        'max': max_val,
        'range': max_val - min_val
    }

def display_histogram_ascii(histogram, max_height=10):
    """Display histogram using ASCII art."""
    if not histogram:
        return
    
    max_count = max(histogram)
    if max_count == 0:
        return
    
    # Group intensities for display (every 32 values)
    grouped_hist = []
    for i in range(0, 256, 32):
        group_sum = sum(histogram[i:i+32])
        grouped_hist.append(group_sum)
    
    # Normalize to max height
    max_group = max(grouped_hist)
    if max_group == 0:
        return
    
    print("Histogram (intensity groups 0-31, 32-63, ..., 224-255):")
    for height in range(max_height, 0, -1):
        line = ""
        for group_count in grouped_hist:
            if group_count * max_height >= height * max_group:
                line += "█"
            else:
                line += " "
        print(f"{height:2d}|{line}")
    
    # Print x-axis
    print("  " + "+" * 8)
    print("   0  32 64 96 128160192224")

# Demonstrate histogram and statistics
print("Image Analysis:")

# Calculate statistics for test image
stats = calculate_image_statistics(test_image)
print("Image Statistics:")
print(f"  Mean: {stats['mean']:.2f}")
print(f"  Median: {stats['median']:.2f}")
print(f"  Standard Deviation: {stats['std_dev']:.2f}")
print(f"  Min: {stats['min']}")
print(f"  Max: {stats['max']}")
print(f"  Range: {stats['range']}")
print()

# Calculate and display histogram
histogram = calculate_histogram(test_image)
display_histogram_ascii(histogram)
print()

# ADVANCED IMAGE PROCESSING APPLICATIONS
print("=== ADVANCED IMAGE PROCESSING APPLICATIONS ===")
print()

def template_matching(image, template, threshold=0.8):
    """
    Simple template matching using normalized cross-correlation.
    Returns list of match positions.
    """
    matches = []
    template_height = len(template)
    template_width = len(template[0])
    
    # Calculate template mean for normalization
    template_sum = sum(sum(row) for row in template)
    template_mean = template_sum / (template_height * template_width)
    
    # Search for template in image
    for start_row in range(image.height - template_height + 1):
        for start_col in range(image.width - template_width + 1):
            # Extract image region
            region_sum = 0
            template_match = 0
            region_sq_sum = 0
            template_sq_sum = 0
            
            for tr in range(template_height):
                for tc in range(template_width):
                    img_val = image.get_pixel(start_row + tr, start_col + tc)
                    template_val = template[tr][tc]
                    
                    region_sum += img_val
                    template_match += img_val * template_val
                    region_sq_sum += img_val * img_val
                    template_sq_sum += template_val * template_val
            
            # Calculate normalized correlation
            region_mean = region_sum / (template_height * template_width)
            
            numerator = template_match - (template_height * template_width * region_mean * template_mean)
            denominator = ((region_sq_sum - (template_height * template_width * region_mean**2)) * 
                          (template_sq_sum - (template_height * template_width * template_mean**2)))**0.5
            
            if denominator > 0:
                correlation = numerator / denominator
                if correlation >= threshold:
                    matches.append((start_row, start_col, correlation))
    
    return matches

def connected_components(binary_image):
    """
    Find connected components in binary image using flood fill.
    Returns list of components, each containing pixel coordinates.
    """
    visited = [[False for _ in range(binary_image.width)] for _ in range(binary_image.height)]
    components = []
    
    def flood_fill(start_row, start_col):
        component = []
        stack = [(start_row, start_col)]
        
        while stack:
            row, col = stack.pop()
            
            if (row < 0 or row >= binary_image.height or 
                col < 0 or col >= binary_image.width or
                visited[row][col] or
                binary_image.get_pixel(row, col) == 0):
                continue
            
            visited[row][col] = True
            component.append((row, col))
            
            # Add neighbors to stack
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                stack.append((row + dr, col + dc))
        
        return component
    
    # Find all components
    for row in range(binary_image.height):
        for col in range(binary_image.width):
            if not visited[row][col] and binary_image.get_pixel(row, col) > 0:
                component = flood_fill(row, col)
                if component:
                    components.append(component)
    
    return components

# Demonstrate advanced applications
print("Advanced Applications:")

# Create binary image for component analysis
component_image = threshold_image(test_image, 150)
print("Binary image for component analysis:")
component_image.display_ascii()

# Find connected components
components = connected_components(component_image)
print(f"Found {len(components)} connected components:")

for i, component in enumerate(components):
    print(f"  Component {i+1}: {len(component)} pixels")
    if len(component) < 20:  # Show coordinates for small components
        print(f"    Coordinates: {component}")

print()

print("=== SUMMARY ===")
print()
print("Image Processing with 2D Arrays Summary:")
print("1. Images are natural 2D array applications")
print("2. Basic operations include brightness, contrast, and color adjustments")
print("3. Filtering uses convolution with various kernels")
print("4. Edge detection identifies important image features")
print("5. Morphological operations modify object shapes")
print("6. Geometric transformations change image orientation and size")
print("7. Statistical analysis provides insight into image characteristics")
print("8. Advanced techniques enable complex computer vision tasks")

"""
KEY TAKEAWAYS:
==============
1. Images are perfect examples of 2D array manipulation
2. Pixel operations can be performed element-wise or with neighborhoods
3. Convolution is fundamental to many image processing techniques
4. Different kernels produce different visual effects
5. Morphological operations are useful for shape analysis
6. Geometric transformations require coordinate mapping
7. Statistical measures help characterize image content
8. Advanced algorithms combine basic operations for complex tasks

IMAGE REPRESENTATION:
=====================
• Grayscale: Single intensity value per pixel (0-255)
• RGB Color: Three values per pixel (Red, Green, Blue)
• Other formats: HSV, CMYK, Lab, etc.
• Bit depth: 8-bit (256 levels), 16-bit, floating point

COMMON OPERATIONS:
==================
• Point operations: Brightness, contrast, gamma correction
• Area operations: Filtering, convolution, morphology
• Geometric: Rotation, scaling, translation, perspective
• Statistical: Histogram, moments, texture measures

FILTERING TECHNIQUES:
=====================
• Smoothing: Gaussian blur, mean filter, median filter
• Sharpening: Unsharp mask, high-pass filters
• Edge detection: Sobel, Canny, Laplacian
• Noise reduction: Bilateral filter, non-local means

MORPHOLOGICAL OPERATIONS:
=========================
• Basic: Erosion, dilation
• Compound: Opening (remove noise), closing (fill holes)
• Advanced: Skeletonization, distance transform
• Applications: Shape analysis, object separation

REAL-WORLD APPLICATIONS:
========================
• Medical imaging: X-rays, MRI, CT scans
• Satellite imagery: Land use, weather monitoring
• Industrial inspection: Quality control, defect detection
• Photography: Filters, enhancement, restoration
• Computer vision: Object recognition, autonomous vehicles

PERFORMANCE CONSIDERATIONS:
===========================
• Large images require significant memory
• Convolution operations can be computationally expensive
• Parallel processing can accelerate many operations
• Specialized libraries (OpenCV, PIL, scikit-image) provide optimizations
• GPU acceleration available for many algorithms

NEXT STEP:
Go to 05-game-development.py to see how 2D arrays power game mechanics!
"""