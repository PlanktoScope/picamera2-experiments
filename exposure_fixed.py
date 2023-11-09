# Start camera with fixed exposure and gain.

import time
import json

from picamera2 import Picamera2, Preview

picam2 = Picamera2()

#with open("camera_controls.txt", "w") as fl:
    #json.dump(picam2.camera_controls, fl)

picam2.start_preview(Preview.QTGL)

controls = {"ExposureTime": 10000, "AnalogueGain": 1.0}
preview_config = picam2.create_preview_configuration(controls=controls)
picam2.configure(preview_config)

picam2.start()
picam2.title_fields = ["ExposureTime", "AnalogueGain"]
time.sleep(7)
