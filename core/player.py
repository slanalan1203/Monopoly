class Player:
    def __init__(self, name: str):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
        self.is_jail = False

    def move(self, steps) -> None:
        pass

    def pay(self, amount: int, recipient=None) -> bool:
        pass

