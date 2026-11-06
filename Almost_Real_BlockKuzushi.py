from machine import Pin, I2C, ADC, PWM
import machine
import ssd1306
import time

i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

button = Pin(14, Pin.IN, pull=Pin.PULL_UP)

buzzer = PWM(Pin(18))

button  = Pin(15, Pin.IN, pull=Pin.PULL_UP)
button1 = Pin(14, Pin.IN, pull=Pin.PULL_UP)

j = 0

x = 50
y = 50
width = 5
height = 5
dx = 2
dy = 2
a=0
hit_miss=0
a1=1
a2=1
a3=1
a4=1
a5=1
yblock=0
b1=1
b2=1
b3=1
b4=1
b5=1

c1=1
c2=1
c3=1
c4=1
c5=1

while True:
    
    oled.fill(0)
    
    oled.fill_rect(0,0,24,5,c1)
    oled.fill_rect(26,0,24,5,c2)
    oled.fill_rect(52,0,24,5,c3)
    oled.fill_rect(78,0,24,5,c4)
    oled.fill_rect(104,0,24,5,c5)
    
    oled.fill_rect(0,8,24,5,b1)
    oled.fill_rect(26,8,24,5,b2)
    oled.fill_rect(52,8,24,5,b3)
    oled.fill_rect(78,8,24,5,b4)
    oled.fill_rect(104,8,24,5,b5)
    
    oled.fill_rect(0,16,24,5,a1)
    oled.fill_rect(26,16,24,5,a2)
    oled.fill_rect(52,16,24,5,a3)
    oled.fill_rect(78,16,24,5,a4)
    oled.fill_rect(104,16,24,5,a5)
    
    if hit_miss==0:
        #oled.text("miss",50,50)
        oled.text("Let`s Start!",10,40)
        
    state = button.value()
    
    if state == 0:
        j=j+8
    if j>=56:
        j=56
 
    state1 = button1.value()
    
    if state1 == 0:
        j=j-8
    if j<=-48:
        j=-48
        
    oled.fill_rect(50+j,60,24,5,1) #bar
    
    x += dx
    y += dy
    
    if x <= 0 or x + width >= 128:
        dx = -dx
    if y <= 20-5*yblock or y+ height >= 62:
        dy = -dy
        
    oled.fill_rect(x, y, width, height, 1) #ball
    
    oled.text(str(x),30,30)
    oled.text(str(y),70,30)
    oled.text(str(yblock),0,25)
        
    if yblock==0:
        oled.text(str(a1),90,30)
        oled.text(str(a2),98,30)
        oled.text(str(a3),106,30)
        oled.text(str(a4),114,30)
        oled.text(str(a5),122,30)
    if yblock==1:
        oled.text(str(b1),90,30)
        oled.text(str(b2),98,30)
        oled.text(str(b3),106,30)
        oled.text(str(b4),114,30)
        oled.text(str(b5),122,30)
    if yblock==2:
        oled.text(str(c1),90,30)
        oled.text(str(c2),98,30)
        oled.text(str(c3),106,30)
        oled.text(str(c4),114,30)
        oled.text(str(c5),122,30)
    
    
    if 74+j>x>42+j and y>56:
        oled.text("hit!",50,50)
        hit_miss=1
        time.sleep(0.1)
        
    if y>55 and x<42+j:
        #oled.text("miss",50,50)
        hit_miss=0
        #oled.text("Game Over!",20,40)
        #time.sleep(1)
        x=50
        y=55
        j=0
        yblock=0
        #oled.text("Let`s Start!!!",10,40)
        time.sleep(1)
        
    if y>55 and x>74+j:
        #oled.text("miss",50,50)
        hit_miss=0
        #oled.text("Game Over!",20,40)
        #time.sleep(1)
        x=50
        y=55
        j=0
        yblock=0
        #oled.text("Let`s Start!!!",10,40)
        time.sleep(1)
        
    if hit_miss==1 and 0<x<24 and y<22:
        a1=0
    if hit_miss==1 and 26<x<50 and y<22:
        a2=0
    if hit_miss==1 and 52<x<76 and y<22:
        a3=0
    if hit_miss==1 and 78<x<102 and 17<y<22:
        a4=0
    if hit_miss==1 and 104<x<128 and 17<y<22:
        a5=0
    
    if hit_miss==1 and 0<x<24 and 12<y<17:
        b1=0
    if hit_miss==1 and 26<x<50 and 12<y<17:
        b2=0
    if hit_miss==1 and 52<x<76 and 12<y<17:
        b3=0
    if hit_miss==1 and 78<x<102 and 12<y<17:
        b4=0
    if hit_miss==1 and 104<x<128 and 12<y<17:
        b5=0
        
    if hit_miss==1 and 0<x<24 and 7<y<12:
        c1=0
    if hit_miss==1 and 26<x<50 and 7<y<12:
        c2=0
    if hit_miss==1 and 52<x<76 and 7<y<12:
        c3=0
    if hit_miss==1 and 78<x<102 and 7<y<12:
        c4=0
    if hit_miss==1 and 104<x<128 and 7<y<12:
        c5=0
        
    if a1==0 and a2==0 and a3==0 and a4==0 and a5==0:
        yblock=1
        
    if b1==0 and b2==0 and b3==0 and b4==0 and b5==0:
        yblock=2
        
    if c1==0 and c2==0 and c3==0 and c4==0 and c5==0:
       oled.text("ALL CLEAR!!!",20,40)
       time_sleep(2)
       yblock=0
       y=55
       j=0
       x=50
       #time_sleep(3.0)
       a1=1
       a2=1
       a3=1
       a4=1
       a5=1
       b1=1
       b2=1
       b3=1
       b4=1
       b5=1
       c1=1
       c2=1
       c3=1
       c4=1
       c5=1
       
    
    oled.show()
    
    time.sleep_ms(16)

