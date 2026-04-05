import streamlit as st

# 1. Set Page Config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂")

# 2. Add the Music Player (Auto-plays if the browser allows, otherwise shows a player)
# Note: You can replace this URL with any direct .mp3 link
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3", loop=True)

# 3. Custom CSS & JavaScript for CONTINUOUS Balloons
# This creates a "CSS Animation" that runs forever in the background
st.markdown("""
    <style>
    .balloon-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        z-index: -1;
        pointer-events: none;
    }
    .balloon {
        position: absolute;
        bottom: -100px;
        width: 40px;
        height: 55px;
        background: rgba(255, 71, 87, 0.7);
        border-radius: 50%;
        animation: float Up 8s infinite ease-in;
    }
    @keyframes floatUp {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-120vh) rotate(20deg); opacity: 0; }
    }
    
    /* Style for the card */
    .birthday-card {
        background: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-top: 50px;
    }
    </style>
    
    <div class="balloon-container" id="balloon-box"></div>

    <script>
    function createBalloon() {
        const box = document.getElementById('balloon-box');
        const balloon = document.createElement('div');
        balloon.className = 'balloon';
        balloon.style.left = Math.random() * 100 + 'vw';
        balloon.style.backgroundColor = `hsl(${Math.random() * 360}, 70%, 60%)`;
        balloon.style.animationDuration = (Math.random() * 5 + 5) + 's';
        box.appendChild(balloon);
        
        // Remove balloon after it floats away to keep the page fast
        setTimeout(() => { balloon.remove(); }, 10000);
    }
    // Create a new balloon every 400 milliseconds
    setInterval(createBalloon, 400);
    </script>
    """, unsafe_allow_html=True)

# 4. The Content
st.markdown("""
    <div class="birthday-card">
        <h1 style='color: #ff4757;'>🎈 Happy Birthday! 🎈</h1>
        <h3>To an amazing friend!</h3>
        <p>Turn up the volume and enjoy your day!</p>
    </div>
    """, unsafe_allow_html=True)

# 5. The "Big Surprise" Button (Still includes Streamlit's built-in burst)
if st.button('Click for Extra Magic! ✨'):
    st.balloons()
    st.snow()
    st.success("Have the best day ever!")