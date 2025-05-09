﻿# Handles the logic of the messenger

# The name of the messenger
default messengerName = "messenger"

# Controls whether the messenger is talking to the knight or the princess
# Will animate a night if done so
default toKnight = True

# rose meter parameters
default roseMeterMin = 50
default roseMeterMax = -50
default roseMeter = 0

# Time given for the reaction of 
define reactionTime = 0.5
define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg', 'audio/B6.ogg', 'audio/B7.ogg', 'audio/B8.ogg']
define marsMusic = '4 knight character theme.wav'
define floraMusic = '3 rose character theme.wav'
define backgroundMusic = '2 regular game theme.wav'
define startMusic = '1 start screen.wav'

init python:
    # dialogue sound effect
    def dialogueSounds(event, interact=True, music=backgroundMusic, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.music.play(music, fadeout=0.5, fadein = 0.5, if_changed=True)
            for i in range(60):
                renpy.sound.queue(renpy.random.choice(sounds))
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    # This swaps the scene from knight to princess and vice versa
    def travelBetween(sprite):
        global toKnight
        toKnight = not toKnight
        renpy.scene()
        if(toKnight):
            renpy.scene()
            renpy.show("bg black")
            renpy.show("leftWalkAnim", at_list=[leftWalkTrans])
            renpy.with_statement(Fade(0.5, 0.0, 0.5))
            renpy.pause(2)
            renpy.scene()
            renpy.show("bg knightBG")
            renpy.show(sprite, at_list=[left])
            renpy.with_statement(Fade(0.5, 0.0, 0.5))
        else:
            renpy.scene()
            renpy.show("bg black")
            renpy.show("rightWalkAnim", at_list=[rightWalkTrans])
            renpy.with_statement(Fade(0.5, 0.0, 0.5))
            renpy.pause(2)
            renpy.scene()
            renpy.show("bg princessBG")
            renpy.show(sprite, at_list=[left])
            renpy.with_statement(Fade(0.5, 0.0, 0.5))
    
    # will return true if above threshold
    def roseMeterAbove( threshold ):
        return store.roseMeter > threshold

    # will return true if below threshold
    def roseMeterBelow( threshold ):
        return store.roseMeter < threshold 
