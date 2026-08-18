from datetime import date
from pydantic import BaseModel,Field
class CostRecord(BaseModel): id:str; day:date; provider:str; service:str; amount:float=Field(ge=0); currency:str="USD"; tags:dict[str,str]=Field(default_factory=dict)
class Budget(BaseModel): name:str; monthly_limit:float=Field(gt=0); owner:str="unassigned"
