from MAIN import MAIN
from enum import Enum

# Класс возможных типов каруселей
class CarouselType(Enum):
    CAROUSEL_HORSE = 1
    CAROUSEL_KARTING = 2
    CAROUSEL_BATUT = 3

# Основной класс
class Carousel(MAIN):
    def __init__(self, time_limit, type_of_carousel):
      super().__init__(self, time_limit, type_of_carousel) # super.__init__(type, location, owner, entrance_payment)
      self.time_limit = time_limit
      self.type_of_carousel = type_of_carousel

    def getType(self):
      return self.type_of_carousel

    def carousel_work(self, time_limit=0): # лимит времени работы карусели
      if time_limit == 0:
        return "Карусель не работает"

      if time_limit > 0:
        return f"Карусель работает {time_limit} минут"


# Наследуем класс Carousel для классов Carousel_horse, Carousel_karting, Carousel_batut
class Carousel_horse(Carousel):
    def __init__(self, time_limit):
        Carousel.__init__(self, time_limit, CarouselType.CAROUSEL_HORSE)

class Carousel_karting(Carousel):
    def __init__(self, time_limit):
        Carousel.__init__(self, time_limit, CarouselType.CAROUSEL_KARTING)

class Carousel_batut(Carousel):
    def __init__(self, time_limit):
        Carousel.__init__(self, time_limit, CarouselType.CAROUSEL_BATUT)