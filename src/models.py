from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Queeue:

    def __init__(self):
        self._queeue = []
        self.numbers = []
        self._mode = "FIFO"

    def enqueue(self, name, number):
        self._queeue.append(name)
        self.numbers.append(number)

    def dequeue(self):
        self._queeue.pop(0)

    def __repr__(self):
       return (self._queeue)