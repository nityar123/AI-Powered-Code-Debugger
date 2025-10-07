#flask backend

from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/debug', methods=['POST'])
async def debug_code():
    data = request.get_json()
    code = data.get('code', '')
    language = data.get('language', 'Python')

    prompt = f"""
    You are an expert {language} debugger.
    Find syntax and logic errors in this code and suggest improvements.
    Code:\n{code}
    """

    try:
        # Asynchronous API call
        response = await asyncio.to_thread(
            lambda: openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
        )
        suggestion = response.choices[0].message["content"]
        return jsonify({"suggestion": suggestion})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
