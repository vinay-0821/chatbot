import altair as alt
import pandas as pd

def generate_plot(df: pd.DataFrame, chart_info: dict):
    chart_type = chart_info.get("type")
    x = chart_info.get("x")
    y = chart_info.get("y")

    df = df.rename(columns=lambda col: col.replace(":", "_").replace("-", "_").replace(" ", "_"))
    x = x.replace(":", "_").replace("-", "_").replace(" ", "_")
    y = y.replace(":", "_").replace("-", "_").replace(" ", "_")

    def infer_type(series):
        if pd.api.types.is_numeric_dtype(series):
            return "Q"
        elif pd.api.types.is_datetime64_any_dtype(series):
            return "T"
        else:
            return "N"

    try:
        x_type = infer_type(df[x])
        y_type = infer_type(df[y])
        x_field = f"{x}:{x_type}"
        y_field = f"{y}:{y_type}"

        if chart_type == "bar":
            chart = alt.Chart(df).mark_bar()
        elif chart_type == "line":
            chart = alt.Chart(df).mark_line()
        elif chart_type == "hist":
            chart = alt.Chart(df).mark_area()
        else:
            return None

        return chart.encode(
            x=x_field,
            y=y_field
        ).properties(width=700, height=400)

    except Exception as e:
        print(f"Altair Chart Error: {e}")
        return None
