# Defines character speaking patterns within game 

define m = Character("Mars", who_color = "#dedede", callback=dialogueSounds, cb_music=marsMusic)
define m_fast = Character("Mars", who_color = "#dedede", what_prefix="{cps=1}", what_suffix="{/cps}")

define f = Character("Flora", who_color = "#ffd1ff", callback=dialogueSounds, cb_music=floraMusic)
define f_fast = Character("Flora", who_color = "#ffd1ff", what_prefix="{cps=1}", what_suffix="{/cps}")

define n = Character("", callback=dialogueSounds)
define nvl_n = Character("", kind=nvl, callback=dialogueSounds)
