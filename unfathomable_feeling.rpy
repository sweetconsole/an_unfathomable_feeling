
init:
    $ path_dir = "mods/an_unfathomable_feeling/"

    $ mods["unfathomable_feeling_start"] = "{font=mods/an_unfathomable_feeling/fonts/pacifico.ttf}{color=#7C501A}Непостижимое чувство{/color}{/font}"

    define ck = Character(u"Повариха", color="#418AF9", what_color="#f1d076")

    image ext_musclub_day_sunset = path_dir + "images/bg/ext_music_club_sunset.jpg" 
    image ext_house_of_un_sunset = path_dir + "images/bg/ext_house_of_un_sunset.png"
    image ext_storage_day = path_dir + "images/bg/ext_storage_day.png"
    image ext_boathouse_sunset = path_dir + "images/bg/ext_boathouse_sunset.jpg"
    image ext_houses_night = path_dir + "images/bg/ext_houses_night.jpg"
    image ext_stage_big_sunset = path_dir + "images/bg/ext_stage_big_sunset.jpg"

    image int_musclub_sunset = path_dir + "images/bg/int_music_club_mattresses_sunset.jpg"
    image int_dining_hall_people_sunset = path_dir + "images/bg/int_dining_hall_people_sunset.jpg"

    image day2_breakfast = path_dir + "images/cg/day2_breakfast.jpg"
    image me_mi_guitar_musclub = path_dir + "images/cg/me_mi_guitar_musclub.jpg"
    image me_mi_piano_musclub = path_dir + "images/cg/me_mi_piano_musclub.jpg"
    image mi_piano_musclub = path_dir + "images/cg/mi_piano_musclub.jpg"
    image me_mirror_normal = path_dir + "images/cg/me_mirror_normal.jpg"

    image ck normal = path_dir + "images/sprites/nt_normal.png"
    image ck sad = path_dir + "images/sprites/nt_sad.png"
    image ck smile = path_dir + "images/sprites/nt_smile.png"
    image ck laugh = path_dir + "images/sprites/nt_laugh.png"
    

label unfathomable_feeling_start:
    jump unfathomable_feeling_prologue