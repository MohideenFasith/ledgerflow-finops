from fastapi import FastAPI,HTTPException,Query
from .models import CostRecord,Budget
from .service import FinOpsService
app=FastAPI(title="LedgerFlow FinOps",version="0.1.0");service=FinOpsService()
@app.get("/health")
def health():return {"status":"ok"}
@app.post("/costs",status_code=202)
def costs(r:CostRecord):return service.ingest(r)
@app.get("/allocation")
def allocation(tag:str="team"):return service.allocate(tag)
@app.get("/anomalies")
def anomaly():return service.anomalies()
@app.get("/forecast")
def fc(days:int=Query(7,ge=1,le=90)):return service.forecast(days)
@app.post("/budgets",status_code=201)
def budget(b:Budget):return service.set_budget(b)
@app.get("/budgets/{name}")
def budget_status(name:str,month:str):
    try:return service.budget_status(name,month)
    except KeyError:raise HTTPException(404,"budget not found")
