class IntegerSet:

    def __init__(self):
        # self.input = input
        self.emp = set()
        self.internal_list = [False] * 101

    def insertElement(self, element):
        self.emp.add(element)
        self.internal_list[element] = True

    def deleteElement(self, element):
        self.emp.remove(element)
        self.internal_list[element] = False

    def print(self):
        print(self.internal_list)

    @staticmethod
    def union(set1, set2):
        union = set1.emp.union(set2.emp)
        print(union)

    @staticmethod
    def intersection(set1, set2):
        intersection = set1.emp.intersection(set2.emp)
        print(intersection)

    @staticmethod
    def isEqualTo(set1, set2):
        if set1.emp == set2.emp:
            print("Sets are Equal")
        else:
            print("Sets are not Equal")


if __name__ == "__main__":
    obj = IntegerSet()
    obj.insertElement(1)
    obj.insertElement(2)
    obj.deleteElement(1)
    obj.print()
    obj1 = IntegerSet()
    obj1.insertElement(2)
    obj1.insertElement(3)
    obj.union(obj, obj1)
    obj.intersection(obj, obj1)
    obj.isEqualTo(obj, obj1)

