import pandas as pd
import matplotlib.pyplot as plt

# Marketing Funnel Data
data = {
    "Channel": [
        "Google Ads",
        "Instagram",
        "Facebook",
        "LinkedIn",
        "Email",
        "YouTube"
    ],
    "Visitors": [5000, 4500, 4000, 3000, 2500, 3500],
    "Leads": [750, 540, 480, 600, 500, 420],
    "Customers": [150, 81, 72, 180, 125, 84]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate conversion rates
df["Traffic_to_Lead"] = (
    df["Leads"] / df["Visitors"] * 100
).round(2)

df["Lead_to_Customer"] = (
    df["Customers"] / df["Leads"] * 100
).round(2)

df["Overall_Conversion"] = (
    df["Customers"] / df["Visitors"] * 100
).round(2)

# Calculate drop-offs
df["Visitor_Dropoff"] = df["Visitors"] - df["Leads"]
df["Lead_Dropoff"] = df["Leads"] - df["Customers"]

# Display analysis
print("\n========== MARKETING FUNNEL ANALYSIS ==========\n")
print(df.to_string(index=False))

# Overall funnel
total_visitors = df["Visitors"].sum()
total_leads = df["Leads"].sum()
total_customers = df["Customers"].sum()

traffic_to_lead = total_leads / total_visitors * 100
lead_to_customer = total_customers / total_leads * 100
overall_conversion = total_customers / total_visitors * 100

print("\n========== OVERALL FUNNEL ==========")
print("Total Visitors:", total_visitors)
print("Total Leads:", total_leads)
print("Total Customers:", total_customers)

print("Traffic to Lead Conversion: {:.2f}%".format(traffic_to_lead))
print("Lead to Customer Conversion: {:.2f}%".format(lead_to_customer))
print("Overall Conversion Rate: {:.2f}%".format(overall_conversion))

# Best performing channels
best_lead = df.loc[df["Traffic_to_Lead"].idxmax(), "Channel"]
best_customer = df.loc[df["Lead_to_Customer"].idxmax(), "Channel"]
best_overall = df.loc[df["Overall_Conversion"].idxmax(), "Channel"]

print("\n========== BEST PERFORMING CHANNELS ==========")
print("Best Traffic-to-Lead Channel:", best_lead)
print("Best Lead-to-Customer Channel:", best_customer)
print("Best Overall Conversion Channel:", best_overall)

# Drop-off analysis
print("\n========== DROP-OFF ANALYSIS ==========")

visitor_dropoff = total_visitors - total_leads
lead_dropoff = total_leads - total_customers

print("Visitors who did not become leads:", visitor_dropoff)
print("Leads who did not become customers:", lead_dropoff)

# Chart 1: Visitors, Leads and Customers
plt.figure(figsize=(10, 6))

x = range(len(df))

plt.bar(
    [i - 0.25 for i in x],
    df["Visitors"],
    width=0.25,
    label="Visitors"
)

plt.bar(
    x,
    df["Leads"],
    width=0.25,
    label="Leads"
)

plt.bar(
    [i + 0.25 for i in x],
    df["Customers"],
    width=0.25,
    label="Customers"
)

plt.xticks(x, df["Channel"], rotation=30)
plt.xlabel("Marketing Channel")
plt.ylabel("Number of Users")
plt.title("Marketing Funnel by Channel")
plt.legend()
plt.tight_layout()
plt.show()

# Chart 2: Traffic to Lead Conversion
plt.figure(figsize=(10, 5))

plt.bar(
    df["Channel"],
    df["Traffic_to_Lead"]
)

plt.xlabel("Marketing Channel")
plt.ylabel("Conversion Rate (%)")
plt.title("Traffic-to-Lead Conversion")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Chart 3: Lead to Customer Conversion
plt.figure(figsize=(10, 5))

plt.bar(
    df["Channel"],
    df["Lead_to_Customer"]
)

plt.xlabel("Marketing Channel")
plt.ylabel("Conversion Rate (%)")
plt.title("Lead-to-Customer Conversion")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Business Insights
print("\n========== BUSINESS INSIGHTS ==========")

print("1. Google Ads generates a high number of visitors and leads.")
print("2. LinkedIn has a strong lead-to-customer conversion rate.")
print("3. Email marketing converts leads effectively into customers.")
print("4. A large number of visitors do not become leads.")
print("5. Improving visitor-to-lead conversion can increase customer acquisition.")
print("6. Marketing channels should be optimized based on both traffic and conversion quality.")

print("\n========== ANALYSIS COMPLETED ==========")

