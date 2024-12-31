import streamlit as st
from utils  import   genereate_xiaohongshu


st.header("爆款小红书设计文案 ")

with st.expander:
    api = st.text_input("请输入你的api密钥",type= "password",key=1)
    st.markdown("[输入秘钥](https://zhenzhu-222.github.io/zijin-www/)")

subject = st.text_input("视频主题",key=2)



click = st.button("点击提交")
# with st.
if click and not  api:
    st.info("请输入openai api秘钥")
    st.stop()
if click and not subject:
    st.info("请输入视频主题")
    st.stop()

if click:
    with st.spinner("正在疯狂的总结,你想不到我多疯狂"):
        result = genereate_xiaohongshu(subject = subject, api = api)

    st.divider()
    cl1,cl2 = st.columns(2)
    with cl1:
        st.markdown("##### 小红书标题1")
        st.write(result.titles[0])
        st.write(result.titles[1])
        st.write(result.titles[2])
        st.write(result.titles[3])
        st.write(result.titles[4])
    with cl2:
        st.markdown("##### 红薯正文")
        st.write(result.content)

