#my program of sap travelling
#all completed except the score part
import pygame
import time
import random

pygame.init()

hight=400# dimentions of window
width=400

dis=pygame.display.set_mode((width,hight))
pygame.display.update()
pygame.display.set_caption("WElcome to Saap gamE")

#colors defined 
white = (255, 255, 255)#colors needed
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (170, 1, 20)
green = (0, 255, 0)
darkgreen=(85,107 ,47)
orange=(255,165,0)
lime_green=(50,205,50)
blue = (50, 153, 213)
dark_grey=(169,169,169)
royalblue=(65,105,225)
darkblue=(0,0,139)
darkslategrey=(47,79,79)
#
grid_color=darkslategrey
background_color=black
message_color=green
fruit_color=darkblue
#
clock=pygame.time.Clock()

#assumed saneke size and speed
snake_size=10
snake_speed=10
#
score=0# initial score is zero
tt1=5
#
font_style = pygame.font.SysFont(None,30)
score_style = pygame.font.SysFont("comicsansms",20)# the fonts is named

def snake(snake_size,snake_list):#snake dsiplaying function, sanke color taken as white
    for i in snake_list:
        pygame.draw.rect(dis,green,[i[0],i[1],snake_size,snake_size])
        pygame.draw.rect(dis,lime_green,[i[0]+4,i[1]+4,snake_size-5,snake_size-5])
def  scoreplus():
    score+=1

def grid():                
    for i in range(0,width,10):
        pygame.draw.lines(dis,grid_color, False, [(i,0),(i,hight)], 1)
    for i in range(0,hight,10):
        pygame.draw.lines(dis,grid_color, False, [(0,i),(width,i)], 1)

def message(msg,tt1,message_color):# msg to display function :will be used to displey msg in game
    mesg = font_style.render(msg, True,message_color)
    dis.blit(mesg,[width/5,hight/tt1])   
   
    

def fruit(f_x,f_y,fruit_color):#displaying the fruit
    for j in range(7,2,-1):
        if j%2:
            pygame.draw.circle(dis,yellow,[int(f_x)+5,int(f_y)+5],j,0)
        else:
            pygame.draw.circle(dis,orange,[int(f_x)+5,int(f_y)+5],j,0)    

def game_loop():#greating a game function loop
    game_over=False
    game_close=False
    tt1=5
    score=0
    
    s_x=width/2 #initial x coordinate positionof snake
    s_y=hight/2 #initial y coordinate positionof snake


    x=0#variables used to store change
    y=0
    
    snake_List = []
    Length_of_snake = 1
        
    f_x=round(random.randrange(0,width - snake_size)/10.0)*10.0 #random gneration of coordinates for food 
    f_y=round(random.randrange(0,hight - snake_size)/10.0)*10.0
    
    dis.fill(white)
    pygame.display.update()
    
    
    while not game_over:
        
    
        while game_close==True:# game exit continue part
   
            message("Q->Quit ",3,message_color)
            message("P-> play again",2,message_color)
            pygame.display.update()
       
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_p:
                        game_loop()
        
        for event in pygame.event.get(): #game movemnt part
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x=-snake_size
                    y=0
                elif event.key==pygame.K_RIGHT:
                    x=snake_size
                    y=0
                elif event.key==pygame.K_UP:
                    x=0
                    y=-snake_size
                elif event.key==pygame.K_DOWN:
                    x=0
                    y=snake_size
     
        if s_x>=width or s_x<0 or s_y >=hight or s_y < 0:# snake head within boundary check part
            game_close = True
        
        s_x+=x# change updated
        s_y+=y#chnge updated
    
        dis.fill(background_color)   #black background
        grid()
        fruit(f_x,f_y,fruit_color)#fruit display , fruit color red
        
        snake_head=[]# empty list taken to store coordinates of head of snake
        snake_head.append(s_x)
        snake_head.append(s_y)
        snake_List.append(snake_head) #adding new bloack to the snake body
        if len(snake_List)>Length_of_snake:
            del snake_List[0]#deleting the excess last bit after snake moves forward
        
        for i in snake_List[:-1]:#checking if the snake block oberlaps itself, is the snake bit itself
            if i ==snake_head:
                game_close=True
        
        snake(snake_size,snake_List)
        
             
        pygame.display.update()
        
        if s_x==f_x and s_y==f_y: #incresing the length of snake everytime it gets a fruit,also generation of next fruit
            f_x=round(random.randrange(0,width - snake_size)/10.0)*10.0 #random gneration of coordinates for food 
            f_y=round(random.randrange(0,hight - snake_size)/10.0)*10.0
            Length_of_snake+=3#increases the length by the number
            
        clock.tick(snake_speed)

   
    pygame.quit()
    #message(score,1,message_color)3 TO BE EDITED
    quit()

game_loop()
