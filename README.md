# googlecontroller

Library for Python 3.8+ to push text message or audio file with the Google Home.Originally made by - Thomas Deblock (@tdeblock) I have expanded most of the code quite a bit little of the original remains, but the idea came from Mr.Deblock.This is a sorta v2 for the googlehomepush module they made.

## Installation

    
pip install https://github.com/dray-cyber/googlecontroller

## Depending On

PyChromeCast

## How to use

``` python
from googlecontroller import GoogleAssistant
from googlecontroller.http_server import serve_file # for local files
host = "ip"
home = GoogleAssistant(host=host)
home.say("test")
home.play("http://www.hubharp.com/web_sound/BachGavotteShort.mp3")

file_url = serve_file("/path/to/file", "audio/mp3") # local
home.play(file_url, "audio/mp3")
home.volume(100)
home.volume(0)

```
### .say(text, speed,ignore, lang)

Push a message on Google home

- `text` is the test message to say
- `speed` is the rate of speed of the message ranges from 0.000+ as slowest to 1 as normal speed.
- `ignore` ignore if audio is playing and play it regardless if ignore=True and only play if not playing if ignore=False or is not specified. 
- `lang` the text language, default value is 'en' to change it have lang = 'language' as described in google translate en-Us, es (spanish), ect

### .play(url, ignore, contentType = 'audio/mp3'):

Push a sound to Google home
- `url` an audio file URL
- `ignore` ignore if audio is playing and play it regardless if ignore=True and only play if not playing if ignore=False or is not specified. 
- `contentType` the audio file content type

### .volume(volumelevel):
- `volumelevel` the volume level from 0-100 by 0.01 to 1 Example: home.volume(volumelevel=0.05 or 5 percent volume. If you want to take it as user input you can do volumelevel=float(input()) the float is required to convert it as it is a decimal.



## Maintainers
- Dray-Cyber
