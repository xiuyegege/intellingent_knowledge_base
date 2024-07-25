from langchain.chains import ConversationChain
import os
from langchain_community.llms import Tongyi

def get_chat_response(prompt, memory, api_key):
    model = Tongyi(dashscope_api_key=api_key)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]
