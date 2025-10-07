# AI-Powered Code Debugger

A web-based tool that helps developers identify **syntax and logic errors** in their code using **AI-generated debugging feedback**.  
Built with **Python**, **Flask**, and the **OpenAI API**, it supports multiple programming languages including **Python**, **Java**, and **JavaScript**.

---

## 🚀 Features
- 🪲 Detects syntax and logic errors across multiple languages  
- 💬 Provides real-time AI explanations and optimized code suggestions  
- ⚡ Uses asynchronous API calls for faster response times  
- 💾 Implements caching to improve performance on repeated queries  
- 🌐 Simple, responsive web interface for an intuitive debugging experience  

---

## 🏗️ Tech Stack
| Component | Technology |
|------------|-------------|
| **Backend** | Python, Flask, OpenAI API |
| **Frontend** | HTML, CSS, JavaScript |
| **AI Model** | GPT-4-series (OpenAI) |
| **Deployment (Optional)** | Render / Railway / Heroku |

---

## ⚙️ Installation & Setup

1. Clone the repository  
   git clone https://github.com/<your-username>/ai_code_debugger.git  
   cd ai_code_debugger  

2. Create a virtual environment  
   python3 -m venv venv  
   source venv/bin/activate     # On Windows: venv\Scripts\activate  

3. Install dependencies  
   pip install flask openai python-dotenv  

4. Add your OpenAI API key  
   Create a `.env` file in the project root and add this line:  
   OPENAI_API_KEY=your_api_key_here  

5. Run the Flask app  
   flask run  

6. Open your browser and go to  
   http://127.0.0.1:5000/  

---

## 💻 Usage
1. Paste your code into the text area.  
2. Select a programming language.  
3. Click **Debug** to get instant AI-generated insights and fixes.  

---

## 🧠 Future Improvements
- Integrate syntax highlighting (e.g., CodeMirror or Monaco Editor)  
- Add code execution sandbox for test runs  
- Include support for more languages (C++, Go, Rust)  
- Save debug history per user session  
- Host on Render or Railway for public access  

---

## 📜 License
This project is licensed under the **MIT License** — feel free to use and modify it.

---

## 👩‍💻 Author
**Nitya Ramireddy**  
*Computer Science @ Purdue University*  
📧 nitya.ramireddy@gmail.com
