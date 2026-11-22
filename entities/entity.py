class Entity:
    def __init__(self, name: str, active: int, observation: str = "", id: int = None):
        self.name = name
        self.active = active
        self.observation = observation
        self.id = id