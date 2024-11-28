from cafe import cafe

class cafe_mono_food(cafe):

    def __init__(self, menu=[], type = None):
        super().__init__(self, menu)
        self._desert_type = type

    def get_desert(self, desert = None):
        if desert in self.menu:
            super().serve_food(self,desert)
        else:
            raise ValueError(f"{desert} нет в меню")
        
    