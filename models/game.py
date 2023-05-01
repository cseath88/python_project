class Game:
    def __init__(self, title, description, stock_level, buy_price, sell_price, platform, id=None):
        self.title = title
        self.description = description
        self.stock_level = stock_level
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.platform = platform
        self.id = id

    def calculate_markup(self):
        markup = self.sell_price - self.buy_price
        return round(markup, 2)