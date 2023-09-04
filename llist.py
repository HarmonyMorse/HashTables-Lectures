class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({repr(self.value)})'


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        """Print entire linked list"""

        if self.head is None:
            return "[Empty List]"

        cur = self.head
        s = ""

        while cur != None:
            s += f'({cur.value}'

            if cur.next is not None:
                s += '-->'

            cur = cur.next

        return s

    def find(self, value):
        cur = self.head

        while cur is not None:
            if cur.value == value:
                return cur

            cur = cur.next

        return None

    def delete(self, value):
        cur = self.head

        # Special case of deleting head

        if cur.value == value:
            self.head = cur.next
            return cur

        # General case of deleting internal node

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:  # found it!
                prev.next = cur.next  # cut it out
                return cur  # return deleted node
            else:
                prev = cur
                cur = cur.next

        return None  # if we got here, nothing found

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_or_overwrite_value(self, value):
        node = self.find(value)

        if node is None:
            # Make a new node
            self.insert_at_head(Node(value))
        else:
            # Overwrite old value
            node.value = value


