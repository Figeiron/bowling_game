from graph_theory.model.Vertex import Vertex


class Pin:
    def __init__(self, pin_id: int, vertex: Vertex):
        self.id = pin_id
        self.pin_vertex = vertex
        self.is_knocked = False

    @property
    def pos(self):
        return self.pin_vertex.x, self.pin_vertex.y

    def __eq__(self, other):
        return isinstance(other, Pin) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Pin {self.id}, ({self.pos[0]}, {self.pos[1]})"
