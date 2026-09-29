import os
import sys
import tiktoken                       
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from openai import OpenAI
# the enx key is not in the local folder so file get the location of file
# the resolve gets the absolute path from c to curr
# parent keeps the required from ai_roadmap to curr
script_dir = Path(__file__).resolve().parent

root_env_path = script_dir.parent / ".env"

# if env is in local file then code remains load_dotenv()
load_dotenv(dotenv_path = root_env_path)

#Intialization of both models with API key
gemini_client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

openrouter_client = OpenAI(
    base_url = "https://openrouter.ai/api/v1", 
    api_key = os.getenv("OPENROUTER_API_KEY")
)

curr_model = "gemini"
Budget_Limit = 150
tokenizer = tiktoken.get_encoding("cl100k_base")


print("=" * 60)
print("FREE MULTI MODEL CHAT INITIALIZED")
print("Commands: Type '\switch' to change provider | '\exit' to quit")
print(f"Current Model: {curr_model}")
print("=" * 60)

while True:
    try:
        user_input = input("\n You: ".strip())
    except (KeyboardInterrupt, EOFError):
        break

    if not user_input:
        continue

    if user_input.lower() == r'\exit':
        print("Goodbye!")
        break

    if user_input.lower() == r'\switch':
        curr_model = "openrouter" if curr_model == "gemini" else "gemini"
        print(f"Switched Provider! Active Provider:{curr_model.upper()}")
        continue

    input_tokens = len(tokenizer.encode(user_input))
    print(f"Token Count: {input_tokens} tokens")

    if input_tokens > Budget_Limit:
        print("---Request Rejected!!!---")
        print(f"Input Tokens: {input_tokens} ... Token Budget: {Budget_Limit}")
        print("Exceeded Token Budget Limited")
        continue

    print("Bot: ", end="", flush = True)
# Provider 1: Gemini
    if curr_model == "gemini":
        target_model = "gemini-2.5-flash-lite" if input_tokens <30 else "gemini-2.5-flash"

        try:
            response_stream = gemini_client.models.generate_content_stream(
                model = target_model,
                contents = user_input,
            )
            for chunk in response_stream:
                if chunk.text:
                    print(chunk.text, end = "", flush=True)
            print() # Yield Terminal newline when Generator exhausts

        except Exception as e:
            print(f"Gemini API Error: {e}")

# Provider 2: OpenRouter
    elif  curr_model == "openrouter":
        target_model = "openai/gpt-oss-20b:free" if input_tokens < 30 else "nvidia/nemotron-3-super-120b-a12b:free"

        try:
            response_stream = openrouter_client.chat.completions.create(
                model = target_model,
                messages = [{"role": "user", "content": user_input}],
                stream = True,
                # temperature=1.0,  # 0.0 for certainity 2.0 for chaos
                # top_p=0.2         # 0.0 for certainity 1.0 for chaos
            )
            for chunk in response_stream:
                content = chunk.choices[0].delta.content
                if content:
                    print(content, end="", flush = True)
            print()
        except Exception as e:
            print(f"OpenRouter API Error: {e}")