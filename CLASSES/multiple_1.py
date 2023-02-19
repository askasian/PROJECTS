class MyClass:
    # objs = []

    def __init__(self):
        pass

    def do_sth(a):
        print("doing now in MyClass!")


objs = [MyClass() for i in range(10)]
# for obj in objs:
#     obj.append(objs)


objs[2].do_sth()
