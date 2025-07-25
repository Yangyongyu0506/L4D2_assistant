import sys
import cv2
from PyQt5 import QtWidgets, QtGui, QtCore
from detect import YoloDetector
from capture import ScreenCapture
from overlay import OverlayWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    overlay = OverlayWindow()
    overlay.show()

    detector = YoloDetector()
    capturer = ScreenCapture()

    timer = QtCore.QTimer()
    def run_detection():
        frame = capturer.grab_frame()
        result = detector.detect(frame)
        overlay.update_boxes(result)

    timer.timeout.connect(run_detection)
    timer.start(30)  # 每 30ms 推理一次

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
