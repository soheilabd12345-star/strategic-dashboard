
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="داشبورد استراتژیک", layout="wide")

st.title("📊 داشبورد هوش تجاری سازمان")
st.markdown("نسخه تحت وب با استفاده از Streamlit")

# بارگذاری فایل‌ها
strategic_df = pd.read_excel("full_strategic_model.xlsx", sheet_name="تحلیل_استراتژیک")
risk_df = pd.read_excel("risk_report.xlsx")
decision_df = pd.read_excel("decision_tracker.xlsx")
personnel_df = pd.read_excel("full_strategic_model.xlsx", sheet_name="پرسنل")

# ---------- نمودار ۱: بهره‌وری ----------
fig1 = px.line(strategic_df.sort_values("بازه_شروع"), x="بازه_شروع", y="بهره‌وری", title="روند بهره‌وری در زمان")
st.plotly_chart(fig1, use_container_width=True)

# ---------- نمودار ۲: منابع ----------
fig2 = px.bar(strategic_df, x="بازه_شروع", y="منابع", title="مصرف منابع در بازه‌ها", color_discrete_sequence=["indianred"])
st.plotly_chart(fig2, use_container_width=True)

# ---------- نمودار ۳: هشدارهای ریسک ----------
fig3 = px.bar(risk_df, x="بازه_شروع", y="تعداد_ریسک", title="تعداد ریسک‌ها در بازه‌ها", color_discrete_sequence=["orange"])
st.plotly_chart(fig3, use_container_width=True)

# ---------- نمودار ۴: تصمیمات ----------
decision_count = decision_df["نتیجه_نهایی"].value_counts()
fig4 = px.pie(names=decision_count.index, values=decision_count.values, title="وضعیت تصمیمات")
st.plotly_chart(fig4, use_container_width=True)

# ---------- نمودار ۵: افراد با عملکرد بالا ----------
top_people = personnel_df[personnel_df["امتیاز_عملکرد"] >= 80]
fig5 = px.bar(top_people, x="نام", y="امتیاز_عملکرد", title="افراد با عملکرد بالا", color_discrete_sequence=["teal"])
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")
st.info("برای نسخه پیشرفته‌تر شامل پیش‌بینی و شبیه‌سازی سناریوها، اتصال به مدل یادگیری ماشین لازم است.")
