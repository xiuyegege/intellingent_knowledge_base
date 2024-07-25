import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response


def initialize_session_state():
    # 初始化session_state，如果第一次运行
    if "memory" not in st.session_state:
        st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "ai", "content": "你好，我是你的AI助手，有什么可以帮你的吗？"}
        ]


def display_conversation():
    # 显示历史对话记录
    for message in st.session_state["messages"]:
        st.chat_message(message["role"]).write(message["content"])


def handle_user_input():
    # 处理用户输入
    prompt = st.chat_input()
    if prompt:
        if not st.session_state.get("api_key"):
            st.info("请输入你的通义 API Key")
            st.stop()

        st.session_state["messages"].append({"role": "human", "content": prompt})
        st.chat_message("human").write(prompt)

        with st.spinner("AI正在思考中，请稍等..."):
            response = get_chat_response(prompt, st.session_state["memory"], st.session_state["api_key"])

        msg = {"role": "ai", "content": response}
        st.session_state["messages"].append(msg)
        st.chat_message("ai").write(response)


def main():
    # 主函数
    st.title("💬 智能知识库聊天对话测试")

    # 从侧边栏获取OpenAI API Key
    with st.sidebar:
        st.session_state["api_key"] = st.text_input("请输入通义 API Key：", type="password")
        st.markdown("[获取通义API key](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key)")

    initialize_session_state()
    display_conversation()
    handle_user_input()


if __name__ == "__main__":
    main()