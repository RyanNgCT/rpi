from sense_hat import SenseHat
from datetime import datetime

curr = datetime.now()

sense = SenseHat()
temp = round(sense.get_temperature())
message = f'{temp:.1f}'
sense.low_light = True
sense.show_message(message, scroll_speed=0.4, text_colour=[0, 0, 255])
sense.clear()

curr_time = curr.strftime('%H:%M')
sense.show_message(curr_time, scroll_speed=0.25, text_colour=[255, 255, 255])
sense.clear()
