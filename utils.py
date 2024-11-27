import openai

def query_llm(prompt, model="gpt-3.5-turbo"):
    # Replace with your actual OpenAI API key
    openai.api_key = 'your-api-key-here'

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']