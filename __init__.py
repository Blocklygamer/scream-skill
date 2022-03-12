from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService
from mycroft.audio import wait_while_speaking
import random
from os.path import dirname, join, walk



class Scream(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        path = join(dirname(__file__),'screams')
        self.playlist = []
        for roots, dirs, files in walk(path):
            for file in files:
                self.playlist.append(join(path,file))

    def initialize(self):
        self.audioservice = AudioService(self.bus)

    @intent_file_handler('scream.intent')
    def handle_scream(self, message):
        scream = random.choice(self.playlist)
        self.audioservice.play(scream)


def create_skill():
    return Scream()

