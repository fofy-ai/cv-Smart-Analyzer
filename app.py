import streamlit as st
from analyzer import extract_text_from_pdf

st.title("🤖 محلل السيرة الذاتية بالذكاء الاصطناعي")

st.write("ارفعي سيرتك الذاتية واكتبي الوظيفة المستهدفة لتحليل مدى توافقها.")

cv_file = st.file_uploader(
    "📄 ارفعي السيرة الذاتية",
    type=["pdf"]
)

job_title = st.text_input(
    "💼 الوظيفة المستهدفة"
)

if st.button("🔍 تحليل السيرة الذاتية"):

    if cv_file is None:
        st.warning("يرجى رفع السيرة الذاتية أولاً.")

    elif not job_title:
        st.warning("يرجى كتابة الوظيفة المستهدفة.")

    else:
        text = extract_text_from_pdf(cv_file)

        st.success("تمت قراءة السيرة الذاتية بنجاح!")

        st.subheader("📄 النص المستخرج من السيرة الذاتية")

        st.write(text)
        