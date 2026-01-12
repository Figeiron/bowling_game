from model.pin_triangle import PinTriangle
from model.kick import Kick
from graph_theory.IO.GraphLoaderJSON import GraphLoaderJSON
from graph_theory.controller.GraphController import GraphController
from model.round import Round

default_triangle = GraphLoaderJSON().load("pin_triangle_schema.json")
triangle_controller = GraphController(default_triangle)

triangle = PinTriangle(default_triangle)
triangle.init_pins()

kick = Kick(triangle_controller, triangle)
round = Round(kick, triangle)

round.run()