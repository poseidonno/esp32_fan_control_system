from machine import Pin, I2C

# OLED=......
i2c = I2C(scl=Pin(22), sda=Pin(21))
from OLED_SSD1306 import SSD1306_I2C

OLED = SSD1306_I2C(128, 64, i2c)

# fonts=......
fonts = {
    0xE6B8A9:
        [0x00,0x00,0x60,0x33,0x12,0x03,0x62,0x33,0x10,0x07,0x15,0x35,0x25,0x6F,0x20,0x00,
         0x00,0x00,0x00,0xF0,0x10,0xF0,0x10,0xF0,0x00,0xF8,0x28,0x28,0x28,0xFC,0x00,0x00],  # 温,

    0xE6B9BF:
        [0x00,0x00,0x60,0x33,0x1A,0x43,0x62,0x33,0x10,0x06,0x03,0x19,0x38,0x60,0x67,0x00,
         0x00,0x00,0x00,0xF8,0x08,0xF8,0x08,0xF8,0xA0,0xAC,0xB8,0xB0,0xA0,0xA0,0xFE,0x00],  # 湿

    0xE5BAA6:
        [0x01,0x00,0x0F,0x09,0x09,0x0B,0x09,0x09,0x08,0x0B,0x0A,0x11,0x10,0x21,0x23,0x00,
         0x00,0x80,0xF8,0x20,0x20,0xF0,0x20,0xE0,0x00,0xF0,0x10,0xA0,0x40,0xB0,0x18,0x00],  # 度
    0xE99BB6:
        [0x00,0x00,0x07,0x08,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x08,0x07,0x00,
         0x00,0x00,0xE0,0x10,0x08,0x08,0x08,0x08,0x08,0x08,0x08,0x08,0x08,0x10,0xE0,0x00],#0
    
     0xE4B880:
        [0x00,0x00,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x00,0x00,
         0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],#1
    
    0xE4BA8C:
        [0x00,0x00,0x07,0x08,0x10,0x00,0x00,0x00,0x00,0x03,0x04,0x08,0x10,0x1F,0x00,0x00,
         0x00,0x00,0xC0,0x20,0x20,0x20,0x20,0x40,0x80,0x00,0x00,0x00,0x00,0xF0,0x00,0x00],#2
    0xE4B889:
        [0x00,0x00,0x0F,0x00,0x00,0x00,0x00,0x0F,0x00,0x00,0x00,0x00,0x00,0x0F,0x00,0x00,
         0x00,0x00,0xC0,0x20,0x20,0x20,0x20,0xE0,0x20,0x20,0x20,0x20,0x20,0xC0,0x00,0x00],#3
    
    0xE59B9B:
        [0x00,0x00,0x08,0x08,0x08,0x08,0x10,0x10,0x10,0x1F,0x00,0x00,0x00,0x00,0x00,0x00,
         0x00,0x00,0x40,0x40,0x40,0x40,0x40,0x40,0x40,0xF0,0x40,0x40,0x40,0x40,0x00,0x00],#4
    0xE4BA94:
        [0x00,0x00,0x0F,0x08,0x08,0x08,0x08,0x0F,0x00,0x00,0x00,0x00,0x00,0x0F,0x00,0x00,
         0x00,0x00,0xE0,0x00,0x00,0x00,0x00,0xE0,0x20,0x20,0x20,0x20,0x20,0xE0,0x00,0x00],#5
    0xE585AD:
        [0x00,0x00,0x0F,0x10,0x10,0x10,0x10,0x10,0x1F,0x10,0x10,0x10,0x10,0x0F,0x00,0x00,
         0x00,0x00,0xC0,0x00,0x00,0x00,0x00,0x00,0xC0,0x20,0x20,0x20,0x20,0xC0,0x00,0x00],#6
    0xE4B883:
        [0x00,0x00,0x0F,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
         0x00,0x00,0xF0,0x10,0x30,0x20,0x20,0x40,0x40,0x40,0x40,0x40,0x40,0x40,0x00,0x00],#7
    0xE585AB:
        [0x00,0x07,0x08,0x08,0x08,0x08,0x08,0x07,0x08,0x08,0x08,0x08,0x08,0x07,0x00,0x00,
         0x00,0xF0,0x08,0x08,0x08,0x08,0x08,0xF0,0x08,0x08,0x08,0x08,0x08,0xF0,0x00,0x00],#8
    0xE4B99D:
        [0x00,0x07,0x08,0x08,0x08,0x08,0x08,0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
         0x00,0xE0,0x10,0x10,0x10,0x10,0x10,0xF0,0x10,0x10,0x10,0x10,0x10,0x10,0x00,0x00]#9

}


def switch_case(value):
    switcher = {
        0: "零",
        1: "一",
        2: "二",
        3:"三",
        4:"四",
        5:"五",
        6:"六",
        7:"七",
        8:"八",
        9:"九",
    }
    return switcher.get(value, 'wrong value')

def getchinese_num(num):
    try:
        return switch_case(int(num[0]))+switch_case(int(num[1]))
    except:
        return switch_case(int(num[0]))

# 函数部分
def chinese(ch_str, x_axis, y_axis):
    offset_ = 0
    for k in ch_str:
        code = 0x00  # 将中文转成16进制编码
        data_code = k.encode("utf-8")
        code |= data_code[0] << 16
        code |= data_code[1] << 8
        code |= data_code[2]
        byte_data = fonts[code]
        for y in range(0, 16):
            a_ = bin(byte_data[y]).replace('0b', '')
            while len(a_) < 8:
                a_ = '0' + a_
            b_ = bin(byte_data[y + 16]).replace('0b', '')
            while len(b_) < 8:
                b_ = '0' + b_
            for x in range(0, 8):
                OLED.pixel(x_axis + offset_ + x, y + y_axis, int(a_[x]))
                OLED.pixel(x_axis + offset_ + x + 8, y + y_axis, int(b_[x]))
        offset_ += 16




