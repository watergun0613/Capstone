################################ 라이브러리 설정 ################################
#-*- coding: utf-8 -*-
import cv2
import tkinter
from PIL import Image, ImageTk
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import time
import mediapipe as mp
import pyrealsense2 as rs
from dataclasses import dataclass
from pathlib import Path
import threading

# 생성한 라이브러리
# from Library import *
# from guideline import *
# from save_media import *


################################ 전역 변수 설정 ################################
GUIDELINE = cv2.imread('C:/lab/Demo/image/GuideLine.png')
FACE_GUIDELINE = cv2.imread('C:/lab/Demo/image/face_guideline_head.png')
WIDTH = 640
HEIGHT = 480
COUNTOUT = 60
N_SECONDS = 2

#카메라 설정 부분
PIPELINE = rs.pipeline()
CONFIG = rs.config()
CONFIG.enable_stream(rs.stream.color, WIDTH, HEIGHT, rs.format.bgr8, 30)    #컬러
CONFIG.enable_stream(rs.stream.depth, WIDTH, HEIGHT, rs.format.z16, 30)     #깊이
ALIGN_TO = rs.stream.depth
ALIGN = rs.align(ALIGN_TO)
lock = threading.Lock()

#컬러
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

#폰트 로드
FONTPATH = 'F:/backup/Project/CapStone/code/Demo/NanumGothicBold.ttf'
FONT = ImageFont.truetype(FONTPATH,20)

@dataclass
class Str:
    guide:str = " "

class Int:
    guide:int = 0
    
class Pos:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

L_SHOULDER = Pos()
R_SHOULDER = Pos()
L_EAR = Pos()
R_EAR = Pos()
NOSE = Pos()
L_CHIN = Pos()
R_CHIN = Pos()
L_FORHEAD = Pos()
R_FORHEAD = Pos()

SUM_LS = Pos()
SUM_RS = Pos()

STR = Str()
R_TEXT = Str()
R_TY_TEXT = Str()


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
mp_holistic = mp.solutions.holistic
mp_face_mesh = mp.solutions.face_mesh
