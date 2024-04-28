# M.A.I.A - An Open Source LLM Agent with Internet Access and Code Execution

![Showcase](./assets/showcase.gif)

## Introduction
M.A.I.A. (short for **M**aster **A**rtificial **I**ntelligence **A**ssistant) is an open-source conversational AI project inspired by ChatGPT-4. 

M.A.I.A. is designed to be a highly advanced language model that can understand and respond to human input in a conversational manner. What sets M.A.I.A. apart from normal large language models is its ability to access the internet and execute code, making it a powerful tool for a wide range of applications.

## Features
👥 - **Conversational AI:** Since M.A.I.A. is powered by Llama-3 you can have normal conversations with it like you have them with regular LLMs.

🌍 - **Internet Access:** M.A.I.A. can use the Google Search tool to retrieve up-to-date information from the internet. 

🖥️ - **Code Execution:** Since I love the ChatGPT Code Interpreter I implemented it for M.A.I.A. Now it is able to solve match problems, visualize data and test your code. You can also read, write, create and delete files on your machine since M.A.I.A. is able to execute not only Python but also Bash code.

🔍 - **Network Scanning:** M.A.I.A. also includes the Nmap tool for network scanning. You can use it to discover hosts and services on a computer network, thus providing additional functionality for security and network administration.

🔐 - **SQL Injection Testing:** SQLMap can be used as well. It's a tool for automated SQL injection testing. You can use it to detect and exploit SQL injection vulnerabilities in web applications, providing an additional layer of security testing.

🔍 - **Directory and Subdomain Bruteforcing:** M.A.I.A. is able to use the ffuf tool for directory and subdomain bruteforcing. You can use it to discover hidden files and directories on a web server, as well as subdomains of a target domain, providing additional functionality for web application testing and reconnaissance.

## Getting Started
To get started with M.A.I.A., follow these steps:

1. Clone the repostiory
```bash
git clone https://github.com/nnxmms/M.A.I.A.git
```

2. Change directory to the downloaded repository
```bash
cd M.A.I.A
```

3. Create a virtual environment
```bash
virtualenv -p python3.11 env
```

4. Activate the environment
```bash
source ./env/bin/activate
```

5. Install requirements
```bash
pip install -r requirements.txt
```

6. Register at [Groq](https://groq.com/) to obtain a `GROQ_API_KEY`

7. Create a [programmable search engine](https://programmablesearchengine.google.com/) to get a `GOOGLE_CSE_ID` and `GOOGLE_API_KEY`

8. Create a `.env` file and update the values
```bash
cp .env.example .env
```

## Usage
Now you can run M.A.I.A. with the following command
```bash
python3 main.py
```

> [!WARNING]  
> M.A.I.A. does not ask for permission when executing code on your machine. Make sure you know what you do!

### Usecases
☀️ - What is the weather like in Berlin?

🧭 - Check if twitter.com is up.

🖥️ - Do you see any .txt files on my desktop?

🎥 - Convert the showcase.mov video into a .mp4

🇺🇸 - Write a poem about the current president of the USA and save it in a file in my Downloads folder.

## Tools
M.A.I.A. can use a variaty of tools. Currently the following tools are implemented:

| Tool          | Description                                |
|---            |---                                         |
| Bash          | Executes any bash command.                 |
| Google Search | Search the internet using Google.          |
| Interpreter   | Executes any Python script.                |
| Nmap          | Network scanning tool.                     |
| SQLMap        | Automated SQL injection testing.           |
| ffuf          | Directory and subdomain bruteforcing tool. |

You can easily add new tools using the [Tool](tools/__init__.py) class. Take some of the already existing tools as a guide.

You can enable and disable tools in the [main.py](main.py) file by including or removing them in the `Initialize tools` section.

