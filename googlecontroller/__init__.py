import pychromecast
name = "googlecontroller"
__all__ = 'GoogleAssistant'
class GoogleAssistant:
    def __init__(self, host = None):
        try:
            if host != None:
                self.cc = pychromecast.Chromecast(host)
            else:
                print('For a host input the ip and have the option like: host = "192.168.0.whatever" home = GoogleHome(host=host) ')
        except:
            print("Some sort of error occured most likely a bad connection or ip adress")
    def play(self, url, ignore = False, contenttype = 'audio/mp3'):
        if self.cc.media_controller.status.player_state != "PLAYING" or ignore == True:
            self.cc.wait()
            media = self.cc.media_controller
            media.play_media(url, contenttype)
            media.block_until_active()
    def say(self, text, speed = 1, ignore = False, lang = 'en-US'):
        speed = str(speed)
        url = u"https://translate.google.com/translate_tts?ie=UTF-8&q=" + text + "%21&tl=" + lang + "&ttsspeed=" + speed + "&total=1&idx=0&client=tw-ob&textlen=14&tk=594228.1040269"
        self.play(url, ignore)
    def volume(self, volumelevel):
        self.cc.set_volume(volumelevel)
