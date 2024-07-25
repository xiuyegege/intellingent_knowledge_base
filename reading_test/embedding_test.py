from dotenv import find_dotenv, load_dotenv
from langchain.embeddings import DashScopeEmbeddings

load_dotenv(find_dotenv())
dashscope_api_key = "sk-235ee0d9260b4670b5cfc64e4b1a1f62"

# 创建 DashScopeEmbeddings 对象
embedding = DashScopeEmbeddings(
    model="text-embedding-v1",  # 通义千问的文本向量模型名称
    dashscope_api_key=dashscope_api_key
)

# 要进行文本向量化的文本
text = "这是要进行向量化的文本"

# 执行文本向量化
vector = embedding.embed_query(text)
print(vector)