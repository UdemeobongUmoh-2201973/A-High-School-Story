import pygame
pygame.init()

from gui import *
from variables import *
from objects import *


SCREEN_SIZE = (800,600)
FPS = 30
BG = (255, 255, 0)
Screen_Surface = pygame.display.set_mode(SCREEN_SIZE,pygame.RESIZABLE,32)
pygame.display.set_caption("A High School Story")

Clock = pygame.time.Clock()

class FullGameObject(object):
    def __init__(self,scr):
        self.screen = scr
        
        self.app = True
        self.current_scene = "home"

        self.audio_on = True
        self.audio_volume = 100

        self.sound_on = True
        self.sound_volume = 100

        self.protagonist = Character("Sam","Student","male","#001")

        self.scenes_dict = {
            "home": lambda:self.home_scene(),
            "select_mode":lambda:self.select_mode(),

            "select_story":lambda:self.select_story(),

            "select_gender": lambda:self.select_gender_scene(),
            "select_avatar": lambda:self.character_select_scene(),
            "enter_name": lambda:self.enter_name_scene(),
            "profile_created": lambda:self.profile_created(),
            
            "phone": lambda:self.phone_scene()
        }

        self.scene_method = lambda:self.home_scene()

        while self.app:
            self.scene_changer()


    def home_scene(self):

        PlayButton = HoverButton(self.screen,"DEMO",(0,0,0),(400,300),(150,150),50,(0,25,135))
        
        while self.app and self.current_scene == "home":
            self.screen.fill((155,0,29))
            PlayButton.draw()

            pygame.display.update()
            Clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.current_scene = "select_gender"

                    if event.key == pygame.K_BACKSPACE:
                        self.current_scene = "select_gender"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if PlayButton.clicked == True:
                        self.current_scene = "select_mode"


    def select_mode(self):
        self.current_scene = "select_mode"

        StoryModeButton = HoverButton(self.screen,"STORY MODE",(0,0,0),(200,255),(100,100),25,(234,25,134))
        FreeModeButton = HoverButton(self.screen,"FREE MODE",(0,0,0),(500,255),(100,100),25,(234,25,134))
        
        while self.app and self.current_scene == "select_mode":
            self.screen.fill((255,25,0))
            StoryModeButton.draw()
            FreeModeButton.draw()

            pygame.display.update()
            Clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if StoryModeButton.clicked == True:
                        self.current_scene = "select_story"
                    if FreeModeButton.clicked == True:
                        self.current_scene = "select_gender"

        pass


    def select_gender_scene(self):
        self.current_scene = "select_gender"

        MaleButton = ImageButton(self.screen,"male.png",(200,200),(100,100))
        FemaleButton = ImageButton(self.screen,"female.png",(600,200),(100,100))

        while self.app and self.current_scene == "select_gender":
            self.screen.fill((255,25,0))
            MaleButton.draw()
            FemaleButton.draw()

            pygame.display.update()
            Clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MaleButton.check_clicked() == True:
                        self.protagonist.gender = "male"
                        self.current_scene = "select_avatar"
                    elif FemaleButton.check_clicked() == True:
                        self.protagonist.gender = "female"
                        self.current_scene = "select_avatar"


    def character_select_scene(self):
        self.current_scene = "select_avatar"

        Images = []

        current_index = 0

        for i in range(5):
            i = (current_index+i+5)%5
            img_path = f"res/images/characters/{self.protagonist.gender}/#00{i+1}/normal.png"
            Images.append(Image(self.screen,img_path,(130*(i+1)+25,300),(90,120)))

            if i == 2:
                Images[i].size = (180,240)
                Images[i].border_colour = (0,0,0)
                Images[i].border_thickness = 3

        
        SelectButton = HoverButton(self.screen,"SELECT",(0,0,0),(400,550),(100,50),20,(0,19,125))


        while self.app and self.current_scene == "select_avatar":
            
            self.screen.fill((155,0,29))
            drawCenteredText(self.screen,"Select your character",(400,100),"arialblack",50,(0,0,0))

            for image in Images:
                image.draw()

            SelectButton.draw()

            pygame.display.update()
            Clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.current_scene = "enter_name"

                    if event.key == pygame.K_BACKSPACE:
                        self.current_scene = "select_gender"

                    if event.key == pygame.K_LEFT:
                        current_index -= 1
                        print(current_index)
                        
                    if event.key == pygame.K_RIGHT:
                        current_index += 1
                        print(current_index)
                


    def enter_name_scene(self):
        self.current_scene = "enter_name"

        self.protagonist.image_id = "#003"

        self.screen.fill((255,255,255))

        img_path = f"res/images/characters/{self.protagonist.gender}/{self.protagonist.image_id}/normal.png"
        CharacterImg = Image(self.screen,img_path,(250,SCREEN_SIZE[1]//2),(270,360))

        OkayButton = HoverButton(self.screen,"OKAY",(0,0,0),(400,525),(100,50),20,(25,133,90))

        TextBox1 = TextBox(self.screen,(600,300),(300,100),"consolas",60,(0,0,0),((255,255,0)))

        while self.app and self.current_scene == "enter_name":

            self.screen.fill((255,255,255))
            CharacterImg.draw()
            TextBox1.draw()

            OkayButton.draw()

            drawCenteredText(self.screen,"Enter your name",(600,150),"arialbold",50,(0,0,0))

            pygame.display.update()
            Clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    TextBox1.key_input(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if OkayButton.clicked == True:
                        self.current_scene = "phone"


    def profile_created(self):
        self.current_scene = "profile_created"

        print("New profile created!")
        print(f"Name: {self.protagonist.name}")
        print(f"Gender: {self.protagonist.gender.capitalize()}")
        print(f"Image ID used: {self.protagonist.image_id}")
        print(f"Class: Class A2")


    def phone_scene(self):
        self.current_scene = "phone"

        MapIcon = ImageButton(self.screen,"res/images/icons/map.png",(200,200),(100,100))
        MessagesIcon = ImageButton(self.screen,"res/images/icons/messages.png",(200,300),(100,100))
        TasksIcon = ImageButton(self.screen,"res/images/icons/tasks.png",(300,200),(100,100))
        ProfileIcon = ImageButton(self.screen,"res/images/icons/profile.png",(300,300),(100,100))
        CalendarIcon = ImageButton(self.screen,"res/images/icons/calendar.png",(400,300),(100,100))
        NewsIcon = ImageButton(self.screen,"res/images/icons/news.png",(400,200),(100,100))

        while self.app and self.current_scene == "phone":
            self.screen.fill((0,0,0,0.75))
            pygame.draw.rect(self.screen,(0,12,0,0.5),[0,0,800,500],border_radius=25)
            pygame.draw.rect(self.screen,(25,123,90),[200,50,400,500],border_radius=25)
            pygame.draw.rect(self.screen,(255,123,190),[210,60,380,480],border_radius=15)
            pass

            drawCenteredText(self.screen,"Apps",(400,125),"arial",25,(0,0,0))

            MapIcon.draw()
            MessagesIcon.draw()
            TasksIcon.draw()
            ProfileIcon.draw()
            CalendarIcon.draw()
            NewsIcon.draw()

            pygame.display.update()
            Clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app = False
                    pygame.quit()


    def select_story(self):
        self.current_scene = "select_story"

        StoryButtons = [
            HoverButton(self.screen,"To Date or Not to Date",(0,0,0),(400,300),(300,75),25,(125,75,0)),
            HoverButton(self.screen,"The Election",(0,0,0),(400,400),(300,75),25,(125,75,0)),
            HoverButton(self.screen,"Confronting your fears",(0,0,0),(400,500),(300,75),25,(125,75,0))
        ]

        while self.app and self.current_scene == "select_story":
            self.screen.fill((25,235,124))
            
            drawCenteredText(self.screen,"Choose your story",(400,100),"arialblack",25,(0,0,0))
            
            for story_button in StoryButtons:
                story_button.draw()

            pygame.display.update()
            Clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app = False



    def scene_changer(self):

        if self.current_scene in self.scenes_dict.keys():
            self.scene_method = self.scenes_dict[self.current_scene]
        else:
            pygame.quit()
            quit()

        self.scene_method()

FullGameObject1 = FullGameObject(Screen_Surface)