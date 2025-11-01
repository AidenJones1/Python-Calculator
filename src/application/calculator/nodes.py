# Internal Node
class OperatorNode():
    def __init__(self, value: str, right_node: OperatorNode | NumberNode, left_node: OperatorNode | NumberNode) -> None:
        self.value = value
        self.children = [right_node, left_node]

# Leaf Node
class NumberNode():
    def __init__(self, value: str):
        self.value = value
