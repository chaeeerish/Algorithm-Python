import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, item, x, y):
        self.item = item
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def get_left_item(self):
        if self.left is None:
            return 0
        else:
            return self.left.item

    def get_right_item(self):
        if self.right is None:
            return 0
        else:
            return self.right.item

class BinaryTree:
    def __init__(self, root):
        self.root = root

def addNode(parent: Node, item: Node):
    if parent.x > item.x:
        if parent.left:
            addNode(parent.left, item)
        else:
            parent.left = item
    else:
        if parent.right:
            addNode(parent.right, item)
        else:
            parent.right = item

def pre_order(item: Node):
    path = [item.item]
    if item.left:
        path += pre_order(item.left)
    if item.right:
        path += pre_order(item.right)
    return path

def post_order(item: Node):
    path = []
    if item.left:
        path += post_order(item.left)
    if item.right:
        path += post_order(item.right)
    path += [item.item]
    return path

def solution(nodeinfo):
    nodeList = []
    for i in range(len(nodeinfo)):
        nodeList.append(Node(i + 1, nodeinfo[i][0], nodeinfo[i][1]))
    nodeList.sort(key=lambda node: (-node.y, node.x))

    tree = BinaryTree(nodeList[0])

    previous = tree.root
    for i in range(1, len(nodeList)):
        addNode(tree.root, nodeList[i])

    ##
    # for node in nodeList:
    #     print(node.item, "은", node.get_left_item(), "과 왼쪽으로 연결,", node.get_right_item(), "와 오른쪽으로 연결되어있다.")

    # 전위 순회
    전위_순회 = pre_order(tree.root)

    # 후위 순회
    후위_순회 = post_order(tree.root)

    return [pre_order(tree.root), post_order(tree.root)]

# [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
