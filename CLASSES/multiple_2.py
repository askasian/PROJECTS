class MyClass:
    # objs = []

    def __init__(self):
        pass

    def do_sth(a):
        print("doing now in MyClass!")


objs = list()
for i in range(10):
    objs.append(MyClass())

objs[0].do_sth()
