import pandas as pd
import plotly.express as px
import plotly.io as pio

# ---------- 1) IMAX vs CNK vs AMC prices ----------
prices = pd.read_csv("data/price_compare.csv")
prices["Date"] = pd.to_datetime(prices["Date"])

fig_price = px.line(
    prices,
    x="Date",
    y=["IMAX", "CNK", "AMC"],
    title="IMAX vs CNK vs AMC Share Prices (Daily)",
    color_discrete_map={
        "IMAX": "#1f77b4",
        "CNK":  "#d62728",
        "AMC":  "#ff7f0e"
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

html_price = pio.to_html(fig_price, include_plotlyjs="cdn", full_html=False)

# ---------- 2) Indexed recovery ----------
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

html_index = pio.to_html(fig_index, include_plotlyjs=False, full_html=False)

# ---------- 3) IMAX financials ----------
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

html_fin = pio.to_html(fig_fin, include_plotlyjs=False, full_html=False)

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

html_box = pio.to_html(fig_box, include_plotlyjs=False, full_html=False)

# ---------- 5) Build one full HTML page ----------
header_html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>IMAX Post-COVID Recovery Dashboard</title>
</head>
<body style="background-color:#001128; color:white; font-family:Arial;">
<h1 style="text-align:center; margin-top:10px;">
  IMAX Post‑COVID Recovery Dashboard
</h1>
<p style="max-width:900px; margin:0 auto 20px auto; font-size:14px;">
  This dashboard analyses how IMAX has recovered after the COVID‑19 shock compared with cinema peers
  Cinemark (CNK) and AMC, and how its financial performance and IMAX box office track against the
  wider global box office market from 2020–2025F.
</p>
<hr style="border-color:#444; margin-bottom:20px;">
"""

footer_html = """
</body>
</html>
"""

full_html = header_html + html_price + html_index + html_fin + html_box + footer_html

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)


