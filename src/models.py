class Queeue:

    def __init__(self):
        self._queeue = []
        self.numbers = []

    def enqueue(self, name, number):
        self._queeue.append(name)
        self.numbers.append(number)

    def dequeue(self):
        return {
            "name": self._queeue.pop(0),
            "number": self._queeue.pop(0)
        }

    def __repr__(self):
       return (self._queeue)