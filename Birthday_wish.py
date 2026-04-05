import streamlit as st
import time

# Set page title and favicon
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂")

# Custom CSS to center the content
st.markdown("""
    <style>
    .main {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4757;
        color: white;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎈 A Special Message for You!")

# The Trigger Button
if st.button('Click for your Birthday Surprise! 🎁'):
    # This is the built-in Streamlit balloon magic
    st.balloons()
    
    # Add a little delay for effect
    time.sleep(0.5)
    
    st.header("Happy Birthday, Friend! 🎂")
    st.subheader("Wishing you an amazing year ahead filled with adventures, success, and lots of laughter.")
    
    # Optional: Add a nice image or a personal note
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJid2pndzh5ZzBqZzBqZzBqZzBqZzBqZzBqZzBqZzBqZzBqJmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZ力を/oX8S43Dq40Z0Vv8L/giphy.gif")
    
    st.write("---")
    st.write("Hope your day is as awesome as you are!")
else:
    st.write("Go ahead... press the red button!")