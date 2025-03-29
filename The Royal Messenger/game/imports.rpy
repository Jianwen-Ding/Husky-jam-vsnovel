#This file links in art/music assets into the game
# Thorn animation
image thornIndicator 1 = "Knight.jpg"
image thornIndicator 2 = "Knight.jpg"
image thornIndicator 3 = "Knight.jpg"
image thornIndicator 4 = "Knight.jpg"
image thornIndicator 5 = "Knight.jpg"

image thornIndicator:
    "thornIndicator 1"
    pause (reactionTime/5)
    "thornIndicator 2"
    pause (reactionTime/5)
    "thornIndicator 3"
    pause (reactionTime/5)
    "thornIndicator 4"
    pause (reactionTime/5)
    "thornndicator 5"
    pause (reactionTime/5)
    alpha 0

# Rose animation
image roseIndicator 1 = "Knight.jpg"
image roseIndicator 2 = "Knight.jpg"
image roseIndicator 3 = "Knight.jpg"
image roseIndicator 4 = "Knight.jpg"
image roseIndicator 5 = "Knight.jpg"

image roseIndicator:
    "roseIndicator 1"
    pause (reactionTime/5)
    "roseIndicator 2"
    pause (reactionTime/5)
    "roseIndicator 3"
    pause (reactionTime/5)
    "roseIndicator 4"
    pause (reactionTime/5)
    "roseIndicator 5"
    pause (reactionTime/5)
    alpha 0

# Knight character 
image bg knightBG = "KnightBackground.jpeg"

image knight = "k_Base.png"
image knight thornReact:
    "KnightThorn.jpg"
    pause reactionTime
    "k_Base.jpg"
image knight roseReact: 
    "KnightRose.jpg"
    pause reactionTime
    "k_Base.jpg"

# Princess character
image bg princessBG =  "PrincessBackground.jpeg"

image princess = "p_Base.png"
image princess thornReact = "PrincessThorn.jpg"
image princess roseReact = "PrincessRose.jpeg"