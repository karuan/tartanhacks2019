import pygame 
import time

#pygame.mixer.init(44100, -16, 2, 2048)
#mixer.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.init()
print pygame.mixer.get_init() 
screen=pygame.display.set_mode((400,400),0,32) 



sound = pygame.mixer.Sound("/Users/kathleenruan/Documents/tartanhacks/temp/sounds/neverGonnaGiveYouUp.mp3")
channel = sound.play()      # Sound plays at full volume by default
#sound.set_volume(0.9)   # Now plays at 90% of full volume.
#sound.set_volume(0.6)   # Now plays at 60% (previous value replaced).
#channel.set_volume(0.5) # Now plays at 30% (0.6 * 0.5).

time.sleep(30) 
