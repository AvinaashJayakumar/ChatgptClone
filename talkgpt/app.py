from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

# Chatbot endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "Invalid request"}), 400

    # Define a conversation with the user's message
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message},
    ]

    try:
        # Generate a response from GPT-3
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
        )

        # Extract and return the assistant's reply
        assistant_reply = response['choices'][0]['message']['content']
        return jsonify({"message": assistant_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
