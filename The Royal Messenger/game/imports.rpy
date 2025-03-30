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
image knight hap = "k_Happy.png"
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

image bg black = "bg black.jpg"

define animSpeed = 0.15

image leftWalkAnim:
    "walk_Left/walkLeft_1.png"
    pause animSpeed
    "walk_Left/walkLeft_2.png"
    pause animSpeed
    "walk_Left/walkLeft_3.png"
    pause animSpeed
    "walk_Left/walkLeft_4.png"
    pause animSpeed
    "walk_Left/walkLeft_5.png"
    pause animSpeed
    "walk_Left/walkLeft_6.png"
    pause animSpeed
    "walk_Left/walkLeft_7.png"
    pause animSpeed
    "walk_Left/walkLeft_8.png"
    repeat

transform leftWalkTrans:
    animation
    xalign 1.0
    yalign 1.0
    pause 0.5
    linear 2.5 xalign 0.0

image rightWalkAnim:
    "walk_Right/walkRight_1.png"
    pause animSpeed
    "walk_Right/walkRight_2.png"
    pause animSpeed
    "walk_Right/walkRight_3.png"
    pause animSpeed
    "walk_Right/walkRight_4.png"
    pause animSpeed
    "walk_Right/walkRight_5.png"
    pause animSpeed
    "walk_Right/walkRight_6.png"
    pause animSpeed
    "walk_Right/walkRight_7.png"
    pause animSpeed
    "walk_Right/walkRight_8.png"
    repeat

transform rightWalkTrans:
    animation
    xalign 0.0
    yalign 1.0
    pause 0.5
    linear 2.5 xalign 1.0