
init:
    $ path_dir = "mods/an_unfathomable_feeling/"

    $ ambience_camp_center_rain = path_dir + "sounds/ambience/ambience_camp_center_rain.ogg"
    $ ambience_lake_shore_rain = path_dir + "sounds/ambience/ambience_lake_shore_rain.ogg"
    $ ambience_lake_shore_rainfall = path_dir + "sounds/ambience/ambience_lake_shore_rainfall.ogg"

    $ scorpions_maybe_i_maybe_you = path_dir + "sounds/music/Scorpions_Maybe_I_Maybe_You.ogg"

    $ sfx_clock_transition_sound = path_dir + "sounds/sfx/sfx_clock_transition_sound.ogg"
    $ sfx_jump_into_hole = path_dir + "sounds/sfx/sfx_jump_into_hole.ogg" 
    $ sfx_blow_to_the_glass = path_dir + "sounds/sfx/sfx_blow_to_the_glass.ogg"

    define gallery_position = ((190, 130), (540, 130), (190, 530), (540, 530))

    default img_now = None
    default gallery_type = "bg"
    default gallery_page = 0

    if not persistent.gallery:
        $ persistent.gallery = {
            "cg": [[
                    ["day2_breakfast.jpg", False],
                    ["daytime_sky.jpg", False],
                    ["me_mi_dance.jpg", False],
                    ["me_mi_guitar_musclub.jpg", False]
                ],[
                    ["me_mirror_normal.jpg", False],
                    ["me_mi_piano_musclub.jpg", False],
                    ["un_crazy_blood.jpg", False],
                    ["un_crazy_torch.jpg", False],
                ],[
                    ["mi_piano_musclub.jpg", False],
                    ["campfire.jpg", False],
                    ["epilogue_inbus_1.jpg", False],
                    ["mi_boat.jpg", False],
                ],
            ],
            "bg": [[
                    ["ext_house_male_day.jpg", False],
                    ["ext_shower_room.jpg", False],
                    ["ext_storage_day.jpg", False],
                    ["int_bus_rain_sunset.jpg", False]
                ],[
                    ["int_house_male_day.jpg", False],
                    ["int_old_building_hatch.jpg", False],
                    ["int_kitchen.jpg", False],
                    ["ext_pathway_boat_station.jpg", False],
                ],[
                    ["int_dining_room_day.jpg", False],
                    ["int_dining_table_day.jpg", False],
                    ["int_dva_dish_day.jpg", False],
                    ["ext_beach_water_sunset.jpg", False],
                ],[
                    ["ext_bush_sunset.jpg", False],
                    ["int_bus_window_view.jpg", False],
                    ["int_flat_day.jpg", False],
                ],
            ]   
        }

    image ext_beach_water_day = path_dir + "images/bg/ext_beach_water_day.jpg"
    image ext_beach_water_sunset = path_dir + "images/bg/ext_beach_water_sunset.jpg"
    image ext_boathouse_rain = path_dir + "images/bg/ext_boathouse_rain.jpg"
    image ext_boathouse_sunset = path_dir + "images/bg/ext_boathouse_sunset.jpg"
    image ext_bush_sunset = path_dir + "images/bg/ext_bush_sunset.jpg"
    image ext_house_male_day = path_dir + "images/bg/ext_house_male_day.jpg"
    image ext_house_of_mt_rain = path_dir + "images/bg/ext_house_of_mt_rain.jpg"
    image ext_house_of_un_night = path_dir + "images/bg/ext_house_of_un_night.jpg"
    image ext_house_of_un_sunset = path_dir + "images/bg/ext_house_of_un_sunset.jpg"
    image ext_houses_day_monochrome = path_dir + "images/bg/ext_houses_day_monochrome.jpg"
    image ext_houses_night = path_dir + "images/bg/ext_houses_night.jpg"
    image ext_houses_rain = path_dir + "images/bg/ext_houses_rain.jpg"
    image ext_musclub_rain = path_dir + "images/bg/ext_musclub_rain.jpg"
    image ext_musclub_night = path_dir + "images/bg/ext_music_club_night.jpg"
    image ext_musclub_sunset = path_dir + "images/bg/ext_music_club_sunset.jpg"
    image ext_music_club_veranda_day = path_dir + "images/bg/ext_music_club_veranda_day.jpg"
    image ext_old_building_day = path_dir + "images/bg/ext_old_building_day.jpg"
    image ext_pathway_boat_station = path_dir + "images/bg/ext_pathway_boat_station.jpg"
    image ext_shower_room = path_dir + "images/bg/ext_shower_room.jpg"
    image ext_stage_big_day = path_dir + "images/bg/ext_stage_big_day.jpg"
    image ext_storage_day = path_dir + "images/bg/ext_storage_day.jpg"
    image ext_warehouse_rain = path_dir + "images/bg/ext_warehouse_rain.jpg"

    image int_bus_rain_sunset = path_dir + "images/bg/int_bus_rain_sunset.jpg"
    image int_bus_window_view = path_dir + "images/bg/int_bus_window_view.jpg"
    image int_dining_hall_people_sunset = path_dir + "images/bg/int_dining_hall_people_sunset.jpg"
    image int_dining_room_day = path_dir + "images/bg/int_dining_room_day.jpg"
    image int_dining_table_day = path_dir + "images/bg/int_dining_table_day.jpg"
    image int_dva_dish_day = path_dir + "images/bg/int_dva_dish_day.jpg"
    image int_flat_day = path_dir + "images/bg/int_flat_day.jpg"
    image int_flat_night = path_dir + "images/bg/int_flat_night.jpg"
    image int_house_male_day = path_dir + "images/bg/int_house_male_day.jpg"
    image int_house_male_night = path_dir + "images/bg/int_house_male_night.jpg"
    image int_house_male_sunset = path_dir + "images/bg/int_house_male_sunset.jpg"
    image int_house_of_mt_rain = path_dir + "images/bg/int_house_of_mt_rain.jpg"
    image int_kitchen = path_dir + "images/bg/int_kitchen.jpg"
    image int_musclub_rain = path_dir + "images/bg/int_musclub_rain.jpg"
    image int_musclub_sunset = path_dir + "images/bg/int_musclub_sunset.jpg"
    image int_old_building_hatch = path_dir + "images/bg/int_old_building_hatch.jpg"

    image uv_background = path_dir + "images/bg/uv_background.jpg"

    image campfire = path_dir + "images/cg/campfire.jpg"
    image day2_breakfast = path_dir + "images/cg/day2_breakfast.jpg"
    image daytime_sky = path_dir + "images/cg/daytime_sky.jpg"
    image epilogue_inbus_1 = path_dir + "images/cg/epilogue_inbus_1.jpg"
    image epilogue_inbus_2 = path_dir + "images/cg/epilogue_inbus_2.jpg"
    image me_mi_dance = path_dir + "images/cg/me_mi_dance.jpg"
    image me_mi_guitar_musclub = path_dir + "images/cg/me_mi_guitar_musclub.jpg"
    image me_mi_piano_musclub = path_dir + "images/cg/me_mi_piano_musclub.jpg"
    image me_mirror_normal = path_dir + "images/cg/me_mirror_normal.jpg"
    image mi_boat_sunset = im.MatrixColor( im.Composite((1920, 1080), (0,0), path_dir + "images/cg/mi_boat.jpg"), im.matrix.tint(0.94, 0.82, 1.0) )
    image mi_boat_day = path_dir + "images/cg/mi_boat.jpg"
    image mi_piano_musclub = path_dir + "images/cg/mi_piano_musclub.jpg"
    image un_crazy_blood = path_dir + "images/cg/un_crazy_blood.jpg"
    image un_crazy_torch = path_dir + "images/cg/un_crazy_torch.jpg"

    image letter_miku = path_dir + "images/misc/letter_miku.png"
    image list_indigrients = path_dir + "images/misc/list_indigrients.png"
    image phone disable = path_dir + "images/misc/phone_disable.png"
    image phone enable = path_dir + "images/misc/phone_enable.png"

    image unfathomable_feeling_clock = path_dir + "images/clock.png"

    # Cook

    image ck normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png") )

    image ck sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png") )

    # Miku

    image mi cry pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_cry_pionerr.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_cry_pionerr.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_cry_pionerr.png") )

    image mi cry pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_cry_pionerr_close.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_cry_pionerr_close.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_cry_pionerr_close.png") )

    image mi monochrome = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_monochrome.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_monochrome.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_monochrome.png") )

    # Summer

    image mi normal summer = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_normal_summer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_normal_summer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_normal_summer.png") )

    image mi grin summer = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_grin_summer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_grin_summer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_grin_summer.png") )

    image mi dontlike summer = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_dontlike_summer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_dontlike_summer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_dontlike_summer.png") )

    image mi happy summer = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_happy_summer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_happy_summer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_happy_summer.png") )

    image mi happy summer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_happy_summer_close.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_happy_summer_close.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_happy_summer_close.png") )

    # Apron 

    image mi normal apron = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_normal_apron.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_normal_apron.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_normal_apron.png") )

    image mi smile apron = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_smile_apron.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_smile_apron.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_smile_apron.png") )

    # Blue Dress

    image mi shy bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_blue_dress_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_blue_dress_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_blue_dress_shy.png") )

    image mi sad bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_blue_dress_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_blue_dress_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_blue_dress_sad.png") )

    image mi smile bluedress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_blue_dress_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_blue_dress_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mi/mi_blue_dress_smile.png") )

    # Yana

    image ya normal pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ya/ya_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ya/ya_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ya/ya_normal.png") )

    image ya normal pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ya/ya_normal_far.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ya/ya_normal_far.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ya/ya_normal_far.png") )

    image ya happy pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ya/ya_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ya/ya_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ya/ya_happy.png") )

    # Semen 

    image sm normal shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/sm/sm_normal_shirt.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/sm/sm_normal_shirt.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/sm/sm_normal_shirt.png") )

    image sm smile shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/sm/sm_smile_shirt.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/sm/sm_smile_shirt.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/sm/sm_smile_shirt.png") )

    image sm grin shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/sm/sm_grin_shirt.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/sm/sm_grin_shirt.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/sm/sm_grin_shirt.png") )