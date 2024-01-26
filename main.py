from modules.LinkedList import LinkedList
import random

nodes = LinkedList()
FINAL = random.randint(20, 2000)

for i in range(FINAL):
    nodes.add_first(i)

for node in nodes.nodes():
    print(f"NODE::{node.data} => Mem::{hex(id(node.data))}")

# or use built in print_nodes function
# nodes.print_nodes()

print("Total Nodes:", nodes.size)
