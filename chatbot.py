from openai import OpenAI
from datetime import datetime
import os

# Create the client (uses your OPENAI_API_KEY from the environment)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("🤖 Baby Chatbot ready! Type 'exit' to quit.")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ("exit", "quit"):
        print("Goodbye! 👋")
        break

    # Always compute your Mac's current local date/time
    current_time = datetime.now().strftime("%A, %b %d, %Y %I:%M %p")

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"You are Baby Agent. The correct current local date/time is: {current_time}. "
                           f"Always use this when answering anything about date or time."
            },
            {"role": "user", "content": user_input},
        ],
    )

    print("Bot:", resp.choices[0].message.content.strip())
