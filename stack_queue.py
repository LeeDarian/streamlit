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
    /* 基础变量定义 */
    :root {
        --primary-color: #4361ee;
        --secondary-color: #3a0ca3;
        --success-color: #2ecc71;
        --background-color: #f8f9fa;
        --text-color: #2d3436;
        --border-color: #e9ecef;
        --card-shadow: 0 2px 8px rgba(0,0,0,0.05);
        --transition-speed: 0.3s;
    }

    /* 基础布局 */
    .stApp {
        background-color: var(--background-color);
        font-family: 'Segoe UI', system-ui;
    }

    /* 标题样式 */
    .main-title {
        text-align: center;
        color: var(--text-color);
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }

    .sub-title {
        text-align: center;
        color: var(--text-color);
        font-size: 1.5rem;
        margin-bottom: 2rem;
    }

    /* 输入区域容器样式 */
    .input-container {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 1rem;
    }

    /* 输入标签样式 */
    .input-label {
        font-size: 1rem;
        color: var(--text-color);
        white-space: nowrap;
        margin-bottom: 0;
        min-width: fit-content;
    }

    /* 确保输入框独占一行 */
    .stTextInput {
        flex-grow: 1;
    }

    /* 输入框样式优化 */
    .stTextInput > div {
        margin: 0 !important;
    }

    .stTextInput input {
        border: 2px solid var(--border-color) !important;
        border-radius: 8px !important;
        padding: 10px 12px !important;
        transition: all var(--transition-speed) ease;
        font-size: 1rem;
        width: 100% !important;
    }

    .stTextInput input:focus {
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.1);
    }

    /* 按钮样式优化 */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 8px 16px !important;
        font-weight: 500;
        transition: all var(--transition-speed) ease;
        width: auto !important;
        min-width: 120px;
    }

    .stButton > button:hover {
        opacity: 0.9;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(67, 97, 238, 0.3);
    }

    .stButton > button:active {
        transform: translateY(1px);
    }

    /* 卡片容器样式 */
    .element-container {
        background: white !important;
        border-radius: 12px !important;
        box-shadow: var(--card-shadow) !important;
        margin: 1rem 0 !important;
        padding: 1.2rem !important;
    }

    /* 标签页样式优化 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        padding: 0.5rem;
        background: white;
        border-radius: 10px;
        box-shadow: var(--card-shadow);
    }

    .stTabs [data-baseweb="tab"] {
        padding: 8px 16px;
        background: none !important;
        border-radius: 8px;
        transition: all var(--transition-speed);
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)) !important;
        color: white !important;
    }

    /* 栈元素样式 */
    .stack-element {
        text-align: center;
        padding: 12px;
        background: linear-gradient(135deg, #f6f8ff, #ffffff);
        border: 2px solid rgba(67, 97, 238, 0.2);
        border-radius: 8px;
        margin: 8px 0;
        transition: transform var(--transition-speed);
    }

    /* 队列元素样式 */
    .queue-element {
        display: inline-block;
        padding: 12px;
        background: linear-gradient(135deg, #f6f8ff, #ffffff);
        border: 2px solid rgba(46, 204, 113, 0.2);
        border-radius: 8px;
        margin: 0 8px;
    }

    /* 作者信息样式 */
    .author-info {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: var(--card-shadow);
    }

    .author-info h3 {
        color: var(--primary-color);
        margin-bottom: 1.2rem;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 0.5rem;
    }

    .author-info p {
        margin: 0.5rem 0;
        line-height: 1.6;
        color: var(--text-color);
    }

    .author-info strong {
        display: block;
        margin-top: 1rem;
        color: var(--text-color);
    }

    .author-info a {
        color: var(--primary-color);
        text-decoration: none;
        transition: color var(--transition-speed);
    }

    .author-info a:hover {
        color: var(--secondary-color);
        text-decoration: underline;
    }

    /* 状态消息样式 */
    .stSuccess, .stError, .stInfo {
        padding: 0.8rem !important;
        border-radius: 8px !important;
        margin: 0.5rem 0 !important;
    }

    /* 操作区域样式 */
    .operation-area {
        margin: 1rem 0;
        padding: 1rem;
        background: white;
        border-radius: 10px;
        box-shadow: var(--card-shadow);
    }

    /* 响应式布局 */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .sub-title {
            font-size: 1.2rem;
        }

        .element-container {
            padding: 1rem !important;
        }
        
        .column {
            width: 100% !important;
            padding: 0.5rem !important;
        }
        
        .stButton > button {
            width: 100% !important;
            min-width: unset;
        }

        .queue-element {
            margin: 4px;
            padding: 8px;
        }

        .input-container {
            flex-direction: column;
            align-items: flex-start;
        }
    }
    </style>
""", unsafe_allow_html=True)
# Password functionality
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hashlib.sha256(str(st.session_state["password"]).encode()).hexdigest() == "c5c04c5b74d7d390bd11c7bc34b111d7cb0f0f397eb8cc4576e8969b502104df":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        with st.container():
            col1, col2, col3 = st.columns([1, 0.8, 1])
            with col2:
                st.image("https://www.cuhk.edu.cn/sites/webmaster.prod1.dpsite04.cuhk.edu.cn/files/zh-hans_logo.png", width=400)
                st.markdown("""
                ### Welcome to Data Structure Visualization
                Please enter the password to access the visualization tool.
                """)
                st.text_input(
                    "Password | 密码", 
                    type="password", 
                    on_change=password_entered, 
                    key="password",
                    placeholder="Enter password | 请输入密码",
                    max_chars=200
                )
        return False
    
    elif not st.session_state["password_correct"]:
        with st.container():
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                st.image("https://www.cuhk.edu.cn/sites/webmaster.prod1.dpsite04.cuhk.edu.cn/files/zh-hans_logo.png", width=400)
                st.text_input(
                    "Password | 密码", 
                    type="password", 
                    on_change=password_entered, 
                    key="password",
                    placeholder="Enter password | 请输入密码"
                )
                st.error("❌ Incorrect password, please try again | 密码错误，请重试")
        return False
    
    return True

# Author information
def show_author_info():
    st.sidebar.markdown("""
    <div class="author-info">
        <h3>Author Information | 作者信息</h3>
        <p><strong>Name | 姓名:</strong></p>
        <p>Li Dingyang (李定洋)</p>
        <p><strong>Email | 邮箱:</strong></p>
        <p><a href="mailto:222051031@link.cuhk.edu.cn">222051031@link.cuhk.edu.cn</a></p>
        <p><strong>Institution | 单位:</strong></p>
        <p>The Chinese University of Hong Kong, Shenzhen</p>
    </div>
    """, unsafe_allow_html=True)

def show_stack():
    st.header("Stack (栈) - LIFO")
    
    if 'stack' not in st.session_state:
        st.session_state.stack = []
    
    left_col, right_col = st.columns([1, 2])
    
    with left_col:
        with st.container():
            st.markdown("### Input & Operations | 输入与操作")
            
            # 创建水平布局的容器
            st.markdown('<div class="input-container">', unsafe_allow_html=True)
            st.markdown('<label class="input-label">Enter element | 输入元素</label>', unsafe_allow_html=True)
            new_item = st.text_input(
                "",
                key="stack_input",
                max_chars=200,
                label_visibility="collapsed"
            )
            st.markdown('</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Push | 入栈", use_container_width=True):
                    if new_item:
                        st.session_state.stack.append(new_item)
                        st.success(f"✅ Pushed: {new_item}")
            with col2:
                if st.button("Pop | 出栈", use_container_width=True):
                    if st.session_state.stack:
                        popped = st.session_state.stack.pop()
                        st.success(f"✅ Popped: {popped}")
                    else:
                        st.error("❌ Stack is empty!")
    
    with right_col:
        st.markdown("### Current Stack Status | 当前栈状态")
        if st.session_state.stack:
            for item in reversed(st.session_state.stack):
                st.markdown(f"""
                <div class="stack-element">{item}</div>
                """, unsafe_allow_html=True)
            st.markdown("<div style='text-align: center;'>⬇ Stack Bottom | 栈底 ⬇</div>", unsafe_allow_html=True)
        else:
            st.info("? Stack is empty | 栈为空")

def show_queue():
    st.header("Queue (队列) - FIFO")
    
    if 'queue' not in st.session_state:
        st.session_state.queue = []
    
    left_col, right_col = st.columns([1, 2])
    
    with left_col:
        with st.container():
            st.markdown("### Input & Operations | 输入与操作")
            
            # 创建水平布局的容器
            st.markdown('<div class="input-container">', unsafe_allow_html=True)
            st.markdown('<label class="input-label">Enter element | 输入元素</label>', unsafe_allow_html=True)
            new_item = st.text_input(
                "",
                key="queue_input",
                max_chars=200,
                label_visibility="collapsed"
            )
            st.markdown('</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Enqueue | 入队", use_container_width=True):
                    if new_item:
                        st.session_state.queue.append(new_item)
                        st.success(f"✅ Enqueued: {new_item}")
            with col2:
                if st.button("Dequeue | 出队", use_container_width=True):
                    if st.session_state.queue:
                        dequeued = st.session_state.queue.pop(0)
                        st.success(f"✅ Dequeued: {dequeued}")
                    else:
                        st.error("❌ Queue is empty!")
    
    with right_col:
        st.markdown("### Current Queue Status | 当前队列状态")
        if st.session_state.queue:
            st.markdown("""
            <div style="display: flex; align-items: center; overflow-x: auto; padding: 10px;">
                <div style="font-weight: bold; margin-right: 10px;">Front | 队头</div>
                {}
                <div style="font-weight: bold; margin-left: 10px;">Rear | 队尾</div>
            </div>
            """.format(" → ".join([f'<div class="queue-element">{item}</div>' for item in st.session_state.queue])),
            unsafe_allow_html=True)
        else:
            st.info("? Queue is empty | 队列为空")

def main():
    if check_password():
        st.markdown("""
        <h1 style="text-align: center; color: var(--text-color); font-size: 2.5rem;">
            堆栈和队列可视化
        </h1>
        <p style="text-align: center; color: var(--text-color); font-size: 2.5rem;">
            Stack & Queue Visualization
        </p>
        """, unsafe_allow_html=True)
        
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









