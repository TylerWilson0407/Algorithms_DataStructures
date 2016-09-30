class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self,i):
        self.heapList.append(i)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        # 1 index instead of 0 index -> remember dummy 0 value in 0th position
        self.heapList[1] = self.heapList.pop()
        self.percDown(1)
        self.currentSize = self.currentSize - 1
        return self.heapList[1]

    def buildHeap(self,alist):
        # i can start at size // 2 instead of size because all \
        # nodes past halfway point have no children
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i - 1

# myheap = BinHeap()
# mylist = [9, 6, 5, 2, 3]
# myheap.buildHeap(mylist)
#
# print myheap.heapList

