class Entity:
    def __init__(self, name: str, active: int, observation: str):
        self.name = name
        self.active = active
        self.observation = observation
        self.id = None