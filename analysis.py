import pandas as pd
import plotly.express as px

# ---------- 1) IMAX vs CNK vs AMC prices ----------
prices = pd.read_csv("data/price_compare.csv")
prices["Date"] = pd.to_datetime(prices["Date"])

fig_price = px.line(
    prices,
    x="Date",
    y=["IMAX", "CNK", "AMC"],
    title="IMAX vs CNK vs AMC Share Prices (Daily)",
    color_discrete_map={
        "IMAX": "#1f77b4",   # blue
        "CNK":  "#d62728",   # red
        "AMC":  "#ff7f0e"    # orange
    }
)

fig_price.update_layout(
    xaxis_title="Date",
    yaxis_title="Share Price (USD)",
    template="plotly_dark",
    plot_bgcolor="#001128",
    paper_bgcolor="#001128",
    font=dict(color="white")
)

fig_price.write_html("index.html", full_html=True)

# ---------- 2) Indexed recovery (Jan 2020 = 100) ----------
idx = pd.read_csv("data/price_index.csv")
idx["Date"] = pd.to_datetime(idx["Date"])

fig_index = px.line(
    idx,
    x="Date",
    y=["IMAX index", "CNK index", "AMC index"],
    title="Post-COVID Stock Recovery (Jan 2020 = 100)"
)

fig_index.update_layout(
    xaxis_title="Date",
    yaxis_title="Price Index (Jan 2020 = 100)",
    template="plotly_dark",
    plot_bgcolor="#001128",
    paper_bgcolor="#001128",
    font=dict(color="white")
)

fig_index.write_html("index_indexed.html", full_html=True)

# ---------- 3) IMAX financials (2020–2025F) ----------
fin = pd.read_csv("data/imax_financials.csv")
fin["Year"] = fin["Year"].astype(str)

fig_fin = px.bar(
    fin,
    x="Year",
    y="Revenue USD millions",
    title="IMAX Revenue and Net Income (2020–2025F)"
)

fig_fin.add_scatter(
    x=fin["Year"],
    y=fin["NetIncome USD millions"],
    mode="lines+markers",
    name="NetIncome USD millions",
    line=dict(color="#d62728")
)

# value labels on revenue bars
fig_fin.update_traces(
    selector=dict(type="bar"),
    texttemplate="%{y:.0f}",
    textposition="outside",
    marker_color="#1f77b4"
)

fig_fin.update_layout(
    xaxis_title="Year",
    yaxis_title="USD millions",
    uniformtext_minsize=10,
    uniformtext_mode="hide",
    template="plotly_dark",
    plot_bgcolor="#001128",
    paper_bgcolor="#001128",
    font=dict(color="white")
)

fig_fin.write_html("index_financials.html", full_html=True)

# ---------- 4) Global vs IMAX box office ----------
box = pd.read_csv("data/global_boxoffice.csv")
box["Year"] = box["Year"].astype(str)

fig_box = px.bar(
    box,
    x="Year",
    y="Global Boxoffice USD billion",
    title="Global vs IMAX Box Office (USD billions)"
)

fig_box.add_scatter(
    x=box["Year"],
    y=box["IMAX Boxoffice USD billion"],
    mode="lines+markers",
    name="IMAX Boxoffice USD billion",
    line=dict(color="#1f77b4")
)

# value labels on global box office bars
fig_box.update_traces(
    selector=dict(type="bar"),
    texttemplate="%{y:.2f}",
    textposition="outside",
    marker_color="#7f7f7f"
)

fig_box.update_layout(
    xaxis_title="Year",
    yaxis_title="USD billions",
    uniformtext_minsize=10,
    uniformtext_mode="hide",
    template="plotly_dark",
    plot_bgcolor="#001128",
    paper_bgcolor="#001128",
    font=dict(color="white")
)

fig_box.write_html("index_boxoffice.html", full_html=True)
