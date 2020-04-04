import serial
ser_port = serial.Serial("COM4", 1200, timeout=0, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO)

from collections import namedtuple

ControlChanel = namedtuple("ControlChanel", ["cw_rotation", "ccw_rotation", 
                                            "cw_rotation_fast", "ccw_rotation_fast"])

stop_all = b'\xAA'

chanel_1 = ControlChanel(cw_rotation=b"\xFF", 
                        ccw_rotation=b"\xBE",
                        cw_rotation_fast=b'\xBE',
                        ccw_rotation_fast=b"\xBA")

chanel_2 = ControlChanel(cw_rotation=b"\xFF", 
                        ccw_rotation=b"\xBE",
                        cw_rotation_fast=b'\xBE',
                        ccw_rotation_fast=b"\xBA")

chanel_3 = ControlChanel(cw_rotation=b"\xFF", 
                        ccw_rotation=b"\xBE",
                        cw_rotation_fast=b'\xBE',
                        ccw_rotation_fast=b"\xBA")

chanel_4 = ControlChanel(cw_rotation=b"\xFF", 
                        ccw_rotation=b"\xBE",
                        cw_rotation_fast=b'\xBE',
                        ccw_rotation_fast=b"\xBA")

chanel_5 = ControlChanel(cw_rotation=b"\xFF", 
                        ccw_rotation=b"\xBE",
                        cw_rotation_fast=b'\xBE',
                        ccw_rotation_fast=b"\xBA")

chanel_6 = ControlChanel(cw_rotation=b"\xFF", 
                        ccw_rotation=b"\xBE",
                        cw_rotation_fast=b'\xBE',
                        ccw_rotation_fast=b"\xBA")

def send_comand(comand):
    ser_port.write(comand)


 