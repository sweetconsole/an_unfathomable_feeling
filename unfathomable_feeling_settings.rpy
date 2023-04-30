
init:
    $ path_dir = "mods/an_unfathomable_feeling/"

    $ an_unfathomable_feeling_slow_dance = path_dir + "music/Scorpions_Maybe_I_Maybe_You.ogg"

    image ext_musclub_day_sunset = path_dir + "images/bg/ext_music_club_sunset.jpg" 
    image ext_house_of_un_sunset = path_dir + "images/bg/ext_house_of_un_sunset.png"
    image ext_storage_day = path_dir + "images/bg/ext_storage_day.png"
    image ext_boathouse_sunset = path_dir + "images/bg/ext_boathouse_sunset.jpg"
    image ext_houses_night = path_dir + "images/bg/ext_houses_night.jpg"
    image ext_stage_big_sunset = path_dir + "images/bg/ext_stage_big_sunset.jpg"
    image ext_bathhouse_day = path_dir + "images/bg/ext_bathhouse_day.png"
    image ext_shower_room = path_dir + "images/bg/ext_shower_room.jpg"
    image ext_house_of_un_night = path_dir + "images/bg/ext_house_of_un_night.jpg"
    image ext_music_club_night = path_dir + "images/bg/ext_music_club_night.png"

    image int_musclub_sunset = path_dir + "images/bg/int_music_club_mattresses_sunset.jpg"
    image int_dining_hall_people_sunset = path_dir + "images/bg/int_dining_hall_people_sunset.jpg"
    image int_house_male_day = path_dir + "images/bg/int_house_male_day.jpg"
    image int_house_male_sunset = path_dir + "images/bg/int_house_male_sunset.jpg"
    image int_house_male_night = path_dir + "images/bg/int_house_male_night.jpg"

    image day2_breakfast = path_dir + "images/cg/day2_breakfast.jpg"
    image me_mi_guitar_musclub = path_dir + "images/cg/me_mi_guitar_musclub.jpg"
    image me_mi_piano_musclub = path_dir + "images/cg/me_mi_piano_musclub.jpg"
    image mi_piano_musclub = path_dir + "images/cg/mi_piano_musclub.jpg"
    image me_mirror_normal = path_dir + "images/cg/me_mirror_normal.jpg"
    image me_mi_dance = path_dir + "images/cg/me_mi_dance.png"
    image un_crazy_blood = path_dir + "images/cg/un_crazy_blood.jpg"
    image un_crazy_torch = path_dir + "images/cg/un_crazy_torch.jpg"
    image daytime_sky = path_dir + "images/cg/daytime_sky.jpg"

    # Cook

    image ck normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png") )

    image ck sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png") )

    image ck smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_smile.png") )

    image ck laugh = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_laugh.png") )

    # Miky

    image mi dontlike bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_dontlike.png") )

    image mi laugh bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_laugh.png") )

    image mi scared bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_scared.png") )

    image mi shoked bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_shoked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_shoked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_shoked.png") )

    image mi shy bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_shy.png") )

    image mi surprise bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_1_blue_dress_surprise.png") )
    
    image mi crysmile bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_cry_smile.png") )
    
    image mi grin bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_grin.png") )
    
    image mi happy bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_happy.png") )

    image mi sad bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_sad.png") )

    image mi smile bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_2_blue_dress_smile.png") )

    image mi angry bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_3_blue_dress_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_3_blue_dress_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_3_blue_dress_angry.png") )

    image mi normal bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_3_blue_dress_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_3_blue_dress_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_3_blue_dress_normal.png") )
    
    image mi upset bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_3_blue_dress_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_3_blue_dress_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_3_blue_dress_upset.png") )