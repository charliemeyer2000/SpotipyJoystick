import RPi.GPIO as GPIO
import time
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOauth

GPIO.setmode(GPIO.BCM)

# might need to change pins depending on how you wired the joystick/what joystick you're using
right_button = 17
left_button = 27
up_button = 22
down_button = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(right_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(left_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(up_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(down_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

sp = Spotify(auth_manager=SpotifyOAuth(client_id='your_client_id', client_secret='your_client_secret', redirect_uri='your_redirect_uri', scope=['app-remote-control','user-library-modify']))

## PLAY A PLAYLIST HERE.....

while True:
    right_state = GPIO.input(right_button)
    if right_state == False:
        sp.next_track()
        print("Next track")
        time.sleep(0.2)
    left_state = GPIO.input(left_button)
    if left_state == False:
        sp.previous_track()
        print("Previous track")
        time.sleep(0.2)
    up_state = GPIO.input(up_button)
    if up_state == False:
        volume = sp.volume()
        if volume < 100:
            sp.volume(volume+10)
            print("Volume increased")
        time.sleep(0.2)
    down_state = GPIO.input(down_button)
    if down_state == False:
        volume = sp.volume()
        if volume > 0:
            sp.volume(volume-10)
            print("Volume decreased")
        time.sleep(0.2)
