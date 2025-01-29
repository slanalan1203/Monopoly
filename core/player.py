class Player:
    def __init__(self, name: str):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
        self.is_jail = False

    def move(self, steps: int) -> None:
        self.position = (self.position + steps) % 40

    def pay(self, amount: int, recipient=None) -> bool:
        if self.money < amount:
            return False
        self.money -= amount
        if recipient:
            recipient.money += amount
        return True

