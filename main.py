import boto3
import json

bedrock = boto3.client(
    service_name='bedrock-runtime', 
    region_name='us-west-2'
)

rapper_name = input("Enter desired rapper's name: ")
subject = input("Enter the subject of the rap verse: ")

prompt_text = (
    f"You're going to generate rap verses for {rapper_name} about {subject}."
    f"Rappers classified as a \"mumble rapper\" will have more basic, repetitive, catchy lyrics."
    f"Rappers classified as a \"lyrical rapper\" will have deeper, more sophisticated, complex lyrics."
    f"\"Lyrical rappers\" will utilize entendres, lots of wordplay, and genius hidden references."
    f"Do not be afraid to show the emotions of {rapper_name} in their lyrics."
    f"If {rapper_name} has recent rap beef with another, make sure to somehow include that in the lyrics."
    f"If {rapper_name} isn't a rapper, rather a singer like Taylor Swift, say \"Please enter a rapper\"."
    )
input_data = {
    "modelId": "anthropic.claude-3-haiku-20240307-v1:0",
    "contentType": "application/json",
    "accept": "application/json",
    "body": json.dumps({
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt_text
                    }
                ]
            }
        ],
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 2000,
        "temperature": 1
    })
}

response = bedrock.invoke_model(
    body=input_data["body"],
    modelId=input_data["modelId"],
    accept=input_data["accept"],
    contentType=input_data["contentType"]
)

response_body = json.loads(response['body'].read().decode('utf-8'))

main_content = response_body['content'][0]['text']

print(main_content)
