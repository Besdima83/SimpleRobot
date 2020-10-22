class SimpleRobot:
    def __init__(self):
        self.name = 'Name'
        self.command = 'Command'

    def get_name(self):
        return self.name

    def get_command(self):
        return self.command


class SmileRobot(SimpleRobot):
    def __init__(self):
        super().__init__()
        self.name = 'Smile'
        self.command = 'Hello Smile'


class LuckyRobot(SimpleRobot):
    def __init__(self):
        super().__init__()
        self.name = 'Lucky'
        self.command = 'Hello Lucky'