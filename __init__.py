from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService
from mycroft.audio import wait_while_speaking
import random
import os



class Scream(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        path = os.path.join(os.path.dirname(__file__),'screams')
        self.playlist = []
        for roots, dirs, files in os.walk(path):
            for file in files:
                self.playlist.append(os.join(path,file))

    def initialize(self):
        self.audioservice = AudioService(self.bus)

    @intent_file_handler('scream.intent')
    def handle_scream(self, message):
        scream = random.choice(self.playlist)
        self.audioservice.play(scream)


def create_skill():
    return Scream()

