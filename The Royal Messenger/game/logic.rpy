# Handles the logic of the messenger

# The name of the messenger
default messengerName = "messenger"

# Controls whether the messenger is talking to the knight or the princess
# Will animate a night if done so
default toKnight = True

# rose meter parameters
default roseMeterMin = 0
default roseMeterMax = 100
default roseMeter = 50

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
    def travelBetween():
        store.toKnight = not store.toKnight
        if(store.toKnight):
            renpy.scene()
            renpy.show("bg knightBG")
            renpy.show("knight", at_list=[left])
            renpy.with_statement(Fade(0.5, 0.0, 0.5))
        else:
            renpy.scene()
            renpy.show("bg princessBG")
            renpy.show("princess", at_list=[left])
            renpy.with_statement(Fade(0.5, 0.0, 0.5))
    
    # will return true if above threshold
    def roseMeterAbove( threshold ):
        return store.roseMeter > threshold

    # will return true if below threshold
    def roseMeterBelow( threshold ):
        return store.roseMeter < threshold 

    # shows a thorn swaying in the top left of the screen
    # does cause a pausing effect that lasts reactionTime
    def triggerThorn():
        renpy.show("thornIndicator 1")
        renpy.with_statement(Pause(reactionTime/5))
        renpy.show("thornIndicator 2")
        renpy.with_statement(Pause(reactionTime/5))
        renpy.show("thornIndicator 3")
        renpy.with_statement(Pause(reactionTime/5))
        renpy.show("thornIndicator 4")
        renpy.with_statement(Pause(reactionTime/5))
        renpy.show("thornIndicator 5")
        renpy.with_statement(Pause(reactionTime/5))
        renpy.hide("thornIndicator")
    # shows a rose blooming in the top left of the screen
    # does cause a pausing effect that lasts reactionTime
    def triggerRose():
        renpy.show("roseIndicator 1")
        renpy.with_statement(Pause(reactionTime/5))
        renpy.show("roseIndicator 2")
        renpy.with_statement(Pause(reactionTime/5))
        renpy.show("roseIndicator 3")
        renpy.with_statement(Pause(reactionTime/5))
        renpy.show("roseIndicator 4")
        renpy.with_statement(Pause(reactionTime/5))
        renpy.show("roseIndicator 5")
        renpy.with_statement(Pause(reactionTime/5))
        renpy.hide("roseIndicator")

    # This animates thex character currently being carried out, potentially puts little animation on screen
    # and actually applies rose effect onto 
    def decisionRoseEffect( numDrop ):
        # applies actual effect on rose drop meter
        store.roseMeter = store.roseMeter + numDrop
        # bounds rose meter
        if(store.roseMeter < store.roseMeterMin):
            store.roseMeter = store.roseMeterMin
        elif(store.roseMeter > store.roseMeterMax):
            store.roseMeter = store.roseMeterMax

        # thorniness anim effect
        if(numDrop < 0):
            if(store.toKnight):
                renpy.show("knight thornReact")
                triggerThorn()
                renpy.show("knight")
            else: 
                renpy.show("princess thornReact")
                triggerThorn()
                renpy.show("princess")
        # rosiness anim effect
        elif(numDrop > 0):
            if(store.toKnight):
                renpy.show("knight roseReact")
                triggerRose()
                renpy.show("knight")
            else: 
                renpy.show("princess roseReact")
                triggerRose()
                renpy.show("princess")
        # neutral effect
        else:
            wow =3
        return
