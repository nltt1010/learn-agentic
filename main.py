from google import genai
from google.genai import types

from dotenv import load_dotenv
from tools import write_text_file, exponentiation, get_current_stock_price

load_dotenv()
client = genai.Client()

my_tools = [write_text_file, exponentiation, get_current_stock_price]

print("🤖 Agent is ready! Sending your question...")

system_prompt = """
You are a professional analytical AI agent. Upon receiving a question, you must follow these steps:
Step 1: Use the compatible tool to search for realistic information.
Step 2: Perform the exact mathematical logic required by the question.
Step 3: Synthesize the findings into a detailed report.
Step 4: Use the 'write_text_file' tool to save the report as a .txt file on the desktop.
"""

question = """
I have a budget of $10,000 USD. 
Check the current Apple (AAPL) stock price. 
Calculate the maximum number of shares I can buy, considering the exchange rate. 
Finally, write all the results into a file named 'report_apple.txt'.
"""

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=question,
    config=types.GenerateContentConfig(
        tools=my_tools, 
        system_instruction=system_prompt,
        temperature=0.0 
    )
)

print(f"\n💬 [Agent response User]:\n{response.text}")