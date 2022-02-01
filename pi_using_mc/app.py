import numpy
import pandas
import plotly.express as px
import streamlit

streamlit.title("Computing PI using Monte Carlo")

streamlit.markdown(
    "![monte carlo](https://miro.medium.com/max/700/1*a9nvv3D0l1fD2uDD4dSNgQ.png)"
)

streamlit.latex(r"A_m \rightarrow \text{ number of point in the cirle}")
streamlit.latex(r"A_n \rightarrow \text{ number of point in the square}")

mc_steps = streamlit.number_input(
    "Enter the number of points", min_value=10, max_value=100000, step=100
)

run = streamlit.button("Run")


if run:
    with streamlit.spinner("Running..."):
        points = pandas.DataFrame(
            {
                "x": numpy.random.random(mc_steps),
                "y": numpy.random.random(mc_steps),
            }
        )

        mask = numpy.sqrt(points.x ** 2 + points.y ** 2) <= 1

        pi = 4 * sum(mask) / mc_steps

        streamlit.latex(r"\pi \approx %f" % pi)

        colors = ["crimson" if value else "blue" for value in mask]

        fig = px.scatter(x=points.x, y=points.y, color=colors)
        fig.update_yaxes(
            scaleanchor="x",
            scaleratio=1,
        )

        streamlit.plotly_chart(fig, use_container_width=True)

        streamlit.dataframe(points)
