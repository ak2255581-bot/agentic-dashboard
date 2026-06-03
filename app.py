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
st.markdown("## 📌 Scenario")

st.markdown("""
<div class='card'>
<b>Goal:</b> Book a trip from <b>Kolkata → Mumbai</b><br><br>

✔ Cheapest Flight / Train <br>
✔ 3-Star Hotel <br>
✔ Cab Booking <br>
✔ User Approval <br>
✔ Payment Confirmation <br>
✔ Notification
</div>
""", unsafe_allow_html=True)

# ---------------- AGENTS ----------------


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
    from_city = st.text_input("From City", "Kolkata")

with col2:
    to_city = st.text_input("To City", "Mumbai")

with col3:
    budget = st.number_input(
        "Budget ₹",
        min_value=1000,
        value=12000
    )
    
     # ---------------- COST CALCULATION ----------------

flight = 4500
hotel = 3500
cab = 800

total = np.sum([flight, hotel, cab])

st.write("### 💰 Total Cost Calculation")
st.success(f"Total Travel Cost: ₹{total}")


 # ---------------- COST + STATUS LOGIC ----------------


# ------------------------- REAL-USE AGENTIC COST LOGIC -------------------------

b_from = from_city if 'from_city' in locals() else "Kolkata"
b_to = to_city if 'to_city' in locals() else "Mumbai"
base_multiplier = len(b_from) + len(b_to)

# ------------------------- SAFE VARIABLE CHECK -------------------------
active_agents = []


if 'selected_agents' in locals() or 'selected_agents' in globals():
    try:
        active_agents = 'selected_agents'
    except NameError:
        pass

if not active_agents and ('agents' in locals() or 'agents' in globals()):
    try:
        active_agents = agents
    except NameError:
        active_agents = []

# Dynamic cost calculation based on active selection
flight_fare = base_multiplier * 350 if "✈️ Flight Search Agent" in active_agents else 0
train_fare = base_multiplier * 120 if "🚆 Train Search Agent" in active_agents else 0
hotel_fare = 3500 if "🏨 Hotel Search Agent" in active_agents else 0
cab_fare = 800 if "🚖 Cab Booking Agent" in active_agents else 0

overall_cost = flight_fare + train_fare + hotel_fare + cab_fare

# Budget threshold evaluation
current_budget = budget if 'budget' in locals() else 12000
if overall_cost == 0:
    status = "No Agents Active ⚠️"
elif overall_cost <= current_budget:
    status = "Approved & Within Budget ✅"
else:
    status = "Rejected: Over Budget ❌"
    
    # ------------------------- LIVE SYSTEM OUTPUT DISPLAY -------------------------
st.markdown("## 📦 Live System Output")

st.markdown(f"""
<div style='background-color: #0F172A; padding: 20px; border-radius: 12px; border: 1px solid #1E293B; color: #E2E8F0;'>
    <h3 style='color: #38BDF8; margin-top: 0;'>🎯 Optimized Itinerary Sheet</h3>
    <hr style='border: 0.5px solid #334155;'>
    <p><b>Current Status:</b> <span style='font-size: 16px; font-weight: bold;'>{status}</span></p>
    <p><b>Route Path:</b> {b_from} ➔ {b_to}</p>
    <ul style='padding-left: 20px;'>
        <li><b>Flight Allocation Cost:</b> ₹{flight_fare}</li>
        <li><b>Train Allocation Cost:</b> ₹{train_fare}</li>
        <li><b>Hotel Stay Booking:</b> ₹{hotel_fare}</li>
        <li><b>Local Cab Allowance:</b> ₹{cab_fare}</li>
    </ul>
    <hr style='border: 0.5px solid #334155;'>
    <h4 style='color: #F59E0B;'>Total Calculated Cost: ₹{overall_cost} / Set Budget: ₹{current_budget}</h4>
</div>
""", unsafe_allow_html=True)

# ------------------------- ML INTERNSHIP ANALYTICS FEATURE -------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📊 Agentic Decision Insights (ML Metric)")

if current_budget > 0 and overall_cost > 0:
    efficiency_score = min(100, int((current_budget / overall_cost) * 100)) if overall_cost > current_budget else int((overall_cost / current_budget) * 100)
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric(label="Cost-to-Budget Ratio", value=f"{efficiency_score}%", delta="Optimal" if overall_cost <= current_budget else "Critical Overrun")
    with col_m2:
        st.progress(efficiency_score / 100)
        st.caption("AI Workflow Optimization Score based on current thresholds.")
        
# ---------------- WORKFLOW ----------------
st.markdown("## 🔄 Design Workflow")

with st.expander("📋 Click to View / Design Workflow", expanded=False):

    selected_agents = st.multiselect(
        "Select AI Agents",
        agents,
        default=agents
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

    st.markdown("### Workflow Flow")

    for i, step in enumerate(workflow, 1):

        st.markdown(
            f"<div class='step-box'>Step {i}: {step}</div>",
            unsafe_allow_html=True
        )
        
        if i != len(workflow):
            st.markdown(
                "<div class='arrow'>⬇️</div>",
                unsafe_allow_html=True
            )
        
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
st.markdown("## 🧠 AI Analysis")

reflection = st.text_area(
    "Why is this orchestration suitable?",
    f"This workflow uses {pattern} orchestration. "
    "Search-related tasks run efficiently while approval, "
    "payment and notification are handled systematically."
)

if reflection:
    st.info(reflection)

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown(
    "<center>✨ AI Agentic Workflow Dashboard | Streamlit Project</center>",
    unsafe_allow_html=True
)