# Autonomous Website Generator

## Description
This project is an autonomous website generator that processes user input, enhances UI/UX, generates website code, and deploys it to GitHub Pages automatically.

## Features
- Accepts user input to generate a website
- Enhances UI/UX automatically
- Creates a GitHub repository
- Uploads the generated website to GitHub
- Enables GitHub Pages for easy access

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/vipreshgupta/4O4_krackhack.git
cd 4O4_krackhack
```

### 2. Install Dependencies
Ensure you have Python installed, then run:
```sh
pip install -r requirements.txt
```

### 3. Set Up API Keys
This project requires API keys stored in a `.env` file.

1. Create a file named `sensitive.env` in the project directory.
2. Add your API keys inside it as follows:
   ```sh
   GITHUB_TOKEN=your_github_personal_access_token
   AGENT_API_KEY=your_agent_api_key
   ```
3. **How to Generate a GitHub API Key:**
   - Go to your **GitHub Profile** → **Settings**
   - Navigate to **Developer Settings** → **Personal Access Tokens** → **Token (classic)**
   - Click on **Generate New Token** → **Generate New Token (classic)**
   - From the checkboxes, select:
     - `admin:org`
     - `admin:public_key`
     - `repo`
     - `workflow`
   - Click **Generate Token**, copy it, and paste it in the `sensitive.env` file under `GITHUB_TOKEN`.

4. **How to Generate an API Key for `AGENT_API_KEY`:**
   - Go to [agent.ai](https://agent.ai) and create an account.
   - In the top-right corner, click on your profile.
   - Navigate to **Settings** → **Credits Tab**.
   - Scroll down until you find your API key.
   - Copy it and paste it in the `sensitive.env` file under `AGENT_API_KEY`.

⚠️ **Important:** Never share this file or push it to GitHub.

### 4. Run the Project
Since the project requires running `main.py` first, then `BackendConnection.py`, follow these steps:

#### **For Windows**
```sh
python main.py
python BackendConnection.py
```

#### **For Linux/Mac**
```sh
python3 main.py
python3 BackendConnection.py
```

Alternatively, create and use a script:

- **Windows:** Create `run.bat` with the following content and double-click it:
  ```bat
  @echo off
  python main.py
  python BackendConnection.py
  pause
  ```
- **Linux/Mac:** Create `run.sh` with the following content:
  ```sh
  #!/bin/bash
  python3 main.py
  python3 BackendConnection.py
  ```
  Then give it execution permission:
  ```sh
  chmod +x run.sh
  ```
  Run it with:
  ```sh
  ./run.sh
  ```

### 5. Open the Frontend
Once the backend scripts are running, open `index.html` in a web browser to access the website.

## File Structure
```
/MyProject
  ├── main.py                 # Core logic to generate GitHub-based websites
  ├── BackendConnection.py     # API endpoint to interact with main.py
  ├── sensitive.env            # API keys (not included in GitHub)
  ├── requirements.txt         # Dependencies list
  ├── .gitignore               # Ignores sensitive files
  ├── README.md                # Instructions for running the project
```

## Notes
- If you encounter issues with API keys, ensure `sensitive.env` is correctly formatted.
- If you modify the code, make sure to restart the scripts.
- Never push `sensitive.env` to GitHub.

## License
This project is licensed under the **MIT License**.

### MIT License
```
MIT License

Copyright (c) 2025 Vipresh Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

