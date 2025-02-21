
init 2:
    screen unfathomable_feeling_menu:
        tag menu

        add path_dir + "images/menu/menu.jpg"         

        textbutton "Играть":
            xpos 160
            ypos 200
            text_idle_color "#fff"
            text_hover_color "#aaa"
            background "#000"
            text_size 65
            text_font path_dir + "fonts/balloon_xbd.ttf"
            action Hide("unfathomable_feeling_menu", transition=dissolve), Jump("unfathomable_feeling_prologue")

        textbutton "Галерея":
            xpos 160
            ypos 360
            text_idle_color "#fff"
            text_hover_color "#aaa"
            background "#000"
            text_size 65
            text_font path_dir + "fonts/balloon_xbd.ttf"
            action ToggleScreen("unfathomable_feeling_gallery_quest", transition=fade)

        textbutton "Выход":
            xpos 160
            ypos 540
            text_idle_color "#fff"
            text_hover_color "#aaa"
            background "#000"
            text_size 65
            text_font path_dir + "fonts/balloon_xbd.ttf"
            action MainMenu(confirm=False)

        imagebutton:
            xpos 100
            ypos 900
            idle path_dir + "images/icons/vk.png"
            action NullAction(), OpenURL("https://vk.com/straightarmsnc")

        imagebutton:
            xpos 224
            ypos 900
            idle path_dir + "images/icons/da.png"
            action NullAction(), OpenURL("https://www.donationalerts.com/r/sweetconsole")
    
    screen unfathomable_feeling_gallery_quest:
        tag menu

        add path_dir + "images/menu/gallery_quest.jpg"

        imagebutton:
            xpos 300
            ypos 370
            idle path_dir + "images/menu/bg.png"
            action ToggleScreen("unfathomable_feeling_gallery", transition=fade), SetVariable("gallery_type", "bg"), SetVariable("gallery_page", 0)

        imagebutton:
            xpos 1120
            ypos 370
            idle path_dir + "images/menu/cg.png"
            action ToggleScreen("unfathomable_feeling_gallery", transition=fade), SetVariable("gallery_type", "cg"), SetVariable("gallery_page", 0)

    screen unfathomable_feeling_gallery:
        tag menu 

        add path_dir + "images/menu/gallery.jpg"

        for key, item in enumerate(persistent.gallery[gallery_type][gallery_page]):
            imagebutton:
                if item[1] == True:
                    xpos gallery_position[key][0]
                    ypos gallery_position[key][1]
                    idle path_dir + "images/menu/prev/" + item[0]
                    action SetVariable("img_now", path_dir + "images/" + gallery_type + "/" + item[0]), Show("unfathomable_feeling_screen_img_now", transition=dissolve)
                else:
                    xpos gallery_position[key][0]
                    ypos gallery_position[key][1]
                    idle path_dir + "images/menu/photographie-empty.jpg"

        for page in range(len(persistent.gallery[gallery_type])):
            if gallery_page != page:
                imagebutton:
                    xpos 875
                    ypos page * 48 + 180
                    idle path_dir + "images/menu/checkbox/idle.png"
                    hover path_dir + "images/menu/checkbox/hover.png"
                    action SetVariable("gallery_page", page)
            else:
                imagebutton:
                    xpos 875
                    ypos page * 48 + 180
                    idle path_dir + "images/menu/checkbox/hover.png"

        textbutton "Выход":
            xpos 120
            ypos 920
            text_idle_color "#fff"
            text_hover_color "#aaa"
            background "#000"
            text_size 65
            text_font path_dir + "fonts/balloon_xbd.ttf"
            action ToggleScreen("unfathomable_feeling_menu", transition=fade)

    screen unfathomable_feeling_screen_img_now:
        modal True

        imagebutton:
            xpos 0 
            ypos 0
            idle img_now

            action Hide("unfathomable_feeling_screen_img_now", transition=dissolve)