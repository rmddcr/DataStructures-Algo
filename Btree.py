class Node:
    def __init__(self,value):
        self.parent = None
        self.left = None
        self.right = None
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

    def find_insert(self,value,current):

        if value <= current.data:
            if current.left is None:
                return current
            else:
                return self.find_insert(value,current.left)
        else:
            if current.right is None:
                return current
            else:
                return self.find_insert(value,current.right)

    def insert(self,value):
        insert_node = Node(value)
        if self.root is None:
            self.root = insert_node
        else:
            leaf_node = self.find_insert(value,self.root)
            insert_node.parent = leaf_node
            if value <= leaf_node.data:
                leaf_node.left = insert_node
            else:
                leaf_node.right = insert_node
    def print_btree(self,print_queue):
        st=""
        new_queue = []
        if not print_queue == []:
            for p in print_queue:
                if p is None:
                    st += "|None| "
                else:
                    st += "|"+str(p.data) +"| "
                    new_queue.append(p.left)
                    new_queue.append(p.right)
            print st
            self.print_btree(new_queue)
        else:
            return

    def print_inorder(self,current):
        if current is None:
            print("None")
        if not current.left is None:
            self.print_inorder(current.left)
        print(current.data)
        if not current.right is None:
            self.print_inorder(current.right)

    def find_left_subtree_right_most_child(self,current):
        if current.right is None:
            current.parent.right = current.left
            current.left.parent = current.parent
            current.left = None
            current.parent = None
            return current
        else:
            return self.find_left_subtree_right_most_child(current.right)
    def find_right_subtree_left_most_child(self,current):
        if current.left is None:
            return current
        else:
            return self.find_right_subtree_left_most_child(current.left)

    def remove(self,value):
        remove_node = self.find(value)
        if remove_node is None:
            print "Invalid vertex to remove"
            return False
        else:
            parent = remove_node.parent
            remove_node.parent = None
            if (remove_node.left is None) and (remove_node.right is None):
                if parent is None:
                    self.root = None
                elif value <= parent.data:
                    parent.left = None
                else:
                    parent.right = None

            elif remove_node.left is None:
                if parent is None:
                    self.root = remove_node.right
                    self.root.parent = None
                elif value <= parent.data:
                    parent.left = remove_node.right
                    parent.left.parent = parent
                else:
                    parent.right = remove_node.right
                    parent.right.parent = parent

            elif remove_node.right is None:
                if parent is None:
                    self.root = remove_node.left
                    self.root.parent = None
                elif value <= parent.data:
                    parent.left = remove_node.left
                    parent.left.parent = parent
                else:
                    parent.right = remove_node.left
                    parent.right.parent = parent

            else:
                child = self.find_left_subtree_right_most_child(remove_node.left)
                child.left = remove_node.left
                child.right = remove_node.right
                if parent is None:
                    self.root = child
                    self.root.parent = None
                elif value <= parent.data:
                    parent.left = child
                    parent.left.parent = parent
                else:
                    parent.right = child
                    parent.right.parent = parent





t = Btree()
t.insert(4)
t.insert(6)
t.insert(5)
t.insert(7)
t.insert(8)
t.insert(1)
t.insert(3)
t.insert(2)
t.insert(-3)
t.insert(-1)
t.insert(-4)
t.print_btree([t.root])
t.remove(3)
t.print_btree([t.root])
t.remove(4)
t.print_btree([t.root])
t.remove(5)
t.print_btree([t.root])
t.remove(7)
t.print_btree([t.root])
#t.print_inorder(t.root)
