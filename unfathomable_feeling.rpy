
init:
    $ path_dir = "mods/an_unfathomable_feeling/"

    $ mods["unfathomable_feeling_start"] = "{font=mods/an_unfathomable_feeling/fonts/pacifico.ttf}{color=#7C501A}Непостижимое чувство{/color}{/font}"

    image bg ext_musclub_day_sunset = path_dir + "images/bg/ext_music_club_sunset.jpg" 
    image bg ext_house_of_un_sunset = path_dir + "images/bg/ext_house_of_un_sunset.png"
    image bg ext_storage_day = path_dir + "images/bg/ext_storage_day.png"

    image bg int_musclub_sunset = path_dir + "images/bg/int_music_club_mattresses_sunset.jpg"
    image bg int_dining_hall_people_sunset = path_dir + "images/bg/int_dining_hall_people_sunset.jpg"

    image day2_breakfast = path_dir + "images/cg/day2_breakfast.jpg"
    image me_mi_guitar_musclub = path_dir + "images/cg/me_mi_guitar_musclub.jpg"
    image me_mi_piano_musclub = path_dir + "images/cg/me_mi_piano_musclub.jpg"
    image mi_piano_musclub = path_dir + "images/cg/mi_piano_musclub.jpg"
    image me_mirror_normal = path_dir + "images/cg/me_mirror_normal.jpg"
    

label unfathomable_feeling_start:
    jump unfathomable_feeling_prologue