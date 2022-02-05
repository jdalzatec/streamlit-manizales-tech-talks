import streamlit as st

st.set_page_config(page_title="Widgets example")

x = st.slider(min_value=-100, max_value=100, label="Number")  # 👈 this is a widget
st.write(x, "squared is", x * x)

st.button("Hit me")
st.checkbox("Check me out")
st.radio("Radio", [1, 2, 3])
st.selectbox("Select", [1, 2, 3])
st.multiselect("Multiselect", [1, 2, 3])
st.slider("Slide me", min_value=0, max_value=10)
st.select_slider("Slide to select", options=[1, 2, 3, 4, 5])
st.text_input("Enter some text")
st.number_input("Enter a number")
st.text_area("Area for textual entry")
st.date_input("Date input")
st.time_input("Time entry")
st.color_picker("Pick a color")

file_uploaded = st.file_uploader("File uploader")
if file_uploaded:
    st.download_button("On the dl", data=file_uploaded.getvalue(), file_name="my.pdf")


st.json({"foo": "bar", "fu": "ba"})
st.metric(label="Temp", value="273 K", delta="1.2 K")


st.code("square = lambda x: x ** 2")

st.text("Fixed width text")
st.markdown("_Markdown_ <strong>Hola<strong/>", unsafe_allow_html=True)  # see *
st.caption("Balloons. Hundreds of them...")
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.write("Most objects")  # df, err, func, keras!
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
