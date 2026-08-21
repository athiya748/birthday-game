#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Let's see what is there ✨👑😘",
    page_icon="👑",
    layout="centered"
)


# ============================================================
# PHOTO PATHS
# ============================================================
# Works on Streamlit Cloud AND Jupyter.
#
# On Streamlit Cloud:
#   photos are expected to be beside apps.py
#
# On Jupyter:
#   if __file__ doesn't exist, it uses the current folder.
# ============================================================

try:
    BASE_DIR = Path(__file__).resolve().parent
except NameError:
    BASE_DIR = Path.cwd()

ANI_IMAGE = BASE_DIR / "Ani.jpg.jpeg"
ATHU_IMAGE = BASE_DIR / "athu.jpg.jpeg"


# ============================================================
# SESSION STATE
# ============================================================

if "level" not in st.session_state:
    st.session_state.level = 0

if "photo_page" not in st.session_state:
    st.session_state.photo_page = 1


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(59,130,246,0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(236,72,153,0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 50% 90%,
            rgba(168,85,247,0.16),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #f8fbff,
            #fff7fb,
            #f7f5ff
        );
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.stMarkdown,
.stMarkdown p,
.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3 {
    opacity: 1 !important;
}

.stRadio label {
    color: #1e293b !important;
    opacity: 1 !important;
}

.stRadio label p {
    color: #1e293b !important;
    opacity: 1 !important;
    font-weight: 700 !important;
}

div[data-testid="stRadio"] p {
    color: #1e293b !important;
    opacity: 1 !important;
}

.stTextInput label {
    color: #1e293b !important;
    font-weight: 800 !important;
}

.stTextInput input {
    color: #1e293b !important;
    background: white !important;
    border: 2px solid #cbd5e1 !important;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 900;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #9333ea,
            #ec4899,
            #2563eb
        );

    background-size: 300% auto;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: gradientText 5s linear infinite;
}

@keyframes gradientText {
    0% {
        background-position: 0% center;
    }

    50% {
        background-position: 100% center;
    }

    100% {
        background-position: 0% center;
    }
}

.center-text {
    text-align: center;
}

.big-emoji {
    text-align: center;
    font-size: 70px;

    animation:
        floating 3s ease-in-out infinite,
        glow 2s ease-in-out infinite;
}

@keyframes floating {
    0% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-12px);
    }

    100% {
        transform: translateY(0);
    }
}

@keyframes glow {
    0% {
        filter: drop-shadow(0 0 2px #93c5fd);
    }

    50% {
        filter: drop-shadow(0 0 18px #f9a8d4);
    }

    100% {
        filter: drop-shadow(0 0 2px #93c5fd);
    }
}

.special-box {
    padding: 30px;
    border-radius: 28px;

    background: rgba(255,255,255,0.82);

    backdrop-filter: blur(12px);

    border: 2px solid rgba(255,255,255,0.9);

    box-shadow:
        0 15px 40px rgba(31,41,55,0.12),
        0 0 30px rgba(147,51,234,0.08);

    text-align: center;

    margin: 20px 0;
}

.question-card {
    padding: 28px;
    border-radius: 25px;

    background:
        linear-gradient(
            135deg,
            rgba(239,246,255,0.96),
            rgba(253,242,248,0.96)
        );

    border: 2px solid #dbeafe;

    box-shadow:
        0 10px 30px rgba(37,99,235,0.10);

    text-align: center;

    margin-bottom: 25px;
}

.question-number {
    color: #7c3aed;
    font-size: 20px;
    font-weight: 900;
    margin-bottom: 8px;
}

.question-title {
    font-size: 25px;
    font-weight: 800;
    color: #1e293b;
}

.stButton > button {
    border-radius: 18px !important;

    border: 2px solid #dbeafe !important;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #7c3aed,
            #ec4899
        ) !important;

    background-size: 200% auto !important;

    color: white !important;

    font-weight: 800 !important;

    font-size: 16px !important;

    padding: 12px !important;

    transition: all 0.3s ease !important;

    box-shadow:
        0 8px 20px rgba(124,58,237,0.22) !important;
}

.stButton > button p {
    color: white !important;
    font-weight: 800 !important;
}

.stButton > button:hover {
    transform:
        translateY(-3px)
        scale(1.02);

    background-position: right center !important;

    box-shadow:
        0 12px 30px
        rgba(236,72,153,0.30) !important;
}

div[data-testid="stAlert"] {
    border-radius: 18px !important;
    font-weight: 700 !important;
}

.photo-card {
    padding: 20px;

    border-radius: 30px;

    background:
        linear-gradient(
            135deg,
            #dbeafe,
            #fce7f3,
            #ede9fe
        );

    box-shadow:
        0 15px 45px
        rgba(124,58,237,0.20);

    margin-top: 20px;
}

.photo-glow {
    padding: 10px;

    border-radius: 28px;

    background:
        linear-gradient(
            45deg,
            #2563eb,
            #9333ea,
            #ec4899,
            #f59e0b,
            #2563eb
        );

    background-size: 400% 400%;

    animation:
        photoBorder 6s ease infinite;

    box-shadow:
        0 0 25px
        rgba(236,72,153,0.35);
}

@keyframes photoBorder {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

.photo-title {
    text-align: center;

    font-size: 28px;

    font-weight: 900;

    color: #7c3aed;

    margin: 15px 0;
}

.heart {
    text-align: center;

    font-size: 65px;

    animation:
        heartbeat 1.2s infinite;
}

@keyframes heartbeat {
    0% {
        transform: scale(1);
    }

    20% {
        transform: scale(1.25);
    }

    40% {
        transform: scale(1);
    }

    60% {
        transform: scale(1.18);
    }

    100% {
        transform: scale(1);
    }
}

.floating-hearts {
    text-align: center;

    font-size: 32px;

    letter-spacing: 8px;

    animation:
        floatingHearts 2.5s ease-in-out infinite;
}

@keyframes floatingHearts {
    0% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-10px);
    }

    100% {
        transform: translateY(0);
    }
}

.final-box {
    padding: 40px 22px;

    border-radius: 32px;

    background:
        linear-gradient(
            135deg,
            #fff1f2,
            #fce7f3,
            #ede9fe,
            #dbeafe
        );

    background-size: 300% 300%;

    animation:
        finalBackground 8s ease infinite;

    border: 3px solid #f9a8d4;

    box-shadow:
        0 20px 60px
        rgba(236,72,153,0.25);

    text-align: center;
}

@keyframes finalBackground {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

.love-text {
    text-align: center;

    font-size: 48px;

    font-weight: 1000;

    color: #e11d48;

    text-shadow:
        0 0 10px rgba(244,63,94,0.35),
        0 0 25px rgba(236,72,153,0.25);

    animation:
        shake 0.7s infinite,
        loveGlow 2s infinite;
}

@keyframes shake {
    0% {
        transform:
            translateX(0)
            rotate(0deg);
    }

    20% {
        transform:
            translateX(-9px)
            rotate(-2deg);
    }

    40% {
        transform:
            translateX(9px)
            rotate(2deg);
    }

    60% {
        transform:
            translateX(-7px)
            rotate(-2deg);
    }

    80% {
        transform:
            translateX(7px)
            rotate(2deg);
    }

    100% {
        transform:
            translateX(0)
            rotate(0deg);
    }
}

@keyframes loveGlow {
    0% {
        text-shadow:
            0 0 5px #fda4af;
    }

    50% {
        text-shadow:
            0 0 25px #ec4899,
            0 0 40px #c084fc;
    }

    100% {
        text-shadow:
            0 0 5px #fda4af;
    }
}

.final-message {
    font-size: 21px;

    line-height: 1.9;

    color: #374151;

    text-align: center;

    font-weight: 600;

    margin: 18px 0;
}

.progress-text {
    text-align: center;

    font-size: 14px;

    color: #475569;

    font-weight: 700;

    margin-bottom: 10px;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# LEVEL 0 — START
# ============================================================

if st.session_state.level == 0:

    st.markdown(
        "<div class='big-emoji'>💙👑✨</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1 class='main-title'>ANAND A</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<h3 class="center-text" style="color:#374151;">
✨ A Secret Birthday Portal ✨
</h3>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="special-box">

<h2 style="color:#1e293b;">
My Special Person 💗🥰
</h2>

<p style="color:#374151;font-size:18px;">
Something beautiful has been prepared
especially for you... 💌
</p>

<p style="color:#374151;font-size:18px;">
Are you ready to unlock it? 🎂🎁👑
</p>

</div>
""",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button(
            "START THE GAME 🚀💙",
            use_container_width=True
        ):
            st.session_state.level = 1
            st.rerun()


# ============================================================
# LEVEL 1 — FAVORITE COLOR
# ============================================================

elif st.session_state.level == 1:

    st.markdown(
        "<div class='progress-text'>🔐 LEVEL 1 / 5</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='big-emoji'>🎨💙✨</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="question-card">

<div class="question-number">
QUESTION 1
</div>

<div class="question-title">
What color lights up your entire world? 💙✨
</div>

</div>
""",
        unsafe_allow_html=True
    )

    color = st.radio(
        "Choose the correct answer:",
        [
            "Red 🔴",
            "Blue 💙",
            "Green 🟢",
            "Yellow 🟡"
        ],
        index=None
    )

    if st.button(
        "🔑 Submit Answer",
        use_container_width=True
    ):

        if color == "Blue 💙":

            st.success("Yay! Correct! 💙😘✨")

            st.session_state.level = 2
            st.rerun()

        else:

            st.error("Wrong answer! 🥺💔 Try again!")


# ============================================================
# LEVEL 2 — FAVORITE FOOD
# ============================================================

elif st.session_state.level == 2:

    st.markdown(
        "<div class='progress-text'>🔐 LEVEL 2 / 5</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='big-emoji'>🍛🔥✨</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="question-card">

<div class="question-number">
QUESTION 2
</div>

<div class="question-title">
What royal dish rules your heart and tummy? 🍽️🔥
</div>

</div>
""",
        unsafe_allow_html=True
    )

    food = st.radio(
        "Choose the correct answer:",
        [
            "Pizza 🍕",
            "Burger 🍔",
            "Biriyani 🍛",
            "Pasta 🍝"
        ],
        index=None
    )

    if st.button(
        "🔑 Submit Answer",
        use_container_width=True
    ):

        if food == "Biriyani 🍛":

            st.success("Correct! Yum! 🍛😘💋")

            st.session_state.level = 3
            st.rerun()

        else:

            st.error("Nope! 😢💔 Try again!")


# ============================================================
# LEVEL 3 — FAVORITE HOBBY
# ============================================================

elif st.session_state.level == 3:

    st.markdown(
        "<div class='progress-text'>🔐 LEVEL 3 / 5</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='big-emoji'>🎮🎧💖</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="question-card">

<div class="question-number">
QUESTION 3
</div>

<div class="question-title">
What activity makes you happiest in your free time? 🎧✨
</div>

</div>
""",
        unsafe_allow_html=True
    )

    hobby = st.radio(
        "Choose the correct answer:",
        [
            "Sleeping 😴",
            "My Hobby / Passion 💖🎮",
            "Cooking 🧑‍🍳",
            "Reading 📚"
        ],
        index=None
    )

    if st.button(
        "🔑 Submit Answer",
        use_container_width=True
    ):

        if hobby == "My Hobby / Passion 💖🎮":

            st.success("Bingo! 💋🥰 Level unlocked!")

            st.session_state.level = 4
            st.rerun()

        else:

            st.error("Wrong guess! 😭💔 Try again!")


# ============================================================
# LEVEL 4 — RELATIONSHIP
# ============================================================

elif st.session_state.level == 4:

    st.markdown(
        "<div class='progress-text'>🔐 LEVEL 4 / 5</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='big-emoji'>👑💎❤️</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="question-card">

<div class="question-number">
QUESTION 4
</div>

<div class="question-title">
Who are you to me in this world? 👑❤️
</div>

</div>
""",
        unsafe_allow_html=True
    )

    relation = st.radio(
        "Choose the correct answer:",
        [
            "Just a friend 🤷‍♂️",
            "✨ My Queen 👑💖",
            "A neighbor 🏡",
            "A stranger 🙈"
        ],
        index=None
    )

    if st.button(
        "🔑 Submit Answer",
        use_container_width=True
    ):

        if relation == "✨ My Queen 👑💖":

            st.success("Aww! Perfect choice! 🥰👑💎")

            st.session_state.level = 5
            st.rerun()

        else:

            st.error("No way! 🥺💔 Try again!")


# ============================================================
# LEVEL 5 — PASSWORD
# ============================================================

elif st.session_state.level == 5:

    st.markdown(
        "<div class='progress-text'>🔐 FINAL LEVEL / 5</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='big-emoji'>🗝️🔐💖</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="question-card">

<div class="question-number">
FINAL SECRET DOOR
</div>

<div class="question-title">
Enter the secret password ❤️
</div>

</div>
""",
        unsafe_allow_html=True
    )

    password = st.text_input(
        "🔐 Password:",
        type="password"
    )

    if st.button(
        "🎁 UNLOCK THE FINAL SURPRISE",
        use_container_width=True
    ):

        if password.strip().lower() == "i love you":

            st.success(
                "ACCESS GRANTED! 🎉💋💎❤️"
            )

            st.session_state.level = 6
            st.session_state.photo_page = 1

            st.rerun()

        else:

            st.error("Incorrect password! 😭💔")


# ============================================================
# LEVEL 6 — FINAL BIRTHDAY SURPRISE
# ============================================================

elif st.session_state.level == 6:

    st.balloons()

    st.markdown(
        "<div class='big-emoji'>👑💖🎉✨</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<h1 class="main-title">
Happy Advance Birthday, My Hero! 👑✨🥰
</h1>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<h2 class="center-text" style="color:#2563eb;">
⏳ 9 days to go ✨🤗
</h2>
""",
        unsafe_allow_html=True
    )

    # ========================================================
    # BIRTHDAY MESSAGE
    # ========================================================

    st.markdown(
        """
<div class="special-box">

<h2 style="color:#7c3aed;">
💌 A Little Birthday Message 💌
</h2>

<p class="final-message">
To my absolute favorite human,
my strength, my joy,
and my everlasting hero —
you make every single moment
feel like a magical fairytale! 🌟
</p>

<p class="final-message">
Every beat of my heart is counting down
the seconds until your official birthday
celebration! 💖💎
</p>

<p class="final-message"
style="color:#e11d48;font-weight:800;">
You are not just special...
You are my forever favorite person. 🥹💋💎
</p>

</div>
""",
        unsafe_allow_html=True
    )


    # ========================================================
    # PHOTO PAGE 1
    # ========================================================

    if st.session_state.photo_page == 1:

        st.divider()

        st.markdown(
            """
<div class="photo-title">
💙✨ A Special Memory ✨💙
</div>
""",
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # CHECK PHOTO 1
        # ----------------------------------------------------

        if ANI_IMAGE.exists():

            st.markdown(
                "<div class='photo-card'>",
                unsafe_allow_html=True
            )

            st.markdown(
                "<div class='photo-glow'>",
                unsafe_allow_html=True
            )

            st.image(
                str(ANI_IMAGE),
                caption="👑 Hero Anand A 💖",
                use_container_width=True
            )

            st.markdown(
                "</div></div>",
                unsafe_allow_html=True
            )

        else:

            st.error("❌ Ani.jpg.jpeg was not found.")

            st.info(
                "Please upload Ani.jpg.jpeg to the same GitHub folder as apps.py."
            )

            st.code(
                f"Looking for:\n{ANI_IMAGE}"
            )

        st.markdown(
            """
<div class="floating-hearts">
💙 💖 💎 👑 💙 💖
</div>
""",
            unsafe_allow_html=True
        )

        if st.button(
            "💕 NEXT BEAUTIFUL MEMORY →",
            use_container_width=True
        ):

            st.session_state.photo_page = 2
            st.rerun()


    # ========================================================
    # PHOTO PAGE 2
    # ========================================================

    elif st.session_state.photo_page == 2:

        st.divider()

        st.markdown(
            """
<div class="photo-title">
💐✨ Another Beautiful Memory ✨💐
</div>
""",
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # CHECK PHOTO 2
        # ----------------------------------------------------

        if ATHU_IMAGE.exists():

            st.markdown(
                "<div class='photo-card'>",
                unsafe_allow_html=True
            )

            st.markdown(
                "<div class='photo-glow'>",
                unsafe_allow_html=True
            )

            st.image(
                str(ATHU_IMAGE),
                caption="💐 My Special Person 💖",
                use_container_width=True
            )

            st.markdown(
                "</div></div>",
                unsafe_allow_html=True
            )

        else:

            st.error("❌ athu.jpg.jpeg was not found.")

            st.info(
                "Please upload athu.jpg.jpeg to the same GitHub folder as apps.py."
            )

            st.code(
                f"Looking for:\n{ATHU_IMAGE}"
            )

        st.markdown(
            """
<div class="floating-hearts">
💖 💐 🥰 💎 🫰🏻 👑
</div>
""",
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "⬅️ BACK",
                use_container_width=True
            ):

                st.session_state.photo_page = 1
                st.rerun()

        with col2:

            if st.button(
                "NEXT 💎",
                use_container_width=True
            ):

                st.session_state.photo_page = 3
                st.rerun()


    # ========================================================
    # THANK YOU PAGE
    # ========================================================

    elif st.session_state.photo_page == 3:

        st.divider()

        st.markdown(
            "<div class='big-emoji'>🥰💐💎</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<h1 class="main-title">
Thank You Hero 🥰🫰🏻💎
</h1>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<div class="special-box">

<p class="final-message">
Thank you for reaching
the end of this little journey. 💖
</p>

<p class="final-message">
But wait... 👀✨
</p>

<p class="final-message"
style="color:#e11d48;font-weight:800;">
There is still ONE final surprise
waiting for you. 🥹💌
</p>

</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div class='heart'>💖</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<div class="floating-hearts">
💙 💖 💎 💐 🥰 💋 👑
</div>
""",
            unsafe_allow_html=True
        )

        if st.button(
            "💌 OPEN ONE LAST SURPRISE ✨",
            use_container_width=True
        ):

            st.session_state.photo_page = 4
            st.rerun()


    # ========================================================
    # FINAL LOVE PAGE
    # ========================================================

    elif st.session_state.photo_page == 4:

        st.markdown(
            "<div class='final-box'>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div class='heart'>💖</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<div class="love-text">
I LOVE YOU
</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<h1 class="main-title">
My 🥹 Husband 💋✨💎💯
</h1>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<p class="final-message">
You are my favorite person,
my happiness, my comfort,
and my forever love. 🥹❤️
</p>

<p class="final-message">
No matter how many birthdays come,
I want to keep celebrating
every beautiful moment with you. 🎂💖
</p>

<p class="final-message">
You are my <b>HERO 👑</b>,
my <b>HUSBAND 💍</b>,
my <b>FOREVER PERSON 💎</b>.
</p>

<p class="final-message">
I love you more than words
can ever explain. 🥹💋✨
</p>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<div class="love-text">
💋✨💎💯
</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<div class="floating-hearts">
💖 💖 💖 💖 💖
</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<div class="heart">
👑 💍 🥹 💋 💎 🎂 🎉 💖
</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "⬅️ BACK",
                use_container_width=True
            ):

                st.session_state.photo_page = 3
                st.rerun()

        with col2:

            if st.button(
                "🔄 REPLAY GAME",
                use_container_width=True
            ):

                st.session_state.level = 0
                st.session_state.photo_page = 1
                st.rerun()


# In[9]:


from pathlib import Path

BASE_DIR = Path.cwd()

ANI_IMAGE = BASE_DIR / "Ani.jpg"
ATHU_IMAGE = BASE_DIR / "athu.jpg"

print("Ani image:",ANI_IMAGE)
print("Athu image:",ATHU_IMAGE)


# In[ ]:




