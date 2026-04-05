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
        animation: floatUp 8s infinite ease-in;
    }
    @keyframes floatUp {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-120vh) rotate(20deg); opacity: 0; }
    }
    
    /* Style for the card */
    body {
        background-color: #000000;
        color: #ffffff;
    }
    .birthday-card {
        background: transparent;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        box-shadow: none;
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

    function createBurst(count = 25) {
        const box = document.getElementById('balloon-box');
        for (let i = 0; i < count; i++) {
            const balloon = document.createElement('div');
            balloon.className = 'balloon';
            balloon.style.left = Math.random() * 100 + 'vw';
            balloon.style.backgroundColor = `hsl(${Math.random() * 360}, 75%, 65%)`;
            balloon.style.animationDuration = (Math.random() * 3 + 4) + 's';
            balloon.style.opacity = 0.95;
            box.appendChild(balloon);
            setTimeout(() => { balloon.remove(); }, 10000);
        }
    }

    // Create a new balloon every 400 milliseconds
    setInterval(createBalloon, 400);
    </script>
    """, unsafe_allow_html=True)


# 4. The Content (Styled with Transparent Background and Colorful Fonts)
st.markdown("""
    <div class="birthday-card">
        <h1 style="
            font-family: 'Arial Black', sans-serif;
            font-size: 4rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(45deg, #ff4500, #ff8c00, #ffd700);
            -webkit-background-clip: text;
            color: transparent;
            text-shadow: 2px 2px 12px rgba(255, 69, 0, 0.45);
        ">
            <h1>🎈 Happy Birthday 🎈<h1>
        </h1>
        <p style="
            font-family: 'Segoe UI', sans-serif;
            font-size: 1.8rem;
            color: #ffa500;
            margin: 0.5rem 0 0;
            line-height: 1.4;
        ">
            Name!<br>
            To an amazing friend!<br>
            Turn up the volume and enjoy your day!
        </p>
    </div>
    """, unsafe_allow_html=True) # <--- THIS IS THE SECRET KEY

# 5. The "Big Surprise" Button (Now triggers a JS balloon burst)
if st.button('Click for Extra Magic! ✨'):
    st.markdown(
        """
        <script>
        if (typeof createBurst === 'function') {
            createBurst(35);
        }
        </script>
        """,
        unsafe_allow_html=True,
    )
    st.balloons()
    st.snow()
    st.success("Have a great year ahead!")
    