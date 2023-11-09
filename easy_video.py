# Use picamera2 high-level API to start the camera and record a video of {duration} seconds.

from picamera2 import Picamera2

picam2 = Picamera2()

# Record a 5 second video.
picam2.start_and_record_video("Captures/test.mp4", duration=4, show_preview=True)
