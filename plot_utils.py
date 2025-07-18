import plotly.express as px

def generate_plot(df, chart_info):
    chart_type = chart_info.get("type")
    x = chart_info.get("x")
    y = chart_info.get("y")

    try:
        if chart_type == "bar":
            return px.bar(df, x=x, y=y, title=f"{y} by {x}")
        elif chart_type == "line":
            return px.line(df, x=x, y=y, title=f"{y} over {x}")
        elif chart_type == "hist":
            return px.histogram(df, x=x, title=f"Distribution of {x}")
        else:
            return None
    except Exception as e:
        print(f"Error creating chart: {e}")
        return None
