class TwoThreeNode:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []         # لیست کلیدها (1 یا 2 کلید)
        self.children = children or [] # لیست فرزندان (2 یا 3 فرزند)

def search(node, key):
    if not node:
        return False
    # بررسی کلیدهای گره
    for k in node.keys:
        if key == k:
            return True
    # اگر برگ است و پیدا نکردیم
    if not node.children:
        return False
    # تصمیم گیری برای فرزند مناسب
    if key < node.keys[0]:
        return search(node.children[0], key)
    elif len(node.keys) == 1 or key < node.keys[1]:
        return search(node.children[1], key)
    else:
        return search(node.children[2], key)

def insert(node, key):
    # اگر گره خالی است
    if not node:
        return TwoThreeNode([key])
    
    # اگر برگ است
    if not node.children:
        node.keys.append(key)
        node.keys.sort()
        # اگر تعداد کلیدها > 2 → تقسیم گره
        if len(node.keys) > 2:
            return split(node)
        return node

    # پیدا کردن فرزند مناسب
    if key < node.keys[0]:
        child_index = 0
    elif len(node.keys) == 1 or key < node.keys[1]:
        child_index = 1
    else:
        child_index = 2

    child = insert(node.children[child_index], key)

    # اگر فرزند تقسیم شده
    if isinstance(child, tuple):
        left, middle_key, right = child
        node.children[child_index] = left
        node.keys.insert(child_index, middle_key)
        node.children.insert(child_index + 1, right)
        if len(node.keys) > 2:
            return split(node)
    return node

def split(node):
    # تقسیم گره 3-کلیدی به دو گره 2-کلیدی
    if len(node.keys) != 3:
        return node
    left = TwoThreeNode([node.keys[0]], node.children[:2] if node.children else [])
    right = TwoThreeNode([node.keys[2]], node.children[2:] if node.children else [])
    middle_key = node.keys[1]
    return (left, middle_key, right)

def print_tree(node, level=0):
    if node:
        print("    " * level + str(node.keys))
        for child in node.children:
            print_tree(child, level + 1)

# تست
root = None
for key in [10, 20, 5, 15, 25, 30]:
    root = insert(root, key)

print("2-3 Tree Structure:")
print_tree(root)

print("\nSearch 15:", search(root, 15))
print("Search 100:", search(root, 100))
