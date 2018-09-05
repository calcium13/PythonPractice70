#coding=utf-8
'''
Created on 2018��9��5��

@author: zh
'''

from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b):
    length = len(ascii_char)
    gray = int(r*0.299 + g*0.587 + b*0.114)
    unit = 256.0/length
    return ascii_char[int(gray/unit)]


if __name__=='__main__':
    img=Image.open('ascii_dora.png', 'r')
    (height,width)=img.size
    