print("snake game")
#my program of sap travelling
#all completed except the score part
import pygame
import time
import random

pygame.init()

hight=400# dimentions of window
width=600

dis=pygame.display.set_mode((width,hight))
pygame.display.update()
pygame.display.set_caption("WElcome to Saap gamE")

#colors defined
white = (255, 255, 255)#colors needed
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


clock=pygame.time.Clock()

#assumed saneke size and speed
snake_size=10
snake_speed=10

font_style = pygame.font.SysFont(None,30)
score_style = pygame.font.SysFont("comicsansms",20)# the fonts is named

def snake(snake_size,snake_list):#snake dsiplaying function, sanke color taken as white
    for i in snake_list:
        pygame.draw.rect(dis,green,[i[0],i[1],snake_size,snake_size])

def message(msg,color):# msg to display function :will be used to displey msg in game
    mesg = font_style.render(msg, True,red)
    dis.blit(mesg,[width/5,hight/3])

def game_loop():    #greating a game function loop
    game_over=False
    game_close=False

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

            message("Press Q to quit or Press P to play again......",red)
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

        dis.fill(black)   #black background
        pygame.draw.rect(dis,red,[f_x,f_y,10,10])#fruit display , fruit color red

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
    quit()

game_loop()
