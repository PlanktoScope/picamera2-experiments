# Capture a full resolution image while still running in the preview mode.
# The preview window QtGL is the most efficient way to display images on the screen connected to RPi,
# but it is not recommended when the image needs to be shown on a remote display.

import time

from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)

preview_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration()
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

picam2.switch_mode_and_capture_file(capture_config, "basic_capture_fullres.jpg")
