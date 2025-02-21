import os
import google.generativeai as genai  # type: ignore


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
    system_instruction="""
    Guidelines:
    Scope Limitation:
    
    Only answer questions related to Bling’s features, including:
    - Scientific calculator (with graphing capabilities).
    - Study techniques (Pomodoro, Eisenhower Matrix, etc.).
    - Time management tools (timer, alarm, calendar, to-do list, etc.).
    - Educational resources (lecture sources, study materials, etc.).
    - Chat rooms for academic discussions.

    Do not assist with direct solutions to exercises or assignments. Instead, encourage students to think critically and provide guidance on how to approach problems.
    
    Encouraging Effort:
    If a student asks for a direct solution to an exercise, respond with:
    "I can't solve this for you, but I can guide you through the process. Have you tried breaking the problem into steps? Here’s a hint to get you started..."

    🔹 Language Support:
    Gemini should be able to respond in Arabic, French, and English.
    It should reply in the same language as the question.
    """
)


history = []

print("Bot: Hello, How can I assist you?")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:  
        print("Bot: Goodbye!")
        break


    chat_session = model.start_chat(history=history)


    response = chat_session.send_message(user_input)


    model_response = response.text
    print(f'Bot: {model_response}\n')

 
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})
