
init 3:
    $ mods["unfathomable_feeling_start"] = "{font=mods/an_unfathomable_feeling/fonts/pacifico.ttf}{color=#7C501A}Непостижимое чувство{/color}{/font}"

    define ck = Character(u"Повариха", color="#418AF9", what_color="#f1d076")


label unfathomable_feeling_start:
    
    $ unfathomable_feeling_timeskip()

    call screen unfathomable_feeling_menu with dissolve

    