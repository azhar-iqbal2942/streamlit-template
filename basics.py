import streamlit as st
import time

st.title("Streamlit tutorial")

st.header("My First Streamlit App")
st.subheader("This is sub header.")
st.text("This is basic text.")
st.caption("This is caption")

# Sidebar
st.sidebar.title("This is sidebar")
st.sidebar.text_input("Email Address")
st.sidebar.text_input("Password")
st.sidebar.button("Login")

# Messages
st.info("This is info")
st.warning("This is warning")
st.error("This is error")
st.success("This is success message")

# Markdown
st.markdown("# This is markdown")
st.markdown("## This is markdown")
st.markdown("### This is markdown")
st.markdown(":moon:")


### Widgets
st.checkbox("login")
st.button("This is button")
st.radio("Please select your gender", ["Male", "Female", "Other"])
st.selectbox(
    "Select your favorite Programming Language", ["Python", "Java", "javaScript", "Go"]
)
st.multiselect(
    "Select your favorite Programming Languages", ["Python", "Java", "javaScript", "Go"]
)
st.select_slider("Rating", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
st.slider("Select your age", 1, 30)
st.number_input("Pick a number", 1, 100)
st.text_input(
    "Your Email", placeholder="example@example.com"
)  # you cannot directly apply regex here for validation
st.date_input("Pleas select your birtdate")

t = st.time_input("Set an alarm for", value=None)
st.write("Alarm is set for", t)

st.text_area("Please share your insights")

st.file_uploader("Please upload your file")

st.color_picker("Select your favorite color")

st.progress(28, text="This is progress bar")

with st.spinner("you are in luck"):
    time.sleep(2)


# Dashboard
import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(50, 2), columns=["x", "y"])

st.title("Bar Chart")
st.bar_chart(data=data)

st.title("Line Chart")
st.line_chart(data=data)

st.title("Area Chart")
st.area_chart(data=data)
