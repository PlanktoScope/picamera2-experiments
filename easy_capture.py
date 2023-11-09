# Test the high-level image capture function "start_and_capture_files" that configures and starts the camera automatically.

from picamera2 import Picamera2

picam2 = Picamera2()

# Capture 3 images. Use a 1 second delay after the first image.
picam2.start_and_capture_files("Captures/multiple_test{:d}.jpg", num_files=3, delay=1, show_preview=True)  # noqa
