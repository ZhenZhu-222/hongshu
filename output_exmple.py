from  langchain_core.pydantic_v1 import BaseModel,Field
from typing import List

#!!!!!!!!!!!!!!!!!!! BaseModel用在这了
class XIAOHONGSHU(BaseModel) :
     titles:list[str]=Field("小红书的五个标题",min_items=5,max_items=5)
     content:str=Field("小红书的正文内容")