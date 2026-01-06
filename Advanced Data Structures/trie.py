class TrieNode:
    def __init__(self):
        self.children = {}          
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return []

        results = []

        def dfs(current_node, path):
            if current_node.is_end_of_word:
                results.append("".join(path))
            for ch, next_node in current_node.children.items():
                dfs(next_node, path + [ch])

        dfs(node, list(prefix))
        return results

 
trie = Trie()

words = ["cat", "car", "cart", "dog", "door", "deer", "deal"]
for w in words:
    trie.insert(w)

print(trie.search("cat"))    
print(trie.search("ca"))     

prefix = input("pishvand :")
suggestions = trie.autocomplete(prefix)
if suggestions:
    print("pisnahad:", suggestions)
else:
    print("not fonded !")
