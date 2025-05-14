import matplotlib.pyplot as plt
import pandas as pd
from icanmakeyourbedrock import get_claude_partner_data

# Load the data
data = get_claude_partner_data()

#final = get_claude_partner_data()

df = pd.DataFrame(data["records"])

# Group by Partner_ID and count how many users
partner_counts = df.groupby("Partner_ID").size().reset_index(name="User Count")

# Sort by Partner_ID
partner_counts = partner_counts.sort_values("Partner_ID")

# Plot
# plt.figure(figsize=(10, 6))
# plt.bar(partner_counts["Partner_ID"], partner_counts["User Count"], color="#FFB6C1")
# plt.xlabel("Partner ID", color="#FF69B4")
# plt.ylabel("User Count", color="#FF69B4")
# plt.title("📬 Users Per Partner ID", color="#FF69B4")
# plt.grid(axis="y", linestyle="--", alpha=0.3, color="#FFC0CB")
# plt.gca().set_facecolor("#FFF0F5")
# plt.xticks(partner_counts["Partner_ID"])
# plt.tick_params(colors="#FF69B4")
# plt.tight_layout()
# plt.show()
#


