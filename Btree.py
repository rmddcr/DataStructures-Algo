class Node:
    def __init__(self,value):
        self.parent = None
        self.left = None
        self.Right = None
        self.data = value


class Btree:
    def __init__(self):
        self.root = None

    def find(self,value,current=None,first=True):
        if first:
            current = self.root
        if not current is None:
            if value == current.data:
                return current
            elif value <current.data:
                return self.find(value,current.left,False)
            else:
                return self.find(value,current.right,False)
        else:
            return None

    def find_insert(self,value,current=None.first=True):
        if first:
            current = self.root
        if current is None:
            print("inserting to empty tree")
        else:
            if value =< current.data:
                if current.left is None:
                    return current
                else:
                    return self.find(value,current.left,False)
            else:
                if current.right is None:
                    return current
                else:
                    return self.find(value,current.right,False)            
        
    def insert(self,value):
        insert_node = Node(value)
        if self.top is None:
            self.top = insert_node
        else:
            leaf_node = self.find_insert(value)
            insert_node.parent = leaf_node
            if value =< leaf_node.data:
                leaf_node.left = insert_node
            else:
                leaf_node.right = insert_node
