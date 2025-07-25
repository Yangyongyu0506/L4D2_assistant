from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class OverlayWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | 
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.X11BypassWindowManagerHint |
                            QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        screen = QtWidgets.QApplication.primaryScreen()
        self.setGeometry(screen.geometry())
        self.boxes = []

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.red, 2))
        font = QtGui.QFont("Arial", 14)
        painter.setFont(font)
        for label, box in self.boxes:
            x1, y1, x2, y2 = box
            painter.drawRect(x1, y1, x2 - x1, y2 - y1)
            painter.drawText(x1, y1 - 10, label)

    def update_boxes(self, detections):
        self.boxes = []
        for result in detections.boxes.data.cpu().numpy():
            x1, y1, x2, y2, conf, cls = result
            label = detections.names[int(cls)]
            self.boxes.append((label, (int(x1), int(y1), int(x2), int(y2))))
        self.update()
