from cgitb import handler
from tracemalloc import start
import pygame , random
from Puzzlesetting import * 
from pygame import mixer
import tkinter
import tkinter.filedialog
import time
import cv2
# print(1111111111111111111111111111111111111)
def prompt_file():
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name

def start_game(mode):
    global cells,cell_width,cell_height,show_start_screen
    row = mode
    cols = mode
    num_cells = row * cols
    cell_width = 1280 // row
    cell_height = 720 // cols
    cells = []
    rand_indexes = list(range(0, num_cells))
    for i in range(num_cells):
        x = (i % row) * cell_width
        y = (i//cols) * cell_height
        rect = pygame.Rect(x,y,cell_width,cell_height)
        rand_pos = random.choice(rand_indexes)
        rand_indexes.remove(rand_pos)
        cells.append({'rect':rect,'border':WHITE,'order': i,'pos':rand_pos})
        print(cells[i])
    show_start_screen = False 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen_first:
                mouse = pygame.mouse.get_pos()
                show_start_screen = False
                if 663 <= mouse[0] <= 1014 and -38 <= mouse[1] <= 398:
                    screen_first = False
                    show_start_screen = True
                if 668 <= mouse[0] <= 982 and 588 <= mouse[1] <= 626:
                    running = False
            elif show_start_screen:
                mouse = pygame.mouse.get_pos()
                if 623 <= mouse[0] <= 974 and 290 <= mouse[1] <= 334:
                    start_game(3)
                    selected_img = []
                    isBackButton = False
                if 582 <= mouse[0] <= 1015 and 367 <= mouse[1] <= 413:
                    start_game(4)
                    selected_img = []
                    isBackButton = False
                if 613 <= mouse[0] <= 982 and 448<= mouse[1] <= 494:
                    start_game(5)
                    selected_img = []
                    isBackButton = False
                if 580 <= mouse[0] <= 1025 and 528 <= mouse[1] <= 576:
                    start_game(6)
                    selected_img = []
                    isBackButton = False
                if 661 <= mouse[0] <= 974 and 613 <= mouse[1] <= 662:
                    running = False 
                if 1503 <= mouse[0] <= 1585 and 706 <= mouse[1] <= 744:
                    screen_first = True
                    show_start_screen = False
                if 1250 <= mouse[0] <= 1576 and 303 <= mouse[1] <= 344:
                    f = prompt_file()
                    bg = pygame.image.load(f)
                    bg1 = pygame.transform.scale(pygame.image.load(f), (460, 350))
                    bg_rect = bg.get_rect()
                    bg_rect.topleft = (0,0)
            elif game_screen:
                 mouse = pygame.mouse.get_pos()
                 if 1533 <= mouse[0] <= 1611 and 652 <= mouse[1] <= 682:
                    show_start_screen = True
                    isBackButton = True
                 if 341 <= mouse[0] <= 500 and 757 <= mouse[1] <= 796:
                    start_game(3)
                    selected_img = []
                 if 562 <= mouse[0] <= 760 and 754 <= mouse[1] <= 795:
                    start_game(4)
                    selected_img = []
                 if 813 <= mouse[0] <= 983 and 756 <= mouse[1] <= 793:
                    start_game(5)
                    selected_img = []
                 if 1051 <= mouse[0] <= 1299 and 753 <= mouse[1] <= 794:
                    start_game(6)
                    selected_img = []
                 if 1541 <= mouse[0] <= 1616 and 757 <= mouse[1] <= 793:
                    running = False 
            else:
                mouse = pygame.mouse.get_pos()
                if 341 <= mouse[0] <= 500 and 757 <= mouse[1] <= 796:
                    show_start_screen = True
                    print(11)
                    pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            for cell in cells:
                rect = cell['rect']
                order = cell['order']
                if rect.collidepoint(mouse_pos):        
                    if not selected_img:
                        print(order)
                        selected_img = {}
                        selected_img = cell
                        cell['border'] = skyblue
                    else:
                        current_img = cell
                        if current_img['order'] != selected_img['order']:
                            try:
                                temp = selected_img['pos']
                                cells[selected_img['order']]['pos'] = cells[current_img['order']]['pos']
                                cells[current_img['order']]['pos'] = temp
                                cells[selected_img['order']]['border'] = skyblue
                                selected_img = None
                                game_over = True
                                # for cell in cells:
                                #     if cell['order'] != cell['pos']:
                                #         game_over = False
                            except:
                                print('error')
        if screen_first:
            screen.fill(BLACK)
            screen.blit(title_1text, title_1rect)
            screen.blit(strat_text, strat_rect)
            screen.blit(Setting_text, Setting_rect)
            screen.blit(Exit_text, Exit_rect)
            show_start_screen = False
        elif show_start_screen:
                screen.fill(BLACK)
                screen.blit(title_text, title_rect)
                screen.blit(choose_text, choose_rect)
                screen.blit(easy_text, easy_rect)
                screen.blit(medium_text, medium_rect)
                screen.blit(hard_text, hard_rect)
                screen.blit(veryhard_text, veryhard_rect)
                screen.blit(Exit1_text, Exit1_rect)
                screen.blit(text , (1250,300))
                screen.blit(Back_text, (1500,700))
                screen_first = False              
        elif game_screen:
                screen_first = False
                show_start_screen = False                                
                screen.fill(BLACK)
                screen.blit(lev_text, (60,750))
                screen.blit(Exit2_text, (1540,740))
                screen.blit(Back_text, (1530,640))
                screen.blit(easy1_text, (340,750))
                screen.blit(medium1_text, (540,750))
                screen.blit(hard1_text, (810,750))
                screen.blit(veryhard1_text, (1050,750))
                screen.blit(bg1,(1300,50))
        if not game_over:
              if not isBackButton:
                for i,val in enumerate(cells):
                    pos = cells[i]['pos']
                    img_area = pygame.Rect(cells[pos]['rect'].x,cells[pos]['rect'].y,cell_width,cell_height)
                    screen.blit(bg,cells[i]['rect'],img_area)
                    pygame.draw.rect(screen,cells[i]['border'],cells[i]['rect'],1)
        else:
            game_screen = False
            screen.fill(BLACK) 
            screen.blit(bg2,(250,0))
            screen.blit(play_agin_text,(540,750))
            screen.blit(complet1_text,(340,750))
            screen.blit(Exit3_text,(1050,750))
            screen.blit(SlidingPuzzle_text,(810,750))
            if game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    game_over = False
                    game_screen = True
    clock.tick(FPS)
    pygame.display.update()
# pygame.quit()
