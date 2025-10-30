import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Page Configuration ---
st.set_page_config(
    page_title="Raziff Gumapon - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS ---
st.markdown("""
<style>
    .main-header {
        font-size: 3rem !important;
        color: var(--text-color);
        text-align: center;
        margin-bottom: 2rem;
    }
    .project-card {
        background-color: var(--background-color);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid var(--primary-color);
    }
    .skill-category {
        background: var(--primary-color);
        color: var(--secondary-background-color);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "👤 About Me", "🛠️ Skills", "💼 Portfolio", "📊 Fun Stats"])

# Contact info in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 📞 Get In Touch")
st.sidebar.markdown("📧 Email: gumaponraziff@gmail.com")
st.sidebar.markdown("💻 GitHub: https://github.com/RaziffAzi")

# --- Home ---
if page == "🏠 Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="main-header">👋 Hi, I\'m Raziff Gumapon</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: justify; font-size: 1.1rem;">
        I'm a passionate Computer Science student at Cebu Institute of Technology - University, eager to explore the world of data science and machine learning. 
        I enjoy problem-solving and programming and am constantly seeking opportunities to learn and grow in my field, even though it is sometimes challenging.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.subheader("🚀 Quick Facts")
        fact_col1, fact_col2, fact_col3 = st.columns(3)
        
        with fact_col1:
            st.metric("Projects Completed", "3+", "100%")
        with fact_col2:
            st.metric("Programming Languages", "8+", "Versatile")
        with fact_col3:
            st.metric("Experience Level", "Student", "Growing")
    
    with col2:
        st.write("")
        st.write("")
        try:
            image = Image.open("images/profile.jpg")
            st.image(image, use_container_width=True, caption="That's me! 👋")
        except:
            st.info("📷 Profile image would appear here")

# --- About Me ---
elif page == "👤 About Me":
    st.header("📚 About Me")
    
    col1, col2 = st.columns([2, 1.3])
    
    with col1:
        st.markdown("""
        ### 🎓 Education
        **Enrolled in Bachelor of Science in Computer Science Program**  
        *Cebu Institute of Technology - University*  
        *Expected Graduation: 2027*
        
        ### 💡 Interests & Passion
        - 🤖 **Artificial Intelligence & Machine Learning**
        - 📊 **Data Science & Analytics**
        - 💻 **Software Development**
        
        ### 🎮 Hobbies & Interests
        - Programming side projects
        - Watching movies and tv series
        - Gaming and interactive media
        - Lying in bed and thinking about life
        """)
    
    with col2:
        st.markdown("""
        ### 📍 Location
        Cebu, Philippines

        ### 📖 Currently Learning
        - Data Analysis and Visualization  
        - Intelligent Systems  
        - Backend Web Development with Django  
        - App Development with React and Spring Boot  
        - Automata Theory and Formal Languages
        """)


# --- Skills ---
elif page == "🛠️ Skills":
    st.header("🛠️ Technical Skills")
    
    skills = {
        "Programming Languages": ["Python", "C#", "C/C++", "Java", "JavaScript", "Kotlin", "MySQL"],
        "Tools & Frameworks": ["Django", "Git", "GitHub", "Jupyter Notebook", "React", "Spring Boot", "Streamlit"],
        "Libraries": ["NumPy", "Pandas"],
        "Other Skills": ["Data Structures & Algorithms", "OOP", "Problem Solving", "Math for Computer Science"]
    }
    
    for category, skill_list in skills.items():
        st.markdown(f'<div class="skill-category"><h3>{category}</h3></div>', unsafe_allow_html=True)
        
        # Create badges for skills
        badges = " ".join([f"`{skill}`" for skill in skill_list])
        st.markdown(badges)
        st.write("")

# --- Portfolio ---
elif page == "💼 Portfolio":
    st.header("💼 Portfolio Projects")

    # === Asatabai App ===
    with st.expander("🎯 Asatabai App - Completed", expanded=True):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.write("**Description:** An Android app built with Kotlin to explore Cebu's jeepney routes and destinations.")
            st.write("**Tech Stack:** Kotlin, Google Maps API, Firebase, Android SDK")
            st.write("**Key Features:**")
            st.write("- Interactive maps")
            st.write("- User authentication")
            st.write("- Destination details")
            st.write("- Landmarks")

        with col2:
            st.metric("Progress", "100%")
            st.progress(100)
            with st.expander("📸 View Project Preview"):
                try:
                    st.image(Image.open("images/asatabai.png"), use_container_width=True)
                except:
                    st.info("📷 Project preview unavailable")

    # === BudgetBuddy ===
    with st.expander("🎯 BudgetBuddy - Completed", expanded=True):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.write("**Description:** A JavaFX-based financial tracking app with MySQL database integration.")
            st.write("**Tech Stack:** Java, JavaFX, MySQL, OOP Design Patterns")
            st.write("**Key Features:**")
            st.write("- Transaction management")
            st.write("- Financial summaries")
            st.write("- Multithreading")

        with col2:
            st.metric("Progress", "100%")
            st.progress(100)
            with st.expander("📸 View Project Preview"):
                try:
                    st.image(Image.open("images/budget_buddy.png"), use_container_width=True)
                except:
                    st.info("📷 Project preview unavailable")

    # === Wildcat's Den ===
    with st.expander("🎯 Wildcat's Den - Completed", expanded=True):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.write("**Description:** A 2D exploration game built with LibGDX showcasing CIT-U's campus.")
            st.write("**Tech Stack:** Java, LibGDX, Gradle, Game Development Patterns")
            st.write("**Key Features:**")
            st.write("- Interactive NPCs")
            st.write("- Collision detection")
            st.write("- Diagonal Movement")
            st.write("- Engaging Exploration Mechanics")

        with col2:
            st.metric("Progress", "100%")
            st.progress(100)
            with st.expander("📸 View Project Preview"):
                try:
                    st.image(Image.open("images/wildcats_den.png"), use_container_width=True)
                except:
                    st.info("📷 Project preview unavailable")

# --- Fun Stats ---
elif page == "📊 Fun Stats":
    st.header("📊 Skills & Analytics")
    
    # Enhanced skills data
    df = pd.DataFrame({
        "Skill": ["Python", "Java", "C", "C++", "C#", "MySQL", "JavaScript","Django", "Kotlin", "React"],
        "Category": ["Language", "Language", "Language", "Language", "Language", "Database", "Language", "Framework", "Language", "Framework"],
        "Proficiency (%)": [70, 68, 65, 65, 45, 40, 35, 30, 25, 25],
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Skill Proficiency Chart")
        fig = px.bar(df, x='Skill', y='Proficiency (%)', 
                    color='Proficiency (%)',
                    color_continuous_scale='viridis')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Skills by Category")
        category_count = df['Category'].value_counts()
        fig_pie = px.pie(values=category_count.values, 
                        names=category_count.index,
                        title="Skill Distribution by Category")
        st.plotly_chart(fig_pie, use_container_width=True)
    
    st.subheader("📋 Detailed Skills Table")
    st.dataframe(df, use_container_width=True, hide_index=True)

# --- Footer ---
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)
with footer_col2:
    st.markdown("<div style='text-align: center;'>© 2025 Raziff Gumapon | Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)