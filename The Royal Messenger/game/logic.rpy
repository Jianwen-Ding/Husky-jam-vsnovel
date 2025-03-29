# Handles the logic of the messanger

# Controls whether the messanger is talking to the knight or the princess
# Will animate a night if done so
default toKnight = True

# rose meter parameters
default roseMeterMin = 0
default roseMeterMax = 100
default roseMeter = 50

init python:
    # This swaps the scene from knight to princess and vice versa
    def travelBetween():
        store.toKnight = not store.toKnight
        if(store.toKnight):
            renpy.hide("princess")
            renpy.show("knight")
            renpy.scene("bg knightBG")
        else:
            renpy.hide("knight")
            renpy.show("princess")
            renpy.scene("bg princessBG")
        
    # will return true if above threshold
    def roseMeterAbove( threshold ):
        return store.roseMeter > threshold

    # will return true if below threshold
    def roseMeterBelow( threshold ):
        return store.roseMeter < threshold 

    # This animates the character currently being carried out, potentially puts little animation on screen
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
            wow = 3
        # rosiness anim effect
        elif(numDrop > 0):
            wow =3
        # neutral effect
        else:
            wow =3
        return

