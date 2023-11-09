# picamera2-experiments

This repository provides several python files used to test the functioning of Picamera2, a libcamera-based replacement for Picamera which was a Python interface to the Raspberry Pi's legacy camera stack.
- Low-level process: for a deeper understanding of what happens under the hood, it is possible to execute the different steps of the image capturing process:
  - configure the camera system
  - launch the preview window
  - start the camera
  - capture an image after a specific wait time
-  High-level capture API: Picamera2 provides some high-level predefined functions to capture one or more images or to record a video without knowing too much about the camera configuration and the details of how the library works.

Some examples of captured images and videos are available in the "Captures" folder.

An example of the main camera controls is also available, showing that some controls have limits that change with the camera configuration. In this case, each control has a (minimum_value, maximum_value, default_value) triple.
Camera controls are well explained in the section "Appendix C: Camera controls" of [The Picamera2 Library Manual](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf).

