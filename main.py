import time
from datetime import datetime
from pygame import mixer
work=0
def player_function(song):
    # Starting the mixer
    mixer.init ()

    # Loading the song
    mixer.music.load ( song )

    # Setting the volume
    mixer.music.set_volume ( 0.7 )

    # Start playing the song
    mixer.music.play ()

    # infinite loop
    while not work=="done":

        print ( "Press work i u compleetd the task")

        query = input ( " " )


        if work == 'done':

            # Stop the mixer
            mixer.music.stop ()

            break

# def water()
#     time_1 = time.time( )
#
#     time.sleep( 3 )
#
#     time_2 = time.time( )
#     time_interval = time_2 - time_1
#     if time_interval >= 7200 :  # '''yahan par 7200 daal dena 😁 😁😁😁'''
#         player_function( "water.mp3" )
#         f = open( "waterlog.txt" , "a" )
#         now_method = datetime.now( )
#         currentTime = now_method.strftime( "%H:%M:%S" )
#         # print ( "Current Time =" , currentTime )
#         f.write( f" drinked water at: {currentTime}" + "\n" )
#     i += 1
#
#
#
# def eyes():
#     time_1 = time.time( )
#
#     time.sleep( 3 )
#
#     time_2 = time.time( )
#     time_interval = time_2 - time_1
#     if time_interval >= 2 :
#         f=open("eyes_log.txt","a")
#         player_function( "eyes.mp3" )
#         now_method = datetime.now( )
#         currentTime = now_method.strftime( "%H:%M:%S" )
#         #         # print ( "Current Time =" , currentTime )
#         f.write( f" eyes exercise at: {currentTime}" + "\n" )
#
#
# def physcial():
#     time_1 = time.time( )
#
#     time.sleep( 3 )
#
#     time_2 = time.time( )
#     time_interval = time_2 - time_1
#     if time_interval >= 2 :
#         f=open("physcial_log.txt","a")
#         player_function( "physical.mp3" )
#         now_method = datetime.now( )
#         currentTime = now_method.strftime( "%H:%M:%S" )
#         #         # print ( "Current Time =" , currentTime )
#         f.write( f" physcial exercise at: {currentTime}" + "\n" )
#
# physcial()


time_1 = time.time( )
i=0
while not i==4:
    time_2 = time.time( )
    time_interval = time_2 - time_1
    if time_interval >= 2 : #EYES
        f=open("eyes_log.txt","a")
        player_function( "eyes.mp3" )
        now_method = datetime.now( )
        currentTime = now_method.strftime( "%H:%M:%S" )
        #         # print ( "Current Time =" , currentTime )
        f.write( f" eyes exercise at: {currentTime}" + "\n" )
        continue
    elif time_interval >= 5 :  #Physical
            f = open( "physcial_log.txt" , "a" )
            player_function( "physical.mp3" )
            now_method = datetime.now( )
            currentTime = now_method.strftime( "%H:%M:%S" )
            #         # print ( "Current Time =" , currentTime )
            f.write( f" physcial exercise at: {currentTime}" + "\n" )
            continue
    elif time_interval >= 7 :  # '''water 😁 😁😁😁'''
        player_function( "water.mp3" )
        f = open( "waterlog.txt" , "a" )
        now_method = datetime.now( )
        currentTime = now_method.strftime( "%H:%M:%S" )
        f.write( f" drinked water at: {currentTime}" + "\n" )
        i+=1
        continue





