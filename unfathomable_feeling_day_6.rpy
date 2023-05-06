
label unfathomable_feeling_day_6:
    window hide

    $ renpy.pause(1.0, hard=True)

    $ backdrop = "days"
    $ new_chapter(6, u"Непостижимое чувство.\Шестой день")
    $ persistent.sprite_time = "day"
    $ day_time()

    $ renpy.pause(1.0, hard=True)

    scene int_house_male_day with fade

    play ambience ambience_lake_shore_day loop fadein 4

    window show

    "Я проснулся на удивление спокойно. Мне никто не щекотал нос, моя спина не была мокрой из-за росы, и я не сидел в накалённом дотла автобусе. За окном щебетали ранние пташки, и как всегда был природный порядок."
    
    scene ext_house_male_day with dissolve

    play ambience ambience_camp_center_day loop fadein 4

    "Подтянувшись и зевнув, я вышел на улицу."

    scene ext_houses_day with dissolve

    $ renpy.pause(1.0, hard=True)

    scene ext_washstand_day with dissolve

    $ renpy.pause(1.0, hard=True)

    scene ext_washstand2_day with dissolve

    "Я просто аккуратно пошёл к умывальникам, ещё раз подтянувшись. Вода сегодня не была ледяной, она была холодной, с нотками теплоты в вырывающейся из смесителя струе. "
    
    scene ext_washstand_day with dissolve

    "Нет, сегодняшнее утро однозначно хотело меня удивить и у него получилось. На улице стояла тихая погода, не нарушаемая даже дыханием ветра, солнце неторопливо отдалялось от горизонта, озаряя небо лазурным сиянием." 
    "Не знаю отчего, но сейчас очень захотелось пойти на пристань."