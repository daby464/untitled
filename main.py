def on_gesture_shake():
    basic.show_leds("""
        # # # . .
                # # # . .
                . # . . #
                # # # # #
                # # # # #
    """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
