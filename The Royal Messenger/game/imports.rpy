#This file links in art/music assets into the game

# Knight character 
image bg knightBG = "KnightBackground.png"

image knight base = "k_Base.png"
image knight = "k_Neutral.png"
image knight cur = "k_Curious.png"
image knight hap = "k_Happy.png"

# Princess character
image bg princessBG =  "PrincessBackground.png"

image princess base = "p_Base.png"
image princess = "p_Neutral.png"
image princess dis = "p_Disappointed.png"
image princess exc = "p_Excited.png"

image bg black = "bg black.jpg"

image good_ending = "goodEnding.png"

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