from .models import CostRecord
class CostStore:
    def __init__(self):self.records={}
    def put(self,r:CostRecord)->bool:
        if r.id in self.records:return False
        self.records[r.id]=r;return True
    def all(self):return list(self.records.values())
