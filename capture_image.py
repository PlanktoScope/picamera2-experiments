# Capture a JPEG while still running in the preview mode. When capturing
# to a file, the return value is the metadata for that image.
# By default the main stream is displayed in the preview window. In some 
# circumstances it may be preferable to display a lower resolution image (lores={"size": (320, 240)}, display="lores").

import time

from picamera2 import Picamera2, Preview

picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
picam2.configure(preview_config)

picam2.start_preview(Preview.QTGL)

picam2.start()
time.sleep(2)

metadata = picam2.capture_file("./base_capture(png).png")
print(metadata)

picam2.close()
