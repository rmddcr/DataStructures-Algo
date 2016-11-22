class vertex:
    def __init__(self,data):
        self.data = data
        self.color = None
        self.dt = None
        self.ft = None
        self.adj = []
        self.prev = None

class graph:
    def __init__(self):
        self.vertices = []
        self.time = 0
        self.search_list = []

    def addVert(self,vert):
        for v in self.vertices:
            if v.data == vert:
                return
        node = vertex(vert)
        self.vertices.append(node)

    def addEdge(self,edge):
        vert1 = None
        vert2 = None
        for v in self.vertices:
            if v.data == edge[0]:
                vert1 = v
            elif v.data == edge[1]:
                vert2 = v
        if not (vert1 is None or vert2 is None):
            for e in vert1.adj:
                if e.data == edge[1]:
                    return
            vert1.adj.append(vert2)
    def dft(self):
        for v in self.vertices:
            if v.color is None:
                self.time = 0
                self.dft_visit(v)
        self.search_list.reverse()

    def dft_visit(self, now):
        self.time +=1
        now.dt = self.time
        now.color = "gray"
        for a in now.adj:
             if a.color is None:
                 a.prev = now
                 self.dft_visit(a)
        now.color = "black"
        self.time +=1
        now.ft = self.time
        self.search_list.append(now.data)

    def dft_make_components(self, s_list):








g = graph()
inp = [(1,2),(2,3),(3,4),(1,11),(11,22)]
h = graph()
for i in inp:
    g.addVert(i[0])
    g.addVert(i[1])
    g.addEdge(i)

for i in inp:
    h.addVert(i[0])
    h.addVert(i[1])
    h.addEdge((i[1],i[0]))
g.dft()

h.dft()
# for v in g.vertices:
#     print v.data
#     print str(v.dt) + " / " + str(v.ft)
#     st = "["
#     for a in v.adj:
#         st += str(a.data) + " ,"
#     print st + " ]"

#
for v in g.vertices:
    print v.data
    print str(v.dt) + " / " + str(v.ft)
    st = "["
    for a in v.adj:
        st += str(a.data) + " ,"
    print st + " ]"

print g.search_list

print("############ Done ################")

for v in h.vertices:
    print v.data
    print str(v.dt) + " / " + str(v.ft)
    st = "["
    for a in v.adj:
        st += str(a.data) + " ,"
    print st + " ]"
