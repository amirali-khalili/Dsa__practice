def build_suffix_tree(s):
    root = {}   
    indexes = {}  

    for i in range(len(s)):
        current = root
        path = ""
        for c in s[i:]:
            path += c
            if c not in current:
                current[c] = {}
                indexes[path] = []
            indexes[path].append(i)
            current = current[c]

    return root, indexes

def print_suffix_tree(node, indexes, prefix=""):
    for char, child in node.items():
        path = prefix + char
        print(path, "->", indexes[path])
        print_suffix_tree(child, indexes, path)

text = "banana"
tree, indexes = build_suffix_tree(text)
print_suffix_tree(tree, indexes)
