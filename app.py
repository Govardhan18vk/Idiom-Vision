import streamlit as st
import base64

st.set_page_config(page_title="Project Idiom Vision", page_icon="🖼️", layout="wide")

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image_base64 = get_base64("pexels-ron-lach-9783353.jpg")

st.markdown(f"""
    <style>
        /* Background Image with Reduced Brightness */
        .stApp {{
            background: url("data:image/png;base64,{bg_image_base64}") no-repeat center center fixed;
            background-size: cover;
            filter: brightness(80%); /* Adjust brightness (lower = darker) */
        }}

        /* Overlay to further darken background (optional) */
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.1); /* Dark overlay */
            z-index: -1;
        }}

        /* Title Styling */
        h1.main-title {{
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #EE1D12 !important; 
            text-shadow: 3px 3px 6px rgba(0,0,0,0.2);
            padding: 20px 0;
        }}
        h3.sub-title {{
            text-align: center;
            font-size: 22px;
            color: #EE1D12 !important;
        }}

        /* Streamlit Button Customization */
        div.stButton > button {{
            background: linear-gradient(135deg, #12C8EE, #9812EE);
            color: #DFEE12;
            font-size: 18px;
            padding: 12px 30px;
            border-radius: 12px;
            border: none;
            font-weight: bold;
            transition: 0.3s;
            box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.3);
        }}
        div.stButton > button:hover {{
            background: linear-gradient(135deg, #12C8EE, #9812EE);
            transform: scale(1.05);
            box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.4);
        }}
    </style>
""", unsafe_allow_html=True)


st.markdown('<h1 class="main-title">🚀 Project Idiom Vision</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="sub-title">A Smart AI-powered Image Analysis System</h3>', unsafe_allow_html=True)


col1, col2, col3 = st.columns([2, 1, 2])

with col2:
    subtask_a = st.button("🅰️ Image Ranking", use_container_width=True)
    subtask_b = st.button("🅱️ Sequence Image Prediction", use_container_width=True)

if subtask_a:
    st.switch_page("Landing Pages for Subtasks/subtask_a.py")

if subtask_b:
    st.switch_page("Landing Pages for Subtasks/subtask_b.py")
