# Real-Time Object Tracker

A simple real-time object tracking application built with Python and OpenCV.

The user selects an object from the first webcam frame, and the program tracks the selected object in the live video using the CSRT tracker.


## Installation

Clone the repository:

git clone <your-repository-url>

Move into the project folder:

cd object-tracker

Install the required package:

pip install -r requirements.txt

## Run

Run:

python tracker.py

A window will open showing the first webcam frame.

1. Draw a bounding box around the object you want to track.
2. Press Enter or Space to confirm the selection.
3. Move the object in front of the camera.
4. Press `q` to stop the program.

## Implementation

The program captures a frame from the webcam and allows the user to select a Region of Interest (ROI).

The selected ROI is used to initialize an OpenCV CSRT tracker.

For every new webcam frame, the tracker estimates the new position of the selected object. The returned bounding-box coordinates are then used to draw a rectangle around the object in the live video.

## Demo

A recorded demonstration of the tracker is included in this repository.

## Limitations

The tracking performance can be affected by fast movement, large appearance changes, or the object leaving the camera view.
