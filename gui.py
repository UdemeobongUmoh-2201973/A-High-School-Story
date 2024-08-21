import pygame
pygame.init()

AlphaKeyInputs = [
    pygame.K_a,
    pygame.K_b,
    pygame.K_c,
    pygame.K_d,
    pygame.K_e,
    pygame.K_f,
    pygame.K_g,
    pygame.K_h,
    pygame.K_i,
    pygame.K_j,
    pygame.K_k,
    pygame.K_l,
    pygame.K_m,
    pygame.K_n,
    pygame.K_o,
    pygame.K_p,
    pygame.K_q,
    pygame.K_r,
    pygame.K_s,
    pygame.K_t,
    pygame.K_u,
    pygame.K_v,
    pygame.K_w,
    pygame.K_x,
    pygame.K_y,
    pygame.K_z,
]


def drawCenteredText(scr,text,pos,font,font_size,text_colour):
    font = pygame.font.SysFont(font,font_size)
    text_surf =  font.render(text,False,text_colour)
    text_width = text_surf.get_width()
    text_height = text_surf.get_height()

    scr.blit(text_surf,(pos[0]-(text_width//2),pos[1]-(text_height//2)))

class HoverButton(object):
    def __init__(self,surf,text,text_color,center_pos,size,font_size,bg_color):
        self.surface = surf

        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.original_fontsize = self.font_size
        
        
        self.font = pygame.font.SysFont("arial",self.font_size,True)
        self.text_surface = self.font.render(self.text,False,self.text_color)
        self.text_size = [self.text_surface.get_width(),self.text_surface.get_height()]

        
        self.bg_color = bg_color

        self.center_pos = center_pos
        self.original_size = size
        self.size = self.original_size


        self.clicked = False

    def draw(self):
        Rect = pygame.draw.rect(self.surface,self.bg_color,[self.center_pos[0]-(self.size[0]//2),self.center_pos[1]-(self.size[1]//2),self.size[0],self.size[1]])

        self.font = pygame.font.SysFont("arial",self.font_size,True)
        self.text_surface = self.font.render(self.text,False,self.text_color)
        self.text_size = [self.text_surface.get_width(),self.text_surface.get_height()]

        self.surface.blit(self.text_surface,(self.center_pos[0]-(self.text_size[0]//2),self.center_pos[1]-(self.text_size[1]//2)))

        MousePos = pygame.mouse.get_pos()

        if Rect.collidepoint(MousePos):
            self.hover()
            self.clicked = True
        else:
            self.inactive()
            self.clicked = False

    def hover(self):
        self.size = [self.original_size[0]+20, self.original_size[1]+20]
        self.font_size = self.original_fontsize + 3
        
    def inactive(self):
        self.size = self.original_size
        self.font_size = self.original_fontsize

    def check_clicked(self):
        MousePos = pygame.mouse.get_pos()

        if self.center_pos[0]-(self.size[0]//2)  < MousePos[0] < self.center_pos[0]+(self.size[0]//2) and self.center_pos[1]-(self.size[1]//2)  < MousePos[1] < self.center_pos[1]+(self.size[1]//2):
            self.hover()
            self.clicked = True

        else:
            self.inactive()
            self.clicked = False

        pass
        


class ImageButton(object):
    def __init__(self,surf,img_path,centre_pos,size):
        self.surface = surf

        self.centre_pos = centre_pos 
        self.original_size = size
        self.size = self.original_size

        self.img_path = img_path
        
        self.clicked = False

        pass

    def draw(self):
        self.image_surface = pygame.transform.scale(pygame.image.load(self.img_path),self.size)
        self.surface.blit(self.image_surface,[self.centre_pos[0]-(self.size[0]//2),self.centre_pos[1]-(self.size[1]//2)])

        MousePos = pygame.mouse.get_pos()

        if self.centre_pos[0]-(self.size[0]//2)  < MousePos[0] < self.centre_pos[0]+(self.size[0]//2) and self.centre_pos[1]-(self.size[1]//2)  < MousePos[1] < self.centre_pos[1]+(self.size[1]//2):
            self.hover()
        else:
            self.inactive()

    def hover(self):
        self.size = [self.original_size[0]+50, self.original_size[1]+50]


    def inactive(self):
        self.size = self.original_size

    def check_clicked(self):
        MousePos = pygame.mouse.get_pos()


        if self.centre_pos[0]-(self.size[0]//2)  < MousePos[0] < self.centre_pos[0]+(self.size[0]//2) and self.centre_pos[1]-(self.size[1]//2)  < MousePos[1] < self.centre_pos[1]+(self.size[1]//2):
            self.hover()
            return True
        else:
            self.inactive()
            self.clicked = False
            return False
        pass

class Image(object):
    def __init__(self,surf,img_path,center_pos,size,border_colour=None,border_thickness:int=0):
        self.screen = surf
        self.img_path = img_path
        self.center_pos = center_pos
        self.size = size

        self.border_colour = border_colour
        self.border_thickness = border_thickness

        self.image_surface = pygame.transform.scale(pygame.image.load(self.img_path),self.size)

    def draw(self):
        self.screen.blit(self.image_surface,[self.center_pos[0]-(self.size[0]//2),self.center_pos[1]-(self.size[1]//2)])

        """if self.border_thickness != 0 and self.border_colour != None:
            for i in range(1):
                start_pos = [self.center_pos[0]-(self.size[0]//2)-2,self.center_pos[1]-(self.size[1]//2)+(self.size[1]*i)]
                end_pos = [self.center_pos[0]+(self.size[0]//2)+2,self.center_pos[1]-(self.size[1]//2)+(self.size[1]*i)]
                
                pygame.draw.line(self.screen,self.border_colour,start_pos,end_pos,self.border_thickness)


            for j in range(1):
                start_pos = [self.center_pos[0]-(self.size[0]//2)+(self.size[0]*j),self.center_pos[1]-(self.size[1]//2)-2]
                end_pos = [self.center_pos[0]-(self.size[0]//2)+(self.size[0]*j),self.center_pos[1]+(self.size[1]//2)+2]
                
                pygame.draw.line(self.screen,self.border_colour,start_pos,end_pos,self.border_thickness)"""


class TextBox(object):
    def __init__(self,scr,center_pos,size,font,font_size,text_color,bg_color) -> None:
        self.screen = scr
        self.pos = center_pos
        self.size = size

        self.text = ""
        self.text_color = text_color
        self.bg_color = bg_color

        self.font = pygame.font.SysFont(font,font_size)
        self.text_surface = self.font.render(self.text,False,self.text_color)
        self.textrect_size = [self.text_surface.get_width(),self.text_surface.get_height()]

    
    def draw(self):
        pygame.draw.rect(self.screen,self.bg_color,(self.pos[0]-(self.size[0]//2),self.pos[1]-(self.size[1]//2),self.size[0],self.size[1]))

        self.text_surface = self.font.render(self.text,False,self.text_color)
        self.textrect_size = [self.text_surface.get_width(),self.text_surface.get_height()]

        self.screen.blit(self.text_surface,(self.pos[0]-(self.textrect_size[0]//2),self.pos[1]-(self.textrect_size[1]//2)))

    def key_input(self,event):
        if event.key in AlphaKeyInputs:
            self.text = self.text + event.unicode.capitalize()

        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]


class MultilineWidthText(object):
    def __init__(self,scr,text,width,top_center_pos,font,font_size) -> None:
        self.screen = scr
        self.text = text
        self.width = width
        self.x,self.y = top_center_pos
        self.fontObj = pygame.font.SysFont(font,font_size)

        self.text_obj = []

        pass

    def draw(self):

        self.text_partition = ""
        self.words = self.text.split(" ")

        for char in range(len(self.text)):
            self.text_partition = self.text_partition + self.text[char]
            current_textObj = self.fontObj.render(self.text_partition,False,(0,0,0))
            if current_textObj.get_width() > self.width:
                current_textObj = self.fontObj.render(self.text_partition[:-1],False,(0,0,0))
                self.text_obj.append(current_textObj)
                self.text_partition = self.text[char]

            else:
                self.text_partition += ""

            if char + 1 == len(self.text):
                current_textObj = self.fontObj.render(self.text_partition,False,(0,0,0))
                self.text_obj.append(current_textObj)

        self.text_height = self.text_obj[0].get_height()


        for i in range(len(self.text_obj)):
            self.screen.blit(self.text_obj[i],(self.x-(self.text_obj[0].get_width()//2),self.y+(i*self.text_height)))

        """#words

        self.text_partition = ""
        self.words = self.text.split(" ")


        for word in range(len(self.words)):
            self.text_partition = self.text_partition + self.text[word]
            current_textObj = self.fontObj.render(self.text_partition,False,(0,0,0))
            if current_textObj.get_width() > self.width:
                current_textObj = self.fontObj.render(self.text_partition[:-1],False,(0,0,0))
                self.text_obj.append(current_textObj)
                self.text_partition = self.text[char]

            else:
                self.text_partition += ""

            if char + 1 == len(self.text):
                current_textObj = self.fontObj.render(self.text_partition,False,(0,0,0))
                self.text_obj.append(current_textObj)

        self.text_height = self.text_obj[0].get_height()
        
        """