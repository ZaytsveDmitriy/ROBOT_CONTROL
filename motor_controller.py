import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGroupBox, QWidget, QLabel, QSpinBox, QVBoxLayout, QHBoxLayout, qApp, QLineEdit
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
import robot_control
import time

class Motor(QHBoxLayout):
    def __init__(self, parent=None):
        QHBoxLayout.__init__(self, parent)
        self.button_ccw_fast = QPushButton("СCW\nFAST")
        self.button_ccw_fast.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.button_ccw_fast.setStyleSheet("color: red")
        self.button_ccw_fast.setMinimumWidth(80)
        self.button_ccw_fast.setMinimumHeight(80)
        self.addWidget(self.button_ccw_fast)

        self.button_ccw = QPushButton("СCW")
        self.button_ccw.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.button_ccw.setStyleSheet("color: blue")
        self.button_ccw.setMinimumWidth(80)
        self.button_ccw.setMinimumHeight(80)
        self.addWidget(self.button_ccw)

        self.button_cw = QPushButton("СW")
        self.button_cw.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.button_cw.setStyleSheet("color: blue")
        self.button_cw.setMinimumWidth(80)
        self.button_cw.setMinimumHeight(80)
        self.addWidget(self.button_cw)

        self.button_cw_fast = QPushButton("СW\nFAST")
        self.button_cw_fast.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.button_cw_fast.setStyleSheet("color: red")
        self.button_cw_fast.setMinimumWidth(80)
        self.button_cw_fast.setMinimumHeight(80)
        self.addWidget(self.button_cw_fast)

class MainButtonGroup(QVBoxLayout):

    def __init__(self, parent=None):
        QVBoxLayout.__init__(self, parent)
        self.button_create = QPushButton("&СОЗДАТЬ")
        self.button_create.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.button_create.setStyleSheet("color: blue")
        self.addWidget(self.button_create)

class MyWindow(QWidget):

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        self.motor_1_label = QLabel("<center>MOTOR 1</center>")
        self.motor_1_label.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.motor_2_label = QLabel("<center>MOTOR 2</center>")
        self.motor_2_label.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.motor_3_label = QLabel("<center>MOTOR 3</center>")
        self.motor_3_label.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.motor_4_label = QLabel("<center>MOTOR 4</center>")
        self.motor_4_label.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.motor_5_label = QLabel("<center>MOTOR 5</center>")
        self.motor_5_label.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.motor_6_label = QLabel("<center>MOTOR 6</center>")
        self.motor_6_label.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.vbox = QVBoxLayout()
        self.vbox.setSpacing(2)

        self.motor_1 = Motor()
        self.motor_2 = Motor()
        self.motor_3 = Motor()
        self.motor_4 = Motor()
        self.motor_5 = Motor()
        self.motor_6 = Motor()

        self.vbox.addWidget(self.motor_1_label)
        self.vbox.addLayout(self.motor_1)

        self.vbox.addWidget(self.motor_2_label)
        self.vbox.addLayout(self.motor_2)
        
        self.vbox.addWidget(self.motor_3_label)
        self.vbox.addLayout(self.motor_3)

        self.vbox.addWidget(self.motor_4_label)
        self.vbox.addLayout(self.motor_4)

        self.vbox.addWidget(self.motor_5_label)
        self.vbox.addLayout(self.motor_5)

        self.vbox.addWidget(self.motor_6_label)
        self.vbox.addLayout(self.motor_6)

        self.setLayout(self.vbox)

        self.motor_1.button_cw.pressed.connect(lambda  comand = robot_control.chanel_1.cw_rotation, 
                                                            button = self.motor_1.button_cw:    
                                                    motor_control(comand, button))
        self.motor_1.button_cw_fast.pressed.connect(lambda  comand = robot_control.chanel_1.cw_rotation_fast, 
                                                            button = self.motor_1.button_cw_fast:    
                                                    motor_control(comand, button))
        self.motor_1.button_ccw.pressed.connect(lambda  comand = robot_control.chanel_1.ccw_rotation, 
                                                            button = self.motor_1.button_ccw:    
                                                    motor_control(comand, button))
        self.motor_1.button_ccw_fast.pressed.connect(lambda  comand = robot_control.chanel_1.ccw_rotation_fast, 
                                                            button = self.motor_1.button_ccw_fast:    
                                                    motor_control(comand, button))


        self.motor_2.button_cw.pressed.connect(lambda  comand = robot_control.chanel_2.cw_rotation, 
                                                            button = self.motor_2.button_cw:    
                                                    motor_control(comand, button))
        self.motor_2.button_cw_fast.pressed.connect(lambda  comand = robot_control.chanel_2.cw_rotation_fast, 
                                                            button = self.motor_2.button_cw_fast:    
                                                    motor_control(comand, button))
        self.motor_2.button_ccw.pressed.connect(lambda  comand = robot_control.chanel_2.ccw_rotation, 
                                                            button = self.motor_2.button_ccw:    
                                                    motor_control(comand, button))
        self.motor_2.button_ccw_fast.pressed.connect(lambda  comand = robot_control.chanel_2.ccw_rotation_fast, 
                                                            button = self.motor_2.button_ccw_fast:    
                                                    motor_control(comand, button))


        self.motor_3.button_cw.pressed.connect(lambda  comand = robot_control.chanel_3.cw_rotation, 
                                                            button = self.motor_3.button_cw:    
                                                    motor_control(comand, button))
        self.motor_3.button_cw_fast.pressed.connect(lambda  comand = robot_control.chanel_3.cw_rotation_fast, 
                                                            button = self.motor_3.button_cw_fast:    
                                                    motor_control(comand, button))
        self.motor_3.button_ccw.pressed.connect(lambda  comand = robot_control.chanel_3.ccw_rotation, 
                                                            button = self.motor_3.button_ccw:    
                                                    motor_control(comand, button))
        self.motor_3.button_ccw_fast.pressed.connect(lambda  comand = robot_control.chanel_3.ccw_rotation_fast, 
                                                            button = self.motor_3.button_ccw_fast:    
                                                    motor_control(comand, button))


        self.motor_4.button_cw.pressed.connect(lambda  comand = robot_control.chanel_4.cw_rotation, 
                                                            button = self.motor_4.button_cw:    
                                                    motor_control(comand, button))
        self.motor_4.button_cw_fast.pressed.connect(lambda  comand = robot_control.chanel_4.cw_rotation_fast, 
                                                            button = self.motor_4.button_cw_fast:    
                                                    motor_control(comand, button))
        self.motor_4.button_ccw.pressed.connect(lambda  comand = robot_control.chanel_4.ccw_rotation, 
                                                            button = self.motor_4.button_ccw:    
                                                    motor_control(comand, button))
        self.motor_4.button_ccw_fast.pressed.connect(lambda  comand = robot_control.chanel_4.ccw_rotation_fast, 
                                                            button = self.motor_4.button_ccw_fast:    
                                                    motor_control(comand, button))


        self.motor_5.button_cw.pressed.connect(lambda  comand = robot_control.chanel_5.cw_rotation, 
                                                            button = self.motor_5.button_cw:    
                                                    motor_control(comand, button))
        self.motor_5.button_cw_fast.pressed.connect(lambda  comand = robot_control.chanel_5.cw_rotation_fast, 
                                                            button = self.motor_5.button_cw_fast:    
                                                    motor_control(comand, button))
        self.motor_5.button_ccw.pressed.connect(lambda  comand = robot_control.chanel_5.ccw_rotation, 
                                                            button = self.motor_5.button_ccw:    
                                                    motor_control(comand, button))
        self.motor_5.button_ccw_fast.pressed.connect(lambda  comand = robot_control.chanel_5.ccw_rotation_fast, 
                                                            button = self.motor_5.button_ccw_fast:    
                                                    motor_control(comand, button))


        self.motor_6.button_cw.pressed.connect(lambda  comand = robot_control.chanel_6.cw_rotation, 
                                                            button = self.motor_6.button_cw:    
                                                    motor_control(comand, button))
        self.motor_6.button_cw_fast.pressed.connect(lambda  comand = robot_control.chanel_6.cw_rotation_fast, 
                                                            button = self.motor_6.button_cw_fast:    
                                                    motor_control(comand, button))
        self.motor_6.button_ccw.pressed.connect(lambda  comand = robot_control.chanel_6.ccw_rotation, 
                                                            button = self.motor_6.button_ccw:    
                                                    motor_control(comand, button))
        self.motor_6.button_ccw_fast.pressed.connect(lambda  comand = robot_control.chanel_6.ccw_rotation_fast, 
                                                            button = self.motor_6.button_ccw_fast:    
                                                    motor_control(comand, button))
                                                            
        self.motor_1.button_cw.released.connect(stop_all)
        self.motor_1.button_cw_fast.released.connect(stop_all)
        self.motor_1.button_ccw.released.connect(stop_all)
        self.motor_1.button_ccw_fast.released.connect(stop_all)

        self.motor_2.button_cw.released.connect(stop_all)
        self.motor_2.button_cw_fast.released.connect(stop_all)
        self.motor_2.button_ccw.released.connect(stop_all)
        self.motor_2.button_ccw_fast.released.connect(stop_all)

        self.motor_3.button_cw.released.connect(stop_all)
        self.motor_3.button_cw_fast.released.connect(stop_all)
        self.motor_3.button_ccw.released.connect(stop_all)
        self.motor_3.button_ccw_fast.released.connect(stop_all)

        self.motor_4.button_cw.released.connect(stop_all)
        self.motor_4.button_cw_fast.released.connect(stop_all)
        self.motor_4.button_ccw.released.connect(stop_all)
        self.motor_4.button_ccw_fast.released.connect(stop_all)

        self.motor_5.button_cw.released.connect(stop_all)
        self.motor_5.button_cw_fast.released.connect(stop_all)
        self.motor_5.button_ccw.released.connect(stop_all)
        self.motor_5.button_ccw_fast.released.connect(stop_all)

        self.motor_6.button_cw.released.connect(stop_all)
        self.motor_6.button_cw_fast.released.connect(stop_all)
        self.motor_6.button_ccw.released.connect(stop_all)
        self.motor_6.button_ccw_fast.released.connect(stop_all)


def motor_control(comand, button):
    print("Инициализация и старт ЭД")
    robot_control.send_comand(robot_control.stop_all)
    robot_control.send_comand(comand)
    QtWidgets.qApp.processEvents()
    while button.isDown():
        time.sleep(0.3)
        print("Повторная отправка команды")
        robot_control.send_comand(comand)
        QtWidgets.qApp.processEvents()


def stop_all():
    print("Команда останов")
    robot_control.send_comand(robot_control.stop_all)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()

    window.setWindowTitle("Motor Controller")
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())