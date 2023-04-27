class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, e, func=None):
        if self.head is None:
            self.head = Element(e)
            self.tail = self.head
            self.size = 1
            return
        if self.head.nextE is None:
            greater = False
            if func is not None:
                greater = func(e, self.head.data)
            else:
                greater = e >= self.head.data
            #e is higher or equal than self.head
            if greater:
                self.head.nextE = Element(e)
                self.tail = self.head.nextE
            else:
                self.head = Element(e, self.head)
                self.tail = self.head.nextE
                self.size = 2
            return

        elif self.head is not None and self.head.nextE is not None:
            el = self.head
            if func is not None:
                greater = func(e, self.head.data)
            else:
                greater = e >= self.head.data
            if not greater:
                self.head = Element(e, self.head)
                self.size += 1
                return

            while el is not self.tail:
                if func is not None:
                    greater = func(e, el.nextE.data)
                else:
                    greater = e >= el.nextE.data
                if not greater:
                    el.nextE = Element(e, el.nextE)
                    self.size += 1
                    return
                el = el.nextE

            el.nextE = Element(e)
            self.tail = el.nextE
            self.size += 1

    def __str__(self):
        el = self.head

        if el is None:
            return str([])
        li = []
        while el.nextE is not None:
            li.append(el.data)
            el = el.nextE
        li.append(el.data)
        return str(li)

    def delete(self, e):
        if self.size == 0:
            print("brak elementow")
            return
        if e < 0 or e >= self.size:
            print("Out of bound")
            self.size -= 1
            return
        if e == 0:
            self.head = self.head.nextE
            self.size-=1
            return
        else:
            counter = 0
            element = self.head
            while counter < e-1:
                element = element.nextE
                counter+=1
            if e == self.size - 1:
                element.nextE = None
                self.tail = element
                self.size-=1
                return
            element.nextE = element.nextE.nextE


            self.size -= 1
            return

    def get(self, e):
        if e >= self.size or e < 0:
            print("Index out of Bound")
            return None
        else:
            count = 0
            element = self.head

            if e == 0:
                return element.data
            while count < e:
                element = element.nextE
                count+= 1

            return element.data
    @staticmethod
    def compareNumber(x, y):
        return x <= y
















