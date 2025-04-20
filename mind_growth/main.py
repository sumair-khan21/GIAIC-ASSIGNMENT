import streamlit as st
import random
from datetime import datetime

quotes = [
    "Mistakes are proof that you are trying.",
    "Your brain is like a muscle. The more you use it, the stronger it gets.",
    "Don't be afraid of failure. It's part of learning.",
    "Effort is the path to mastery.",
    "Every challenge is an opportunity to grow."
]

st.set_page_config(page_title="Growth Mindset App", layout="centered")
st.title("🌱 Growth Mindset Challenge")

page = st.sidebar.selectbox("Navigate", ["Home", "Learn", "Set a Goal", "Daily Reflection", "Quote of the Day"])

if page == "Home":
    st.subheader("Welcome! 👋")
    st.write("This app helps you develop and track a growth mindset.")
    st.write("Navigate from the sidebar to learn, set goals, and reflect daily.")

elif page == "Learn":
    st.subheader("📘 What is a Growth Mindset?")
    st.markdown("""
    A **growth mindset** is the belief that intelligence and abilities can be developed
    through effort, learning, and persistence. 

    ### Growth vs Fixed Mindset:
    - Growth: "I can learn anything with enough effort."
    - Fixed: "I'm just not good at this."

    Adopt a mindset that embraces challenges and keeps learning alive! 💪
    """)

elif page == "Set a Goal":
    st.subheader("🎯 Set Your Learning Goal")
    goal = st.text_input("What do you want to achieve this week?")
    if st.button("Save Goal"):
        if goal:
            st.session_state["goal"] = goal
            st.success("Goal saved!")
        else:
            st.warning("Please enter a goal before saving.")

    if "goal" in st.session_state:
        st.info(f"Your current goal: {st.session_state['goal']}")

elif page == "Daily Reflection":
    st.subheader("📝 Daily Reflection")
    st.write("Take a moment to reflect on your learning today.")

    struggle = st.text_area("What did you struggle with today?")
    lesson = st.text_area("What did you learn from it?")

    if st.button("Save Reflection"):
        if struggle and lesson:
            date = datetime.now().strftime("%Y-%m-%d")
            st.session_state["reflection"] = {"date": date, "struggle": struggle, "lesson": lesson}
            st.success("Reflection saved!")
        else:
            st.warning("Please complete both fields before saving.")

    if "reflection" in st.session_state:
        st.write("---")
        st.write(f"**Last Reflection ({st.session_state['reflection']['date']})**")
        st.write(f"**Struggle:** {st.session_state['reflection']['struggle']}")
        st.write(f"**Lesson:** {st.session_state['reflection']['lesson']}")

elif page == "Quote of the Day":
    st.subheader("💬 Motivation")
    quote = random.choice(quotes)
    st.success(quote)
    st.caption("Refresh the page for a new quote!")





























































































































# =============================================================================================
# NEW PROJECT
# import streamlit as st
# import pandas as pd
# import numpy as np
# import altair as alt
# import json
# import os
# import datetime
# import random
# from pathlib import Path

# # ----- App Configuration -----
# st.set_page_config(
#     page_title="Growth Mindset Challenge",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ----- Functions -----
# def load_data():
#     """Load user data from file or create new data structure if not exists"""
#     if os.path.exists("data/user_data.json"):
#         with open("data/user_data.json", "r") as f:
#             return json.load(f)
#     else:
#         # Create data directory if it doesn't exist
#         Path("data").mkdir(exist_ok=True)
        
#         # Return default data structure
#         return {
#             "challenges_completed": 0,
#             "reflection_count": 0,
#             "streak": 0,
#             "last_activity_date": "",
#             "mindset_score": 50,
#             "reflections": [],
#             "challenges": [],
#             "goals": []
#         }

# def save_data(data):
#     """Save user data to file"""
#     with open("data/user_data.json", "w") as f:
#         json.dump(data, f)

# def update_streak(data):
#     """Update user streak based on last activity"""
#     today = datetime.date.today().isoformat()
    
#     if data["last_activity_date"] == "":
#         data["streak"] = 1
#     elif data["last_activity_date"] == today:
#         # Already logged activity today, don't increment streak
#         pass
#     elif data["last_activity_date"] == (datetime.date.today() - datetime.timedelta(days=1)).isoformat():
#         # Activity was yesterday, increment streak
#         data["streak"] += 1
#     else:
#         # Activity was before yesterday, reset streak
#         data["streak"] = 1
    
#     data["last_activity_date"] = today
#     return data

# def get_challenge():
#     """Return a random growth mindset challenge"""
#     challenges = [
#         "Try something new today that you might not be immediately good at.",
#         "When you face a setback today, write down what you learned from it.",
#         "Replace 'I can't do this' with 'I can't do this yet' when you face difficulties today.",
#         "Ask for feedback on something you're working on and use it to improve.",
#         "Set a learning goal (not a performance goal) for something you want to achieve.",
#         "Celebrate someone else's success and growth today.",
#         "Find a mentor or role model who demonstrates a growth mindset.",
#         "Reflect on a past failure and identify the growth opportunities it presented.",
#         "Practice deliberate learning by focusing on your weakest area for 30 minutes.",
#         "Share something you learned recently with someone else.",
#         "Express gratitude for a challenge that helped you grow.",
#         "Use the word 'yet' when discussing something you're struggling with.",
#         "Identify and challenge a limiting belief you hold about your abilities.",
#         "Spend 20 minutes learning about a topic outside your comfort zone.",
#         "Respond to criticism today by looking for the valuable feedback within it."
#     ]
#     return random.choice(challenges)

# def calculate_mindset_score(data):
#     """Calculate a growth mindset score based on user activity"""
#     base_score = 50
#     activity_bonus = min(30, data["challenges_completed"] + data["reflection_count"])
#     streak_bonus = min(20, data["streak"] * 2)
    
#     return base_score + activity_bonus + streak_bonus

# # ----- Load User Data -----
# user_data = load_data()

# # ----- Sidebar -----
# st.sidebar.title("🧠 Growth Mindset Challenge")

# # User stats in sidebar
# st.sidebar.subheader("Your Stats")
# col1, col2 = st.sidebar.columns(2)
# with col1:
#     st.metric("Challenges Completed", user_data["challenges_completed"])
#     st.metric("Current Streak", user_data["streak"])
# with col2:
#     st.metric("Reflections", user_data["reflection_count"])
#     st.metric("Mindset Score", user_data["mindset_score"])

# # Navigation
# page = st.sidebar.radio("Navigate to", ["Dashboard", "Daily Challenge", "Reflect", "Goals", "Resources"])

# # ----- Pages -----

# if page == "Dashboard":
#     st.title("📊 Your Growth Mindset Journey")
    
#     col1, col2 = st.columns([2, 1])
    
#     with col1:
#         st.subheader("Your Growth Over Time")
        
#         # Generate example data if no reflections exist
#         if len(user_data["reflections"]) < 3:
#             chart_data = pd.DataFrame({
#                 'date': pd.date_range(start='2023-01-01', periods=10),
#                 'mindset_score': [45, 48, 52, 55, 60, 58, 65, 70, 72, 75]
#             })
#         else:
#             # Use actual reflection data for chart
#             dates = [r['date'] for r in user_data["reflections"][-10:]]
#             values = [r.get('score', 50) for r in user_data["reflections"][-10:]]
#             chart_data = pd.DataFrame({
#                 'date': dates,
#                 'mindset_score': values
#             })
            
#         chart = alt.Chart(chart_data).mark_line(point=True).encode(
#             x='date:T',
#             y=alt.Y('mindset_score:Q', scale=alt.Scale(domain=[0, 100])),
#             tooltip=['date', 'mindset_score']
#         ).properties(height=300)
        
#         st.altair_chart(chart, use_container_width=True)
        
#         st.subheader("Recent Reflections")
#         if user_data["reflections"]:
#             for reflection in user_data["reflections"][-3:]:
#                 with st.expander(f"{reflection['date']}: {reflection['title']}"):
#                     st.write(reflection['content'])
#         else:
#             st.info("No reflections yet. Head to the Reflect tab to add your first reflection!")
    
#     with col2:
#         st.subheader("Growth Tips")
#         tips = [
#             "Embrace challenges as opportunities to learn.",
#             "View effort as a path to mastery.",
#             "Learn from criticism rather than ignoring it.",
#             "Find lessons and inspiration in others' success.",
#             "Remember that abilities can be developed through dedication and hard work."
#         ]
        
#         for tip in tips:
#             st.markdown(f"• {tip}")
        
#         st.subheader("Challenge Streak")
#         streak_days = min(user_data["streak"], 7)
#         progress_html = ""
#         for i in range(7):
#             if i < streak_days:
#                 progress_html += "🔵 "
#             else:
#                 progress_html += "⚪ "
        
#         st.markdown(f"**Last 7 days:** {progress_html}")
        
#         if streak_days == 7:
#             st.success("Amazing! You've completed a full week of challenges!")
#         elif streak_days >= 3:
#             st.info(f"Great job maintaining a {streak_days}-day streak!")
#         else:
#             st.info("Complete daily challenges to build your streak!")

# elif page == "Daily Challenge":
#     st.title("🎯 Daily Growth Challenge")
    
#     # Get today's date
#     today = datetime.date.today().isoformat()
    
#     # Check if a challenge has already been completed today
#     today_challenge_completed = any(c.get('date') == today for c in user_data["challenges"])
    
#     if today_challenge_completed:
#         st.success("You've already completed today's challenge. Great job!")
        
#         # Show the completed challenge
#         for challenge in user_data["challenges"]:
#             if challenge.get('date') == today:
#                 st.markdown(f"**Today's Challenge:** {challenge['challenge']}")
#                 st.markdown(f"**Your Response:** {challenge['response']}")
#                 break
#     else:
#         # Generate a new challenge
#         daily_challenge = get_challenge()
        
#         st.markdown(f"## Today's Challenge:\n\n**{daily_challenge}**")
        
#         st.markdown("---")
#         st.markdown("### Your Response")
        
#         with st.form("challenge_form"):
#             response = st.text_area("How did you approach this challenge? What did you learn?", 
#                                     height=150)
            
#             rating = st.slider("How difficult was this challenge for you?", 
#                                1, 10, 5, 
#                                help="1 = Very Easy, 10 = Very Challenging")
            
#             submitted = st.form_submit_button("Complete Challenge")
            
#             if submitted and response:
#                 # Record the challenge completion
#                 user_data["challenges"].append({
#                     "date": today,
#                     "challenge": daily_challenge,
#                     "response": response,
#                     "difficulty": rating
#                 })
                
#                 # Update user stats
#                 user_data["challenges_completed"] += 1
#                 user_data = update_streak(user_data)
#                 user_data["mindset_score"] = calculate_mindset_score(user_data)
                
#                 # Save updated data
#                 save_data(user_data)
                
#                 st.success("Challenge completed! Your growth mindset is strengthening.")
#                 st.balloons()
#             elif submitted:
#                 st.warning("Please provide a response to complete the challenge.")

# elif page == "Reflect":
#     st.title("📝 Reflection Journal")
    
#     st.markdown("""
#     Reflection is a powerful tool for developing a growth mindset. Use this space to:
    
#     * Document your learning experiences
#     * Analyze how you responded to challenges
#     * Celebrate your growth and progress
#     * Plan how to improve going forward
#     """)
    
#     with st.form("reflection_form"):
#         title = st.text_input("Reflection Title")
#         content = st.text_area("Your Reflection", height=200)
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             growth_rating = st.slider("Rate your growth mindset in this situation", 
#                                     1, 10, 7,
#                                     help="1 = Fixed Mindset, 10 = Strong Growth Mindset")
        
#         with col2:
#             categories = st.multiselect("Categories", 
#                                      ["Challenge", "Learning", "Setback", "Success", "Feedback", "Goal"])
        
#         submitted = st.form_submit_button("Save Reflection")
        
#         if submitted and title and content:
#             # Record the reflection
#             user_data["reflections"].append({
#                 "date": datetime.date.today().isoformat(),
#                 "title": title,
#                 "content": content,
#                 "score": growth_rating * 10,  # Scale to 0-100
#                 "categories": categories
#             })
            
#             # Update user stats
#             user_data["reflection_count"] += 1
#             user_data = update_streak(user_data)
#             user_data["mindset_score"] = calculate_mindset_score(user_data)
            
#             # Save updated data
#             save_data(user_data)
            
#             st.success("Reflection saved! Taking time to reflect is key to developing a growth mindset.")
#         elif submitted:
#             st.warning("Please provide both a title and content for your reflection.")
    
#     if user_data["reflections"]:
#         st.markdown("---")
#         st.subheader("Your Previous Reflections")
        
#         for reflection in reversed(user_data["reflections"]):
#             with st.expander(f"{reflection['date']} - {reflection['title']}"):
#                 st.write(reflection['content'])
#                 st.markdown(f"**Growth Score:** {reflection.get('score', 50)}/100")
                
#                 if reflection.get('categories'):
#                     st.markdown(f"**Categories:** {', '.join(reflection['categories'])}")

# elif page == "Goals":
#     st.title("🎯 Growth Goals")
    
#     st.markdown("""
#     Setting learning-oriented goals (rather than just performance goals) is essential for 
#     developing a growth mindset. Focus on what you want to learn and how you want to improve, 
#     not just what you want to achieve.
#     """)
    
#     with st.form("goal_form"):
#         goal_title = st.text_input("Goal Title")
#         goal_description = st.text_area("What do you want to learn or improve?")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             goal_timeline = st.selectbox("Timeline", ["1 week", "1 month", "3 months", "6 months", "1 year"])
        
#         with col2:
#             goal_difficulty = st.select_slider("Challenge Level", 
#                                              options=["Easy", "Moderate", "Challenging", "Very Challenging"])
        
#         steps = st.text_area("What steps will you take to achieve this goal?")
        
#         submitted = st.form_submit_button("Set Goal")
        
#         if submitted and goal_title and goal_description:
#             # Record the goal
#             goal_id = len(user_data["goals"])
#             user_data["goals"].append({
#                 "id": goal_id,
#                 "date_created": datetime.date.today().isoformat(),
#                 "title": goal_title,
#                 "description": goal_description,
#                 "timeline": goal_timeline,
#                 "difficulty": goal_difficulty,
#                 "steps": steps,
#                 "completed": False
#             })
            
#             # Save updated data
#             save_data(user_data)
            
#             st.success("New growth goal set! Setting learning goals is a key aspect of the growth mindset.")
#         elif submitted:
#             st.warning("Please provide both a title and description for your goal.")
    
#     if user_data["goals"]:
#         st.markdown("---")
#         st.subheader("Your Growth Goals")
        
#         # Active goals
#         active_goals = [g for g in user_data["goals"] if not g.get('completed', False)]
#         if active_goals:
#             st.markdown("### Active Goals")
#             for goal in active_goals:
#                 with st.expander(f"{goal['title']} ({goal['timeline']})"):
#                     st.write(goal['description'])
#                     st.markdown(f"**Difficulty:** {goal['difficulty']}")
                    
#                     if goal.get('steps'):
#                         st.markdown("**Steps:**")
#                         st.write(goal['steps'])
                    
#                     if st.button(f"Mark Complete", key=f"complete_{goal['id']}"):
#                         # Mark goal as completed
#                         for g in user_data["goals"]:
#                             if g['id'] == goal['id']:
#                                 g['completed'] = True
#                                 g['date_completed'] = datetime.date.today().isoformat()
                        
#                         # Update mindset score
#                         user_data["mindset_score"] = min(100, user_data["mindset_score"] + 5)
                        
#                         # Save updated data
#                         save_data(user_data)
#                         st.experimental_rerun()
        
#         # Completed goals
#         completed_goals = [g for g in user_data["goals"] if g.get('completed', False)]
#         if completed_goals:
#             st.markdown("### Completed Goals")
#             for goal in completed_goals:
#                 with st.expander(f"✅ {goal['title']}"):
#                     st.write(goal['description'])
#                     st.markdown(f"**Completed on:** {goal.get('date_completed', 'Unknown')}")

# elif page == "Resources":
#     st.title("📚 Growth Mindset Resources")
    
#     st.markdown("""
#     ## Understanding Growth Mindset
    
#     The concept of growth mindset was developed by psychologist Carol Dweck after decades of research on 
#     achievement and success. Here are some key resources to deepen your understanding:
#     """)
    
#     resources = [
#         {
#             "title": "Mindset: The New Psychology of Success",
#             "author": "Carol Dweck",
#             "type": "Book",
#             "description": "The foundational book that introduced the concept of growth mindset to the world."
#         },
#         {
#             "title": "The Power of Believing You Can Improve",
#             "author": "Carol Dweck",
#             "type": "TED Talk",
#             "description": "A concise introduction to growth mindset principles in an engaging format."
#         },
#         {
#             "title": "Grit: The Power of Passion and Perseverance",
#             "author": "Angela Duckworth",
#             "type": "Book",
#             "description": "Explores how persistence and resilience contribute to growth and achievement."
#         },
#         {
#             "title": "The Growth Mindset Coach",
#             "author": "Annie Brock & Heather Hundley",
#             "type": "Book",
#             "description": "A month-by-month guidebook for teachers implementing growth mindset principles."
#         },
#         {
#             "title": "Mindset Works",
#             "author": "Founded by Carol Dweck and Lisa Blackwell",
#             "type": "Website",
#             "description": "Offers programs and resources for developing growth mindset in educational settings."
#         }
#     ]
    
#     for resource in resources:
#         with st.expander(f"{resource['title']} by {resource['author']} ({resource['type']})"):
#             st.write(resource['description'])
    
#     st.markdown("---")
    
#     st.subheader("Growth Mindset Principles")
    
#     principles = {
#         "Embrace Challenges": "Seek out difficult tasks rather than avoiding them.",
#         "Persist Through Obstacles": "View obstacles as opportunities to grow, not reasons to give up.",
#         "Value Effort": "See effort as a path to mastery, not a sign of inadequacy.",
#         "Learn from Criticism": "Use feedback as valuable information for improvement.",
#         "Find Inspiration in Others' Success": "Learn from others instead of feeling threatened."
#     }
    
#     for principle, description in principles.items():
#         st.markdown(f"**{principle}:** {description}")
    
#     st.markdown("---")
    
#     st.subheader("Growth Mindset vs. Fixed Mindset")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("### Growth Mindset")
#         st.markdown("• Embraces challenges")
#         st.markdown("• Persists in the face of setbacks")
#         st.markdown("• Sees effort as a path to mastery")
#         st.markdown("• Learns from criticism")
#         st.markdown("• Finds lessons in others' success")
#         st.markdown("• Believes abilities can be developed")
    
#     with col2:
#         st.markdown("### Fixed Mindset")
#         st.markdown("• Avoids challenges")
#         st.markdown("• Gives up easily")
#         st.markdown("• Views effort as fruitless")
#         st.markdown("• Ignores useful feedback")
#         st.markdown("• Feels threatened by others' success")
#         st.markdown("• Believes abilities are static")

# # Add CSS for improved appearance
# st.markdown("""
# <style>
#     .stApp {
#         max-width: 1200px;
#         margin: 0 auto;
#     }
#     h1 {
#         color: #1E3A8A;
#     }
#     h2 {
#         color: #1E3A8A;
#     }
#     h3 {
#         color: #2563EB;
#     }
#     .stButton>button {
#         background-color: #2563EB;
#         color: white;
#     }
#     .stButton>button:hover {
#         background-color: #1E40AF;
#         color: white;
#     }
# </style>
# """, unsafe_allow_html=True)