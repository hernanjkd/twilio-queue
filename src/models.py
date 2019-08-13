class Queeue:

    def __init__(self):
        self._queeue = []

    def enqueue(self, name, number):
        self._queeue.append({
            "name": name,
            "number": number
        })

    def dequeue(self):
        return self._queeue.pop(0)

    def get_queue(self):
       return self._queeue