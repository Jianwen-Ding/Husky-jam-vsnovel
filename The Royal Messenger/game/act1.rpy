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
            f "Wonderful! I sincerely thank you."

        "No, this letter is for a different princess.":
            f "How unfortunate. I do look forward to receiving mail."

    n "You give Flora her mail."

    f "If it wouldn’t trouble you too much, would you mind doing me a little favor?"

    menu: 
        "Of course, princess!":
            $placeholder = "whoa"

        "Depends what it is.":
            $placeholder = "whoa"

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
            m "The princess would like to speak with me? About what?" 
            $ roseMeter = roseMeter + 1

        "The princess demands your presence at her tower.":
            m "The princess would like to see me? What for?"
            $ roseMeter = roseMeter - 1

    m "Sorry, I’ve been stationed here at the front gates, and I can’t leave my post."

    m "But now I’m curious. Could you go find out why the princess asked to see me?"

    menu: 
        "Normally I just hand out letters, but sure...":
            $placeholder = "whoa"
        
        "I’m happy to help!":
            $placeholder = "whoa"

    $ travelBetween("princess")

    f "You return, but with no knight. What happened?"  

    menu:
        "She has to stay at her post.":
            $ roseMeter = roseMeter + 1
        "She can’t leave the gates unattended.":
            $ roseMeter = roseMeter - 1

    f "Oh... I suppose that makes sense."

    menu:
        "She wanted to know why you wanted to speak with her.":
            $ roseMeter = roseMeter + 1

        "Why did you want to talk to her, anyways?":
            $ roseMeter = roseMeter

    f "Well, to be perfectly honest, I find her to be quite attractive"

    menu:
        "I see!":
            $ placeholder = "whoa"

        "She is pretty cute.":
            $ roseMeter = roseMeter + 1

    f "I would like to take her out on a date." 

    menu:
        "Should I go ask her?":
            f "You know what, why not?"
        
        "Let me go see what she thinks!":
            f "Okay, but make sure you come back and tell me what she says!"

    $ travelBetween("knight")
    jump act2start

