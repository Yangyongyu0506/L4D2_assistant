import mss
import numpy as np

class ScreenCapture:
    def __init__(self, monitor_index=1):
        self.sct = mss.mss()
        self.monitor = self.sct.monitors[monitor_index]

    def grab_frame(self):
        sct_img = self.sct.grab(self.monitor)
        frame = np.array(sct_img)
        return frame[..., :3]  # 去掉alpha通道
