from spisok_del import *
def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node

def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    previous_node = get_node_by_index(head, index-1)
    new_node.next = previous_node.next 
    previous_node.next = new_node
    return head


node5 = Node("node5", None)
node4 = Node("node4", node5)
node3 = Node("node3", node4)
node2 = Node("node2", node3)
node1 = Node("node1", node2)
node0 = Node("node0", node1)

node, index, value = node0, 3, 'new_node'
head = insert_node(node, index, value)
print(solution(head))