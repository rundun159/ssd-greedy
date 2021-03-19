import numpy as np
class BLPages:
    def __init__(self, idx):
        self.block_idx = idx
        self.block_live_pages = 0
    def add_live_page(self,idx):
        self.block_live_pages += 1
    def minus_live_page(self,idx):
        assert self.block_live_pages > 0
        self.block_live_pages -= 1

a=np.empty(shape=10,dtype=BLPages)
for i in range(10):
    a[i]=BLPages(i)
for i in range(10):
    a[i].block_live_pages = 10 - i
print(a)
print(sorted(a,key=lambda x: x.block_live_pages,reverse=True))
print(a)