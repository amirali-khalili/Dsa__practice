head = None

def create_node(data):
    return {"data": data, "next": None}

def append(data, head):
    new = create_node(data)
    if head is None:
        return new
    
    current = head
    while current["next"]:
        current = current["next"]
    current["next"] = new
    return head

def display(head):
    current = head
    while current:
        print(current["data"], end=" → ")
        current = current["next"]
    print("None")

head = append(10, head)
head = append(20, head)
head = append(30, head)

display(head)
