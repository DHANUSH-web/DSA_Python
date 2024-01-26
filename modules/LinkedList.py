"""
    LinkedList Data Structure implementation
"""
from typing import Iterator


class Node:

    def __init__(self, data: any) -> None:
        self.data: any = data
        self.next: Node or None = None


class LinkedList:

    def __init__(self) -> None:
        self.head: Node or None = None
        self.size: int = 0

    def isEmpty(self) -> bool:
        return self.size == 0
    
    def add_first(self, data: any) -> None:
        node: Node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def add_last(self, data: any) -> None:
        node: Node = Node(data)

        if self.head is None:
            self.head = node

        else:
            current: Node = self.head

            while current.next != None:
                current = current.next
            
            current.next = node
        
        self.size += 1

    def insert(self, index: int, data: any) -> None:
        if self.head is None and index != 0:
            raise ValueError("Linked List is empty")
        
        if index == 0:
            self.add_first(data)

        elif index == -1:
            self.add_last(data)

        else:
            node: Node = Node(data)
            current: Node = self.head
            idx: int = 0

            while current:
                if idx == index-1:
                    break
                idx += 1
                current = current.next
            
            node.next = current.next
            current.next = node
            self.size += 1

    def nodes(self) -> Iterator[Node]:
        node: Node = self.head

        while node:
            yield node
            node = node.next

    def print_nodes(self) -> None:
        node: Node or None = self.head

        while node:
            print(node.data, end=" ", flush=True)
            node = node.next

        print(f"\n>>> Total Nodes: {self.size}", flush=True)

    def show_details(self) -> None:
        current: Node or None = self.head

        while current:
            print(f"NODE_DATA::{current.data}\tMEM_ADDR::{hex(id(current.data)).upper()}", flush=True)
            current = current.next
        
        print(f"\nTotal Nodes: {self.size}", flush=True)
