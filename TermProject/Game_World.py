objects = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

def Add_Object(obj, depth):
    objects[depth].append(obj)


def Add_Objects(ol, depth):
    objects[depth] += ol


def All_Objects():
    for layer in objects:
        for obj in layer:
            yield obj


def Clear():
    for obj in All_Objects():
        del obj
    for layer in objects:
        layer.clear()


def Remove_Object(obj):
    for layer in objects:
        if obj in layer:
            layer.remove(obj)
            del obj

    raise ValueError('Trying Destroy non existing object')