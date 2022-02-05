import streamlit
import pandas
import time
from matplotlib import pyplot

streamlit.set_page_config(
    layout="wide", page_title="Titanic (as usual)", page_icon="random"
)

from utils import get_sex_name, get_class_name

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"


@streamlit.cache(suppress_st_warning=True)
def load_data():
    with streamlit.spinner("downloading data ..."):
        time.sleep(10)
        return pandas.read_csv(url)


streamlit.title("Titanic dataset")
streamlit.markdown(
    f"This project is to answer some basic questions with the [titanic dataset]({url})."
)


data = load_data()
streamlit.dataframe(data)

streamlit.markdown("---")

col1, col2 = streamlit.columns(2)

fig = pyplot.figure()
data.Pclass.value_counts().sort_index().plot.bar()
pyplot.xlabel("Pclass")
col1.pyplot(fig)

fig = pyplot.figure()
data.Sex.value_counts().sort_index().plot.bar()
pyplot.xlabel("Sex")
col2.pyplot(fig)

streamlit.markdown("---")

sex = streamlit.selectbox("Sex", sorted(data.Sex.unique()))
pclass = streamlit.radio("Pclass", sorted(data.Pclass.unique()))
age_range = streamlit.slider(
    "Age range",
    min_value=int(min(data.Age)),
    max_value=int(max(data.Age)),
    value=(int(min(data.Age)), int(max(data.Age))),
    step=1,
)

mask = (
    (data.Pclass == pclass)
    & (data.Sex == sex)
    & (data.Age >= age_range[0])
    & (data.Age <= age_range[1])
)
survived = mask & (data.Survived == 1)
probability = sum(survived) / sum(mask) * 100

streamlit.markdown(
    f"""If you were a **{get_sex_name(sex)}** at **{get_class_name(pclass)}** class, 
    and your age was between **{age_range[0]}** and **{age_range[1]}** years, then the probability to have survived was:
    **{probability:.2f}** % 
    """
)
