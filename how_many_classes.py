# BFS
st = {type}
queue = [object]

while queue:
    fa_t = queue.pop(0)
    if fa_t not in st:
        st.add(fa_t)
        print "%s's father is %s" % (fa_t, fa_t.__bases__)
        for t in fa_t.__subclasses__():
            queue.append(t)

print len(st)  # 685


# DFS
st = {type}

def f(fa_t):
    if fa_t not in st:
        st.add(fa_t)
        for t in fa_t.__subclasses__():
            f(t)
f(object)
print len(st)
