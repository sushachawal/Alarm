import simpleaudio as sa
import keyboard
import sys
import time
import threading

def playAlarm(alarm, e):
    start = time.time()
    while(time.time() - start < 120 and not e.isSet()):
        play = alarm.play()
        time.sleep(1.2)
        play.stop()

alarm = sa.WaveObject.from_wave_file("old-fashioned-school-bell-daniel_simon.wav")
if sys.argv[2] == "seconds" or sys.argv[2] == "second" or sys.argv[2] == "s":
    timer = int(sys.argv[1])
else:
    timer = int(sys.argv[1]) * 60

time.sleep(timer)

e = threading.Event()
t = threading.Thread(target=playAlarm, args=(alarm, e))
t.start()

while t.is_alive():
    if(keyboard.is_pressed(' ')):
        e.set()
        t.join()