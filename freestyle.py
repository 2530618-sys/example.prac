import streamlit as st

st.title('당신의 의견을 구합니다.')

agree= st.checkbox("개인정보 이용에 동의하십니까?")
if agree:
  st.write("감사합니다! 지금부터 설문을 시작합니다.")

age= st.number_input("나이를 입력하세요", min_value=0, max_value=110, step=1)
st.write("입력된 나이:", age)

gender= st.radio("성별을 선택하세요", ["남", "여"])
st.write("선택한 성별:", gender)

subjects= st.multiselect("배우고 싶은 언어를 선택하세요", ["영어", "한국어", "일본어", "중국어", "러시아어", "이탈리아어", "독일어", "프랑스어", "스페인어"])

level= st.selectbox("난이도를 선택하세요", ["하", "중", "상"])
st.write("선택한 난이도:", level)

st.write("학습을 시작합니다!")
