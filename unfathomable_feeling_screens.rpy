
init 2:
    screen Menu:
        tag menu

        add path_dir + "images/menu/background.jpg"         

        textbutton "Играть":
            xpos 160
            ypos 220
            text_idle_color "#fff"
            text_hover_color "#aaa"
            background "#000"
            text_size 65
            text_font path_dir + "fonts/balloon_xbd.ttf"
            action Call("unfathomable_feeling_prologue")

        textbutton "Галерея":
            xpos 160
            ypos 380
            text_idle_color "#fff"
            text_hover_color "#aaa"
            background "#000"
            text_size 65
            text_font path_dir + "fonts/balloon_xbd.ttf"
            action Call("unfathomable_feeling_prologue")

        textbutton "Достижения":
            xpos 160
            ypos 540
            text_idle_color "#fff"
            text_hover_color "#aaa"
            background "#000"
            text_size 65
            text_font path_dir + "fonts/balloon_xbd.ttf"
            action Call("unfathomable_feeling_prologue")

        textbutton "Выход":
            xpos 160
            ypos 880
            text_idle_color "#fff"
            text_hover_color "#aaa"
            background "#000"
            text_size 65
            text_font path_dir + "fonts/balloon_xbd.ttf"
            action MainMenu()