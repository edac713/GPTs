import cv2
import numpy as np
from PIL import Image
import os
import json

# Function to convert png to jpeg
def convert_png_to_jpeg(png_path):
    image = Image.open(png_path)
    rgb_im = image.convert('RGB')
    jpeg_path = png_path.replace('.png', '.jpeg')
    rgb_im.save(jpeg_path, 'JPEG')
    return jpeg_path

# Function for enhanced edge detection and segmentation
def enhanced_edge_detection_and_segmentation(image, edge_threshold1, edge_threshold2):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, edge_threshold1, edge_threshold2)
    h_projection = np.sum(edges, axis=1)
    transitions = np.where(np.diff(h_projection > 0))[0]
    if len(transitions) % 2 == 1:
        transitions = transitions[:-1]  # Ensure we have pairs of transitions
    return transitions

# Function to calculate whitespace and merge segments
def calculate_whitespace_and_merge_segments(image, boundaries, whitespace_threshold):
    merged_segments = []
    prev_end = 0
    for start, end in boundaries:
        if start - prev_end <= whitespace_threshold:
            if merged_segments:
                merged_segments[-1] = (merged_segments[-1][0], end)
            else:
                merged_segments.append((start, end))
        else:
            merged_segments.append((start, end))
        prev_end = end
    return merged_segments

# Function to save segment images and return their info
def save_segment(image, start, end, segment_number, base_path='/mnt/data/'):
    segment = image[start:end, :]
    segment_filename = f"segment_{segment_number}.jpeg"
    segment_path = os.path.join(base_path, segment_filename)
    cv2.imwrite(segment_path, segment)
    # Convert numpy int64 to Python int for JSON serialization
    return {
        "path": segment_path,
        "dimensions": (int(segment.shape[1]), int(end - start))  # Width and height
    }

# Main function to process the image and structure the output
def process_image_modularized(image_path):
    if image_path.lower().endswith('.png'):
        image_path = convert_png_to_jpeg(image_path)

    wireframe_image = cv2.imread(image_path)
    if wireframe_image is None:
        raise FileNotFoundError(f"The image at path {image_path} could not be loaded. Please check the file path and try again.")
    
    # Scale the image to 750x1500 pixels
    scaled_wireframe_image = cv2.resize(wireframe_image, (750, 1500), interpolation=cv2.INTER_AREA)

    edge_threshold1 = 50
    edge_threshold2 = 150
    whitespace_threshold = 30

    transitions = enhanced_edge_detection_and_segmentation(scaled_wireframe_image, edge_threshold1, edge_threshold2)
    initial_boundaries = [(transitions[i], transitions[i+1]) for i in range(0, len(transitions), 2)]
    merged_boundaries = calculate_whitespace_and_merge_segments(scaled_wireframe_image, initial_boundaries, whitespace_threshold)

    segments_info = [save_segment(scaled_wireframe_image, start, end, i) for i, (start, end) in enumerate(merged_boundaries)]
    wireframe_image_size = (750, 1500)  # Width, height since we scaled every image to this size

    output_structure = {
        "wireframe_size": wireframe_image_size,
        "segments": segments_info,
        "instructions": (
            "Each segment is an image that has been horizontally cropped to isolate "
            "parts of the UI. The width of each segment matches the wireframe's width. "
            "The height varies, corresponding to the vertical space each UI element occupies. "
            "Treat each segment as a building block, stacking from the top of the wireframe "
            "to the bottom to reconstruct the full layout."
        )
    }
    return json.dumps(output_structure, indent=2)

def main(image_path):
    # Process the image and output structured JSON
    json_output = process_image_modularized(image_path)
    return json_output