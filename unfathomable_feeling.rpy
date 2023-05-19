
init 3:
    $ mods["unfathomable_feeling_start"] = "{font=mods/an_unfathomable_feeling/fonts/pacifico.ttf}{color=#7C501A}Непостижимое чувство{/color}{/font}"

    define ck = Character(u"Повариха", color="#418AF9", what_color="#f1d076")

    define gallery_position = [[190, 130], [540, 130], [190, 530], [540, 530]]

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


init 4 python:
    def unfathomable_feeling_open_image_gallery(type, page, item):
        persistent.gallery[type][page - 1][item - 1][1] = True


label unfathomable_feeling_start:
    call screen unfathomable_feeling_menu with dissolve