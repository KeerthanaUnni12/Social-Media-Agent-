import os
import streamlit as st
from openai import OpenAI

# ----------------- Setup -----------------
# Uses the OPENAI_API_KEY from your environment
client = OpenAI()

st.set_page_config(page_title="Social Media Agent", page_icon="🧠")

st.title("🧠 Social Media Content Agent")
st.write("Generate social media post ideas and captions in seconds.")

# ----------------- UI Inputs -----------------
platform = st.selectbox(
    "Choose platform",
    ["Instagram", "Facebook", "LinkedIn", "Twitter/X", "YouTube", "Generic"]
)

tone = st.selectbox(
    "Choose tone",
    ["Casual", "Professional", "Emotional", "Funny", "Inspirational"]
)

goal = st.selectbox(
    "Content goal",
    ["Brand awareness", "Product promotion", "Engagement (likes/comments)", "Educational", "Announcement"]
)

topic = st.text_area(
    "Describe your brand / topic / campaign",
    placeholder="Example: Launching a new eco-friendly skincare product for women in their 20s..."
)

num_posts = st.slider("How many posts to generate?", min_value=1, max_value=5, value=3)

generate_button = st.button("✨ Generate Content")


# ----------------- Prompt Builder -----------------
def build_prompt(platform, tone, goal, topic, num_posts):
    return f"""
You are a social media content strategist.

Create {num_posts} {platform} post ideas with full captions.

Requirements:
- Tone: {tone}
- Goal: {goal}
- Topic / Brand description: {topic}
- Each idea should have:
  1) A short title (hook)
  2) A full caption (2–5 lines)
  3) 3–5 suggested hashtags

Format clearly, like:

Post 1:
Title: ...
Caption: ...
Hashtags: ...

Post 2:
...
"""


# ----------------- Main Logic -----------------
if generate_button:
    if not topic.strip():
        st.warning("Please describe your brand/topic first.")
    else:
        with st.spinner("Thinking of great content for you..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",  # use any available chat model in your account
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert social media marketer and copywriter."
                        },
                        {
                            "role": "user",
                            "content": build_prompt(platform, tone, goal, topic, num_posts)
                        },
                    ],
                    temperature=0.9,
                )

                content = response.choices[0].message.content

                st.markdown("### 📌 Generated Content")
                st.write(content)

            except Exception as e:
                st.error("Something went wrong.")
                st.code(str(e))
                st.info("Check that your OPENAI_API_KEY is set correctly and you have internet access.")
