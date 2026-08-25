import time
import streamlit as st

st.title("My Simple Clock & Timer")


st.subheader("Current Time")
st.write(time.strftime("%H:%M:%S"))

st.write("---")


st.subheader("Timer")


mins = st.number_input("Enter Minutes", min_value=0, value=1)
secs = st.number_input("Enter Seconds", min_value=0, value=0)

if st.button("Start Timer"):
    
    total_seconds = (mins * 60) + secs
    timer_box = st.empty()
    for t in range(int(total_seconds), -1, -1):
            m = t // 60
            s = t % 60
            timer_box.write(f"Time left: {m:02d}:{s:02d}")
            time.sleep(1)
            
