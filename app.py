
import streamlit as st
import pandas as pd
import plotly.express as px

# تنظیمات صفحه
st.set_page_config(page_title="داشبورد هوشمند", layout="wide")

# بارگذاری CSS برای فونت فارسی و راست‌چین
def local_css(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# تیتر اصلی
st.title("📊 داشبورد هوشمند عملکرد سازمان")

# بارگذاری داده‌ها
strategic_df = pd.read_excel("full_strategic_model.xlsx", sheet_name="تحلیل_استراتژیک")
risk_df = pd.read_excel("risk_report.xlsx")
decision_df = pd.read_excel("decision_tracker.xlsx")
personnel_df = pd.read_excel("full_strategic_model.xlsx", sheet_name="پرسنل")

st.markdown("---")

# نمودار ۱: بهره‌وری
st.subheader("🔹 روند بهره‌وری در بازه‌های زمانی")
fig1 = px.line(
    strategic_df.sort_values("بازه_شروع"),
    x="بازه_شروع",
    y="بهره‌وری",
    markers=True,
    line_shape="spline",
    title="نمودار بهره‌وری"
)
fig1.update_layout(font=dict(family='BNazanin', size=14), title_font=dict(size=20), height=400)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# نمودار ۲: مصرف منابع
st.subheader("🔹 میزان مصرف منابع در بازه‌ها")
fig2 = px.bar(
    strategic_df,
    x="بازه_شروع",
    y="منابع",
    color="منابع",
    color_continuous_scale="Reds",
    title="مصرف منابع"
)
fig2.update_layout(font=dict(family='BNazanin', size=14), title_font=dict(size=20), height=400)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# نمودار ۳: تعداد ریسک‌ها
st.subheader("🔹 ریسک‌های ثبت‌شده")
fig3 = px.bar(
    risk_df,
    x="بازه_شروع",
    y="تعداد_ریسک",
    color="تعداد_ریسک",
    color_continuous_scale="Oranges",
    title="ریسک‌ها در بازه‌های زمانی"
)
fig3.update_layout(font=dict(family='BNazanin', size=14), title_font=dict(size=20), height=400)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# نمودار ۴: تصمیمات
st.subheader("🔹 وضعیت تصمیم‌گیری‌ها")
decision_count = decision_df["نتیجه_نهایی"].value_counts()
fig4 = px.pie(
    names=decision_count.index,
    values=decision_count.values,
    title="نتیجه تصمیمات"
)
fig4.update_layout(font=dict(family='BNazanin', size=14), title_font=dict(size=20), height=400)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# نمودار ۵: عملکرد پرسنل
st.subheader("🔹 افراد با عملکرد بالا")
top_people = personnel_df[personnel_df["امتیاز_عملکرد"] >= 80]
fig5 = px.bar(
    top_people,
    x="نام",
    y="امتیاز_عملکرد",
    color="امتیاز_عملکرد",
    color_continuous_scale="Teal",
    title="پرسنل برتر"
)
fig5.update_layout(font=dict(family='BNazanin', size=14), title_font=dict(size=20), height=400)
st.plotly_chart(fig5, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)
