from pathlib import Path
from PIL import Image
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "isteyak_cs_resume.pdf"
profile_pic = current_dir / "assets" / "profile_pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Isteyak"
PAGE_ICON = ":wave:"
NAME = "Isteyak "
DESCRIPTION = """
To introduce myself to you, I am a third year computer science student at the University of Windsor currently pursuing Bachelor of Computer Science and actively looking for coop opportunities. 
I have started my computer science journey back in 2021 at the highest ranked private university of Bangladesh, infamously known as Independent University, Bangladesh until I transferred to University of Windsor for a better hands-on learning experience. 
As a volunteer in the systems administration position, I am currently working for DEFEND, a tech company known for making technologies that are focused primarily on the authentication systems for the safety of vulnerable people.
Similarly, it has been a great Fall 2023 semester as a teaching assistant for the Data Structure and Algorithms course at the University of Windsor.
Fun fact: I am a big fan of C++ but my projects are based on Python. Personally, I believe I make the best chicken stew and love listening to R&B, soft rock and on weekends I find it cool riding escooter in the middle of the night.
"""
EMAIL = "isteyak@uwindsor.ca"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCrGx72-VbdhGtzibiOawfIQ",
    "LinkedIn": "https://www.linkedin.com/in/isteyak-409578230/",
    "GitHub": "https://github.com/Isteyak12",

}

PROJECTS = {
    "🏆Github Repos--> ": "https://github.com/Isteyak12?tab=repositoriess",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Hello Friends!")


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
        st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write("#")
cols=st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
      cols[index].write(f"[{platform}]({link})")
        
        
# ---EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write("""
- ✔️ Strong hands-on experience and knowledge in Python and Java
- ✅ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team player and displaying a strong sense of initiative on tasks
- ✅ Intuitive understanding of linear algebra-based applications
"""
)

#---SKILLS--
st.write('\n')
st.subheader("Hard Skills")
st.write("""
- 👩‍💻 Programming: Python, Java, C++, C
         """)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Teacher's Assistant | University of Windsor**")
st.write("09/2023 - Present")
st.write(
    """
- ► Mentored more than 100+ students single-handedly in the absence of TAs during labs 

"""
)

st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    