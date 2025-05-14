import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

global result
global result2

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


# Make the request
response = bedrock.converse(
    messages= [ {"role": "user", "content": [{"text":
                                                 "You are an advanced data analysis model. You will be given a structured dataset as a three-column table representing email activity across 12 months. Each row contains: PSN: a string starting with \"PSN\" followed by a random number; Email: a valid email address; Partner_ID: an integer from 1 to 10. The dataset spans 12 months of historical records. Some PSNs may appear in multiple months, with the same or changing emails and/or partner IDs. Your task is to analyze this dataset and return a single JSON object with the following five top-level keys: partner_email_distribution_analysis, email_stability_analysis, partner_confidence_scoring, data_quality_metrics, and relationship_network_analysis. Each section must include the following: partner_email_distribution_analysis: Distinct email count per partner ID; Email domain distribution per partner; Mean, median, min, max of emails per partner; Identify partners with anomalously high or low email counts (±2 standard deviations); Include analysis timestamp and data range. email_stability_analysis: Detect email changes for each PSN over time, grouped by partner; Percentage of stable vs. changing emails per partner; Categorize email changes (domain-only vs. full changes); Average lifespan (in months) of emails before they change; Highlight any seasonal patterns or spikes in changes. partner_confidence_scoring: Score each partner (0-100) based on Email consistency, Domain reputation (common vs. suspicious domains), Email format validity, Engagement frequency (based on PSN repetition across months), Data completeness rate, Longevity of PSN relationships; Include confidence intervals; Flag partners with rapid shifts in score. data_quality_metrics: Missing field percentages per partner and column; Duplicate email rate per partner; Format compliance rate for emails; Temporal consistency: do PSNs appear in logical month patterns? relationship_network_analysis: Identify clusters of PSNs with shared email or domain patterns; Map cross-partner relationships for reused PSNs; Calculate network density metrics and bridge PSNs. Return only valid JSON output. Every section must include metadata: timestamp of analysis, analysis_version, data_range (\"YYYY-MM\" format), exclusion_criteria (e.g., \"none\", \"removed malformed emails\"), and confidence (float between 0 and 1 for reliability). Do not return any explanation or text, just the JSON output."}]} ],
    modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    #inferenceProfileArn=inference_profile_arn,
    #contentType="application/json",
    #accept="application/json",
    #body=json.dumps(body)
)

response2 = bedrock.converse(
    messages= [ {"role": "user", "content": [{"text":
                                                 "You are an advanced data analysis model. You will be given a structured dataset as a three-column table representing email activity across 12 months. Each row contains: PSN: a string starting with \"PSN\" followed by a random number; Email: a valid email address; Partner_ID: an integer from 1 to 10. The dataset spans 12 months of historical records. Some PSNs may appear in multiple months, with the same or changing emails and/or partner IDs. Your task is to analyze this dataset and return a single JSON object with the following five top-level keys: partner_email_distribution_analysis, email_stability_analysis, partner_confidence_scoring, data_quality_metrics, and relationship_network_analysis. Each section must include the following: partner_email_distribution_analysis: Distinct email count per partner ID; Email domain distribution per partner; Mean, median, min, max of emails per partner; Identify partners with anomalously high or low email counts (±2 standard deviations); Include analysis timestamp and data range. email_stability_analysis: Detect email changes for each PSN over time, grouped by partner; Percentage of stable vs. changing emails per partner; Categorize email changes (domain-only vs. full changes); Average lifespan (in months) of emails before they change; Highlight any seasonal patterns or spikes in changes. partner_confidence_scoring: Score each partner (0-100) based on Email consistency, Domain reputation (common vs. suspicious domains), Email format validity, Engagement frequency (based on PSN repetition across months), Data completeness rate, Longevity of PSN relationships; Include confidence intervals; Flag partners with rapid shifts in score. data_quality_metrics: Missing field percentages per partner and column; Duplicate email rate per partner; Format compliance rate for emails; Temporal consistency: do PSNs appear in logical month patterns? relationship_network_analysis: Identify clusters of PSNs with shared email or domain patterns; Map cross-partner relationships for reused PSNs; Calculate network density metrics and bridge PSNs. Return only valid JSON output. Every section must include metadata: timestamp of analysis, analysis_version, data_range (\"YYYY-MM\" format), exclusion_criteria (e.g., \"none\", \"removed malformed emails\"), and confidence (float between 0 and 1 for reliability). Do not return any explanation or text, just the JSON output."}]} ],
    modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    #inferenceProfileArn=inference_profile_arn,
    #contentType="application/json",
    #accept="application/json",
    #body=json.dumps(body)
)





# Print output
result = response['output']['message']['content'][0]['text']
print(result)

# result2 = response['output']['message']['content'][0]['text']
# print(result)


import json

def get_claude_partner_data():
    # This is where you put your actual Bedrock call
    # Simulated response from Claude:
    result_text = result

    result_dict = json.loads(result_text)
    return result_dict


def howToReadPltOutput():
    #something

    result = result2

    #interperet result
    #plt.show????

    return result2

