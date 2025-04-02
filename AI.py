import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def plot_metrics(title, metrics, values):
    fig, ax = plt.subplots()
    ax.barh(metrics, values, color='skyblue')
    ax.set_xlabel("Metric Value")
    ax.set_title(title)
    st.pyplot(fig)

# Function to define new metrics for tariff impact
def get_tariff_impact():
    metrics = ["Supply Chain Efficiency", "Profit Margins", "IT System Costs", "Customer Price Index", "Operational Adaptability"]
    values = [60, 50, 70, 80, 65]
    plot_metrics("Tariff Impact Metrics", metrics, values)
    return """
    **Tariff Impact Metrics**
    - **Supply Chain Efficiency**: Measures how well supply chains adapt to increased costs and restrictions.
    - **Profit Margins**: Assesses the impact of tariffs on profitability and cost structures.
    - **IT System Costs**: Evaluates increased IT expenses due to compliance and regulatory changes.
    - **Customer Price Index**: Tracks the influence of tariffs on consumer pricing and demand.
    - **Operational Adaptability**: Examines the ability of organizations to adjust business models in response to tariffs.
    """

# Function to define new metrics for war impact
def get_war_impact():
    metrics = ["Supply Chain Stability", "Economic Confidence", "Cybersecurity Threat Level", "Workforce Availability", "Regulatory Compliance"]
    values = [40, 45, 85, 55, 50]
    plot_metrics("War Impact Metrics", metrics, values)
    return """
    **War Impact Metrics**
    - **Supply Chain Stability**: Evaluates the reliability of supply chains amid geopolitical conflicts.
    - **Economic Confidence**: Measures investor and consumer trust during wartime.
    - **Cybersecurity Threat Level**: Assesses risks of cyberattacks and breaches due to conflict.
    - **Workforce Availability**: Tracks the impact of war on labor force participation and talent retention.
    - **Regulatory Compliance**: Examines changes in laws and regulations affecting business operations.
    """

# Function to define new metrics for pandemic impact
def get_pandemic_impact():
    metrics = ["Remote Work Efficiency", "Health & Safety Investment", "Supply Chain Reliability", "Market Demand Stability", "Automation Utilization"]
    values = [75, 90, 50, 60, 85]
    plot_metrics("Pandemic Impact Metrics", metrics, values)
    return """
    **Pandemic Impact Metrics**
    - **Remote Work Efficiency**: Measures productivity levels in remote work settings.
    - **Health & Safety Investment**: Evaluates business spending on safety protocols and infrastructure.
    - **Supply Chain Reliability**: Assesses the ability of supply chains to function amid lockdowns and restrictions.
    - **Market Demand Stability**: Tracks fluctuations in consumer demand due to health crises.
    - **Automation Utilization**: Examines the adoption of AI and automation in response to workforce disruptions.
    """

# Function to define new metrics for recession impact
def get_recession_impact():
    metrics = ["Budget Reduction Rate", "Job Stability Index", "Consumer Spending Index", "Market Competition Intensity", "Revenue Diversification"]
    values = [65, 50, 40, 70, 80]
    plot_metrics("Recession Impact Metrics", metrics, values)
    return """
    **Recession Impact Metrics**
    - **Budget Reduction Rate**: Measures the rate at which companies cut expenses during economic downturns.
    - **Job Stability Index**: Assesses the security of employment within various industries.
    - **Consumer Spending Index**: Tracks changes in household and business spending habits.
    - **Market Competition Intensity**: Evaluates competitive pressures as companies fight for fewer customers.
    - **Revenue Diversification**: Measures efforts by businesses to create new income streams.
    """


# Sidebar for company supply chain definitions (Before and After Query)
def supply_chain_sidebar(crisis_type=None):
    # Default metrics before any crisis is applied
    supply_chain_metrics = {
        "1": "Supply Chain Efficiency: How quickly materials are sourced and distributed.",
        "2": "Inventory Turnover: Frequency with which inventory is sold and replaced.",
        "3": "Lead Time: Time taken to fulfill an order from procurement to delivery.",
        "4": "Cost of Goods Sold: The total cost of producing goods sold by the company.",
        "5": "Logistics Costs: Expenses related to transporting materials and goods.",
        "6": "Supplier Relationship Strength: Quality and stability of relationships with suppliers.",
        "7": "Demand Forecasting Accuracy: Ability to predict customer demand.",
        "8": "Supply Chain Risk Management: Measures taken to handle potential disruptions.",
        "9": "Warehouse Utilization: Effectiveness of warehouse space management.",
        "10": "Sustainability Index: The environmental and social responsibility in the supply chain."
    }

    # Update definitions based on the selected crisis type
    if crisis_type == "Tariffs":
        st.sidebar.subheader("After Tariff Query: Updated Supply Chain Metrics")
        supply_chain_metrics["1"] = "Supply Chain Efficiency: Adjusted to include the impact of tariffs on sourcing and transportation costs."
        supply_chain_metrics["5"] = "Logistics Costs: Revised to account for the rise in transport expenses due to tariff-induced restrictions."
    elif crisis_type == "War":
        st.sidebar.subheader("After War Query: Updated Supply Chain Metrics")
        supply_chain_metrics["6"] = "Supplier Relationship Strength: Changes in supplier relationships due to geopolitical instability."
        supply_chain_metrics["8"] = "Supply Chain Risk Management: Increased focus on risk management due to potential disruptions caused by conflict."
    elif crisis_type == "Pandemic":
        st.sidebar.subheader("After Pandemic Query: Updated Supply Chain Metrics")
        supply_chain_metrics["3"] = "Lead Time: Extended due to lockdowns and transportation restrictions."
        supply_chain_metrics["7"] = "Demand Forecasting Accuracy: Increased uncertainty in demand due to shifting consumer behavior during pandemics."
    elif crisis_type == "Recession":
        st.sidebar.subheader("After Recession Query: Updated Supply Chain Metrics")
        supply_chain_metrics["4"] = "Cost of Goods Sold: Increased focus on cost reduction strategies to survive the recession."
        supply_chain_metrics["9"] = "Warehouse Utilization: More focus on optimizing warehouse space during an economic downturn."

    # Show the current (updated) metrics or initial metrics if no crisis type is selected
    if crisis_type:
        for key, value in supply_chain_metrics.items():
            st.sidebar.write(f"{key}. {value}")
    else:
        # Show the default (initial) metrics if no crisis is selected
        st.sidebar.subheader("Current Supply Chain Metrics")
        for key, value in supply_chain_metrics.items():
            st.sidebar.write(f"{key}. {value}")

def quality_assurance_page():
    st.title("Quality Assurance for Crisis Impact Metrics")

    # Generating random data points for the metrics
    data = {
        "Metric": ["Supply Chain Efficiency", "Profit Margins", "Logistics Costs",
                   "Cybersecurity Threat Level", "Economic Confidence",
                   "Lead Time", "Demand Forecasting Accuracy", "COGS", "Warehouse Utilization"],
        "Value": np.random.uniform(40, 90, 9),
        "Threshold Min": [50, 40, 30, 60, 50, 30, 50, 30, 40],
        "Threshold Max": [80, 70, 60, 90, 75, 60, 80, 60, 75],
    }

    # Create a DataFrame to display the metrics data
    df = pd.DataFrame(data)
    # Function to validate data
    def validate_metric(row):
        if row['Value'] < row['Threshold Min']:
            return "Below Minimum"
        elif row['Value'] > row['Threshold Max']:
            return "Above Maximum"
        else:
            return "Within Range"

    # Apply the validation function to each row
    df['Validation'] = df.apply(validate_metric, axis=1)

    # Display the metrics in a table
    st.write("### Metrics Data and Validation")
    st.dataframe(df)
# New Metrics Definitions Page
def show_metrics_definitions():
    st.title("New Metrics Based on Crisis Events")

    st.write("The following metrics are defined and modified based on different global crises:")

    # Metrics and corresponding logical formulas
    metrics_info = {
        "Supply Chain Efficiency": "Measures how effectively the company adapts to disruptions in material sourcing and distribution. \
        Formula: \( \text{Efficiency} = \frac{\text{Total Output}}{\text{Total Input}} \)",

        "Profit Margins": "This metric assesses how profits change in response to tariffs. \
        Formula: \( \text{Profit Margin} = \frac{\text{Net Profit}}{\text{Revenue}} \times 100 \)",

        "Lead Time": "Tracks the time it takes for an order to be fulfilled. A crisis could increase this time due to delays in logistics. \
        Formula: \( \text{Lead Time} = \text{Order Fulfillment Time} \)",

        "Logistics Costs": "This metric quantifies the cost of transporting goods, which increases with tariffs or disruptions. \
        Formula: \( \text{Logistics Costs} = \text{Transportation Costs} + \text{Storage Costs} \)",

        "Cybersecurity Threat Level": "Evaluates the risk of cyberattacks during a crisis. \
        Formula: \( \text{Cybersecurity Threat Level} = \frac{\text{Number of Attacks}}{\text{Total Network Access Points}} \)",

        "Economic Confidence": "Assesses the stability of the economy during crises like war or recession. \
        Formula: \( \text{Economic Confidence} = \frac{\text{Consumer Spending}}{\text{GDP}} \)"
    }

    for metric, description in metrics_info.items():
        st.subheader(metric)
        st.write(description)
        st.markdown("___")
    # Streamlit UI


def predictive_analytics_page():
    st.title("Predictive Analytics - Pandemic Scenario")

    # Display text about the model
    st.write("### Predicting the Impact of a Pandemic on Metrics")
    st.write(
        "In this page, we predict how the impact of a pandemic can change various business metrics over time using Machine Learning (ML) and Deep Learning (DL) models.")

    # Display the ML / DL Model being used
    st.write(
        "**Model Used**: We are using a **Linear Regression** model to predict the change in metrics based on pandemic severity and other influencing factors.")

    # Set up pandemic scenario parameters (sliders for user input)
    pandemic_severity = st.slider("Pandemic Severity (0 - 100)", 0, 100, 50)
    remote_work_factor = st.slider("Remote Work Factor (0 - 100)", 0, 100, 50)
    healthcare_investment = st.slider("Healthcare Investment (0 - 100)", 0, 100, 50)
    lockdown_duration = st.slider("Lockdown Duration (Weeks)", 1, 52, 12)

    # Button to predict impact based on user input
    if st.button("Predict Impact of Pandemic on Business Metrics"):
        st.write(f"### Predicting based on the following parameters:")
        st.write(f"Pandemic Severity: {pandemic_severity}%")
        st.write(f"Remote Work Factor: {remote_work_factor}%")
        st.write(f"Healthcare Investment: {healthcare_investment}%")
        st.write(f"Lockdown Duration: {lockdown_duration} Weeks")

        # Call the predictive function and display the results
        predictions = predict_pandemic_impact(pandemic_severity, remote_work_factor, healthcare_investment,
                                              lockdown_duration)

        # Display predicted new metrics
        st.write("### Predicted Impact on Business Metrics:")
        st.write(predictions)

        # Plot the predicted metrics
        plot_predictions(predictions)
# Function to plot the predicted impact
def plot_predictions(predictions):
    fig, ax = plt.subplots()
    ax.barh(predictions['Metric'], predictions['Predicted Impact'], color='lightcoral')
    ax.set_xlabel("Predicted Impact Value")
    ax.set_title("Predicted Impact on Business Metrics")
    st.pyplot(fig)

# Function to predict impact based on parameters (simple model simulation)
def predict_pandemic_impact(severity, remote_work, healthcare_investment, lockdown_duration):
    # Simulating a simple prediction model (linear regression analogy)
    # The formula could be more complex in real scenarios
    supply_chain_impact = max(0,
                              100 - severity * 0.5 + remote_work * 0.3 - healthcare_investment * 0.2 + lockdown_duration * 0.1)
    profit_margin_impact = max(0, 50 - severity * 0.4 + healthcare_investment * 0.5 - lockdown_duration * 0.3)
    logistics_cost_impact = max(0, 60 + severity * 0.6 - remote_work * 0.2 + healthcare_investment * 0.1)
    remote_work_efficiency_impact = max(0, remote_work * 0.7 + healthcare_investment * 0.2)
    demand_forecasting_impact = max(0, 70 - severity * 0.5 + healthcare_investment * 0.3)

    # Create a DataFrame to display the results
    metrics = {
        "Metric": ["Supply Chain Efficiency", "Profit Margins", "Logistics Costs", "Remote Work Efficiency",
                   "Demand Forecasting Accuracy"],
        "Predicted Impact": [supply_chain_impact, profit_margin_impact, logistics_cost_impact,
                             remote_work_efficiency_impact, demand_forecasting_impact]
    }

    df = pd.DataFrame(metrics)

    return df

def show_metrics_definitions():
    st.title("New Metrics Based on Crisis Events")

    # Crisis buttons for selecting the impact type
    crisis_type = st.radio("Select a Crisis to View Metrics:", ["None", "Tariffs", "War", "Pandemic", "Recession"])

    if crisis_type == "Tariffs":
        st.subheader("Tariff Impact on Business Metrics")
        st.write(
            "When tariffs are imposed, several business metrics are impacted. Below are the formulas and definitions:")

        st.markdown("### 1. **Supply Chain Efficiency**")
        st.write("Measures how effectively the company adapts to disruptions in material sourcing and distribution.")
        st.markdown(r"**Formula**: $ \text{Efficiency} = \frac{\text{Total Output}}{\text{Total Input}} $")

        st.markdown("### 2. **Profit Margins**")
        st.write("This metric assesses how profits change in response to tariffs.")
        st.markdown(r"**Formula**: $ \text{Profit Margin} = \frac{\text{Net Profit}}{\text{Revenue}} \times 100 $")

        st.markdown("### 3. **Logistics Costs**")
        st.write("This metric quantifies the cost of transporting goods, which increases with tariffs.")
        st.markdown(r"**Formula**: $ \text{Logistics Costs} = \text{Transportation Costs} + \text{Storage Costs} $")

    elif crisis_type == "War":
        st.subheader("War Impact on Business Metrics")
        st.write("War leads to disruptions in business operations in various ways. Below are the metrics impacted:")

        # For War Impact Metrics
        st.markdown("### 1. **Cybersecurity Threat Level**")
        st.write("Evaluates the risk of cyberattacks during a crisis like war.")
        st.markdown(r"**Formula**: $ \text{Threat Level} = \frac{\text{Number of Attacks}}{\text{Total Network Access Points}} $")

        st.markdown("### 2. **Economic Confidence**")
        st.write("Assesses the stability of the economy during crises like war.")
        st.markdown(r"**Formula**: $ \text{Economic Confidence} = \frac{\text{Consumer Spending}}{\text{GDP}} $")

    elif crisis_type == "Pandemic":
        st.subheader("Pandemic Impact on Business Metrics")
        st.write(
            "A pandemic disrupts supply chains, workforce availability, and demand forecasting. Here are the key metrics:")

        st.markdown("### 1. **Lead Time**")
        st.write("Extended due to lockdowns and transportation restrictions.")
        st.markdown(r"**Formula**: $ \text{Lead Time} = \text{Order Fulfillment Time} $")

        st.markdown("### 2. **Demand Forecasting Accuracy**")
        st.write("Increased uncertainty in demand due to shifting consumer behavior during pandemics.")
        st.markdown(
            r"**Formula**: $ \text{Forecast Accuracy} = \frac{\text{Predicted Demand}}{\text{Actual Demand}} \times 100 $")


    elif crisis_type == "Recession":
        st.subheader("Recession Impact on Business Metrics")
        st.write(
            "During a recession, businesses face reduced budgets and altered market behavior. The following metrics are affected:")

        st.markdown("### 1. **Cost of Goods Sold (COGS)**")
        st.write("Increased focus on cost reduction strategies to survive the recession.")
        st.markdown(r"**Formula**: $ \text{COGS} = \text{Direct Labor} + \text{Direct Materials} $")

        st.markdown("### 2. **Warehouse Utilization**")
        st.write("More focus on optimizing warehouse space during an economic downturn.")
        st.markdown(
            r"**Formula**: $ \text{Utilization Rate} = \frac{\text{Used Space}}{\text{Total Space}} \times 100 $")

    else:
        st.write("Select a crisis from the radio buttons above to view its impact on business metrics.")


st.set_page_config(page_title="Global Crisis Chatbot", layout="wide")
page = st.sidebar.selectbox("Select Page", ["Dashboard", "New Metrics Definitions","Quality Assurance","Predictive Analytics"])

# Show content based on selected page
if page == "Dashboard":
    st.sidebar.title("User Query")
    user_query = st.sidebar.text_input("Enter a custom query about crisis impact:")

    st.title("🌎 Global Crisis Impact on Organizations 🏭")
    st.write("Understand how various global crises affect different business processes with key metrics.")
    def set_background_image(image_path):
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url('data:image/jpg;base64,{encode_image(image_path)}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 100%;
                width: 100%;
            """, unsafe_allow_html=True)

    # Function to encode the image into base64 for embedding
    def encode_image(image_path):
        import base64
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        return encoded_image

    # Set the background image for the app (local image)
    # set_background_image("w.jpg")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Impact of Tariffs💸"):
            supply_chain_sidebar(crisis_type="Tariffs")
            st.write(get_tariff_impact())
        if st.button("Impact of War ⚔"):
            supply_chain_sidebar(crisis_type="War")
            st.write(get_war_impact())

    with col2:
        if st.button("Impact of Pandemics🤒"):
            supply_chain_sidebar(crisis_type="Pandemic")
            st.write(get_pandemic_impact())
        if st.button("Impact of Recessions🧾"):
            supply_chain_sidebar(crisis_type="Recession")
            st.write(get_recession_impact())

    # If no button is selected, show the default (initial) metrics in the sidebar
    if not user_query and not any(st.session_state.get("button_pressed", False) for button in [ "Impact of Tariffs💸", "Impact of War ⚔", "Impact of Pandemics🤒", "Impact of Recessions🧾"]):
        supply_chain_sidebar()
elif page=='New Metrics Definitions':
    show_metrics_definitions()
elif page == "Quality Assurance":
    quality_assurance_page()
elif page == "Predictive Analytics":
    predictive_analytics_page()
