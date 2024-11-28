class MAIN:
    def __init__(self, type=None, location=None, owner=None, entrance_payment=None):
        self.type = type
        self.location = location
        self.owner = owner
        self.entrance_payment = entrance_payment

    def start(self):
        print("start")

    def stop(self):
        print("stop")