import random
from graph_theory.algorithms.Algorithm import Algorithm, AlgorithmEvent, AlgorithmEventType


class DFS(Algorithm):
    def __init__(self, graph, start_vertex, end_vertex=None):
        super().__init__(graph)
        self.name = "DFS (Random)"
        self.start = start_vertex
        self.end = end_vertex


        edges = list(start_vertex.get_from_edges())
        random.shuffle(edges)

        self.stack = [(start_vertex, iter(edges))]
        self.visited = {start_vertex}

        self.parent = {}
        self.parent_edge = {}

        self.last_event_was_visit = False

    def step(self):
        if self.finished:
            return AlgorithmEvent(AlgorithmEventType.FINISHED)

        if not self.stack:
            self.finished = True
            return AlgorithmEvent(AlgorithmEventType.FINISHED)

        u, edge_iter = self.stack[-1]

        if not self.last_event_was_visit:
            self.last_event_was_visit = True
            return AlgorithmEvent(
                AlgorithmEventType.VISIT_VERTEX,
                vertex=u
            )

        try:
            edge = next(edge_iter)
            v = edge.to_vertex

            if v not in self.visited:
                self.visited.add(v)
                self.parent[v] = u
                self.parent_edge[v] = edge

                edges = list(v.get_from_edges())
                random.shuffle(edges)

                self.stack.append((v, iter(edges)))
                self.last_event_was_visit = False

                if v == self.end:
                    pass

                return AlgorithmEvent(
                    AlgorithmEventType.DISCOVER_VERTEX,
                    from_vertex=u,
                    to_vertex=v,
                    edge=edge
                )
            else:
                return None

        except StopIteration:
            self.stack.pop()
            self.last_event_was_visit = True

            if not self.stack:
                self.finished = True
                return AlgorithmEvent(AlgorithmEventType.FINISHED)

            return AlgorithmEvent(
                AlgorithmEventType.BACKTRACK,
                vertex=u
            )

    def get_path(self):
        if not self.end or self.end not in self.parent:
            return []

        path = []
        v = self.end
        while v != self.start:
            path.append(v)
            v = self.parent[v]
        path.append(self.start)

        return list(reversed(path))
