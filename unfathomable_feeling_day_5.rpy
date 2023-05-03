
label unfathomable_feeling_day_5:
    window hide

    pause(1)

    $ backdrop = "days"
    $ new_chapter(5, u"Непостижимое чувство.\nПятый день")
    $ persistent.sprite_time = "day"
    $ day_time()

    pause(1)

    window show

    "Сколько раз за последнее время я просыпаюсь от яркого солнца? {w}Ослепляющий свет ударил прямо по глазам, и я поёжился, отвернувшись к стенке."
    "От солнечного тепла постель начала нагреваться, да так, что спать на ней было уже невозможно. {w}Я нехотя встал, и с полураскрытыми глазами пошёл к умывальникам."

    scene ext_house_male_day with dissolve

    $ renpy.pause(1.0, hard=True)

    scene ext_houses_day with dissolve

    $ renpy.pause(1.0, hard=True)

    scene ext_washstand_day with dissolve

    $ renpy.pause(1.0, hard=True)

    scene ext_washstand2_day with dissolve

    play sound sfx_open_water_sink

    play sound sfx_water_sink_stream loop fadein 4

    "Вода освежает и пробуждает, но не ледяная: она прямо выбивает твой разум из головы. {w}Мир начал плыть, а лицо жгло, но я своего добился – сон ушёл."
    
    play sound sfx_dinner_horn_processed 
    
    "Когда с чисткой зубов было покончено, раздался горн."

    play sound sfx_close_water_sink

    "Я закрыл вентиль, отчего он протяжно скрипнул."
    
    scene ext_washstand_day with dissolve
    
    "Всё тот же лесной пейзаж, деревья качаются в такт утреннему ветру, а солнце одаряет своими лучами пионерлагерь и меня."
    
    scene ext_houses_day with dissolve

    "Светило уже давно выглянуло из-за горизонта, и продолжало лениво выползать. {w}Яркие его лучи нагревали остывшую почву, каменную дорожку и мокрую от росы траву." 
    "Где-то вдалеке играла тихая, ненавязчивая музыка.{w} Хотя, стоп! {w}Откуда здесь музыка? {w}М-да... это странно, но в этом нет ничего плохого, потом спрошу у кого-нибудь." 
    "Пионеры небольшими кучками плелись в сторону столовой, весело перекидываясь фразами. {w}Не придумав ничего лучше, я присоединился к ним."