class Game:
    def __init__(self, title, description, stock_level, buy_cost, sell_price, platform, id=None):
        self.title = title
        self.description = description
        self.stock_level = stock_level
        self.buy_cost = buy_cost
        self.sell_price = sell_price
        self.platform = platform
        self.id = id