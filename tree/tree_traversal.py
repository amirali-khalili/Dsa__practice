class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        
def inorder(node):
    if node:
        inorder(node.left)      
        print(node.value, end=" ")  
        inorder(node.right)     

def preorder(node):
    if node:
        print(node.value, end=" ")  
        preorder(node.left)          
        preorder(node.right)        

def postorder(node):
    if node:
        postorder(node.left)             
        postorder(node.right)            
        print(node.value, end=" ")

from collections import deque
def bfs(root):
    if not root:
        return
    
    queue = deque([root]) 
    
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")  
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")


print("Inorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)
print("\nbfs Traversal:")
bfs(root)
