from abc import ABC, abstractmethod


class ObservableEngine:
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)


class Hero(AbstractObserver):
    def __init__(self):
        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,}
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message['title'])
        for i in message["impact"]:
            self.stats[i] += message["impact"][i]




super = ObservableEngine()
object_1 = FullNotificationPrinter()
object_2 = ShortNotificationPrinter()
hero = Hero()
super.subscribe(hero)
super.subscribe(object_1)
super.subscribe(object_2)
super.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре",
              "impact": { "HP": 10, "MP": 10, "SP": 10,}})
print(hero.stats)
print(object_1.achievements)
print(object_2.achievements)
super.notify({"title": "Герой", "text": "Закрыл сессию без долгов", "impact": { "HP": 12, "MP": 50, "SP": 10,}})
print(hero.stats)
print(object_1.achievements)
print(object_2.achievements)