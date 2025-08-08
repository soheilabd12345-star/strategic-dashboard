
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="داشبورد هوشمند", layout="wide")

# بارگذاری CSS سفارشی
def local_css(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

st.title("📊 داشبورد هوشمند سازمان")

# بارگذاری داده‌ها
strategic_df = pd.read_excel("full_strategic_model.xlsx", sheet_name="تحلیل_استراتژیک")
risk_df = pd.read_excel("risk_report.xlsx")
decision_df = pd.read_excel("decision_tracker.xlsx")
personnel_df = pd.read_excel("full_strategic_model.xlsx", sheet_name="پرسنل")

st.markdown("---")

# بهره‌وری
st.subheader("📈 روند بهره‌وری")
fig1 = px.area(
    strategic_df.sort_values("بازه_شروع"),
    x="بازه_شروع",
    y="بهره‌وری",
    title="نمودار روند بهره‌وری",
    markers=True
)
fig1.update_traces(line=dict(width=2), marker=dict(size=6))
fig1.update_layout(font=dict(family='Vazir', size=14), title_font=dict(size=18), height=380)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("### ")

# مصرف منابع
st.subheader("📊 مصرف منابع")
fig2 = px.bar(
    strategic_df,
    x="بازه_شروع",
    y="منابع",
    title="میزان مصرف منابع",
    text_auto=True,
    color_discrete_sequence=["#7E57C2"]
)
fig2.update_layout(font=dict(family='Vazir', size=14), title_font=dict(size=18), height=380)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("### ")

# ریسک‌ها
st.subheader("⚠️ وضعیت ریسک‌ها")
fig3 = px.bar(
    risk_df,
    x="بازه_شروع",
    y="تعداد_ریسک",
    title="ریسک‌ها در بازه‌های زمانی",
    text_auto=True,
    color_discrete_sequence=["#FFA000"]
)
fig3.update_layout(font=dict(family='Vazir', size=14), title_font=dict(size=18), height=380)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("### ")

# تصمیم‌ها
st.subheader("📌 تصمیم‌گیری‌ها")
decision_count = decision_df["نتیجه_نهایی"].value_counts()
fig4 = px.pie(
    names=decision_count.index,
    values=decision_count.values,
    title="وضعیت تصمیمات",
    hole=0.4
)
fig4.update_layout(font=dict(family='Vazir', size=14), title_font=dict(size=18), height=380)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("### ")

# عملکرد پرسنل
st.subheader("👥 عملکرد پرسنل برتر")
top_people = personnel_df[personnel_df["امتیاز_عملکرد"] >= 80]
fig5 = px.bar(
    top_people,
    x="نام",
    y="امتیاز_عملکرد",
    title="پرسنل با عملکرد بالا",
    text_auto=True,
    color_discrete_sequence=["#009688"]
)
fig5.update_layout(font=dict(family='Vazir', size=14), title_font=dict(size=18), height=380)
st.plotly_chart(fig5, use_container_width=True)
