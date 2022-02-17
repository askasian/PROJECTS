class Try:
    def do_somthing(self):
        print("Hello")


if __name__ == "__main__":
    obj_list = []
    for obj in range(10):
        obj = Try()
        obj_list.append(obj)

for i in range(len(obj_list)):
    obj_list[i].do_somthing()
