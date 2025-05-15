import matplotlib.pyplot as plt
import pandas as pd
from icanmakeyourbedrock import get_claude_vendor_data

# Load the data
data = get_claude_vendor_data()

#final = get_claude_vendor_data()

df = pd.DataFrame(data["records"])

# Group by vendor_ID and count how many users
vendor_counts = df.groupby("vendor_ID").size().reset_index(name="User Count")

# Sort by vendor_ID
vendor_counts = vendor_counts.sort_values("vendor_ID")

# Plot
# plt.figure(figsize=(10, 6))
# plt.bar(vendor_counts["vendor_ID"], vendor_counts["User Count"], color="#FFB6C1")
# plt.xlabel("vendor ID", color="#FF69B4")
# plt.ylabel("User Count", color="#FF69B4")
# plt.title("📬 Users Per vendor ID", color="#FF69B4")
# plt.grid(axis="y", linestyle="--", alpha=0.3, color="#FFC0CB")
# plt.gca().set_facecolor("#FFF0F5")
# plt.xticks(vendor_counts["vendor_ID"])
# plt.tick_params(colors="#FF69B4")
# plt.tight_layout()
# plt.show()
#


