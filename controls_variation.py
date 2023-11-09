# Manipulate multiple camera controls: they are well explained in "Appendix C: Camera controls"
# available here https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

import time

from picamera2 import Picamera2, Preview
from libcamera import controls

picam2 = Picamera2()

controls = {"ExposureTime": 30000, "AwbMode": controls.AwbModeEnum.Daylight} #"Brightness": 0.1

# Controls stored with the configuration, so that they will be re-applied whenever that configuration is requested
preview_config = picam2.create_preview_configuration(controls=controls)
picam2.configure(preview_config)

picam2.start_preview(Preview.QTGL)

picam2.start()

# Display camera information on the window title bar
picam2.title_fields = ["ExposureTime"]
time.sleep(7)

metadata = picam2.capture_file("better_background(1).png")
print(metadata)

picam2.close()
