import time
import streamlit as st

st.set_page_config(page_title="Clock & Timer", page_icon="⏰")

st.title("Digital Clock & Timer")

clock_placeholder = st.empty()


st.subheader("Timer")
seconds_input = st.number_input(
    "Set Timer (seconds):", min_value=1, value=60, step=1
)
start_button = st.button("Start Timer")


if start_button:
    timer_placeholder = st.empty()
    for t in range(int(seconds_input), -1, -1):
        mins, secs = divmod(t, 60)
        timer_placeholder.metric("Time Remaining", f"{mins:02d}:{secs:02d}")
        time.sleep(1)
    st.success("Time's Up!")


current_time = time.strftime("%H:%M:%S | %d-%m-%Y")
clock_placeholder.header(f"Current Time: {current_time}")
