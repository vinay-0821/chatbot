import os
import json
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Initialize OpenAI client with OpenRouter config
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openrouter_api_key,
)

MODEL_NAME = "deepseek/deepseek-r1-0528:free"  # Valid OpenRouter model

def get_llm_response(df, user_query):
    # Preview first few rows of the data
    preview = df.head(100).to_dict(orient="records")

    # Instructional system prompt
    system_prompt = """You are a helpful data analyst.

You will be given:
1. A preview of a dataset (in JSON format)
2. A user's natural language question

Your task:
- Answer the question in markdown.
- If the user asks for a chart, also provide a chart plan in this exact format:

```json
{
  "type": "bar",         // bar, line, or hist
  "x": "column_name",
  "y": "column_name"
}
```

Only include the chart block if the user clearly asks for a chart.
"""

    # Prepare messages for chat completion
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Data Preview:\n{preview}\n\nQuestion:\n{user_query}"}
    ]

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            extra_headers={
                "HTTP-Referer": "http://localhost",  # optional
                "X-Title": "Excel Chat Assistant"      # optional
            }
        )
        content = completion.choices[0].message.content.strip()
    except Exception as e:
        return f"API Error: {e}", None

    # Extract chart info if present
    chart_info = None
    answer = content

    if "```json" in content:
        try:
            start = content.index("```json") + len("```json")
            end = content.index("```", start)
            json_block = content[start:end].strip()
            chart_info = json.loads(json_block)
            answer = content[:content.index("```json")].strip()
        except Exception as e:
            print("Failed to parse chart JSON:", e)
            chart_info = None

    return answer, chart_info
