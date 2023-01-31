# import datetime
# from pygame import mixer
#
# a = datetime.datetime.now()
# current_time = a.strftime("%H:%M:%S").split(':')
# waterTime = 9.00
# eyesTime = 9.00
# physicalTime = 9.00
#
# while True:
#     pass
#
#
# # Starting the mixer
# mixer.init()
#
# # Loading the song
# mixer.music.load("mySong.mp3")
#
# # Setting the volume
# # mixer.music.set_volume(0.7)
#
# # Start playing the song
# mixer.music.play()
# #
# # # infinite loop
# while True:
#     print("Press 'Drank' to exit the program")
#     query = input("  ")
#
#     if query == 'Drank':
#
#         # Pausing the music
#         mixer.music.pause()
#     elif query == 'r':
#
#         # Resuming the music
#         mixer.music.unpause()
#     elif query == 'Drank':
#         # Stop the mixer
#         mixer.music.stop()
#         break


# healthy program
# 9am to 5 pm
# water-water.mp3(3.5 litter)-drank-log
# Eyes-eyes.mp3-every 30 min-eydone-logging
# physical activity=physical.mp3 every-45 min-ex done-log
#
# Rules
# pygame module to play audio.

from pygame import mixer

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
if __name__ == '__main__':
    musiconloop('water.mp3','stop')






















