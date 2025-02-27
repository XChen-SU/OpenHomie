import cv2
import numpy as np
import isaacgym

# Initialize Isaac Gym simulator and environment
sim = isaacgym.create_sim()
env = isaacgym.create_env(sim)

# Define the video output path and settings
frame_width = 1920  # Frame width (adjust according to your environment)
frame_height = 1080  # Frame height
fps = 30  # Frames per second for the video
output_video_path = 'simulation_output.mp4'

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Video codec (you can use 'XVID' or 'MP4V')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Simulate and capture frames
for step in range(1000):  # Number of simulation steps
    # Step the simulation
    sim.step()

    # Capture the current frame (assuming we have a method to get the frame)
    frame = isaacgym.get_simulation_frame(sim)  # Replace with actual method to get frame
    frame = np.array(frame)  # Ensure frame is a numpy array if needed

    # Convert frame to the correct format if necessary
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR if needed
    
    # Write the frame to the video file
    out.write(frame)

# Release the video writer object
out.release()

# Optionally, close the simulation
isaacgym.destroy_sim(sim)
