from math import fabs
from os import remove
from tkinter import font
from turtle import title, window_height, window_width
from numpy import choose
from pyautogui import mouseDown
import pyautogui
import pygame , random
from pygame import mixer
import cv2
from PIL import Image

pygame.init()
window_width = 1800
window_height = 850
screen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Puzzle Game image')
FPS = 60
f = "No Select"
clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)
skyblue = (59, 161, 227)
green = (86,255,86)
purple = (170,86,255)
Red = (210, 43, 43)
green1 = (184, 240, 150)
pink = (238, 95, 210)
green2 = (230,230,250)
row = None
cols = None
cell_width = None
cell_height = None
cells = []
# bg = pygame.image.load('yande.re 726631 ass cameltoe dress loli pantsu thighhighs yukie1.jpg')
bg = pygame.image.load('elephant.jpg')
bg_rect = bg.get_rect()
bg_rect.topleft = (0,0)
bg1 = pygame.transform.scale(bg, (460, 350))
bg2 = pygame.transform.scale(bg, (1280, 720))
font_title = pygame.font.Font('Hello Avocado.ttf',60)
font_content = pygame.font.Font('Hello Avocado.ttf',45)
title_text = font_title.render('Puzzle Game',True,pink)
title_rect = title_text.get_rect()
title_rect.center = (window_width//2,window_height//2.6 - 170)

choose_text = font_content.render('Choose your difficulty',True,skyblue)
choose_rect = choose_text.get_rect()
choose_rect.center = (window_width//2,window_height//2.6 - 90)

easy_text = font_content.render("Press'E' - Easy (3x3)",True,purple)
easy_rect = easy_text.get_rect()
easy_rect.center = (window_width//2,window_height//2.6 -10)

medium_text = font_content.render("Press'M' - Medium (4x4)",True,purple)
medium_rect = medium_text.get_rect()
medium_rect.center = (window_width//2,window_height//2.6 + 70)

hard_text = font_content.render("Press'H' - Hard (5x5)",True,purple)
hard_rect = hard_text.get_rect()
hard_rect.center = (window_width//2,window_height//2.6 + 150)

veryhard_text = font_content.render("Press'V' - Veryhard (6x6)",True,purple)
veryhard_rect = veryhard_text.get_rect()
veryhard_rect.center = (window_width//2,window_height//2.6 + 230)

play_agin_text = font_title.render("Game complete",True,skyblue)
play_agin_rect = play_agin_text.get_rect()
play_agin_rect.center = (window_width//2,window_height//2-150)


play_agin1_text = font_title.render("Play Again?",True,skyblue)
play_agin1_rect = play_agin1_text.get_rect()
play_agin1_rect.center = (window_width//2,window_height//2 -70)

continue_text = font_content.render('press Space',True,skyblue)
continue_rect = continue_text.get_rect()
continue_rect.center = (window_width//2,window_height//2 + 50)

title_1text = font_title.render('Sliding Puzzle in python',True,pink)
title_1rect = title_text.get_rect()
title_1rect.center = (window_width//2.4+40,window_height//3.2)

strat_text = font_title.render("Press'S' - Strat",True,purple)
strat_rect = title_text.get_rect()
strat_rect.center = (window_width//2,window_height//2.2)

Setting_text = font_title.render("Press'T' - Setting",True,skyblue)
Setting_rect = title_text.get_rect()
Setting_rect.center = (window_width//2 - 30,window_height//1.7)

Exit_text = font_title.render("Press'X' - Exit",True,Red)
Exit_rect = title_text.get_rect()
Exit_rect.center = (window_width//2.2+80,window_height//1.38)

Exit1_text = font_title.render("Press'X' - Exit",True,Red)
Exit1_rect = title_text.get_rect()
Exit1_rect.center = (window_width//2,window_height//2.6 + 320)
color_light = (170,170,170)
color_dark = (100,100,100)
color = (255,255,255)
smallfont = pygame.font.SysFont('Hello Avocado.ttf',60)
text = smallfont.render('Picture Selection' , True , skyblue)

Back_text = font_content.render("Back",True,Red)
Back_rect = Back_text.get_rect()

lev_text = font_content.render("level change",True,green1)
lev_rect = lev_text.get_rect()

Exit2_text = font_title.render("Exit",True,Red)
Exit2_rect = Exit2_text.get_rect()

easy1_text = font_content.render("Easy(3x3)",True,purple)
easy1_rect = easy1_text.get_rect()

medium1_text = font_content.render("Medium(4x4)",True,purple)
medium1_rect = medium1_text.get_rect()

hard1_text = font_content.render("Hard(5x5)",True,purple)
hard1_rect = hard1_text.get_rect()

veryhard1_text = font_content.render("Veryhard(6x6)",True,purple)
veryhard1_rect = veryhard1_text.get_rect()

random_text = font_content.render("Random again",True,skyblue)
random_rect = random_text.get_rect()

picture_text = font_content.render("Picture Selection",True,skyblue)
picture_rect = picture_text.get_rect()

SlidingPuzzle_text = font_content.render("SlidingPuzzle Home Screen",True,green2)
SlidingPuzzle = SlidingPuzzle_text.get_rect()

Exit3_text = font_content.render("Exit",True,green2)
Exit3 = Exit3_text.get_rect()

complet1_text = font_content.render("Game complete",True,green2)
complet1 = complet1_text.get_rect()


selected_img = None
game_over = False
show_start_screen = True
screen_first = True
screen_two = True
game_screen = True
game_screen1 = True
isBackButton = False
