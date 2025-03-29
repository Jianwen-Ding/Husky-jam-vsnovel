# 

define m = Character("Mars", callback=dialogueSounds, cb_music=marsMusic)
define f = Character("Flora", callback=dialogueSounds, cb_music=floraMusic)
define n = Character("", callback=dialogueSounds)

define config.debug_sound = True
# The game starts here. 

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    show princess at left
    f "You've created a new Ren'Py game."

    f "Once you add a story, pictures, and music, you can release it to the world!"

    $ travelBetween()

    f "crazy"

    $ decisionRoseEffect(0.5)

    f "rose"
    # This ends the game.

    jump act3start
