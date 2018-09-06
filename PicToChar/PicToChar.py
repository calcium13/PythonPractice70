#coding=utf-8
'''
Created on 2018��9��5��

@author: zh
'''

from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha=255):
    if(alpha==0):
        return ''
    length = len(ascii_char)
    gray = int(r*0.298 + g*0.586 + b*0.112)
    unit = 255.0/length
    return ascii_char[int(gray/unit)]


if __name__=='__main__':
    img=Image.open('sheep.png', 'r')
    (height,width)=img.size
    print(*(height,width))
    #img=img.resize((int(height/10),int(width/10)))
    (height,width)=img.size
    text=''
    print((height,width))
    for i in range(height):
        for j in range(width):
            text+=get_char(*img.getpixel((j,i)))
        text+='\n'
    file=open('output.txt','w')
    file.write(text)
    file.flush
    file.close
    print(text)