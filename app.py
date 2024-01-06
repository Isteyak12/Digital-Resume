from pathlib import Path
from PIL import Image
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "isteyak_cs_resume.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Isteyak"
NAME = "Isteyak "
DESCRIPTION = """
I am a third-year student at the University of Windsor currently pursuing a Bachelor of
Computer Science degree and actively looking for coop opportunities. I have started my 
computer science journey back in 2021 at the highest ranked private university of 
Bangladesh, infamously known as Independent University, Bangladesh, until I transferred 
to University of Windsor for a better hands-on learning experience. As a volunteer in a 
systems administration position, I am currently working for DEFEND, a tech company known
for making technologies that are focused primarily on authentication systems for the safety 
of vulnerable people. Similarly, it has been a great Fall 2023 semester as I was a teaching
assistant for a data structure and algorithms course at the University of Windsor where 
I taught 100+ students how to apply Java in various data structure problems. 
Fun fact: I am a big fan of C++, but my projects are based on Python. Personally, 
I believe I make the best chicken stew, I love listening to R&B and soft rock, and on 
weekends, I enjoy riding my E Scooter at night."""

EMAIL = "isteyak@uwindsor.ca"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/isteyak-409578230/",
    "GitHub": "https://github.com/Isteyak12",

}

PROJECTS = {
    "🏆Github Repos--> ": "https://github.com/Isteyak12?tab=repositoriess",
}

st.set_page_config(page_title=PAGE_TITLE)
st.title("Hello, Friends!")


# --- LOAD CSS, PDF & PROFIL PIC ---
# with open(css_file) as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    
profile_pic = Image.open(profile_pic)
# --HERO SECTION---
col1, col2= st.columns(2, gap="small")
with col2:
        st.image(profile_pic, width=230)
with col1:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label= "📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",)
        # st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
# st.write("#")
# cols=st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#       cols[index].write(f"[{platform}]({link})")
        
        
# ---EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("🌐 Experience & Qualifications")
st.write("""
-  Strong hands-on experience and knowledge in Python and Java
-  Good understanding of statistical principles and their respective applications
-  Excellent team player and displaying a strong sense of initiative on tasks
-  Intuitive understanding of linear algebra-based applications
"""
)

#---SKILLS--
st.write('\n')
st.subheader("🛠️ Technical Skills")
st.write("""
- 👩‍💻 Programming Languages: Python, Java, C++, C
- Web Development:  HTML, CSS, JavaScript. 
- Streamlit  App Development. 
- tKinter GUI App Development. 
- Data Structures  and Algorithms. 
""")

st.write("---")
# --- WORK HISTORY ---
st.write('\n')
st.subheader("⚡ Work History")
# --- JOB 1
st.write("**Teaching Assistant | University of Windsor**")
st.write("*Aug 2023 - Present*")
st.write(
    """
-  Mentored more than 100+ students single-handedly in the absence of TAs during labs. 
-  Guided students  with understanding  of codes correlating  to its algorithm. 
-  Checked and marked 100+ assignments  within a tight schedule and provided feedback  to every 
individual student within 1 day.
"""
)
# --- JOB 2
st.write("💎", "**Event Assistant | A.C.M. Club Independent  University, Bangladesh**")
st.write("*Mar 2021 - Aug 2022*")
st.write(
    """
-  Assisted with organizing  10 events per annum related to computer  science and technology  with no 
    less than 70% attendance  per event. 
-  Collaborated  with others as a team for event logistics, including venue selection,  setup, and 
    equipment  arrangement,  ensuring events were well-prepared  and visually appealing
"""
)

st.write("---")
#---Education--
st.write('\n')
st.subheader("🎓 Education")
# st.write("")
# st.write("---")
st.subheader("University of Windsor, Windsor, ON")
st.write("*[Jan 2023 – Present]*")
st.write("Bachelor  of Computer  Science, Honors Applied Computing CO-OP ")
st.write("""
- Major average: 83.0.
""")

# st.write("---")
# st.write("January 2022 - Present")
st.subheader("Independent University, Bangladesh")
st.write("*[Jan 2021 - Aug 2022]*")
st.write("Bachelor of Science in Computer Science & Engineering")
st.write("""
- Attained Dean's Honor's List Award for Summer 2021.
- Achieved Dean's List Award for Spring 2022.
""")

st.write("---")
st.write('\n')
st.subheader("💡 Projects")
# st.write("")
st.subheader("🚀 NASA Space Apps Hackathon  Windsor Edition")
st.write("""
-  Cleaned a database and converted it to a JSON file using Streamlit technology. 
-  Implemented  a search bar option for user-friendly  data retrieval. 
-  Automated  machine-independent  digital resume web page portfolio based on Streamlit technology. 
""")

st.write('\n')
# st.write("")
st.subheader("🐳 Docker Containerization and CI/CD Workflow")
st.write("""
- Configured  with containerization  of a web page to make it  runnable on any machine. 
- Orchestrated Docker containers for a Python web app, ensuring seamless deployment across various 
environments and platforms.
- Utilized Docker for isolating a Binary Search Tree implementation in Python, optimizing resource utilization.
- Implemented a robust CI/CD workflow using GitHub Actions, automating the build and deployment 
processes for both the web app and Binary Search Tree applications. """)
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
   
st.write('\n')
st.write("---")
st.subheader("**PLEASE CONTACT ME VIA:**")
st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/isteyak-409578230/)")
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Isteyak12)")
st.markdown("[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:isteyak@uwindsor.ca)")
