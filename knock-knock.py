#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import time


def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('whose there')
    recognizer.expect_phrase('a broken pencil who')

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    while True:
        print('Press the button and speak')
        aiy.audio.say('press the button')
        button.wait_for_press()
        print('Listening...')
        aiy.audio.say("knock knock")
        text = recognizer.recognize()
        if text is None:
            print('Sorry, I did not hear you.')
            aiy.audio.say("sorry, i did not hear you")
        else:
            print('You said "', text, '"')
            if 'there' in text:
                aiy.audio.say('a broken pencil')
                text = recognizer.recognize()
                print('You said "', text, '"')
                if 'pencil' in text:
                   aiy.audio.say('never mind. its pointless')
                   time.sleep(5)
            elif 'goodbye' in text:
                break


if __name__ == '__main__':
    main()
