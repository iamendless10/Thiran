import streamlit as st
import requests

# Azure OpenAI Configuration
azure_endpoint = "https://opeanai-eastus.openai.azure.com/"
api_key = "a00d081fe4b849beb5b5c0c4ed8d837f"
model = "gpt4o"

# Thiran 2025 Data
thiran_data = {
    "hackathons": [
        {"name": "AI-Innovate", "description": "A platform to showcase innovative AI solutions."},
        {"name": "Codeathon", "description": "A coding marathon testing programming skills."},
        {"name": "CTF Quest", "description": "A Capture The Flag event focusing on cybersecurity challenges."},
        {"name": "Creatathon", "description": "Encourages creative problem-solving and innovation."},
        {"name": "Blockathon", "description": "Focuses on blockchain technology applications."},
        {"name": "Designathon", "description": "A design-centric hackathon emphasizing user experience and aesthetics."}
    ],
    "workshops": "Sessions led by industry experts covering various technical domains.",
    "master_classes": "In-depth classes focusing on specialized topics for skill enhancement.",
    "creative_workshops": "Workshops aimed at fostering creativity in various fields.",
    "technical_events": "Competitions and challenges in various technical disciplines.",
    "non_technical_events": "Engaging activities designed for participants from all backgrounds.",
    "cultural_contests": "Talent showcases judged by celebrities.",
    "spotlight_events": [
        {"name": "Youth Summit – The Gen Z Factor", "description": "Discussions and activities focusing on Generation Z."},
        {"name": "Leadership Talk", "description": "Insights from leaders across various industries."},
        {"name": "Tech-Talk", "description": "Presentations on cutting-edge technological advancements."},
        {"name": "Pitch Fest – Pitch Your Business Idea", "description": "Opportunity to present business ideas to potential investors."},
        {"name": "Start-up Stories: Founder’s Forum", "description": "Entrepreneurs share their journey and experiences."},
        {"name": "International Education Expo", "description": "Exhibition featuring educational opportunities abroad."}
    ],
    "mega_celebrity_shows": "Evening performances by renowned artists, providing entertainment and a chance to unwind.",
    "sports_fest": {
        "dates": "February 14-16, 2025",
        "description": "Various sports competitions promoting physical fitness and teamwork."
    },
    "event_details": [
        {
            "name": "The Campus Carnival: Fun Arena",
            "date_time": "February 22, 2025, 9:00 AM - 1:00 PM",
            "description": "A dynamic challenge where teams face six exciting games, with every spin deciding their journey. Complete all assigned rounds to emerge victorious and claim the grand prize!",
            "organized_by": "SLC & MEDIA",
            "faculty_coordinator": "Dr. S. Kavitha, AP/S&H (9442944414)",
            "student_coordinator": "Ms. Shreenithii SJ (9600248984)",
            "prize_details": "Grand prize for the winning team."
        },
        {
            "name": "CEO for a Day",
            "date_time": "February 21, 2025, 12:00 PM - 2:00 PM",
            "description": "Experience the challenges and rewards of leading an organization for a day. Perfect for aspiring leaders ready to take charge.",
            "organized_by": "CSBS",
            "faculty_coordinator": "Mr. M. Mohanraj, AP/CSBS (7010531709)",
            "student_coordinator": "Mr. Nithish (9384302078)",
            "prize_details": "Not specified."
        }
    ],
    "ticket_information": {
        "one_day_pass": "₹300 per person, includes access to all events, spotlight events, workshops, contests, and mega celebrity shows scheduled for that day, along with veg/non-veg lunch.",
        "premium_pass": "₹500 per person, includes access to all events over two days, with lunch provided on both days.",
        "elite_pass": "₹750 per person, includes access to all events across all three days, with lunch provided each day."
    },
    "website": "[thiran.sece.ac.in](https://thiran.sece.ac.in/?utm_source=chatgpt.com)"
}

def query_openai(prompt):
    """Send a prompt to Azure OpenAI and get the response."""
    url = f"{azure_endpoint}/openai/deployments/{model}/chat/completions?api-version=2023-05-15"
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    
    data = {
        "messages": [
            {"role": "system", "content": "You are an AI chatbot named 'Thiran Chatbot'. You are designed to provide details about Thiran 2025, organized by Sri Eshwar College of Engineering. Use the provided data to answer questions. If asked anything outside the data, respond with 'I am an AI made to give details about Thiran.'"},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Error: {response.status_code}, {response.text}"

    return response.json()["choices"][0]["message"]["content"]

# Streamlit UI for the Thiran Chatbot
st.title("Thiran Chatbot")

# User input
user_input = st.text_input("Type your question here...", placeholder="Ask about Thiran 2025 events, workshops, or ticket details.")

if st.button("Send") and user_input:
    # Get response from OpenAI
    bot_response = query_openai(user_input)
    
    # Display user input and bot response
    st.write(f"**User:** {user_input}")
    st.write(f"**Bot:** {bot_response}")
