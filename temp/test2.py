import pygame.mixer
from time import sleep
pygame.mixer.init()
#pygame.mixer.music.load(open("/Users/kathleenruan/Documents/tartanhacks/temp/sounds/neverGonnaGiveYouUp.mp3","rb"))
song = pygame.mixer.Sound("/Users/kathleenruan/Documents/tartanhacks/temp/sounds/neverGonnaGiveYouUp.mp3");
song2 = pygame.sndarray.samples(song)
song3 = pygame.sndarray.make_sound(song2)


#print ""
song3.play()


while True:
   sleep(.5)
   #song2.play()

   print "done"
