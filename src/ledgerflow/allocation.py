from collections import defaultdict
def allocate_by_tag(records,key:str,default:str="unallocated"):
    out=defaultdict(float)
    for r in records:out[r.tags.get(key,default)]+=r.amount
    return {k:round(v,2) for k,v in sorted(out.items())}
