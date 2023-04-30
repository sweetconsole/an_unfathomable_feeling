
init 3:
    $ mods["unfathomable_feeling_start"] = "{font=mods/an_unfathomable_feeling/fonts/pacifico.ttf}{color=#7C501A}Непостижимое чувство{/color}{/font}"

    define ck = Character(u"Повариха", color="#418AF9", what_color="#f1d076")

label unfathomable_feeling_start:

    call screen Menu with dissolve


    # $ persistent.sprite_time = "sunset"
    # show ck normal
    # "sunset"

    # $ persistent.sprite_time = "day"
    # show ck sad
    # "day"

    # $ persistent.sprite_time = "night"
    # show ck smile
    # "night"

    # jump unfathomable_feeling_prologue