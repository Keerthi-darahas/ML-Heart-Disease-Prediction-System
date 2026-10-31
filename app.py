"""
Main Application Entry Point: Heart Disease Prediction System Using SVM
Handles session initialization, authentication gating, sidebar navigation, and multi-page routing.
"""

import streamlit as st
import os
import sys

# Ensure current directory is on Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.styling import apply_custom_styles

# 1. Page Configuration
st.set_page_config(
    page_title="Heart Disease Prediction System (SVM)",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom heart-health CSS theme
apply_custom_styles()

# 2. Session State Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_info" not in st.session_state:
    st.session_state.user_info = None

if "last_prediction" not in st.session_state:
    st.session_state.last_prediction = None

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []

if "batch_results" not in st.session_state:
    st.session_state.batch_results = None

# 3. Define Pages using Streamlit Page API
login_page = st.Page("pages/login.py", title="Login", icon="🔐", default=True)
register_page = st.Page("pages/register.py", title="Register", icon="📝")

home_page = st.Page("pages/home.py", title="Home", icon="🏠", default=True)
prediction_page = st.Page("pages/prediction.py", title="Prediction Form", icon="❤️")
dataset_upload_page = st.Page("pages/dataset_upload.py", title="Dataset & Batch", icon="📁")
performance_page = st.Page("pages/performance.py", title="Model Performance", icon="📊")
about_page = st.Page("pages/about.py", title="About Project", icon="ℹ️")
help_page = st.Page("pages/help.py", title="Help & FAQ", icon="❓")
result_page = st.Page("pages/result.py", title="Prediction Result", icon="📋")

# 4. Role-based Navigation Routing
if not st.session_state.logged_in:
    # Sidebar for unauthenticated visitors
    with st.sidebar:
        st.markdown("""
            <div style="text-align: center; padding: 10px 0;">
                <div style="font-size: 38px;">❤️</div>
                <h3 style="color: #8B0000; margin-bottom: 2px;">Heart Disease AI</h3>
                <p style="color: #718096; font-size: 13px;">Support Vector Machine (SVM)</p>
            </div>
            <hr style="margin: 10px 0 20px 0;">
        """, unsafe_allow_html=True)
        st.info("👋 Please log in or register to access the prediction system.")

    # Only show authentication pages in navigation
    current_page = st.navigation([login_page, register_page], position="sidebar")
else:
    # Sidebar for authenticated users
    user = st.session_state.get("user_info", {})
    user_name = user.get("full_name", "Student")
    username = user.get("username", "user")

    with st.sidebar:
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #FFF5F5 0%, #FED7D7 100%); 
                        border-radius: 10px; padding: 14px; margin-bottom: 15px; border: 1px solid #FEB2B2;">
                <div style="font-size: 11px; text-transform: uppercase; color: #9B2C2C; font-weight: 700; letter-spacing: 0.5px;">
                    Current User
                </div>
                <div style="font-size: 16px; font-weight: bold; color: #742A2A; margin-top: 3px;">
                    {user_name}
                </div>
                <div style="font-size: 12px; color: #718096;">
                    @{username} • B.Tech CSE
                </div>
            </div>
        """, unsafe_allow_html=True)

        if st.button("🚪 Logout", use_container_width=True, type="secondary"):
            st.session_state.logged_in = False
            st.session_state.user_info = None
            st.session_state.last_prediction = None
            st.session_state.batch_results = None
            st.rerun()

        st.divider()

    # Define main application navigation menu
    current_page = st.navigation(
        [
            home_page,
            prediction_page,
            dataset_upload_page,
            performance_page,
            about_page,
            help_page,
            result_page
        ],
        position="sidebar"
    )

# 5. Run Selected Page
current_page.run()
