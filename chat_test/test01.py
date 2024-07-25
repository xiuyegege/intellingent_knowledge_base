import langchain

import os
from langchain_community.llms import Tongyi

os.environ["DASHSCOPE_API_KEY"] = 'sk-235ee0d9260b4670b5cfc64e4b1a1f62'

llm_tongyi = Tongyi()
llm_tongyi.invoke("你好")
print(llm_tongyi.invoke("你好"))