import random

class Node:
    def __init__(self, id):
        self.id = id
        self.alive = True
        self.coordinator = None

    def election(self, nodes):
        higher_nodes = [node for node in nodes if node.id > self.id and node.alive]
        if not higher_nodes:
            self.coordinator = self
            for node in nodes:
                if node != self:
                    node.notify_elected(self)
        else:
            higher_nodes.sort(key=lambda x: x.id)
            highest_node = higher_nodes[-1]
            highest_node.start_election(nodes)

    def start_election(self, nodes):
        print(f"Node {self.id} starts the election.")
        higher_nodes = [node for node in nodes if node.id > self.id and node.alive]
        if not higher_nodes:
            self.coordinator = self
            for node in nodes:
                if node != self:
                    node.notify_elected(self)
        else:
            for node in higher_nodes:
                node.election(nodes)

    def notify_elected(self, coordinator):
        print(f"Node {self.id} is notified of new coordinator: Node {coordinator.id}")
        self.coordinator = coordinator

    def crash(self):
        self.alive = False
        print(f"Node {self.id} crashed.")

    def __str__(self):
        return f"Node {self.id}, Coordinator: {self.coordinator.id if self.coordinator else None}"


if __name__ == "__main__":
    num_nodes = 5
    nodes = [Node(i) for i in range(1, num_nodes + 1)]
    nodes[random.randint(1, 5)].start_election(nodes)
    nodes[random.randint(1, 5)].crash()
    print(nodes[2])
    print(nodes[3])
