# Defines character speaking patterns within game 

define m = Character("Mars", who_color = "#636363", callback=dialogueSounds, cb_music=marsMusic)
define m_fast = Character("Mars", who_color = "#636363", what_prefix="{cps=1}", what_suffix="{/cps}")

define f = Character("Flora", who_color = "#752065", callback=dialogueSounds, cb_music=floraMusic)
define f_fast = Character("Flora", who_color = "#752065", what_prefix="{cps=1}", what_suffix="{/cps}")

define n = Character("", callback=dialogueSounds)
define nvl = Character("", kind=nvl, callback=dialogueSounds)

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

    $ travelBetween("princess")

    f "crazy"

    $ decisionRoseEffect(0.5)

    f "rose"
    # This ends the game.

    jump act1start
