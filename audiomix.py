import pygame
import time
print(1)
print("-")
#plays first mp3 file
# file = 'C:\\Users\\Nitish Shankar\\PycharmProjects\\pythonTuts\\audio\\largemusic.mp3'
#
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load(file)
# pygame.mixer.music.play()
#
# print(2)
# time.sleep(5)
# pygame.mixer.music.pause()
# print(3)
#
#
#  #next mp3 file
#
# file = 'C:\\Users\\Nitish Shankar\\PycharmProjects\\pythonTuts\\audio\\smallmusic.mp3'
# # pygame.init()
# # pygame.mixer.init()
# pygame.mixer.music.load(file)
# pygame.mixer.music.play()
# time.sleep(5)
#
# print(4)
# pygame.mixer.music.pause()
t = 1
while(t>0):
    if(t<1):

        file = 'C:\\Users\\Nitish Shankar\\PycharmProjects\\pythonTuts\\audio\\largemusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        # pygame.mixer.music.unpause()
        print(2)

        time.sleep(5)
        pygame.mixer.music.pause()
        print("-")
        print(1)
        file = 'C:\\Users\\Nitish Shankar\\PycharmProjects\\pythonTuts\\audio\\smallmusic.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        # pygame.mixer.music.unpause()

        time.sleep(5)
        print("-")

        pygame.mixer.music.pause()
        t+=1
    else:
        file = 'C:\\Users\\Nitish Shankar\\PycharmProjects\\pythonTuts\\audio\\largemusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        # pygame.mixer.music.play()

        pygame.mixer.music.unpause()
        # pygame.mixer.music.play()

        time.sleep(5)
        pygame.mixer.music.pause()
        print(3)

        # time.sleep(5)
        # pygame.mixer.music.pause()
        print("-")
        print(4)
        file = 'C:\\Users\\Nitish Shankar\\PycharmProjects\\pythonTuts\\audio\\smallmusic.mp3'
        pygame.mixer.music.load(file)
        # pygame.mixer.music.play()
        pygame.mixer.music.unpause()
        # pygame.mixer.music.play()

        time.sleep(5)

        pygame.mixer.music.pause()

        # time.sleep(5)
        print("-")

        # pygame.mixer.music.pause()
























































































#play and pause funtionnality
#
# while pygame.mixer.music.get_busy():
#     timer = pygame.mixer.music.get_pos()
#     time.sleep(1)
#     control = input()
#     pygame.time.Clock().tick(10)
#     if control == "pause":
#         pygame.mixer.music.pause()
#     elif control == "play" :
#         pygame.mixer.music.unpause()
#     elif control == "time":
#         timer = pygame.mixer.music.get_pos()
#         timer = timer/1000
#         print (str(timer))
#     elif int(timer) > 10:
#         print ("True")
#         pygame.mixer.music.stop()
#         break
#     else:
#         pass