# Example: reuse your existing OpenAI client code
# Change the baseUrl to point to LM Studio
import json
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
    model="meta-llama-3.1-8b-instruct",
    messages=[{"role": "system", "content": "Hello."}],
    temperature=0.7,
)

message = completion.choices[0].message.model_dump()

print(json.dumps(message, indent=2, default=str, ensure_ascii=False))
