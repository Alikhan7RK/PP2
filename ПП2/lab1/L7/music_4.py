import pygame
import os


#Spacebar (SPACE) → Play/Pause
#S (S) → Stop
#Right Arrow (RIGHT) → Next Track
#Left Arrow (LEFT) → Previous Track

pygame.init()
pygame.mixer.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")


BACKGROUND_IMAGE = "C:/Users/uzzer/Downloads/bgim.png"
background = pygame.image.load(BACKGROUND_IMAGE)
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)) 


MUSIC_FOLDER = "C:/Users/uzzer/Desktop/pygame/music" 
songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
current_song_index = 0


def play_music():
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_song_index]))
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_music()


def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_music()


if songs:
    play_music()

running = True
while running:
    screen.blit(background, (0, 0))  
    pygame.display.flip()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s: 
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT: 
                previous_song()

pygame.quit()
