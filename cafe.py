from MAIN import MAIN

class Cafe(MAIN):
    def __init__(self, menu=[]):
        super().__init__(self, 'cafe')
        self._menu = menu
    
    def display_menu(self):
        return self._menu
    
    def serve_food(self,food):
        return f"{food} подано."
    
    def get_many(self, foods_to_get):
        res=''
        for i in foods_to_get:
            res += self.serve_food(i)
        return res
    
    def get_tips(self, tip =0):
        return f"{tip} руб. чаевые"

