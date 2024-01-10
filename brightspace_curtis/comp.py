from PIL import Image
import streamlit as st

# Function to display a block for a person
def display_person(name, description, email, image_path, size):
    profile_pic = Image.open(image_path)
    profile_pic.thumbnail((size, size))

    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(profile_pic)
    with col2:
        st.title(name)
        st.write(description)
        st.write("📫", email)
        

# Define details for multiple people
people_info = [
    {
        "name": "Jovic",
        "description": """I am a third-year student at the University of Windsor currently pursuing a Bachelor of
        Computer Science degree and actively looking for coop opportunities. I have started my
        computer science journey back in 2021 at the highest ranked private university of
        Bangladesh, infamously known as Independent University, Bangladesh, until I transferred
        to University of Windsor for a better hands-on learning experience. As a volunteer in a
        """,
        "email": "jovic@uwindsor.ca",
        "image_path": "tesla.jpg",
        "size": 260
    },
    # Add more people with their details in the same format
    {
        "name": "Isteyak",
        "description": "Hey, how u doin'...",
        "email": "isteyak@uwindsor.ca",
        "image_path": "deadpool.jpg",
        "size": 260
    },
    {
        "name": "Aiden",
        "description": "Hola'...",
        "email": "isteyak@uwindsor.ca",
        "image_path": "aiden.jpg",
        "size": 260
    },
    {
        "name": "Boi",
        "description": "Hola'...",
        "email": "isteyak@uwindsor.ca",
        "image_path": "Johnny_Silverhand.webp",
        "size": 260
    },
    {
        "name": "Boi",
        "description": "Hola'...",
        "email": "isteyak@uwindsor.ca",
        "image_path": "Johnny_Silverhand.webp",
        "size": 260
    },
    {
        "name": "Boi",
        "description": "Hola'...",
        "email": "isteyak@uwindsor.ca",
        "image_path": "cap.jpg",
        "size": 260
    },
    # Add as many people as needed
]

# Display blocks for each person
for person in people_info:
    display_person(
        person["name"],
        person["description"],
        person["email"],
        person["image_path"],
        person["size"]
    )
    st.write('\n')
