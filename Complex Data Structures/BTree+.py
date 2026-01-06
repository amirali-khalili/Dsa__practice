class BPlusNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusNode(True)
        self.t = t  # حداقل درجه (حداقل تعداد کلیدها در هر Node)

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2*self.t - 1):
            new_root = BPlusNode()
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        self._insert_nonfull(self.root, key)

    def _insert_nonfull(self, node, key):
        if node.leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2*self.t - 1):
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_nonfull(node.children[i], key)

    def split_child(self, parent, i):
        t = self.t
        node = parent.children[i]
        new_node = BPlusNode(node.leaf)
        parent.keys.insert(i, node.keys[t-1])
        parent.children.insert(i+1, new_node)
        new_node.keys = node.keys[t:]
        node.keys = node.keys[:t-1]
        if not node.leaf:
            new_node.children = node.children[t:]
            node.children = node.children[:t]

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level+1)


# مثال استفاده
tree = BPlusTree(2)  # حداقل درجه 2
for key in [10, 20, 5, 6, 12, 30, 7, 17]:
    tree.insert(key)

tree.print_tree()
