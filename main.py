import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
# sys.path.insert(0, '/mnt/c/Users/hp/Desktop/catkin_ws/src')
import images_rc
import cv2

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_gui.ui", self)
        self.pushButton.clicked.connect(self.gototasks)
    
    def gototasks(self):
        screen2_tasks = Screen2_Tasks()
        widget.addWidget(screen2_tasks)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Screen2_Tasks(QMainWindow):
    def __init__(self):
        super(Screen2_Tasks, self).__init__()
        loadUi("page2_tasks.ui", self)
        self.pushButton.clicked.connect(self.gototask1)
    
    def gototask1(self):
        task_1 = Task_1()
        widget.addWidget(task_1)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Task_1(QMainWindow):
    def __init__(self):
        super(Task_1, self).__init__()
        loadUi("task1.ui", self)
        self.buttonBox_4.accepted.connect(self.start_cam_1)
        self.buttonBox_4.rejected.connect(self.stop_cam_1)
    
    def show_frame(self):
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True & cam_on:
                # self.displayImage(label_3, 1)
                frame = cv2.flip(frame, 180)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (395, 260))

                image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
                self.label_3.setPixmap(QPixmap.fromImage(image))
                self.label_5.setPixmap(QPixmap.fromImage(image))
                self.label_6.setPixmap(QPixmap.fromImage(image))
                self.label_4.setPixmap(QPixmap.fromImage(image))
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
    
    def start_cam_1(self):
        global cam_on, cap
        cam_on = True
        cap = cv2.VideoCapture(0) 
        self.show_frame()
        print("Camera ON")

    def stop_cam_1(self):
        global cam_on
        cam_on = False
        if cap:
            cap.release()
        print("Camera OFF")


#Main
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
widget.addWidget(mainwindow)

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Closed")