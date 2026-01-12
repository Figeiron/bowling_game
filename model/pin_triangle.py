from model.pin import Pin


class PinTriangle:
    def __init__(self, graph):
        self.default_triangle = graph

        self.pins = []

    def init_pins(self):
        for i, vertex in enumerate(self.default_triangle.vertices):
            self.pins.append(Pin(i, vertex))

    def print_pins(self):
        if not self.pins:
            return

        rows = {}
        for pin in self.pins:
            _, y = pin.pos
            row_key = round(y / 50) 
            rows.setdefault(row_key, []).append(pin)
        sorted_row_keys = sorted(rows.keys())

        max_row_width = max(len(row) for row in rows.values())

        for row_key in sorted_row_keys:
            row = sorted(rows[row_key], key=lambda p: p.pos[0])

            padding = "  " * (max_row_width - len(row))
            line = padding + "   ".join("X" if p.is_knocked else str(p.id) for p in row)
            print(line)


