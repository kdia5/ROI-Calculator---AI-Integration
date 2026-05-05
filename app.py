import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Ridgeline CX: Business Case & ROI", layout="wide")

st.title("Ridgeline CX: Business Case & ROI Calculator")
st.markdown("Interactive financial model for AI CX automation.")

# --- SIDEBAR: User Inputs ---
st.sidebar.header("1. Ticket Volume & Costs")
ticket_volume = st.sidebar.number_input("Monthly Ticket Volume", min_value=100, value=10000, step=500)

# --- OPTIONAL: COMPASS DATA TIE-IN ---
with st.sidebar.expander("Compass QA: Ticket Mix & Automation Rate", expanded=True):
    st.markdown("Adjust based on Ridgeline's 6-category taxonomy:")
    wismo_pct = st.slider("Order Status / WISMO (%) - Full AI", 0, 100, 40)
    returns_pct = st.slider("Returns / Refunds (%) - Hybrid", 0, 100, 25)
    
    # Calculate the automation potential
    auto_eligible_volume = ticket_volume * ((wismo_pct + returns_pct) / 100)
    st.caption(f"Based on Compass Data, **{int(auto_eligible_volume):,}** tickets are highly eligible for AI/Hybrid deflection.")

st.sidebar.subheader("Cost per Resolution Estimates ($)")
human_cost = st.sidebar.slider("Human (Industry Avg: $8-$15)", 5.0, 20.0, 12.0)
hybrid_cost = st.sidebar.slider("Hybrid (Industry Avg: $4-$8)", 2.0, 12.0, 6.0)
ai_cost = st.sidebar.slider("AI-Only (Industry Avg: $0.50-$2)", 0.1, 5.0, 1.0)

st.sidebar.header("2. ROI & Labor Variables")
num_agents = st.sidebar.number_input("Number of Human Agents", min_value=1, value=15)
hourly_cost = st.sidebar.number_input("Agent Hourly Fully-Loaded Cost ($)", value=25.0)
hours_saved = st.sidebar.number_input("Hours Saved per Agent/Month via AI", value=46)

# --- CALCULATIONS ---
# Cost per resolution totals
total_human = ticket_volume * human_cost
total_hybrid = ticket_volume * hybrid_cost
total_ai = ticket_volume * ai_cost

# ROI totals
monthly_savings = hours_saved * num_agents * hourly_cost
annual_savings = monthly_savings * 12

# --- DASHBOARD DISPLAY ---
col1, col2, col3 = st.columns(3)
col1.metric(label="Total Monthly Cost (Human)", value=f"${total_human:,.2f}")
col2.metric(label="Total Monthly Cost (Hybrid)", value=f"${total_hybrid:,.2f}", delta=f"-${(total_human - total_hybrid):,.2f}", delta_color="inverse")
col3.metric(label="Total Monthly Cost (AI-First)", value=f"${total_ai:,.2f}", delta=f"-${(total_human - total_ai):,.2f}", delta_color="inverse")

st.markdown("---")

# Visualizing the Cost Comparison
st.subheader("Cost Comparison by Deployment Model")
cost_data = pd.DataFrame({
    "Model": ["Human-Only", "Hybrid (Human + AI)", "AI-First"],
    "Monthly Cost ($)": [total_human, total_hybrid, total_ai]
})

fig = px.bar(cost_data, x="Model", y="Monthly Cost ($)", text="Monthly Cost ($)",
             color="Model", color_discrete_sequence=["#EF553B", "#636EFA", "#00CC96"])
fig.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
fig.update_layout(showlegend=False, yaxis_title="Total Monthly Cost")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- ROI Framing (Final Clean Version) ---
st.subheader("Labor ROI Framing")

# Using a standard f-string without extra spaces in the formatting
info_text = f"**Estimated Monthly Savings:** ${monthly_savings:,.2f} | **Estimated Annual Savings:** ${annual_savings:,.2f}"
st.info(info_text)

# Using standard '*' for multiplication to avoid encoding boxes
st.write(f"*(Calculated as {hours_saved} hours saved * {num_agents} employees * ${hourly_cost:.2f} hourly cost)*")