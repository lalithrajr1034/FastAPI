from pydantic import BaseModel
from typing import Optional, List, Dict


class pydantic_model(BaseModel):
    name:str
    gender:bool
    contact_details:Dict[str, str]
    

def persnal_info(object):
    print(object.name)
    print(obj.gender)

# data = {'name':'Lalith Raj R', 'gender':True, 'contact_details':{'mobile_nor':'13254135345', 'gmail':'lalith@gmail.com'}}
obj = pydantic_model(name='lalith raj r', gender= True ,contact_details={'gmail':'lalithrajr1034@gmail.com'})
persnal_info(obj)
