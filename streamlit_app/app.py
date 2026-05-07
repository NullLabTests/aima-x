import streamlit as st

st.title("AIMA-X")

st.subheader("Modern AI Systems Laboratory")

sections = [
    "Search",
    "Reinforcement Learning",
    "Transformers",
    "Multi-Agent Systems",
    "Probabilistic AI"
]

for section in sections:
    st.write("-", section)

st.success("Interactive AI Engineering Playground Ready")
