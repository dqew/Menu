import pygame
import button

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

asset_dir = ".\\assets\\"

bg_img = pygame.image.load(f"{asset_dir}yper_saber_no_buttons.png")
bg_img = pygame.transform.scale(bg_img,(SCREEN_WIDTH, SCREEN_HEIGHT))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

pygame.mixer.init()
pygame.mixer.music.load(f"{asset_dir}High_Contrast_-_If_We_Ever.wav")
pygame.mixer.music.play(loops=-1)

#game variables
game_paused = True
menu_state = "main"


#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
start_img = pygame.image.load(f"{asset_dir}Start_Button.png").convert_alpha()
options_img = pygame.image.load(f"{asset_dir}Options_Button.png").convert_alpha()
quit_img = pygame.image.load(f"{asset_dir}Quit_Button.png").convert_alpha()
controls_img = pygame.image.load(f"{asset_dir}Controls_Button.png").convert_alpha()
audio_img = pygame.image.load(f"{asset_dir}Audio_Button.png").convert_alpha()
video_settings_img = pygame.image.load(f"{asset_dir}Video_settings_Button.png").convert_alpha()
mute_menu_music_img = pygame.image.load(f"{asset_dir}Mute_menu_music_Button.png").convert_alpha()

back_img = pygame.image.load(f"{asset_dir}Back_Button.png").convert_alpha()

#create button instances
start_button = button.Button(328, 380, start_img, 1)
options_button = button.Button(325, 435, options_img, 1)
quit_button = button.Button(355, 485, quit_img, 1)
#option menu buttons
controls_button = button.Button(304, 373, controls_img, 1)
audio_button = button.Button(304, 473, audio_img, 1)
Video_settings_Button = button.Button(304 ,423, video_settings_img, 1) 
back_button = button.Button(355, 530, back_img, 1)
#audio menu buttons
mute_menu_music_button = button.Button (350, 473, mute_menu_music_img, 1)


#game loop
run = True
while run:

  event_list = pygame.event.get()
  for event in event_list:
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  screen.blit(bg_img,(0,0))






  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      start_button.is_visible = True
      options_button.is_visible = True
      quit_button.is_visible = True
      audio_button.is_visible = False
      controls_button.is_visible = False
      Video_settings_Button.is_visible = False
      back_button.is_visible = False
      mute_menu_music_button.is_visible = False


      #draw pause screen butttons
      if start_button.draw(screen):
        game_paused = True
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      audio_button.is_visible = True
      controls_button.is_visible = True
      Video_settings_Button.is_visible = True
      back_button.is_visible = True
      start_button.is_visible = False
      quit_button.is_visible = False
      mute_menu_music_button.is_visible = False
      
      #draw the different options buttons
      if controls_button.draw(screen):
        print("Controls")
      if audio_button.draw(screen):
        menu_state = "Audio"
      if Video_settings_Button.draw(screen):
        print("Video settings")
      if back_button.draw(screen):
        menu_state = "main"
    #check if the controls menu is open **TO DO**

    #check if the audio menu is open
    if menu_state == "Audio":
      mute_menu_music_button.is_visible = True
      
      #other buttons cant be seen
      audio_button.is_visible = False
      controls_button.is_visible = False
      Video_settings_Button.is_visible = False
      back_button.is_visible = False
      start_button.is_visible = False
      quit_button.is_visible = False
      options_button.is_visible = False


      #draw the different audio options buttons
      if mute_menu_music_button.draw(screen):
        pygame.mixer.music.pause()

      

    pygame.display.update()


pygame.quit()
