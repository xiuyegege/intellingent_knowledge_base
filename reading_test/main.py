import streamlit as st

from langchain.memory import ConversationBufferMemory
from core import qa_agent

def setup_streamlit_interface():
    """
    设置Streamlit界面，包括标题、侧边栏输入API密钥、文件上传器和问题输入框。
    """
    # 设置页面标题
    st.title("📑 本地知识库PDF问答工具")

    # 侧边栏获取API密钥
    with st.sidebar:
        api_key = st.text_input("请输入千问 API密钥：", type="password")

    # 初始化会话记忆
    if "memory" not in st.session_state:
        st.session_state["memory"] = ConversationBufferMemory(
            return_messages=True,
            memory_key="chat_history",
            output_key="answer"
        )

    # 文件上传器
    uploaded_file = st.file_uploader("上传你的PDF文件：", type="pdf")

    # 提问输入框
    question = st.text_input("对PDF的内容进行提问", disabled=not uploaded_file)

    return api_key, uploaded_file, question

def handle_user_input(api_key, uploaded_file, question):
    """
    根据用户输入处理PDF文件和提问，调用qa_agent进行问答。
    """
    # 检查是否已输入API密钥
    if uploaded_file and question and not api_key:
        st.info("请输入你的千问 API密钥")
        return

    # 如果有上传文件、问题且有API密钥，则进行问答
    if uploaded_file and question and api_key:
        with st.spinner("AI正在思考中，请稍等..."):
            response = qa_agent(api_key, st.session_state["memory"],
                                uploaded_file, question)
        st.write("### 答案")
        st.write(response["answer"])
        st.session_state["chat_history"] = response["chat_history"]

def display_chat_history():
    """
    显示历史聊天记录。
    """
    if "chat_history" in st.session_state:
        with st.expander("历史消息"):
            for i in range(0, len(st.session_state["chat_history"]), 2):
                human_message = st.session_state["chat_history"][i]
                ai_message = st.session_state["chat_history"][i+1]
                st.write(human_message.content)
                st.write(ai_message.content)
                if i < len(st.session_state["chat_history"]) - 2:
                    st.divider()

# 主函数，组织上述功能
def main():
    api_key, uploaded_file, question = setup_streamlit_interface()
    handle_user_input(api_key, uploaded_file, question)
    display_chat_history()

# 运行主函数
if __name__ == "__main__":
    main()
