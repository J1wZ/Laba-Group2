from cafe import cafe

class shop(cafe):

    def __init__(self, catalog=[]):
        super().__init__(self, catalog)

    def display_item(self, item=None):
        if item in self.menu:
            return f"{item}"
        else:
            raise ValueError(f"{item} нет в каталоге")

    def purchase_item(self, item=None, money=0): 
        if item in self.menu:
            return f"{item} куплен за {money} руб."
        else:
            raise ValueError(f"{item} нет в каталоге")
        
    def give_change(self, price=0, money=0):
        if money > price:
            return f"Сдача {money-price} руб."
        else:
            return "Нет сдачи."
        