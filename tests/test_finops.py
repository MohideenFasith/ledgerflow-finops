from datetime import date,timedelta
from ledgerflow.models import CostRecord,Budget
from ledgerflow.service import FinOpsService

def test_allocation_budget_forecast():
    s=FinOpsService();base=date(2026,1,1)
    for i,v in enumerate([10,12,14]):s.ingest(CostRecord(id=str(i),day=base+timedelta(days=i),provider="aws",service="compute",amount=v,tags={"team":"ml"}))
    assert s.allocate("team")["ml"]==36
    s.set_budget(Budget(name="cloud",monthly_limit=100))
    assert s.budget_status("cloud","2026-01")["spent"]==36
    assert s.forecast(2)["daily"]==[16.0,18.0]
