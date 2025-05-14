# import os
# import json
# import boto3
# from dotenv import load_dotenv
#
# # Load environment variables
# load_dotenv()
#
#
# def ask_claude(prompt):
#     """Ask Claude 3.7 a question using an inference profile"""
#     # Get ALL credential components including session token
#     aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
#     aws_secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
#     aws_session_token = os.environ.get('AWS_SESSION_TOKEN')
#     aws_region = os.environ.get('AWS_REGION', 'us-east-1')
#
#     # Get the inference profile ARN
#     inference_profile_arn = os.environ.get('INFERENCE_PROFILE_ARN')
#     if not inference_profile_arn:
#         raise ValueError("INFERENCE_PROFILE_ARN environment variable is required for Claude 3.7")
#
#     # Create Bedrock Runtime client WITH session token
#     bedrock_runtime = boto3.client(
#         'bedrock-runtime',
#         region_name=aws_region,
#         aws_access_key_id=aws_access_key,
#         aws_secret_access_key=aws_secret_key,
#         aws_session_token=aws_session_token
#     )
#
#     # Prepare request for Claude 3.7
#     request_body = {
#         "anthropic_version": "bedrock-2023-05-31",
#         "max_tokens": 4000,
#         "messages": [
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ],
#         "temperature": 0.7
#     }
#
#     # Call the model USING THE INFERENCE PROFILE
#     response = bedrock_runtime.invoke_model(
#         modelId="us.anthropic.claude-3-5-sonnet-20240620-v1:0",
#         body=json.dumps(request_body),
#         contentType="application/json",
#         accept="application/json",
#         inferenceProfileArn=inference_profile_arn  # This is the key addition!
#     )
#
#     # Parse and return response
#     response_body = json.loads(response['body'].read())
#     return response_body["content"][0]["text"]
#
#
# # Simple interactive mode
# if __name__ == "__main__":
#     if not os.environ.get('INFERENCE_PROFILE_ARN'):
#         print("⚠️ Warning: INFERENCE_PROFILE_ARN not set in environment variables.")
#         print("Please add your inference profile ARN to your .env file:")
#         print("INFERENCE_PROFILE_ARN=arn:aws:bedrock:region:account:inference-profile/name")
#         profile_arn = input("\nAlternatively, paste your inference profile ARN here: ")
#         if profile_arn:
#             os.environ['INFERENCE_PROFILE_ARN'] = profile_arn
#         else:
#             print("No inference profile provided. Exiting.")
#             exit(1)
#
#     print("=== Claude 3.5 Sonnet AI Assistant ===")
#     print("Type your questions/prompts and press Enter.")
#     print("Type 'exit' to quit.\n")
#
#     while True:
#         user_input = input("\nYou: ")
#
#         if user_input.lower() in ['exit', 'quit', 'bye']:
#             print("Goodbye!")
#             break
#
#         try:
#             print("\nThinking...")
#             response = ask_claude(user_input)
#             print(f"\nClaude 3.7: {response}")
#         except Exception as e:
#             print(f"\nError: {str(e)}")


