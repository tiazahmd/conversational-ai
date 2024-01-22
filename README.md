# Conversational Voice Assistant

## Description

This code implements a simple voice-based conversational assistant using the OpenAI API. The assistant listens to voice input, sends the input to the OpenAI API, and outputs the assistant's response. The conversation takes place in a threaded environment, and the assistant continues to listen for user input until the user says "bye."

## Setup Instructions

### 1. Install Required Libraries

Ensure you have the necessary libraries installed by running the following command:

```bash
pip install -r requirements.txt
```

### 2. Obtain OpenAI API Key

To use the OpenAI API, you need an API key. Create an `apikey.py` file in the same directory as the code and add the following line:

```python
api_key = "YOUR_API_KEY"
```

Replace "YOUR_API_KEY" with your actual OpenAI API key.

## Usage

1. Run the script by executing the following command:

   ```bash
   python main.py
   ```

2. The voice assistant will prompt you to speak. Provide your input.

3. The assistant will send the input to the OpenAI API, generate a response, and output the response.

4. Continue the conversation by responding to the assistant's prompts. Say "bye" to end the conversation.

## Notes

- The assistant uses the Google Speech Recognition service for voice input, so ensure your microphone is properly set up.
- The assistant utilizes the `say` command for voice output. Ensure your system supports this command for proper functionality.

Feel free to customize the code and experiment with different models and configurations based on the OpenAI API documentation.