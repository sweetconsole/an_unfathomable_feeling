
label unfathomable_feeling_day_3:
    window hide

    pause(1)

    $ backdrop = "days"
    $ new_chapter(3, u"Третий  день")
    $ persistent.sprite_time = "sunset"
    $ day_time()

    pause(1)

    play music music_list["i_want_to_play"] loop fadein 2

    window show

    "Я просыпался несколько раз за ночь."