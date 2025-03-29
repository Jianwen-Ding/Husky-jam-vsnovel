label act2start:
    m "Hi! Do you know anymore about why the princess wanted to see me?"

    menu:
        "The princess has requested a date with you. Will you oblige?":
            $ roseMeter = roseMeter - 1
        "It seems you have caught the eye of the princess. Are you interested in going on a date with her?":
            $ roseMeter = roseMeter + 1

    m "Oh wow, I’m flattered, but I wouldn’t want to rush into things too quickly. I mean, she’s the princess. Plus I’m sure she has more important royal duties than seeing me."
    $ travelBetween()

    f "What did she say?! Will I be seeing her soon? I already have my dress picked out!"

    menu:
        "I think Mars would like to get to know you a little more before going on a date?":
            f "I can hardly wait to see her, but I suppose we can get to know each other a little more first. I hope she knows that I wish I had more freedom to explore things other than being a princess."

        "Mars seems nervous about moving too quickly with you since you’re the princess.":
            f "This is unfortunate, I was hoping it wouldn’t be an issue. And I don’t love talking through a courier, no offense. She should know there’s a lot more to me than my role in the kingdom."
    $ travelBetween()

    m "Did the princess take it well? I wouldn’t want to disappoint her."

    menu:
        "The princess seemed a little disappointed and wanted you to know that there’s a lot more to her than being a princess.":
            m "If I’m being honest, the most important thing about me is my work. I take great honor in it and devote a lot to it. I assumed she would understand that as the princess."
        "The princess would be happy to get to know you a little more first. She for one wishes she could explore around more.":
            m "I suppose being the princess could be a bit limiting in that regard, but it’s such an important role. And work means a lot to me."
    $ travelBetween()

    f "Does Mars understand where I’m coming from?"

    menu:
        "Mars understands that you might not enjoy how your role can be a bit restricting even if it is important":
            f "I’m glad she can acknowledge that. Maybe she’s ready for a date now too?"
        "Work seems to mean a lot to Mars and wants you to know it is an important part of her life":
            f "I can appreciate that, but I just hate being cooped up in this castle like I’m helpless! It’s why I want to get out of here and do something so bad. Why don’t you see if she’s ready for a date now?"
    $ travelBetween()

    m "It’s good to see you. I was worried I wouldn’t hear from the princess again."

    menu:
        "Don’t worry. The princess was actually hoping you’d go out on a date with her.":
            m "Oh, that’s good. I’d be happy to go on a date with her."
        "I think it would mean a lot to the princess if you would take her on a date.":
            m "I think I’m ready now. Tell her I’d be happy to."
    $ travelBetween()
    jump act3start
