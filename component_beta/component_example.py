import json
import time
import pandas as pd
import pandas_highcharts
import streamlit as st

from io import StringIO
from pandas_highcharts.core import serialize

# Register "my_component" as a Streamlit component.
st.register_component("my_component", "component_template/build")

if st.button("Lift Off"):
    t = st.empty()
    text = "Welcome to the first day... of the rest... of your life"
    emojis = [":sparkler:", ":fire:", ":rocket:"]

    for i in range(len(list(text)) + 1):
        t.markdown("## %s..." % text[0:i])
        time.sleep(0.1)

    for i in emojis:
      time.sleep(0.3)
      t.markdown("## %s %s" % (text, i))

    " "
    " "
    time.sleep(1)
    st.markdown("# High Charts integration with Streamlit!")
    time.sleep(2)

    data = """ts;A;B;C
    2015-01-01 00:00:00;27451873;29956800;113
    2015-01-01 01:00:00;20259882;17906600;76
    2015-01-01 02:00:00;11592256;12311600;48
    2015-01-01 03:00:00;11795562;11750100;50
    2015-01-01 04:00:00;9396718;10203900;43
    2015-01-01 05:00:00;14902826;14341100;53
    """

    def parse_json(chart):
        return json.loads(chart.split("new Highcharts.Chart(")[1].split(");")[0])

    df = pd.read_csv(StringIO(data), sep=';', index_col='ts', parse_dates=['ts'])

    chart = serialize(df, render_to="my-chart", title="My Chart")
    st.my_component(name="Basic Line Plot", default=0, options=parse_json(chart))
    time.sleep(2)

    chart = serialize(df, render_to="my-chart", title="Test", kind="bar")
    st.my_component(name="Basic column Plot", default=0, options=parse_json(chart))
    time.sleep(2)

    chart = serialize(df, render_to="my-chart", title="Test", kind="barh")
    st.my_component(name="Basic column plot", default=0, options=parse_json(chart))
    time.sleep(2)

    chart = serialize(df, render_to="my-chart", title="Test", secondary_y = ["C"])
    st.my_component(name="Plot C on secondary axis", default=0, options=parse_json(chart))
    time.sleep(2)

    chart = serialize(df, render_to="my-chart", title="Test", figsize = (1000, 700))
    st.my_component(name="Plot on a 1000x700 div", default=0, options=parse_json(chart))
    time.sleep(2)

    st.markdown("## We can easily support drawing a High Chart but need internal")
    st.markdown("## Streamlit library changes to support additional functionality")

    # Resources
    # https://www.highcharts.com/docs/working-with-data/live-data
    # https://github.com/gtnx/pandas-highcharts
