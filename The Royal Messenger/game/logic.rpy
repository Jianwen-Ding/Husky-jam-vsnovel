# Handles the logic of the messanger

# The name of the messanger
default messangerName = "messanger"

# Controls whether the messanger is talking to the knight or the princess
# Will animate a night if done so
default toKnight = True

# rose meter parameters
default roseMeterMin = 0
default roseMeterMax = 100
default roseMeter = 50

# Time given for the reaction of 
define reactionTime = 0.5

init python:
    # This swaps the scene from knight to princess and vice versa
    def travelBetween():
        store.toKnight = not store.toKnight
        if(store.toKnight):
            renpy.hide("princess")
            renpy.show("knight")
            renpy.with_statement(Dissolve(1.0))
        else:
            renpy.hide("knight")
            renpy.show("princess")
            renpy.show("bg princessBG")
            renpy.with_statement(Dissolve(1.0))
    
    # will return true if above threshold
    def roseMeterAbove( threshold ):
        return store.roseMeter > threshold

    # will return true if below threshold
    def roseMeterBelow( threshold ):
        return store.roseMeter < threshold 

    # shows a thorn swaying in the top left of the screen
    # does cause a pausing effect that lasts reactionTime
    def triggerThorn():
        renpy.show("thornIndicator")
    # shows a rose blooming in the top left of the screen
    # does cause a pausing effect that lasts reactionTime
    def triggerRose():
        renpy.show("roseIndicator")

    # This animates thex character currently being carried out, potentially puts little animation on screen
    # and actually applies rose effect onto 
    def decisionRoseEffect( numDrop ):
        renpy.pause(0, hard=True)

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
                renpy.show("thornIndicator")
            else: 
                renpy.show("princess thornReact")
                renpy.show("thornIndicator")
        # rosiness anim effect
        elif(numDrop > 0):
            if(store.toKnight):
                renpy.show("knight roseReact")
                renpy.show("roseIndicator")
            else: 
                renpy.show("princess roseReact")
                renpy.show("roseIndicator")
        # neutral effect
        else:
            wow =3
        return
