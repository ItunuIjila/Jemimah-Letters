import streamlit as st
import random
import string
import time

st.title("Jemimah Letters and Alphabets App")

# Settings (same as before)
display_numbers = st.sidebar.checkbox("Display Numbers", value=True)
display_letters = st.sidebar.checkbox("Display Letters", value=True)
num_min = st.sidebar.number_input("Number Range Min", value=0, step=1)
num_max = st.sidebar.number_input("Number Range Max", value=100, step=1)
letter_case = st.sidebar.radio("Letter Case", options=["both", "upper", "lower"], index=0)
display_speed = st.sidebar.slider("Display Speed (seconds)", 0.1, 5.0, 1.0, 0.1)

display_placeholder = st.empty()

def generate_random_content():
    content_options = []
    if display_numbers:
        min_val = min(num_min, num_max)
        max_val = max(num_min, num_max)
        content_options.append(str(random.randint(min_val, max_val)))
    if display_letters:
        if letter_case == "upper":
            content_options.append(random.choice(string.ascii_uppercase))
        elif letter_case == "lower":
            content_options.append(random.choice(string.ascii_lowercase))
        else:
            content_options.append(random.choice(string.ascii_letters))
    if not content_options:
        return "⚠️"
    return random.choice(content_options)

# Initialize running state
if "running" not in st.session_state:
    st.session_state.running = False

start = st.button("Start")
stop = st.button("Stop")
generate_single = st.button("Generate Single")

if start:
    st.session_state.running = True

if stop:
    st.session_state.running = False

if generate_single:
    content = generate_random_content()
    display_placeholder.markdown(f"<h1 style='font-size:120px; text-align:center;'>{content}</h1>", unsafe_allow_html=True)
    st.session_state.running = False

if st.session_state.running:
    content = generate_random_content()
    display_placeholder.markdown(f"<h1 style='font-size:120px; text-align:center;'>{content}</h1>", unsafe_allow_html=True)
    time.sleep(display_speed)
    st.experimental_rerun()
