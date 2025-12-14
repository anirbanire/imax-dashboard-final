import pandas as pd
import plotly.express as px

# 1) Load daily price comparison data
prices = pd.read_csv("data/price_compare.csv")

# Make sure Date column is parsed as dates
prices["Date"] = pd.to_datetime(prices["Date"])

# 2) Line chart: IMAX vs CNK vs AMC prices
fig_price = px.line(
    prices,
    x="Date",
    y=["IMAX", "CNK", "AMC"],  # use your actual column names
    title="IMAX vs CNK vs AMC Share Prices (Daily)"
)

# 3) Save to HTML dashboard
fig_price.write_html("index.html", full_html=True)
# 4) Load price index data
idx = pd.read_csv("data/price_index.csv")
idx["Date"] = pd.to_datetime(idx["Date"])

# 5) Line chart: indexed recovery (Jan 2020 = 100)
fig_index = px.line(
    idx,
    x="Date",
    y=["IMAX index", "CNK index", "AMC index"],
    title="Post-COVID Stock Recovery (Jan 2020 = 100)"
)

# 6) Save index chart as separate HTML for now
fig_index.write_html("index_indexed.html", full_html=True)
# 7) Load IMAX financials (2020–2025F)
fin = pd.read_csv("data/imax_financials.csv")

# Ensure Year is treated as a number or string (no dates needed here)
fin["Year"] = fin["Year"].astype(str)

# 8) Bar + line chart: Revenue and Net Income
fig_fin = px.bar(
    fin,
    x="Year",
    y="Revenue USD millions",
    title="IMAX Revenue and Net Income (2020–2025F)"
)

# Add Net Income as a line on top
fig_fin.add_scatter(
    x=fin["Year"],
    y=fin["NetIncome USD millions"],
    mode="lines+markers",
    name="NetIncome USD millions"
)

# 9) Save financial chart
fig_fin.write_html("index_financials.html", full_html=True)
# 10) Load global vs IMAX box office
box = pd.read_csv("data/global_boxoffice.csv")
box["Year"] = box["Year"].astype(str)

# 11) Column + line chart: Global vs IMAX box office (USD billions)
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
    name="IMAX Boxoffice USD billion"
)

# 12) Save box office chart
fig_box.write_html("index_boxoffice.html", full_html=True)

