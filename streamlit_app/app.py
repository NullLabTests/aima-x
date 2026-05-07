import streamlit as st

st.title("AIMA-X V3")

st.write(
    "Interactive AI Engineering Laboratory"
)

st.header("Modules")

modules = [
    "Search",
    "Reinforcement Learning",
    "Transformers",
    "Robotics"
]

for m in modules:
    st.write("-", m)
