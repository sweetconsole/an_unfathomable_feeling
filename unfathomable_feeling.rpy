
init 3:
    $ mods["unfathomable_feeling_start"] = "{font=mods/an_unfathomable_feeling/fonts/pacifico.ttf}{color=#7C501A}Непостижимое чувство{/color}{/font}"

    define ck = Character(u"Повариха", color="#418AF9", what_color="#f1d076")

    default img_now = None
    default gallery_type = "bg"
    default gallery_page = 0

    default gallery = {
        "cg": [[
                ["day2_breakfast.jpg", False],
                ["daytime_sky.jpg", False],
                ["me_mi_dance.jpg", False],
                ["me_mi_guitar_musclub.jpg", False]
            ],[
                ["me_mirror_normal.jpg", True],
                ["me_mi_piano_musclub.jpg", True],
                ["un_crazy_blood.jpg", True],
                ["un_crazy_torch.jpg", True],
            ],[
                ["mi_piano_musclub.jpg", True],
                ["campfire.jpg", True],
            ],
        ],
        "bg": [[
                ["ext_house_male_day.jpg", True],
                ["ext_shower_room.jpg", True],
                ["ext_storage_day.jpg", True],
                ["int_bus_rain_sunset.jpg", True]
            ],[
                ["int_house_male_day.jpg", True],
                ["int_old_building_hatch.jpg", True],
                ["ext_lake_swim_day.jpg", True],
                ["ext_pathway_boat_station.jpg", True],
            ],[
                ["int_dining_room_day.jpg", True],
                ["int_dining_table_day.jpg", True],
                ["int_dva_dish_day.jpg", True],
            ],
        ]   
    }

    define gallery_position = [
        [190, 130], 
        [540, 130],
        [190, 530],
        [540, 530]
    ]

label unfathomable_feeling_start:
    call screen unfathomable_feeling_menu with dissolve

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