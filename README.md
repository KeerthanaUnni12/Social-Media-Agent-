# 🧠 Social Media Content Agent
Live Demo: https://social-media-agent-git-3pbyneszey8djnjkzb2kzc.streamlit.app/


## 1. Overview

This AI agent helps marketing and content teams quickly generate social media post ideas and captions.  
The user selects a platform (e.g., Instagram, LinkedIn), tone, and content goal, then describes the brand or campaign.  
The agent uses an LLM (OpenAI API) to generate multiple post ideas, each with a hook, caption, and hashtags.

This project is submitted for the **48-Hour AI Agent Development Challenge** under the **Social Media Agent** category.

---

## 2. Features

- Generate 1–5 social media post ideas in one click.
- Supports multiple platforms:
  - Instagram, Facebook, LinkedIn, Twitter/X, YouTube, Generic.
- Customizable tone:
  - Casual, Professional, Emotional, Funny, Inspirational.
- Customizable content goal:
  - Brand awareness, Product promotion, Engagement, Educational, Announcement.
- Each generated post includes:
  - A short title/hook.
  - A full caption (2–5 lines).
  - Suggested hashtags.

---

## 3. Limitations

- Requires a valid OpenAI API key and internet connection.
- Does not store user history or generated content (no database).
- Does not directly connect to or post on social media platforms.
- Does not generate full long-term content calendars yet.

---

## 4. Tech Stack & APIs Used

- **Language:** Python
- **Frontend & App Framework:** Streamlit
- **LLM API:** OpenAI Chat Completions (e.g., `gpt-4.1-mini`)
- **Environment:** Streamlit Community Cloud (for deployment)

---

## 5. Architecture (High-Level Flow)

1. **User (Browser)**  
   - Enters platform, tone, goal, topic, and number of posts in the Streamlit UI.

2. **Streamlit App (`app.py`)**  
   - Collects inputs and builds a structured prompt using a helper function.

3. **Agent Logic / Backend**  
   - Uses the OpenAI Python client to call the Chat Completion API with the prompt and parameters.

4. **OpenAI LLM (Cloud)**  
   - Generates multiple social media post ideas, including captions and hashtags.

5. **Streamlit App**  
   - Displays the generated content in a readable format to the user.

See `assets/architecture.png` for the visual architecture diagram.

---

## 6. Setup & Run Instructions (Local)

### Prerequisites

- Python 3.11+ (64-bit)
- OpenAI API key

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/social-media-agent.git
   cd social-media-agent
