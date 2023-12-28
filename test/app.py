import streamlit as st
import subprocess


def launch_app():
    subprocess.Popen(["streamlit", "run", "app2.py"], shell=True)

def launch_app2():
    subprocess.Popen(["streamlit", "run", "app2.py"], shell=True)

# def launch_app3():
#     subprocess.Popen(["streamlit", "run", "app2.py"], shell=True)

# def launch_app4():
#     subprocess.Popen(["streamlit", "run", "app2.py"], shell=True)

# def launch_app5():
#     subprocess.Popen(["streamlit", "run", "app2.py"], shell=True)

# def launch_app6():
#     subprocess.Popen(["streamlit", "run", "app2.py"], shell=True)


st.title("ABOUT")

if st.button("Isteyak"):
    launch_app()

if st.button("John"):
    launch_app()
    
# if st.button("Isteyak"):
#     launch_app()
# if st.button("Isteyak"):
#     launch_app()
