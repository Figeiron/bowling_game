import time
from random import choice, randint
from graph_theory.algorithms.BFS import BFS
from graph_theory.algorithms.Algorithm import AlgorithmEventType


class Kick:
    def __init__(self, graph_controller, triangle):
        self.graph = graph_controller
        self.pin_triangle = triangle

    def is_touch(self):
        return choice([True, True, False])

    def pick_pin(self):
        available_pins = [pin for pin in self.pin_triangle.pins if not pin.is_knocked]
        if not available_pins:
            return None

        max_y = max(pin.pos[1] for pin in available_pins)
        front_pins = [pin for pin in available_pins if pin.pos[1] >= max_y - 20]
        
        return choice(front_pins)

    def pick_len(self):
        standing_pins = [pin for pin in self.pin_triangle.pins if not pin.is_knocked]
        if not standing_pins:
            return 0
        return randint(1, len(standing_pins))

    def find_pin(self, vertex):
        for pin in self.pin_triangle.pins:
            if pin.pin_vertex == vertex:
                return pin
        return None


    def run(self):
        if not self.is_touch():
            print("Куля пройшла повз!")
            return

        pin_to_hit = self.pick_pin()
        if not pin_to_hit:
            return

        print(f"Влучання у кеглю {pin_to_hit.id}!")
        self.graph.add_algorithm(BFS)
        self.graph.pick_vertex(pin_to_hit.pin_vertex)
        self.graph.init_algorithm()
        
        target_count = self.pick_len()
        kicked_pins = set()
        finished = False

        while not finished:
            event = self.graph.step_algorithm()
            
            if event.type in (AlgorithmEventType.VISIT_VERTEX, AlgorithmEventType.DISCOVER_VERTEX):
                vertex = event.data.get("vertex") or event.data.get("to_vertex")
                pin = self.find_pin(vertex)
                if pin and not pin.is_knocked:
                    pin.is_knocked = True
                    kicked_pins.add(pin)

            if event.type == AlgorithmEventType.FINISHED or len(kicked_pins) >= target_count:
                self.graph.current_algorithm = None
                finished = True

        print(f"Збито кеглів: {len(kicked_pins)}")



