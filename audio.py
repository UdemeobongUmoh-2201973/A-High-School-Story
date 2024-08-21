import pygame

from gui import *
from variables import *

pygame.mixer.init()
pygame.mixer.music.load("demo.mp3")

pygame.mixer.music.set_volume(0.1)


Screen_Surface = pygame.display.set_mode((800,600),0,32)
app = True

def display_conversation(scr,location,response_dict):
    #background, covering_rect, character,name,text/choices,phone,pause
    scr.fill((25,55,255))

    Backgrnd = pygame.transform.scale(pygame.image.load(location_backgrounds[location]),(800,350))
    scr.blit(Backgrnd,(0,0))

    pygame.draw.rect(scr,(190,90,9),[0,350,800,500])
    Img = pygame.transform.scale(pygame.image.load("res/char5.png"),(250,250))
    scr.blit(Img,(0,100))
    drawCenteredText(scr,response_dict["character"].upper()+":",(125,375),"arialblack",35,(0,0,0))

    pygame.draw.rect(scr,(0,90,19),[250,375,525,200],border_radius=25)
    pygame.draw.rect(scr,(110,190,19),[250,550,525,25],border_bottom_left_radius=50,border_bottom_right_radius=50)
    drawCenteredText(scr,"Press Enter to continue",(512,562),"consolas",15,(0,0,0))

    ResponseTxt = MultilineWidthText(scr,response_dict["response"],500,(520,385),"consolas",25)
    ResponseTxt.draw()

def display_choices(scr,backgrnd,response_dict):
    scr.fill((25,55,255))
    pygame.draw.rect(scr,(190,90,9),[0,350,800,500])
    Img = pygame.transform.scale(pygame.image.load("res/char5.png"),(250,250))
    scr.blit(Img,(0,100))
    

    ResponseTxt = MultilineWidthText(scr,"Make your choice!",500,(520,385),"consolas",25)
    ResponseTxt.draw()

demoData = {
    "type":"response",
    "character":"Marcus",
    "emotion":"normal",
    "response":"Hi. My name is Marcus. I'll be your tour guide throughout the day. You can choose which option to say, for instance. Sounds good?"
}

while app:
    
    display_conversation(Screen_Surface,"hallway",demoData)

    pygame.display.update()
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app = False
            pygame.mixer.music.stop()
            pygame.quit()

