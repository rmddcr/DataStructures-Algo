class vertex:
    def __init__(self,index,_object):
        self.index = index
        self._object = _object
        self.adj = []
        self.traversed = False
        self.in_time = -1
        self.out_time = -1
        self.prev = None
        self.next = None

class edge:
    def __init__(self,_in,weight):
        self._in = _in
        self.weight = weight


class graph:
    def __init__(self,directed = False,weighted = False):
        self.top = None
        self.tail = None
        self.directed = directed
        self.weighted = weighted

    def search_vertex(self,index,current=-1):
        if current == -1:
            current = self.top
        if current is None:
            return None
        elif current.index == index:
            return current
        else:
            return self.search_vertex(index,current.next)

    def search_edge(self,edges,index):
        for i in range(0,len(edges)):
            if edges[i]._in.index == index:
                return i
        return None

    def add_vertex(self,index,_object=None):
        if self.search_vertex(index) is None:
            new_vertex = vertex(index,_object)

            if self.top is None:
                self.top = new_vertex
                self.tail = new_vertex
            else:
                self.tail.next = new_vertex
                new_vertex.prev = self.tail
                self.tail = new_vertex
            return True
        else:
            return False

    def add_edge(self,index1,index2,weight=None):
        if self.weighted and (weight is None):
            print("Weight not given on edge creation on weighted graph")
            return False
        if (not self.weighted) and (not weight is None):
            print("Weight given for non-weighted graph on edge creation")
            return False
        out = self.search_vertex(index1)
        _in = self.search_vertex(index2)
        ret_val = False
        if self.search_edge(out.adj,index2) is None:
                edge1 = edge(_in,weight)
                out.adj.append(edge1)
                ret_val = True
        if not self.directed:
            if self.search_edge(_in.adj,index1) is None:
                    edge2 = edge(out,weight)
                    _in.adj.append(edge2)
            else:
                ret_val = False
        return ret_val

    def print_graph(self,current=-1):
        if current == -1:
            current = self.top
        if not current is None:
            st = ""
            st += str(current.index) + " : ["
            for e in current.adj:
                st += "(" + str(e._in.index)
                if self.weighted:
                    st +=  "," + str(e.weight)
                st +="), "
            st += "]"
            print(st)
            self.print_graph(current.next)

    def make_path(self,current,path=-1):
        if path == -1:
            path = [current]
        if not current is None:
            path.append(path[-1].prev)
            return self.make_path(path[-1],path)
        else:
            path.pop(-1)
            path.reverse()
            return path

    def BFT(self,start,end,queue=None,time=0):
        if queue is None:
            #print
            print("#### BFT ####")
            print("")
            #print
            start_vertex = self.search_vertex(start)
            if start_vertex is None:
                return None
            else:
                start_vertex.traversed = True
                start_vertex.in_time = time
                queue = [start_vertex]

        if not queue == []:
            current = queue.pop(0)
            current.time = time
            #print
            print "level :" + str(time) + " ,Vertex :" + str(current.index)
            #print
            if current.index == end:
                current.traversed = True
                print("#### END OF BFT ####")
                return self.make_path(current)
            else:
                #print
                st="---> out : "
                #print
                for e in current.adj:
                    a = e._in
                    #print
                    st+= str(a.index) + ", "
                    #print
                    if not a.traversed:
                        a.traversed = True
                        a.prev = current
                        queue.append(a)
                print(st)
                print("---------------------------")
                return self.BFT(start,end,queue,time+1)

        else:
            return None

    def clear_all(self,current=-1):
        if current == -1:
            current = self.top
        current.traversed = False
        current.prev = None
        current.in_time = -1
        current.out_time = -1

    def print_path(self,path):
        st = "["
        for v in path:
            st += str(v.index) + ", "
        st += "]"
        print(st)

    def search_path(self,start,end):
        self.clear_all()
        if not self.weighted:
            path = self.BFT(start,end)
        else:
            path = self.BFT(start,end)

        if not path is None:
            self.print_path(path)
        return path


g= graph(True,True)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')
g.add_vertex('G')
g.add_edge('A','B',2)
g.add_edge('B','C',4)
g.add_edge('C','D',2)
g.add_edge('A','E',6)
g.add_edge('B','F',1)

g.print_graph()

g.search_path('A','D')
