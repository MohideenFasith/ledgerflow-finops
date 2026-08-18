from collections import defaultdict
from statistics import median

def daily_totals(records):
    d=defaultdict(float)
    for r in records:d[r.day]+=r.amount
    return dict(sorted(d.items()))

def anomalies(records,threshold:float=3.5):
    totals=daily_totals(records); vals=list(totals.values())
    if len(vals)<3:return []
    med=median(vals); mad=median([abs(v-med) for v in vals])
    if mad==0:return []
    out=[]
    for day,v in totals.items():
        score=.6745*(v-med)/mad
        if abs(score)>=threshold:out.append({"day":day.isoformat(),"amount":round(v,2),"score":round(score,3)})
    return out

def forecast(records,days:int=7):
    totals=daily_totals(records); y=list(totals.values())
    if not y:return {"daily":[],"total":0.0}
    if len(y)==1:slope=0.0
    else:slope=(y[-1]-y[0])/(len(y)-1)
    daily=[round(max(0,y[-1]+slope*i),2) for i in range(1,days+1)]
    return {"daily":daily,"total":round(sum(daily),2)}
