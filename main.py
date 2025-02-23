from flask import Flask, request, jsonify
import requests
import os
import base64
import time
from dotenv import load_dotenv

app = Flask(__name__)

# GitHub Credentials
load_dotenv("sensitive.env")
GITHUB_USERNAME = "vipreshgupta"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Store your token securely
GITHUB_API_URL = "https://api.github.com"
AGENT_API_KEY=os.getenv("AGENT_API_KEY")
# API Headers
AGENT_API_HEADERS = {
    "Authorization": f"Bearer {AGENT_API_KEY}",
    "Content-Type": "application/json"
}

@app.route('/process', methods=['POST'])
def process_input():
    data = request.get_json()
    user_input = data.get("prompt", "")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    print("⏳ Generating UI/UX-enhanced prompt...")
    url_ui_ux = "https://api-lr.agent.ai/v1/action/invoke_llm"
    payload_ui_ux = {
        "llm_engine": "o1-mini",
        "instructions": f"Analyze the user input: '{user_input}' and suggest UI/UX improvements. \
        Provide structured insights on color scheme, layout, responsiveness, accessibility, \
        and interactive elements to make the website visually appealing and user-friendly."
    }
    response_ui_ux = requests.post(url_ui_ux, json=payload_ui_ux, headers=AGENT_API_HEADERS)
    ui_ux_suggestions = response_ui_ux.json().get("response", "").strip()
    
    print("⏳ Generating structured prompt...")
    url_1 = "https://api-lr.agent.ai/v1/action/invoke_llm"
    payload_1 = {
        "llm_engine": "o1-mini",
        "instructions": "Make this user input '"+user_input+ "' into a detailed prompt for AI. \
        The output should guide AI to generate an attractive and user-friendly website. \
        Include UI/UX enhancements: "+ui_ux_suggestions +". Use <img> tags with image URLs from sources\
        like unsplash.com or freepik.com to enhance the website visuals.\
        Ensure HTML, CSS, and JS are in one file."
    }
    response_1 = requests.post(url_1, json=payload_1, headers=AGENT_API_HEADERS)
    structured_prompt = response_1.json().get("response", "").strip()
    
    print("⏳ Generating website code...")
    url_2 = "https://api-lr.agent.ai/v1/action/invoke_llm"
    payload_2 = {"llm_engine": "gemini-2.0-pro-exp-02-05", "instructions": structured_prompt +"   \
                \n\nRemember to Only give the code dont write any explainations." , }
    response_2 = requests.post(url_2, json=payload_2, headers=AGENT_API_HEADERS)
    generated_code = response_2.json().get("response", "").strip()
    generated_code=generated_code[7:-3]
    repo_name = f"generated-site-{int(time.time())}"
    
    def create_repo():
        print("⏳ Creating GitHub repository...")
        url = f"{GITHUB_API_URL}/user/repos"
        data = {"name": repo_name, "private": False, "auto_init": True}
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        response = requests.post(url, json=data, headers=headers)
        print("📌 GitHub API Response Code:", response.status_code)
        print("📌 GitHub API Response:", response.json())
        return response.json()
    
    def upload_file():
        print("⏳ Uploading files to GitHub...")
        url = f"{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{repo_name}/contents/index.html"
        data = {
            "message": "Initial commit",
            "content": base64.b64encode(generated_code.encode()).decode(),
            "branch": "main"
        }
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        response = requests.put(url, json=data, headers=headers)
        return response.json()
    
    def enable_github_pages():
        print("⏳ Enabling GitHub Pages...")
        url = f"{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{repo_name}/pages"
        data = {"source": {"branch": "main", "path": "/"}}
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        response = requests.post(url, json=data, headers=headers)
        return response.json()
    
    repo_response = create_repo()
    if "html_url" not in repo_response:
        return jsonify({"error": "Failed to create GitHub repository"}), 500
    
    upload_response = upload_file()
    if "content" not in upload_response:
        return jsonify({"error": "Failed to upload index.html to GitHub"}), 500
    
    enable_github_pages()
    
    final_url = f"https://{GITHUB_USERNAME}.github.io/{repo_name}/"
    return jsonify({"output": final_url})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
