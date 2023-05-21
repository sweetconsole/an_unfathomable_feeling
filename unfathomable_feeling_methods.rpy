
init 4 python:
    def unfathomable_feeling_open_image_gallery(type, page, item):
        persistent.gallery[type][page - 1][item - 1][1] = True

    def bkrr_timeskip_transition():
        return ImageDissolve(path_dir + "images/transitions/timeskip.png", 2.0, ramplen=0, reverse=False, alpha=True)

    def unfathomable_feeling_timeskip():
        renpy.scene()
        renpy.show("bg black")
        renpy.with_statement(dissolve)
        renpy.play(path_dir + "sounds/sfx/sfx_clock_transition_sound.ogg", channel="sound")
        renpy.show("unfathomable_feeling_clock", at_list=[truecenter])
        renpy.with_statement(bkrr_timeskip_transition())
        renpy.hide("unfathomable_feeling_clock")
        renpy.with_statement(bkrr_timeskip_transition())
        renpy.music.stop(channel="sound", fadeout=2.0)