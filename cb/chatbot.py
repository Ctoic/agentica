import requests

def ask_ollama(question):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "llama3",
        "messages": [
            {"role": "user", "content": question}
        ],
        "stream": False   # Important: tell Ollama not to stream
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

