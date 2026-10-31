import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Sales Performance Dashboard", page_icon="📊", layout="wide")
DATA = Path("data/superstore_clean.csv")

@st.cache_data
def read_data(upload):
    if upload is not None:
        df = pd.read_csv(upload)
    elif DATA.exists():
        df = pd.read_csv(DATA)
    else:
        df = pd.read_csv("data/Sample - Superstore.csv")
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    for c in ["Sales", "Profit", "Quantity", "Discount"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=["Order Date", "Order ID", "Region", "Category", "Sales", "Profit"])
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()
    return df

st.title("📊 Sales Performance Dashboard")
st.caption("Analisis interaktif performa penjualan, pesanan, dan keuntungan berdasarkan dataset Sample Superstore.")
with st.sidebar:
    st.header("Filter Dashboard")
    upload = st.file_uploader("Unggah dataset CSV (opsional)", type="csv")

try:
    df = read_data(upload)
except Exception as e:
    st.error(f"Dataset tidak dapat dibaca: {e}")
    st.stop()

with st.sidebar:
    years = sorted(df["Year"].dropna().unique().tolist())
    categories = sorted(df["Category"].dropna().unique().tolist())
    ysel = st.multiselect("Tahun", years, default=years)
    csel = st.multiselect("Kategori produk", categories, default=categories)

d = df[df["Year"].isin(ysel) & df["Category"].isin(csel)]
if d.empty:
    st.warning("Tidak ada data untuk filter yang dipilih.")
    st.stop()

a, b, c = st.columns(3)
a.metric("Total Penjualan", f"${d.Sales.sum():,.2f}")
b.metric("Jumlah Pesanan", f"{d['Order ID'].nunique():,}")
c.metric("Total Keuntungan", f"${d.Profit.sum():,.2f}")
st.divider()

monthly = d.groupby("Month", as_index=False)["Sales"].sum()
category = d.groupby("Category", as_index=False)["Sales"].sum()
region = d.groupby("Region", as_index=False)["Sales"].sum()

x, y = st.columns(2)
with x:
    st.subheader("1. Tren Penjualan Bulanan")
    st.plotly_chart(px.line(monthly, x="Month", y="Sales", markers=True,
        labels={"Month":"Bulan","Sales":"Penjualan ($)"}), use_container_width=True)
with y:
    st.subheader("2. Penjualan Berdasarkan Kategori")
    st.plotly_chart(px.bar(category, x="Category", y="Sales", color="Category",
        labels={"Category":"Kategori","Sales":"Penjualan ($)"}), use_container_width=True)

x, y = st.columns(2)
with x:
    st.subheader("3. Penjualan Berdasarkan Wilayah")
    st.plotly_chart(px.bar(region, x="Region", y="Sales", color="Region",
        labels={"Region":"Wilayah","Sales":"Penjualan ($)"}), use_container_width=True)
with y:
    st.subheader("4. Hubungan Penjualan dan Keuntungan")
    st.plotly_chart(px.scatter(d, x="Sales", y="Profit", color="Category",
        hover_data=["Order ID","Region","Sub-Category"],
        labels={"Sales":"Penjualan ($)","Profit":"Keuntungan ($)"}), use_container_width=True)

st.divider()
st.subheader("💡 Insight Utama")
top_cat = category.sort_values("Sales", ascending=False).iloc[0]
top_reg = region.sort_values("Sales", ascending=False).iloc[0]
m1, m2 = st.columns(2)
m1.markdown(f"- Kategori penjualan tertinggi: **{top_cat.Category}** (${top_cat.Sales:,.2f}).")
m1.markdown(f"- Wilayah penjualan tertinggi: **{top_reg.Region}** (${top_reg.Sales:,.2f}).")
m2.markdown(f"- Total keuntungan pada filter ini: **${d.Profit.sum():,.2f}**.")
m2.markdown(f"- Jumlah baris data yang ditampilkan: **{len(d):,}**.")
st.subheader("Pratinjau Data")
st.dataframe(d.head(10), use_container_width=True)
st.download_button("Unduh data hasil filter", d.to_csv(index=False).encode("utf-8"),
                   "data_penjualan_terfilter.csv", "text/csv")
st.caption("Jumlah pesanan dihitung dari Order ID unik; satu baris dataset adalah satu baris item pesanan.")
