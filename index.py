from tkinter import CENTER
import pygame
from sys import exit

#init and screen definiton
pygame.init()
info = pygame.display.Info()
SIZE = WIDTH, HEIGHT = info.current_w, info.current_h
print(WIDTH, HEIGHT)
mainsurface = pygame.display.set_mode(SIZE)
screen = pygame.Surface((800, 600))

pygame.display.set_caption("Gme")
clock = pygame.time.Clock()

#rect stuff
x_val = 300
y_val = 300
floor_surf = pygame.image.load('map/floor.png')
floor_rect = floor_surf.get_rect(midleft = (x_val,y_val))
#screen.blit(floor_surf,floor_rect)

#floor_rect = floor_surf.get_rect(midleft = (0,0))
#screen.blit(floor_surf,floor_rect)


#Trying to create a tile map
lst_to_str = ""
with open('map/Map_Floor.txt') as f:#opens a txt file
    lines = f.readlines()#reads
    #lines = lines.join()
    #print(lines)
    x = 0
    for items in lines:#this turnes the original data into a string that can be parsed easily
        lst_to_str += items#this turnes the original data into a string that can be parsed easily

        str_to_lst = lst_to_str.split(",")#parses string at the "," to create individual elements
        #print(str_to_lst)
        
        for position in str_to_lst:#idderates though the new list. If the value of the item in the string is 0 then it will try to blit a surface
            x_val += 32

            #print(position)
            if position == '0':
                
                        
                #floor_rect = floor_surf.get_rect(midright = (x_val,y_val))        
                mainsurface.blit(floor_surf,(x_val,y_val))
                #print("full")
                pygame.display.update()
                

            elif position == '\n':#if it is /n then it will do down by 1 tile
                y_val += 32
                #print("New line")

            elif position == "-1":#if it is -1 it will skip the tile
                print("skipping")
                #print("empty")



    

#print("Out of function")

 



while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                print("quitting")
                pygame.quit()
                exit()

    #mainsurface.blit(floor_surf,floor_rect)
        
    



    pygame.display.update()
    clock.tick(60)
