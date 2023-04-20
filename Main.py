#import
import sys 
import pygame as pg
#import

#class
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,color=(0,0,0)):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = color # Color
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, color=(0,0,0)):
        Rectangle.__init__(self, x, y, w, h, color)
    
    def isMouseOn(self):
        mousex,mousey = pg.mouse.get_pos()
        if mousex >= self.x and mousey >= self.y and mousex <= self.x+self.w and mousey <= self.y+self.h:
            # print("True")
            return True
        else : 
            # print("False")
            return False
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2) 
#class

#set up
pg.init()
run = True
pg.key.set_repeat(500)
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
firstObject = Rectangle(20,20,100,100,(100,20,30)) # สร้าง Object จากคลาส Rectangle ขึ้นมา
btn = Button(20,20,100,100,(255,0,0)) # สร้าง Object จากคลาส Button ขึ้นมา
COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font('C:\WINDOWS\FONTS\IMPACT.ttf', 16)
#set up

#exercise 1
# while(run):
#     screen.fill((255, 255, 255))
#     # firstObject.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด
#     if btn.isMouseOn():
#         if pg.mouse.get_pressed()[0] :
#             btn.color = (153,51,255)
#         else :
#             btn.color = (85,85,85)
#     else:
#         btn.color = (255,0,0)
#     btn.draw(screen)
#     pg.display.update()
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             run = False
#exercise 1

#exercise 2
# while(run):
#     screen.fill((255, 255, 255))
#     firstObject.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด
#     pg.display.update()
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             run = False
#         if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกปล่อยและเป็นปุ่ม W
#             print("Key W down")
#             firstObject.y -= 1
#         if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
#             print("Key A down")
#             firstObject.x -= 1
#         if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม S
#             print("Key S down")
#             firstObject.y += 1
#         if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
#             print("Key D down")
#             firstObject.x += 1
#exercise 2

#exercise 3
name_box = InputBox(100, 100, 140, 32) # สร้าง InputBox1
surname_box = InputBox(500, 100, 140, 32) # สร้าง InputBox2
ages_box = InputBox(305, 250, 140, 32) # สร้าง InputBox3
submit_box_text = "                       SUBMIT"
submit_box = InputBox(305, 300, 140, 32, submit_box_text)
input_boxes = [name_box, surname_box, ages_box, submit_box] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
submit = FONT.render('Hello ' + str(name_box.text) + str(surname_box.text) +'! You are ' + str(ages_box.text) + ' years old.', True, (0,0,0)) # (text,is smooth?,letter color,background color)
submitRect = submit.get_rect() # text size
submitRect.center = (win_x//2, 400)
submiterror = FONT.render('Please enter your correct information', True, (0,0,0)) # (text,is smooth?,letter color,background color)
submiterrorRect = submiterror.get_rect() # text size
submiterrorRect.center = (win_x//2, 400) # text size
ageserror = FONT.render('Please enter your ages with 0-9', True, (0,0,0))
ageserrorRect = ageserror.get_rect()
ageserrorRect.center = (400, 230)
nameerror = FONT.render('Please enter your name or surname with alphabetic characters', True, (0,0,0))
nameerrorRect = ageserror.get_rect()
nameerrorRect.center = (400, 230)

name = FONT.render('Name', True, (0,0,0))
nameRect = ageserror.get_rect()
nameRect.center = (150, 116)
surname = FONT.render('Surname', True, (0,0,0))
surnameRect = ageserror.get_rect()
surnameRect.center = (530, 116)
ages = FONT.render('Ages', True, (0,0,0))
agesRect = ageserror.get_rect()
agesRect.center = (360, 266)
while(run):
    screen.fill((255, 255, 255))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    screen.blit(name, nameRect)
    screen.blit(surname, surnameRect)
    screen.blit(ages, agesRect)
    if submit_box.active :
        if name_box.text != '' and surname_box.text != '' and ages_box.text != '' :
            submit = FONT.render('Hello ' + str(name_box.text) + ' ' + str(surname_box.text) +'! You are ' + str(ages_box.text) + ' years old.', True, (0,0,0))
            screen.blit(submit, submitRect)
        else :
            screen.blit(submiterror, submiterrorRect)
    if name_box.active or surname_box.active :
        if name_box.text.isdigit() == True or surname_box.text.isdigit() == True :
            screen.blit(nameerror, nameerrorRect)
    if ages_box.active :
        if ages_box.text.isdigit() == False:
            screen.blit(ageserror, ageserrorRect)
    pg.time.delay(1)
    pg.display.update()
#exercise 3