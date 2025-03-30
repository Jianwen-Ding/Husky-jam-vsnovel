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
image bg knightBG = "KnightBackground.png"

image knight base = "k_Base.png"
image knight = "k_Neutral.png"
image knight cur = "k_Curious.png"
image knight hap = "k_TalkingNeutral.png"
image knight thornReact:
    "KnightThorn.jpg"
    pause reactionTime
    "k_Base.png"
image knight roseReact: 
    "KnightRose.jpg"
    pause reactionTime
    "k_Base.png"

# Princess character
image bg princessBG =  "PrincessBackground.jpeg"

image princess base = "p_Base.png"
image princess = "p_Neutral.png"
image princess dis = "p_Disappointed.png"
image princess exc = "p_Excited.png"
image princess thornReact:
    "PrincessThorn.jpg"
    pause reactionTime
    "p_Base.png"
image princess roseReact: 
    "PrincessRose.jpg"
    pause reactionTime
    "p_Base.png"
