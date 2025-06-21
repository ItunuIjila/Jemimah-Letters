import streamlit as st
import random
import string
import time

# Title
st.title("Jemimah Letters and Alphabets App")

# Settings sidebar
st.sidebar.header("Settings")

display_numbers = st.sidebar.checkbox("Display Numbers", value=True)
display_letters = st.sidebar.checkbox("Display Letters", value=True)

num_min = st.sidebar.number_input("Number Range Min", value=0, step=1)
num_max = st.sidebar.number_input("Number Range Max", value=100, step=1)

letter_case = st.sidebar.radio("Letter Case", options=["both", "upper", "lower"], index=0)

display_speed = st.sidebar.slider("Display Speed (seconds)", 0.1, 5.0, 1.0, 0.1)

# Display area
display_placeholder = st.empty()

# Validate selection
if not display_numbers and not display_letters:
    st.warning("Select at least one display option (Numbers or Letters).")

def generate_random_content():
    if not display_numbers and not display_letters:
        return "⚠️"

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
        else:  # both
            content_options.append(random.choice(string.ascii_letters))

    return random.choice(content_options)

# Buttons for controls
start = st.button("Start")
stop = st.button("Stop")
generate_single = st.button("Generate Single")

# Session state for running loop
if "running" not in st.session_state:
    st.session_state.running = False

if start:
    st.session_state.running = True

if stop:
    st.session_state.running = False

if generate_single:
    content = generate_random_content()
    display_placeholder.markdown(f"<h1 style='font-size:120px; text-align:center;'>{content}</h1>", unsafe_allow_html=True)
    st.session_state.running = False

# If running, keep updating display
while st.session_state.running:
    content = generate_random_content()
    display_placeholder.markdown(f"<h1 style='font-size:120px; text-align:center;'>{content}</h1>", unsafe_allow_html=True)
    time.sleep(display_speed)
    # This stops Streamlit from throwing "Script ran too long" errors
    # and allows UI updates properly
    st.experimental_rerun()
