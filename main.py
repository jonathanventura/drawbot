
def sad():
    music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(220, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(500)

def on_button_pressed_a():
    if check_line_sensors():
        music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(330, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(392, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(500)
        move(10)
        turn(45)
        move(10)
        move(-10)
        turn(-45)
    else:
        sad()
input.on_button_pressed(Button.A, on_button_pressed_a)

def turn(deg: number):
    if deg > 0:
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 100)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 100)
    else:
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 100)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 100)
    basic.pause(abs(deg) * 4)
    Maqueen_V5.motor_stop(Maqueen_V5.Motors.ALL)
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    basic.pause(500)

def on_button_pressed_b():
    if check_line_sensors():
        music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(330, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(392, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(500)
        move(10)
        turn(45)
        move(10)
        move(-10)
        turn(-45)
    else:
        sad()
input.on_button_pressed(Button.B, on_button_pressed_b)

def check_line_sensors():
    return maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1
def move(distanceCm: number):
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    if distanceCm > 0:
        Maqueen_V5.motor_run(Maqueen_V5.Motors.ALL, Maqueen_V5.Dir.CW, 100)
    else:
        Maqueen_V5.motor_run(Maqueen_V5.Motors.ALL, Maqueen_V5.Dir.CCW, 100)
    basic.pause(66 * abs(distanceCm))
    Maqueen_V5.motor_stop(Maqueen_V5.Motors.ALL)
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    basic.pause(500)
basic.show_icon(IconNames.HEART)

def on_forever():
    if check_line_sensors():
        basic.show_leds("""
                            . # . # .
                            . # . # .
                            . . . . .
                            # . . . #
                            . # # # .
                            """)
    else:
        basic.show_leds("""
                        . . . . .
                        . # . # .
                        . . . . .
                        . # # # .
                        # . . . #
                        """)
basic.forever(on_forever)
