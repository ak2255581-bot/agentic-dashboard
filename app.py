import streamlit as st
import pandas as pd
import numpy as np
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Agentic Workflow Dashboard",
    page_icon="🤖",
    layout="wide"
)
# ---------------- RESET FUNCTION ----------------
def reset_app():
    st.session_state.clear()
    st.cache_data.clear()
    st.cache_resource.clear()

if st.sidebar.button("🔄 Reset App"):
    reset_app()
    st.rerun()

# ---------------- LOAD CSS ----------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<div class='big-title'>🤖 AI Agentic Workflow Dashboard</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Travel Booking Automation using Multiple AI Agents</div>",
    unsafe_allow_html=True
)

# ---------------- SCENARIO ----------------
st.markdown("## 🎯 Travel Booking Scenario")

st.info(
    "🎯 Goal: Book a trip from to from | ✈️ Flight/Train | 🏨 3-Star Hotel | 🚖 Cab Service | ✅ Approval | 💳 Payment | 📩 Notification"
)

# ---------------- AGENTS ---------------

st.markdown("## 🤖 Available Agents")

agents = [
    "🔍 Search Agent",
    "✈️ Flight Search Agent",
    "🚆 Train Search Agent",
    "🏨 Hotel Search Agent",
    "🚖 Cab Booking Agent",
    "✅ Approval Agent",
    "💳 Payment Agent",
    "📩 Notification Agent"
]

cols = st.columns(4)

for i, agent in enumerate(agents):
    with cols[i % 4]:
        st.markdown(
            f"<div class='agent-card'>{agent}</div>",
            unsafe_allow_html=True
        )
        
        
        # ---------------- INPUT ----------------
st.markdown("## ✈️ Travel Input")

col1, col2, col3 = st.columns(3)

with col1:
    from_city = st.text_input(
        "From City",
        key="from_city"
    )

with col2:
    to_city = st.text_input(
        "To City",
        key="to_city"
    )

with col3:
    budget = st.number_input(
        "Budget ₹",
        min_value=15000,
        key="budget"
    )

overall_cost = 8800

if overall_cost <= budget:
    status = "Approved & Booked ✅"
else:
    status = "Over Budget ❌"
    
    # Dashboard Summary Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Cost", f"₹{overall_cost}")

with col2:
    st.metric("📊 Budget", f"₹{budget}")

# ---------------- OUTPUT ----------------

if from_city and to_city:

    st.markdown("## 🎯 Best Travel Itinerary")

    st.write(f"**Route:** {from_city} ➜ {to_city}")
    st.write("**Travel Mode:** Flight ✈️")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Flight", "₹4500")
    col2.metric("Hotel", "₹3500")
    col3.metric("Cab", "₹800")
    col4.metric("Total", f"₹{overall_cost}")

    st.write(f"**Budget:** ₹{budget}")
    st.write(f"**Status:** {status}")
    st.success("Payment Successful 💳")
    st.info("Ticket Sent 📩")
# ---------------- WORKFLOW ----------------
st.markdown("## 🔄 Design Workflow")

with st.expander("📋 Click to View / Design Workflow", expanded=False):

    selected_agents = st.multiselect(
        "Select AI Agents",
        agents,
        default=[],
        key="selected_agents"
    )
    
    # Step 1
    # Step 2
    # Selected Agents Summary
    # etc. 
        
        
workflow = []

if "🔍 Search Agent" in selected_agents:
    workflow.append("Search route")
    
if "✈️ Flight Search Agent" in selected_agents:
    workflow.append("Find Flights")
    
if "🚆 Train Search Agent" in selected_agents:
    workflow.append("Find Trains")

if "🏨 Hotel Search Agent" in selected_agents:
    workflow.append("Book 3-star Hotel")

if "🚖 Cab Booking Agent" in selected_agents:
    workflow.append("Book cab")

if "✅ Approval Agent" in selected_agents:
    workflow.append("Get Approval")

if "💳 Payment Agent" in selected_agents:
    workflow.append("Process payment")

if "📩 Notification Agent" in selected_agents:
    workflow.append("Send ticket + confirmation")

col1, col2 = st.columns([1, 1])
# ---------------- FLOW ----------------
with col1:

    st.markdown("### 📋 Workflow Execution Plan")

    for i, step in enumerate(workflow, 1):
        st.write(f"{i}. {step}")
        
# ---------------- SUMMARY ----------------
with col2:

    st.markdown("### 📊 Selected Agents Summary")

    df = pd.DataFrame({
        "Step": list(range(1, len(workflow)+1)),
        "Agent": workflow
    })

    st.dataframe(df, use_container_width=True)

# ---------------- ORCHESTRATION ----------------
st.markdown("## ⚙️ Orchestration Pattern")

pattern = st.radio(
    "Choose Pattern",
    ["Sequential", "Parallel", "Hierarchical", "Hybrid"],
    horizontal=True
)

st.success(f"Selected Pattern: {pattern}")

  
# ---------------- RUN ----------------
st.markdown("## 🚀 Run AI Workflow")

if st.button("Run Workflow Simulation"):

    st.subheader("⚡ Running Agents...")

    progress = st.progress(0)

    for i, step in enumerate(workflow):

        st.write(f"✅ {step}")

        time.sleep(0.7)

        progress.progress((i + 1) / len(workflow))

    st.success("🎉 Workflow Completed Successfully!") 

# ---------------- AI Analysis----------------

# Basic reflection summary to avoid undefined variable
reflection_text = (
    f"Selected Pattern: {pattern}. Workflow steps: {len(workflow)}. "
    f"Total Cost: ₹{overall_cost} vs Budget: ₹{budget}. Status: {status}."
)

with st.expander("🧠 AI Analysis", expanded=False):
    st.write(reflection_text)
# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown(
    "<center>✨ AI Agentic Workflow Dashboard | Streamlit Project</center>",
    unsafe_allow_html=True
)