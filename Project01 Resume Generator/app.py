import streamlit as st

st.set_page_config(
    page_title="AI Resume Generator",
    page_icon="📄",
    layout="wide"
)

# Styling
st.markdown("""
<style>
.main-title {
    font-size: 45px;
    font-weight: bold;
    color: #1E88E5;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<p class="main-title">📄 AI Resume & Cover Letter Generator</p>',
    unsafe_allow_html=True
)

st.write("Generate ATS-Friendly Resumes & Cover Letters")

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("""
    AI Resume Generator

    Features:
    - Resume Generation
    - Cover Letter Generation
    - ATS Score
    - Download Resume
    """)

# Layout
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Full Name")
    job_role = st.text_input("Target Job Role")

with col2:
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")

skills = st.text_area("Skills")
experience = st.text_area("Experience")

if st.button("Generate Resume"):

    ats_score = 92

    st.success("Resume Generated Successfully")

    st.metric("ATS Score", f"{ats_score}%")

    resume = f"""
# {name}

Target Role: {job_role}

Email: {email}
Phone: {phone}

PROFESSIONAL SUMMARY
Cybersecurity enthusiast with experience in SOC operations,
AI applications, Python automation and security monitoring.

SKILLS
{skills}

EXPERIENCE
{experience}

CERTIFICATIONS
- Microsoft Security Operations Analyst Associate
- Microsoft Azure AI Engineer Associate

LEADERSHIP
- Secretary, IEEE SB MIET
- Treasurer, IAS SBC MIET
"""

    st.subheader("Generated Resume")
    st.code(resume)

    st.download_button(
        label="📥 Download Resume",
        data=resume,
        file_name="Resume.txt",
        mime="text/plain"
    )

if st.button("Generate Cover Letter"):

    cover_letter = f"""
Dear Hiring Manager,

I am writing to express my interest in the {job_role} position.

My background includes cybersecurity, AI projects,
SOC operations and Python development.

Key Skills:
{skills}

Experience:
{experience}

I believe my technical expertise and leadership
experience make me a strong candidate.

Thank you for your consideration.

Regards,
{name}
"""

    st.subheader("Generated Cover Letter")
    st.text_area(
        "Cover Letter",
        cover_letter,
        height=400
    )

