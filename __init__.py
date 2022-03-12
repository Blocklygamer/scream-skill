from mycroft import MycroftSkill, intent_file_handler


class Scream(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('scream.intent')
    def handle_scream(self, message):
        self.speak_dialog('scream')


def create_skill():
    return Scream()

