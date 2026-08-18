from datetime import date
from .store import CostStore
from .models import CostRecord,Budget
from .analytics import anomalies,forecast
from .allocation import allocate_by_tag
class FinOpsService:
    def __init__(self):self.store=CostStore();self.budgets={}
    def ingest(self,r:CostRecord):return {"accepted":self.store.put(r),"id":r.id}
    def allocate(self,key):return allocate_by_tag(self.store.all(),key)
    def anomalies(self):return anomalies(self.store.all())
    def forecast(self,days=7):return forecast(self.store.all(),days)
    def set_budget(self,b:Budget):self.budgets[b.name]=b;return b
    def budget_status(self,name:str,month:str):
        b=self.budgets[name]; spent=sum(r.amount for r in self.store.all() if r.day.strftime("%Y-%m")==month)
        return {"name":name,"spent":round(spent,2),"limit":b.monthly_limit,"remaining":round(b.monthly_limit-spent,2),"utilization":round(spent/b.monthly_limit,4)}
