import streamlit as st
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="Toolbox Talk 회의록", layout="centered")

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# 로그인 처리
def login():
    st.title("🔐 Toolbox Talk 로그인")
    name = st.text_input("이름", key="username")
    role = st.radio("역할", ["관리자", "팀원"], key="userrole")
    if st.button("입장"):
        if name:
            st.session_state['name'] = name
            st.session_state['role'] = role
            st.session_state.page = 'meeting'
        else:
            st.warning("이름을 입력해주세요.")

# 회의록 메인 페이지
def meeting():
    st.title(f"📋 Toolbox Talk 회의록 - [{st.session_state.get('name', '')}]")

    with st.form("meeting_form"):
        today = datetime.now().strftime("%Y-%m-%d")
        now_time = datetime.now().strftime("%H:%M")
        st.write("### 1️⃣ 회의 정보")
        col1, col2 = st.columns(2)
        with col1:
            date = st.text_input("날짜", today)
            place = st.text_input("장소")
        with col2:
            time = st.text_input("시간", now_time)
            task = st.text_input("작업 내용")
        st.write("### 2️⃣ 참석자")
        leader = st.text_input("리더")
        members = st.text_area("참석자 명단")
        st.form_submit_button("저장")

    if st.button("⬅ 로그아웃"):
        st.session_state.page = 'login'

# 페이지 라우팅
if st.session_state.page == 'login':
    login()
elif st.session_state.page == 'meeting':
    meeting()