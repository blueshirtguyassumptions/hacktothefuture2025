import boto3
import json
import os
from dotenv import load_dotenv
import pandas as pd
import re

load_dotenv()

global result
global result2

def load_pipe_delimited_files(folder_path):
    data_blocks = []

    for filename in os.listdir(folder_path):
        if  filename.endswith(".csv"):
            filepath = os.path.join(folder_path, filename)
            df = pd.read_csv(filepath, delimiter="|")
            block = f"--- {filename} ---\n{df.to_string(index=False)}\n"
            data_blocks.append(block)

    return "\n".join(data_blocks)





# Create Bedrock client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name="us-east-1"
    # aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    # aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),

)

# Replace with your actual inference profile ARN
inference_profile_arn = os.getenv("INFERENCE_PROFILE_ARN")

# Request body for Claude 3

dataFiles = load_pipe_delimited_files(r"C:\Workspace\hacktothefuture2025")


# Make the request
response = bedrock.converse(
    messages= [ {"role": "user", "content": [{"text":
                                                 f"You are an advanced data analysis model. You will be given a structured dataset as a three-column table representing email activity across 12 months. Each row contains: PSN: a string starting with \"PSN\" followed by a random number; Email: a valid email address; vendor_ID: an integer from 1 to 10. The dataset spans 12 months of historical records. Some PSNs may appear in multiple months, with the same or changing emails and/or vendor IDs. Here is the data {dataFiles}. Your task is to analyze this dataset and return a single JSON object with the following five top-level keys: vendor_email_distribution_analysis, email_stability_analysis, vendor_confidence_scoring, data_quality_metrics, and relationship_network_analysis. Each section must include the following: vendor_email_distribution_analysis: Distinct email count per vendor ID; Email domain distribution per vendor; Mean, median, min, max of emails per vendor; Identify vendors with anomalously high or low email counts (±2 standard deviations); Include analysis timestamp and data range. email_stability_analysis: Detect email changes for each PSN over time, grouped by vendor; Percentage of stable vs. changing emails per vendor; Categorize email changes (domain-only vs. full changes); Average lifespan (in months) of emails before they change; Highlight any seasonal patterns or spikes in changes. vendor_confidence_scoring: Score each vendor (0-100) based on Email consistency, Domain reputation (common vs. suspicious domains), Email format validity, Engagement frequency (based on PSN repetition across months), Data completeness rate, Longevity of PSN relationships; Include confidence intervals; Flag vendors with rapid shifts in score. data_quality_metrics: Missing field percentages per vendor and column; Duplicate email rate per vendor; Format compliance rate for emails; Temporal consistency: do PSNs appear in logical month patterns? relationship_network_analysis: Identify clusters of PSNs with shared email or domain patterns; Map cross-vendor relationships for reused PSNs; Calculate network density metrics and bridge PSNs. Return only valid JSON output. Every section must include metadata: timestamp of analysis, analysis_version, data_range (\"YYYY-MM\" format), exclusion_criteria (e.g., \"none\", \"removed malformed emails\"), and confidence (float between 0 and 1 for reliability). ALSO make sure in the JSON there is a value that trakcs the distinct email count per partner over eaach month. Do not return any explanation or text, just the JSON output."}]} ],
    modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    #inferenceProfileArn=inference_profile_arn,
    #contentType="application/json",
    #accept="application/json",
    #body=json.dumps(body)
)


# Print output
result = response['output']['message']['content'][0]['text']
#print(result)

response2 = bedrock.converse(
    messages= [ {"role": "user", "content": [{
        "text": f"Here is a JSON object containing analytical data: ```json {result} ``` Please analyze the structure and contents, and generate the following matplotlib graphs based on the available information. the first graph should be a line graph with x axis being the months for each data set and the y axis being the the number of distinct emails as they change over the months for each vendor. each vendor should have its own line within the first graph. a second graph should consist of  box and whicker graph of the confidence level we have for each vendor. having the x axis of the second graph have each vendor and the y axis being the confidence level.. A third graph being a pie chart should display the percent change in the number of emails as they change per vendor over time.  Include titles, axis labels, and comments in the Python code for all graphs into one figure. Skip any sections that do not contain graphable data. Style the graphs coquette pink. ONLY RETURN MATPLOTLIB CODE nothing else."

    }
    ]} ],
    modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0"
)




result2 = response2['output']['message']['content'][0]['text']
#print(result2)


response3 = bedrock.converse(
    messages= [ {"role": "user", "content": [{
        "text": f"Here is a JSON object containing analytical data ```json {result} ``` please analyze the data and provide a short summary of every vendor on its shortcomings in the data and possible its best advantages if any.  Output this analysis in a text format. ."

    }
    ]} ],
    modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0"
)

result3 = response3['output']['message']['content'][0]['text']

with open("suggestion.txt", "w", encoding="utf-8") as f:
    f.write(result3)







# Example: extract Claude response content
claude_response_text = result2

# Use regex to extract code inside ```python ... ```
match = re.search(r"```python\n(.*?)```", claude_response_text, re.DOTALL)
if match:
    code_block = match.group(1)
else:
    raise ValueError("No Python code block found in response")

# Write to a file
with open("generated_plot.py", "w") as f:
    f.write(code_block)

# (Optional) Run it
import subprocess
subprocess.run(["python", "generated_plot.py"])



def get_claude_vendor_data():
    result_text = result

    result_dict = json.loads(result_text)
    return result_dict

