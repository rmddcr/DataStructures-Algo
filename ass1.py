class Edge:
    def __init__(self,val):
        self.data = val
        self.color = None
        self.adj = []
        self.p = None

class Graph():
    def __init__(self):
        self.verts = []
    def addvert(self,vert):
        for i in self.verts:
            if i.data == vert:
                    return
        node  = Edge(vert)
        self.verts.append(node)
    def addedge(self,edg):
        vert1 = None
        vert2 = None
        for i in self.verts:

            if i.data == edg[0]:
                vert1 = i
            elif i.data == edg[1]:
                vert2 = i
        if not ((vert1 == None) or (vert2 == None)):

            for a in vert1.adj:
                if not a is None:
                    if a.data == vert2.data:
                        print(a.data)
                        return
            vert1.adj.append(vert2)
            vert2.adj.append(vert1)

    def bft(self,queue):
        if queue == []:
            return False
        else:
            now = queue.pop(0)
            if now.color == "m":
                chi_color = "f"
            else:
                chi_color = "m"
            for child in now.adj:
                if not child.color is None:
                    if now.color == child.color:
                        return True
                else:
                    child.color = chi_color
                    child.p = now
                    queue.append(child)
            return self.bft(queue)

    def chck(self):
        qu = [self.verts[0]]
        self.verts[0].color = "m"

        ch = self.bft(qu)

        if ch :
            print("yes")
        else:
            print("no")

g= Graph()

lists = [(1,2),(2,3),(3,4),(4,5)]
for v in lists:
    g.addvert(v[0])
    g.addvert(v[1])
    g.addedge(v)


for v in g.verts:
    print v.data
    st="["
    for a in v.adj:
        st += str(a.data) +" ,"
    print st
g.chck()
