# Defines character speaking patterns within game 

define m = Character("Mars", who_color = "#636363", callback=dialogueSounds, cb_music=marsMusic)
define m_fast = Character("Mars", who_color = "#636363", what_prefix="{cps=1}", what_suffix="{/cps}")

define f = Character("Flora", who_color = "#752065", callback=dialogueSounds, cb_music=floraMusic)
define f_fast = Character("Flora", who_color = "#752065", what_prefix="{cps=1}", what_suffix="{/cps}")

define n = Character("", callback=dialogueSounds)
define nvl = Character("", kind=nvl, callback=dialogueSounds)

# The game starts here. 

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "Test start of game"

    $ travelBetween("knight")
    jump act2start
