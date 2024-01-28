from openai import OpenAI
from apikey import api_key
import time
import speech_recognition as sr
import subprocess

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=20, phrase_time_limit = 20)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your audio.")
        return "bye"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "bye"
    
def voice_output(text, rate = 150):
    try:
        subprocess.run(['say', text])
    except Exception as e:
        print(f"Error: {e}")

def loading():
    symbols = ["█", "▓", "▒", "░"]
    for i in range (0, len(symbols)):
        i = (i + 1) % len(symbols)
        print('\r\033[K%s Generating answer...' % symbols[i], flush=True, end='')
        time.sleep(0.099)

def run_ai(client, thread_id, run_id):
    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )

        if run.status == "completed":
            print("\r", end="", flush=True)
            break
        else:
            loading()
            time.sleep(0.1)

def converse(client, assistant, thread):
    while True:
        print("Waiting for voice input...")
        prompt = get_voice_input()
        print("User: " + prompt)
        
        if prompt == "bye":
            break

        message = client.beta.threads.messages.create(
            thread_id = thread.id,
            role = "user",
            content = prompt
        )

        run = client.beta.threads.runs.create(
            thread_id = thread.id,
            assistant_id = assistant.id
        )

        run_ai(client, thread.id, run.id)

        messages = client.beta.threads.messages.list(
            thread_id = thread.id
        )

        assistant_response = messages.data[0].content[0].text.value
        print("Assistant: " + assistant_response + "\n")
        voice_output(assistant_response)

def main():
    client = OpenAI(api_key = api_key)
    
    assistant = client.beta.assistants.create(
        name = "Imtiaz's Assistant",
        instructions = "You are my personal assistant. You will provide me with\
                        answers to the questions I ask.",
        tools=[{"type": "retrieval"}],
        model = "gpt-4-1106-preview",
    )

    thread = client.beta.threads.create()
    converse(client, assistant, thread)

if __name__ == "__main__":
    main()