# app.py
# Run with: streamlit run app.py
# Place this file in the study_tracker/ folder (same level as main.py)

import streamlit as st
from database.db_manager import DatabaseManager
from features.logger import prompt_new_session
from features.stats import (
    calculate_average_score, get_best_subject,
    get_worst_subject, get_most_studied_subject,
    display_summary, _load_dataframe
)
from features.streak import calculate_streak
from features.tips import get_tips, get_resources, get_worst_subject as tips_worst
from utils.helpers import get_today, validate_score, validate_duration, format_date
from models.study_session import StudySession

# --- Setup ---
db = DatabaseManager()
db.create_table()

st.set_page_config(page_title="Study Tracker", page_icon="📚", layout="centered")
st.title("📚 Study Tracker")

# --- Sidebar Navigation ---
page = st.sidebar.radio("Navigate", [
    "🏠 Dashboard",
    "➕ Log Session",
    "📋 View Sessions",
    "📊 Statistics",
    "🔥 Streak",
    "💡 Tips & Resources"
])

# ─────────────────────────────────────────────
# 🏠 DASHBOARD
# ─────────────────────────────────────────────
if page == "🏠 Dashboard":
    st.subheader("Your Overview")

    df = _load_dataframe()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sessions", len(df) if not df.empty else 0)
    col2.metric("Total Study Time", f"{int(df['duration'].sum())} min" if not df.empty else "0 min")
    col3.metric("🔥 Streak", f"{calculate_streak()} days")

    if not df.empty:
        st.divider()
        best = get_best_subject()
        worst = get_worst_subject()
        most = get_most_studied_subject()
        col4, col5, col6 = st.columns(3)
        col4.metric("🏆 Best Subject", best or "—")
        col5.metric("⚠️ Needs Work", worst or "—")
        col6.metric("📖 Most Studied", most or "—")

        st.divider()
        st.subheader("Sessions Over Time")
        daily = df.groupby("date")["duration"].sum().reset_index()
        daily = daily.rename(columns={"date": "index"}).set_index("index")
        st.line_chart(daily)
    else:
        st.info("No sessions logged yet. Head to **Log Session** to get started!")

# ─────────────────────────────────────────────
# ➕ LOG SESSION
# ─────────────────────────────────────────────
elif page == "➕ Log Session":
    st.subheader("Log a New Study Session")

    with st.form("log_form"):
        subject = st.text_input("Subject", placeholder="e.g. Math, Biology...")
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=600, value=30)
        score = st.slider("Score (0–100)", min_value=0, max_value=100, value=75)
        date = st.date_input("Date", value=__import__("datetime").date.today())
        submitted = st.form_submit_button("Log Session")

    if submitted:
        if not subject.strip():
            st.error("Please enter a subject name.")
        else:
            session = StudySession(
                subject=subject.strip(),
                duration=duration,
                score=score,
                date=str(date)
            )
            db.insert_session(session)
            st.success(f"✅ Logged: **{subject}** | {duration} min | Score: {score} | {date}")

# ─────────────────────────────────────────────
# 📋 VIEW SESSIONS
# ─────────────────────────────────────────────
elif page == "📋 View Sessions":
    st.subheader("All Study Sessions")

    df = _load_dataframe()

    if df.empty:
        st.info("No sessions logged yet.")
    else:
        subjects = ["All"] + sorted(df["subject"].unique().tolist())
        filter_subject = st.selectbox("Filter by subject", subjects)

        if filter_subject != "All":
            df = df[df["subject"] == filter_subject]

        st.dataframe(
            df[["id", "subject", "duration", "score", "date"]].rename(columns={
                "id": "ID", "subject": "Subject",
                "duration": "Duration (min)", "score": "Score", "date": "Date"
            }),
            use_container_width=True,
            hide_index=True
        )
        st.caption(f"Showing {len(df)} session(s)")

# ─────────────────────────────────────────────
# 📊 STATISTICS
# ─────────────────────────────────────────────
elif page == "📊 Statistics":
    st.subheader("Statistics & Performance")

    df = _load_dataframe()

    if df.empty:
        st.info("No sessions logged yet.")
    else:
        # Per-subject breakdown table
        summary = df.groupby("subject").agg(
            Sessions=("id", "count"),
            Total_Minutes=("duration", "sum"),
            Avg_Score=("score", "mean")
        ).reset_index()
        summary["Avg_Score"] = summary["Avg_Score"].round(1)
        summary.columns = ["Subject", "Sessions", "Total Minutes", "Avg Score"]
        st.dataframe(summary, use_container_width=True, hide_index=True)

        st.divider()

        # Charts side by side
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Avg Score by Subject**")
            score_chart = df.groupby("subject")["score"].mean().reset_index()
            score_chart.columns = ["Subject", "Avg Score"]
            st.bar_chart(score_chart.set_index("Subject"))
        with col2:
            st.markdown("**Study Time by Subject**")
            time_chart = df.groupby("subject")["duration"].sum().reset_index()
            time_chart.columns = ["Subject", "Total Minutes"]
            st.bar_chart(time_chart.set_index("Subject"))

        # Score lookup
        st.divider()
        st.markdown("**Look Up Average Score**")
        subjects = sorted(df["subject"].unique().tolist())
        selected = st.selectbox("Select a subject", subjects)
        avg = calculate_average_score(selected)
        if avg is not None:
            st.metric(f"Average Score — {selected}", avg)

# ─────────────────────────────────────────────
# 🔥 STREAK
# ─────────────────────────────────────────────
elif page == "🔥 Streak":
    st.subheader("Study Streak")

    streak = calculate_streak()

    if streak == 0:
        st.warning("No active streak. Study today to start one! 💪")
    elif streak == 1:
        st.success("🔥 Day 1 streak — you studied today! Keep going!")
    else:
        st.success(f"🔥 You're on a **{streak}-day** study streak! Keep it going!")

    st.metric("Current Streak", f"{streak} day(s)")

    # Show recent study dates
    df = _load_dataframe()
    if not df.empty:
        st.divider()
        st.markdown("**Recent Study Dates**")
        recent = df[["date"]].drop_duplicates().sort_values("date", ascending=False).head(7)
        st.dataframe(recent.rename(columns={"date": "Date"}), use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────
# 💡 TIPS & RESOURCES
# ─────────────────────────────────────────────
elif page == "💡 Tips & Resources":
    st.subheader("Tips & Resources")

    df = _load_dataframe()
    worst = get_worst_subject()

    if worst:
        st.info(f"📉 Your lowest-scoring subject is **{worst}** — here's some help:")
        subject_input = worst
    else:
        st.write("No sessions yet. Pick a subject below to explore tips:")
        subject_input = None

    subjects_list = ["math", "english", "science", "history", "programming", "biology", "chemistry"]
    selected_subject = st.selectbox(
        "Choose a subject",
        subjects_list,
        index=subjects_list.index(worst.lower()) if worst and worst.lower() in subjects_list else 0
    )

    tips = get_tips(selected_subject)
    resources = get_resources(selected_subject)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**💡 Study Tips**")
        for tip in tips:
            st.markdown(f"- {tip}")
    with col2:
        st.markdown("**🔗 Resources**")
        for resource in resources:
            name, url = resource.rsplit(": ", 1)
            st.markdown(f"- [{name}]({url})")
