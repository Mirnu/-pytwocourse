class Observer:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer) 

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer(*args, **kwargs)