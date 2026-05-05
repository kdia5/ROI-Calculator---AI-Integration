# Ridgeline CX: Business Case & ROI Calculator 

## Project Overview
This interactive financial modeling tool was developed for **Ridgeline Agency** as part of the **Spring 2026 IT Consulting Lab**. It addresses the agency's urgent need to quantify the financial value of AI-integrated customer experience (CX) solutions following a significant market shift and revenue drop in late 2025.

The application serves as a strategic sales tool for leadership to demonstrate hard ROI to prospective clients, moving beyond theoretical benefits to data-backed financial projections.

## Key Features
* **Dynamic Cost-per-Resolution Modeling**: Compares the financial impact of Human, Hybrid, and AI-First deployment models based on industry benchmarks.
* **Compass QA Integration**: Anchors ROI calculations to Ridgeline’s proprietary **6-category ticket taxonomy** (WISMO, Returns, Billing, Shipping Delay, Product Defect, and VIP).
* **Labor ROI Framing**: Instantly calculates monthly and annual savings based on agent headcount and hourly fully-loaded costs.
* **Interactive Scenario Planning**: Utilizes Streamlit's reactive components to allow real-time adjustments of ticket volume and automation rates.

## Strategic Pivot & Business Logic
Ridgeline Agency faced a sharp drop in consulting revenue starting in **September 2025**. This tool supports the agency's pivot toward **high-value AI/Human hybrid models** by providing a clear, transparent ROI formula:

**Hours Saved × Number of Employees × Hourly Cost = Total Savings**

## Tech Stack
* **Language**: Python
* **Framework**: Streamlit (for interactive UI)
* **Data Handling**: Pandas
* **Visualization**: Plotly (for cost comparison charting)

## How to Use
1.  **Input Ticket Volume**: Enter the Monthly Ticket Volume and estimated Cost per Resolution benchmarks.
2.  **Adjust the Mix**: Use the **Compass QA** sidebar to adjust the ticket mix based on the client’s specific taxonomy.
3.  **Set Labor Variables**: Enter the current agent headcount and hourly rates to calculate total potential savings.
4.  **Review Metrics**: Use the dynamic charts to visualize the total monthly cost reductions and annual labor ROI projections.
