"""Render the current rover data flow; historical tldraw files are preserved."""
from pathlib import Path
from io import BytesIO
import base64
import re
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
source = (ROOT / 'tldraw-current-pi-render.svg').read_text()
font_bytes = base64.b64decode(re.search(r'data:font/ttf;base64,([A-Za-z0-9+/=]+)', source).group(1))
font = ImageFont.truetype(BytesIO(font_bytes), 26)
small = ImageFont.truetype(BytesIO(font_bytes), 21)
title = ImageFont.truetype(BytesIO(font_bytes), 48)
im = Image.new('RGB', (1600, 1120), '#f8fafc')
draw = ImageDraw.Draw(im)
draw.text((55, 35), 'EXPLORATION ROVER', font=title, fill='#173b50')
draw.text((55, 100), 'Current proposal: planar mapping, image capture, advisory AI', font=small, fill='#506576')

def box(x, y, w, h, lines, color='#dceefa'):
    draw.rounded_rectangle((x,y,x+w,y+h), 15, fill=color, outline='#315b73', width=3)
    for n, line in enumerate(lines):
        draw.text((x+w/2,y+25+n*43), line, font=font, fill='#173b50', anchor='mt')

def arrow(a,b,both=False,label='',label_xy=None):
    draw.line((a,b),fill='#42647b',width=3)
    def tip(x,y):
        angle=math.atan2(y[1]-x[1],y[0]-x[0])
        draw.polygon([y,(y[0]-17*math.cos(angle-.4),y[1]-17*math.sin(angle-.4)),(y[0]-17*math.cos(angle+.4),y[1]-17*math.sin(angle+.4))],fill='#42647b')
    tip(a,b)
    if both:tip(b,a)
    if label:draw.text(label_xy,label,font=small,fill='#315b73')

box(45,185,400,225,['Left / Right ToF','Encoders + IMU','2 bumpers / 4 edge sensors'])
box(590,185,420,225,['Motion ESP','Wheel control + feedback','Local stop / timeout'], '#ffead8')
box(1185,185,365,225,['Motor driver','2 encoder motors'], '#ffead8')
box(45,510,400,155,['2D LiDAR','Planar range scans'])
box(590,510,420,215,['Raspberry Pi','Pose, map, navigation','Events + web backend'], '#e0f4ee')
box(1185,510,365,155,['ESP CAM S3','Image capture'])
box(45,825,400,135,['Phone / laptop browser','Map, images, controls'])
box(1185,825,365,135,['Home PC','Clef-Flash Q8_0'], '#e0f4ee')
arrow((445,295),(590,295),label='I2C / GPIO',label_xy=(453,258))
arrow((1010,295),(1185,295),label='Drive signals',label_xy=(1018,253))
arrow((800,410),(800,510),True,'UART / USB',(820,445))
arrow((445,585),(590,585),False,'USB',(485,548))
arrow((1185,585),(1010,585),True,'WiFi',(1050,548))
arrow((445,885),(640,725),True,'WiFi / WebSocket',(450,795))
arrow((960,725),(1185,885),True,'Authenticated HTTPS',(1000,745))
draw.text((1070,920),'Advisory scores',font=small,fill='#315b73',anchor='mm')
box(45,1010,1505,80,['Power: battery + protection + regulated supplies'], '#f8eee0')
im.save(ROOT / 'current-proposal-block-diagram.png')
print(ROOT / 'current-proposal-block-diagram.png')
