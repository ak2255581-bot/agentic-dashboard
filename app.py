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
st.markdown("## 🧾 Travel Input")

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
    # Step 3
    # Selected Agents Summary
    # etc.

workflow = []

if "🔍 Search Agent" in selected_agents:
    workflow.append("Search travel route & policies")

if "✈️ Flight Search Agent" in selected_agents:
    workflow.append("Find lowest-cost flights")

if "🚆 Train Search Agent" in selected_agents:
    workflow.append("Find lowest-cost trains")

if "🏨 Hotel Search Agent" in selected_agents:
    workflow.append("Book 3-star hotel")

if "🚖 Cab Booking Agent" in selected_agents:
    workflow.append("Arrange cab booking")

if "✅ Approval Agent" in selected_agents:
    workflow.append("Ask for user approval")

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
        "Step": list(range(1, len(selected_agents)+1)),
        "Agent": selected_agents
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


    # ---------------- COST CALCULATION ----------------

flight = 4500
hotel = 3500
cab = 800

total = np.sum([flight, hotel, cab])

st.write("### 💰 Total Cost Calculation")
st.success(f"Total Travel Cost: ₹{total}")

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
    
    #---------------------- COST + STATUS LOGIC ----------------------
    
    
    overall_cost = 8800

    if overall_cost <= budget:
        status = "Approved & Booked ✅"
    else:
        status = "Over Budget ❌"

    # ---------------- OUTPUT ----------------
    st.markdown("## 📦 Final Output")

    st.markdown(f"""
    <div class='output-box'>

    <h2>🎯 Best Travel Itinerary</h2>
    <hr>

    <b>Route:</b> {from_city} → {to_city}<br><br>

    <b>Travel Mode:</b> Flight ✈️<br><br>

    <b>Flight Cost:</b> ₹4500<br>
    <b>Hotel:</b> 3-Star Hotel (₹3500)<br>
    <b>Cab:</b> Airport Pickup (₹800)<br><br>

    <b>Total Cost:</b> ₹{overall_cost}<br>
    <b>Budget:</b> ₹{budget}<br><br>

    <b>Status:</b> {status}<br>
    <b>Payment:</b> Successful 💳<br>
    <b>Notification:</b> Ticket Sent 📩

    </div>
    """, unsafe_allow_html=True)

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