import streamlit as st
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# .envの読み込み（APIキーを設定）
load_dotenv()

# OpenAIのAPIキーは .env に OPENAI_API_KEY=... で設定済みとする
api_key = os.getenv("OPENAI_API_KEY")

# LangChainのChatモデル初期化
chat = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo")

# 回答を生成する関数
def generate_response(user_input, expert_type):
    if expert_type == "金融アドバイザー":
        system_prompt = "あなたは経験豊富な金融アドバイザーです。分かりやすく丁寧に答えてください。"
    elif expert_type == "栄養士":
        system_prompt = "あなたは国家資格を持つ栄養士です。健康や食事について正確にアドバイスしてください。"
    else:
        system_prompt = "あなたは親切で知識豊富な一般的な専門家です。"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]
    
    return chat(messages).content

# Streamlit UI
st.title("専門家AIチャット")
st.write("以下のフォームに質問を入力し、相談したい専門家を選んでください。")

# 専門家の選択
expert = st.radio("専門家の種類を選んでください", ("金融アドバイザー", "栄養士"))

# 入力フォーム
user_input = st.text_input("質問を入力してください")

# 送信ボタン
if st.button("送信"):
    if user_input:
        with st.spinner("回答を生成中..."):
            response = generate_response(user_input, expert)
            st.markdown("### 回答")
            st.write(response)
    else:
        st.warning("質問を入力してください。")