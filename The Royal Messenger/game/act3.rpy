# 


# The game starts here. 

label act3start:
    f "Mars has agreed to meet with me, then? Wonderful! Set up a time for us to meet, please. Perhaps tomorrow? I simply can’t wait any longer to meet her."
    f "Oh, and, do make sure you refer to this a date. I wouldn’t want there to be any confusion."

    $ travelBetween()

    m "You got a response from Flora? What’d she say?"
    menu:
        "Flora wants to go on a date with you tomorrow. She seemed antsy.":
            m "Tomorrow? That’s… I dunno, I’ll be busy until pretty late."
            m "You did say she looked antsy, though. I guess I’ll make it work somehow."
            $ date = "tomorrow"
            $ travelBetween()
            jump .choice1
        "Flora wanted to ask you the next time you’re available to go on a date with her. She’s hoping for tomorrow.":
            m "I could probably meet tomorrow, but I’ll be tired after a day of work. My next day off is Saturday, that’d probably be better."
            m "Hmm... I'd rather not be tired for our date, let’s do Saturday, instead."
            $ date = "Saturday"
            $ travelBetween()
            jump .choice2

label .choice1:
    f "Ah, perfect, you’ve returned! What news from Mars?"
    menu:
        "Mars said that tomorrow will work for her.":
            f "Perfect! I cannot wait to meet her. I hope she’s just as excited about this as I am!"

        "Mars didn’t seem happy about meeting tomorrow, but she said she’ll make it work.":
            f "Oh. I see. I guess she’s busy, then. I’m glad she could make the time to meet with me, but I was hoping she’d be more excited…"

label .choice2:
    f "Ah, perfect, you’ve returned! What news from Mars?"
    menu:
        "Mars is too busy to go on a date until Saturday.":
            f "Saturday?! But that’s so far from now…"
            f "If she’s busy, though, I suppose it cannot be helped. Saturday it is."

        "Mars has work, so she doesn’t want to go on a date until Saturday.":
            f "Saturday?! But that’s so far from now…"
            f "I guess she’s probably busy with work and all, but…"
            f "Fine, Saturday it is."
    jump .part2

label .part2:
    f "Where should we meet, then? I think we should do something exciting or adventurous! Perhaps we could go to the archery range?"

    $ travelBetween()
    m "You’re back! Are we set for [date]?"
    menu:
        "Yes, Flora is thinking of going to the archery range. She wants to do something “adventurous”.":
            m "The archery range? I don’t know, I do a lot of training for work already."
            m "I was hoping that we could go to a quiet place to share a meal, but she wants to do something adventurous…"
            m "I suppose it might be fun since it’ll be with her, even if it’s not my first choice."
            $ travelBetween()
            jump .choice3
        "Yes, Flora is asking about where to meet. She suggested the archery range.":
            m "Oh, the archery range? I’m not sure about that, I’m already training a lot for work…"
            m "Maybe we could go someplace calmer? Have a meal together, maybe."
            $ travelBetween()
            jump .choice4

label .choice3:
    f "Ah, you’re back! How did Mars respond?"
    menu:
        "She was disappointed, but she said she was okay with it.":
            f "Oh… Really? I do wish she would not acquiesce if it isn’t what she wants to do."
            f "I would hate for her to be going along with it only because of… you know."
        "She said that it sounds okay to her, since it’ll be fun if it’s with you.":
            f "Oh! Did she really? That’s awfully sweet of her to say, I truly cannot wait for [date]!"
    jump .act3end

label .choice4:
    f "Ah, you’re back! How did Mars respond?"
    menu:
        "Mars didn’t like the idea of archery since it’s part of what she does for work. She wants to get a meal together, instead": 
            f "Oh… I suppose that makes sense. How embarrassing for me. That’s a shame, I was hoping to do something more… exciting."
            f "Ah, well. It’s a bit boring, but a meal with Mars does sound amenable, indeed."

        "Mars was thinking about getting a meal together, instead.":
            f "Oh, really? That’s a shame, I was hoping to do something more… exciting."
            f "Ah, well. It’s a bit boring, but a meal with Mars does sound amenable, indeed."

label .act3end:
    f "Please, let her know that I will see her soon, and that I am looking forward to our date!"
