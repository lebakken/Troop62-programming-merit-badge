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

def ask_question_abcd(question, optiona, optionb, optionc, optiond, answer):
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase(answer)
    while True:
	    aiy.audio.say(question)
	    time.sleep(1)
	    aiy.audio.say(optiona)
	    time.sleep(2)
	    aiy.audio.say(optionb)
	    time.sleep(2)
	    aiy.audio.say(optionc)
	    time.sleep(2)
	    aiy.audio.say(optiond)
	    text = recognizer.recognize()
	    if text is None:
                print('Sorry, I did not hear you.')
                aiy.audio.say("sorry, i did not hear you")
	    elif 'repeat' in text:
                print('repeating question')
	    else:
                if answer in text:
                    print(answer)
                    print('thats correct')
                    aiy.audio.say("thats correct")
                    break
                else:
                    print(answer)
                    aiy.audio.say("thats wrong. the correct answer was")
                    if 'a' in answer:
                        aiy.audio.say(optiona)
                    elif 'b' in answer:
                        aiy.audio.say(optionb)
                    elif 'c' in answer:
                        aiy.audio.say(optionc)
                    elif 'd' in answer:
                        aiy.audio.say(optiond)
                    else:
                        aiy.audio.say(answer)
                break
				
				
	


def main():
    recognizer = aiy.cloudspeech.get_recognizer()

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    while True:
        print('Press the button and speak')
        aiy.audio.say('press the button')
        button.wait_for_press()
        ask_question_abcd("who started boy scouts in the usa?", "a. Baden Powell", "b. Teddy Roosevelt", "c. robert noyce", "d. john white","c")
        time.sleep(10)


if __name__ == '__main__':
    main()
