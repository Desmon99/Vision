import cv2
import depthai as dai
from ImageSearch import data_matrix_code_detection
from matplotlib import pyplot as plt

# Create pipeline
pipeline = dai.Pipeline()

# Define source and output
camRgb = pipeline.create(dai.node.ColorCamera)
xoutVideo = pipeline.create(dai.node.XLinkOut)
stillEncoder = pipeline.create(dai.node.VideoEncoder)

controlIn = pipeline.create(dai.node.XLinkIn)
stillMjpegOut = pipeline.create(dai.node.XLinkOut)

controlIn.setStreamName('control')

# Properties
camRgb.setBoardSocket(dai.CameraBoardSocket.CAM_A)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setVideoSize(1920, 1080)

stillEncoder.setDefaultProfilePreset(1, dai.VideoEncoderProperties.Profile.MJPEG)

xoutVideo.input.setBlocking(False)
xoutVideo.input.setQueueSize(1)

xoutVideo.setStreamName("video")
stillMjpegOut.setStreamName('still')

# Linking
camRgb.video.link(xoutVideo.input)
camRgb.still.link(stillEncoder.input)
stillEncoder.bitstream.link(stillMjpegOut.input)
controlIn.out.link(camRgb.inputControl)

# Connect to device and start pipeline
with dai.Device(pipeline) as device:

    print(device.getConnectedCameraFeatures())
    controlQueue = device.getInputQueue('control')
    video = device.getOutputQueue(name="video", maxSize=1, blocking=False)
    stillQueue = device.getOutputQueue('still')

    while True:
        videoIn = video.tryGetAll()
        for vidFrame in videoIn:
            cv2.imshow('video', vidFrame.getCvFrame())

        stillFrames = stillQueue.tryGetAll()
        for stillFrame in stillFrames:
            # Decode JPEG
            frame = cv2.imdecode(stillFrame.getData(), cv2.IMREAD_UNCHANGED)

            # Display
            image = simple_barcode_detection.detect(frame)

            # Display greyscale image
            cv2.imshow("grey", image)

            """
            # display histogram
            plt.figure()
            plt.title("Greyscale histogram")
            plt.xlabel("Bins")
            plt.ylabel("# of pixels")
            plt.plot(hist)
            plt.xlim([0, 256])
            plt.show()
            """

            # cv2.drawContours(image=frame, contours=image, contourIdx=-1, color=(0, 255, 0), thickness=3)
            # cv2.imshow('still', image)


        # Get BGR frame from NV12 encoded video frame to show with opencv
        # Visualizing the frame on slower hosts might have overhead
        # cv2.imshow("video", videoIn.getCvFrame())

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('c'):
            ctrl = dai.CameraControl()
            still = True
            ctrl.setCaptureStill(True)
            controlQueue.send(ctrl)
        elif key == ord('f'):
            print("Autofocus enable, continuous")
            ctrl = dai.CameraControl()
            ctrl.setAutoFocusMode(dai.CameraControl.AutoFocusMode.CONTINUOUS_VIDEO)
            controlQueue.send(ctrl)
        elif key == ord('e'):
            print("Autoexposure enable")
            still = False
            ctrl = dai.CameraControl()
            ctrl.setAutoExposureEnable()
            controlQueue.send(ctrl)
