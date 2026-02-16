import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title= "My Portfolio", page_icon=":tada:", layout="wide")

#page background
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2, #ff758c);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

h1, h2, h3, h4, h5, h6, p {
    color: white;
    
}
/*  Contact Bar */
.contact-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: rgba(0,0,0,0.6);
    backdrop-filter: blur(10px);
    padding: 15px;
    text-align: center;
    color: white;
    font-weight: 500;
    z-index: 999;
}

.contact-bar a {
    color: #ffcc70;
    text-decoration: none;
    margin: 0 20px;
    font-size: 18px;
}

.contact-bar a:hover {
    color: white;
}

</style>
""", unsafe_allow_html=True)







def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = "https://lottie.host/0b81c405-7b33-4c14-a8c5-83c2145207f4/y8ANE9si9u.json"
lottie_json = load_lottie(lottie_coding)


st.subheader("Hi There! My Name is Lumi :wave:")
st.title("A Web Developer From Canada")
(st.write("I’m a passionate Web Developer with 1 years of experience building responsive, user-friendly websites and web applications. I specialize in front-end development and enjoy turning ideas into functional, visually appealing digital experiences. I focus on writing clean, efficient code and continuously improving my skills to stay current with modern web technologies. "))


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("I build fast, responsive, and user-friendly websites for small businesses. From idea to launch, I help businesses establish a professional online presence that supports growth and success.")


        with right_column:
            st_lottie(lottie_json, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Project")
video_column, text_column = st.columns((1, 2))


with video_column:
       st.video("past.mp4")


with text_column:
        st.subheader("Business Website Project")
        st.write("""Designed and developed a fully responsive website for a local hair salon to help increase online visibility and attract new clients. 
The website features a modern layout, mobile-friendly design, service listings, pricing details, and an easy-to-use contact section. 
I focused on creating a clean user interface, smooth navigation, and fast loading speed to improve user experience and engagement.""")

# Contact Bar (ADD THIS BELOW EVERYTHING)
st.markdown("""
<div class="contact-bar">
    📞 <a href="tel:9024520281">902-452-0281</a>
    |
    ✉ <a href="mailto:afolabipelu25@gmail.com">afolabipelu25@gmail.com</a>
</div>
""", unsafe_allow_html=True)