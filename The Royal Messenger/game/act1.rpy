#the game starts here
label start:
    n "The soft morning sun shines down on the people of the kingdom. People who need their mail."

    n "You weave your way through crowded streets, handing letters to merchants, artisans, and performers."

    n "Opening your satchel, you find an envelope that’s marked different from the others. It bears the royal seal."

    n "You run to the castle, and pass through its heavily guarded gates."

    $ travelBetween("princess")

    f "You there, might you have a letter for me?"

    menu:
        "Here you go!":
            show princess
            f "Wonderful! I sincerely thank you."

        "No, this letter is for a different princess.":
            show princess dis
            f "How unfortunate. I do look forward to receiving mail."

    n "You give Flora her mail."

    show princess
    f "If it wouldn’t trouble you too much, would you mind doing me a little favor?"

    menu: 
        "Of course, princess!":
            $placeholder = "whoa"

        "Depends what it is.":
            $placeholder = "whoa"

    show princess
    f "Could you go tell the knight at the front gates to come speak to me?"

    menu:
        "Sure!":
            $placeholder = "whoa"

        "Whatever you say, boss.":
            $placeholder = "whoa"

    $ travelBetween("knight")

    m "Hello. Do you need help with something?"

    menu: 
        "The princess would like to speak with you.":
            show knight cur
            m "The princess would like to speak with me? About what?" 
            $ roseMeter = roseMeter + 1

        "The princess demands your presence at her tower.":
            show knight cur
            m "The princess would like to see me? What for?"
            $ roseMeter = roseMeter - 1

    show knight
    m "Sorry, I’ve been stationed here at the front gates, and I can’t leave my post."

    show knight cur
    m "But now I’m curious. Could you go find out why the princess asked to see me?"

    menu: 
        "Normally I just hand out letters, but sure...":
            $placeholder = "whoa"
        
        "I’m happy to help!":
            $placeholder = "whoa"

    $ travelBetween("princess")

    show princess dis
    f "You return, but with no knight. What happened?"  

    menu:
        "She has to stay at her post.":
            $ roseMeter = roseMeter + 1
        "She can’t leave the gates unattended.":
            $ roseMeter = roseMeter - 1

    show princess dis
    f "Oh... I suppose that makes sense."

    menu:
        "She wanted to know why you wanted to speak with her.":
            $ roseMeter = roseMeter + 1

        "Why did you want to talk to her, anyways?":
            $ roseMeter = roseMeter

    show princess
    f "Well, to be perfectly honest, I find her to be quite attractive."

    menu:
        "I see!":
            $ placeholder = "whoa"

        "She is pretty cute.":
            $ roseMeter = roseMeter + 1

    show princess
    f "I would like to take her out on a date." 

    menu:
        "Should I go ask her?":
            show princess exc
            f "You know what, why not?"
        
        "Let me go see what she thinks!":
            show princess exc
            f "Okay, but make sure you come back and tell me what she says!"

    $ travelBetween("knight cur")
    jump act2start

