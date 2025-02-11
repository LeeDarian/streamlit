import streamlit as st
import hashlib

# Page configuration
st.set_page_config(
    page_title="Stack & Queue Visualization | 栈与队列可视化",
    page_icon="🔄",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    .element-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Password functionality
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        # Hash for 'CUHKSZ'
        if hashlib.sha256(str(st.session_state["password"]).encode()).hexdigest() == "c5c04c5b74d7d390bd11c7bc34b111d7cb0f0f397eb8cc4576e8969b502104df":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.image("https://www.cuhk.edu.cn/sites/webmaster.prod1.dpsite04.cuhk.edu.cn/files/zh-hans_logo.png", width=200)
        st.markdown("""
        ### Welcome to Data Structure Visualization | 欢迎使用数据结构可视化工具
        Please enter the password to access the visualization tool.  
        请输入密码以访问可视化工具。
        """)
        st.text_input(
            "Password | 密码", 
            type="password", 
            on_change=password_entered, 
            key="password",
            placeholder="Enter password | 请输入密码"
        )
        return False
    
    elif not st.session_state["password_correct"]:
        st.image("https://www.cuhk.edu.cn/sites/webmaster.prod1.dpsite04.cuhk.edu.cn/files/zh-hans_logo.png", width=200)
        st.text_input(
            "Password | 密码", 
            type="password", 
            on_change=password_entered, 
            key="password",
            placeholder="Enter password | 请输入密码"
        )
        st.error("😕 Incorrect password, please try again | 密码错误，请重试")
        return False
    
    return True

# Author information
def show_author_info():
    st.sidebar.markdown("### Author Information | 作者信息")
    st.sidebar.markdown("""
    **Name | 姓名:** Li Dingyang (李定洋)  
    **Email | 邮箱:** [222051031@link.cuhk.edu.cn](mailto:222051031@link.cuhk.edu.cn)  
    **Institution | 单位:** The Chinese University of Hong Kong, Shenzhen  
    """)

def show_stack():
    st.header("Stack (栈) - LIFO")
    st.markdown("""
    ### Operations | 操作
    - **Push | 入栈:** Add element to top | 将元素添加到栈顶
    - **Pop | 出栈:** Remove element from top | 从栈顶移除元素
    - **Principle | 原理:** Last-In-First-Out | 后进先出
    """)
    
    if 'stack' not in st.session_state:
        st.session_state.stack = []
    
    # 使用columns分割左右两侧
    left_col, right_col = st.columns([1, 2])
    
    # 左侧：输入和操作按钮
    with left_col:
        st.markdown("### Input & Operations | 输入与操作")
        new_item = st.text_input("Enter element | 输入元素", key="stack_input")
        if st.button("Push | 入栈"):
            if new_item:
                st.session_state.stack.append(new_item)
                st.success(f"Pushed: {new_item} | 已入栈: {new_item}")
        
        if st.button("Pop | 出栈"):
            if st.session_state.stack:
                popped = st.session_state.stack.pop()
                st.success(f"Popped: {popped} | 已出栈: {popped}")
            else:
                st.error("Stack is empty! | 栈为空！")
    
    # 右侧：状态显示
    with right_col:
        st.markdown("### Current Stack Status | 当前栈状态")
        if st.session_state.stack:
            for item in reversed(st.session_state.stack):
                st.markdown(f"""
                <div style='text-align: center; padding: 10px; 
                            background-color: #e6f3ff; margin: 5px; 
                            border: 2px solid #0066cc; border-radius: 5px;'>
                    {item}
                </div>
                """, unsafe_allow_html=True)
            st.markdown("<div style='text-align: center;'>⬇ Stack Bottom | 栈底 ⬇</div>", unsafe_allow_html=True)
        else:
            st.info("Stack is empty | 栈为空")

def show_queue():
    st.header("Queue (队列) - FIFO")
    st.markdown("""
    ### Operations | 操作
    - **Enqueue | 入队:** Add element to rear | 将元素添加到队尾
    - **Dequeue | 出队:** Remove element from front | 从队头移除元素
    - **Principle | 原理:** First-In-First-Out | 先进先出
    """)
    
    if 'queue' not in st.session_state:
        st.session_state.queue = []
    
    # 使用columns分割左右两侧
    left_col, right_col = st.columns([1, 2])
    
    # 左侧：输入和操作按钮
    with left_col:
        st.markdown("### Input & Operations | 输入与操作")
        new_item = st.text_input("Enter element | 输入元素", key="queue_input")
        if st.button("Enqueue | 入队"):
            if new_item:
                st.session_state.queue.append(new_item)
                st.success(f"Enqueued: {new_item} | 已入队: {new_item}")
        
        if st.button("Dequeue | 出队"):
            if st.session_state.queue:
                dequeued = st.session_state.queue.pop(0)
                st.success(f"Dequeued: {dequeued} | 已出队: {dequeued}")
            else:
                st.error("Queue is empty! | 队列为空！")
    
    # 右侧：状态显示
    with right_col:
        st.markdown("### Current Queue Status | 当前队列状态")
        if st.session_state.queue:
            st.markdown("""
            <div style='display: flex; justify-content: center; align-items: center; gap: 10px;'>
                <div style='font-weight: bold;'>Front | 队头</div>
                {}
                <div style='font-weight: bold;'>Rear | 队尾</div>
            </div>
            """.format(" → ".join([f"<div style='padding: 10px; background-color: #f0fff0; border: 2px solid #006400; border-radius: 5px;'>{item}</div>" for item in st.session_state.queue])), 
            unsafe_allow_html=True)
        else:
            st.info("Queue is empty | 队列为空")

def main():
    if check_password():
        st.title("Data Structure Visualization | 数据结构可视化")
        show_author_info()
        
        tab1, tab2 = st.tabs(["Stack | 栈", "Queue | 队列"])
        
        with tab1:
            show_stack()
        
        with tab2:
            show_queue()

if __name__ == "__main__":
    main()

#import hashlib
#new_password = "CUHKSZ"
#hashed = hashlib.sha256(new_password.encode()).hexdigest()
#print(f"Hash for '{new_password}': {hashed}")









