import json
import requests
import os
import boto3
from botocore.exceptions import ClientError
import openai
from dotenv import load_dotenv

# IT WORKED!!!!


def fetch_top_5_cryptos():
    """
    Fetches the top 5 cryptocurrencies by market cap from CoinGecko.
    Returns a list of dicts with id, symbol, name, and current price.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    top_5 = [
        {
            "id": coin["id"],
            "symbol": coin["symbol"],
            "name": coin["name"],
            "current_price": coin["current_price"]
        }
        for coin in data
    ]
    if not top_5:
        return {
            'statusCode': 500,
            "headers":{
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps({"error": "Failed to fetch data from CoinGecko"})
        }

    return top_5


def build_gpt_prompt(coin_data):
    """
    Builds a GPT prompt based on the top 5 cryptocurrencies.
    """
    
    
    coin_summary = "\n".join(
        f"{coin['name']} ({coin['symbol'].upper()}): ${coin['current_price']}" for coin in coin_data
    )

    prompt = (
        "You are a responsible financial AI advisor advising a new client with no crypto experience. Based on the following crypto market data:\n\n"
        f"{coin_summary}\n\n"
        "1. Which of these coins appears to be the best investment based on strong financial fundamentals? Provide relatable analogies that avoid other traditional investment options like stocks\n"
        "2. Are there any that resemble meme coins or should be approached with caution? If none present, still mention any currently popular as of today meme and specifically give opinion on trump coin.\n"
        "3. What red flags should someone watch for if approached in-person to invest in a new coin?\n"
        "Respond clearly and concisely."
    )
    return prompt

def get_secret():

    secret_name = "CryptoBuyAdvisor/OpenAI"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']

    return secret


def gpt_recommendation(prompt):
    """
    Placeholder function for GPT recommendation logic.
    In a real implementation, this would call the OpenAI API with the provided prompt.
    """

    # Step 1: Load the OpenAI API key

    # Local testing
    # load_dotenv()
    # openai.api_key = os.getenv("OPENAI_API_KEY")

    # Call to AWS Secrets Manager
    openai.api_key = get_secret()

    if not openai.api_key:
        raise ValueError("OpenAI API key not found.")
    client = openai.OpenAI(api_key=openai.api_key)
    
    # Step 2: Call OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a seasoned crypto advisor who loves helping people with no knowledge of crypto."},
            {"role": "user", "content": prompt}
    ],
    temperature=0.7
)


    # Step 3: Return the GPT response
    print(response)
    if not response or not response.choices:
        raise ValueError("Invalid response from OpenAI API")
    return {
        "GPT Response": response.choices[0].message.content
     } 


def lambda_handler(event, context):
    """
    Lambda function scaffold for CryptoBuyAdvisor

    Functionality:
    - Fetch real-time crypto data from CoinGecko API
    - Securely retrieve OpenAI API key from Secrets Manager
    - Construct GPT prompt for crypto recommendations and risk warnings
    - Cache responses for cost efficiency
    """
    # Step 1: Fetch top 5 cryptocurrencies
    top_5 = fetch_top_5_cryptos()

    # Step 2: Build GPT prompt
    prompt = build_gpt_prompt(top_5)

    # Step 3: Get GPT recommendation
    gpt_recommendation_response = gpt_recommendation(prompt)

    print("\nGPT Analysis:\n")
    print(gpt_recommendation_response["GPT Response"])


    return {
        'statusCode': 200,
        "headers":{
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps({
            "coins":top_5,
            "gpt_recommendation": gpt_recommendation_response["GPT Response"]
        })
    }   

if __name__ == "__main__":
    # For local testing
    event = {}
    context = {}
    response = lambda_handler(event, context)
    print(response)

    # Get mock file
    response["body"] = json.loads(response["body"])

    # Save mock file
    mock_path = os.path.join(os.getcwd(), "frontend", "mock_crypto.json")
    with open(mock_path, "w") as f:
        json.dump(response["body"], f, indent=2)
