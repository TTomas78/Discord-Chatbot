# Conversational bot with ChatGPT

How to run the project:

Install virtualenv

```bash
  pip install virtualenv
```

Create a new virtual environment 

```bash
  virtualenv venv
```

Activate the virtual environment

(Windows)
```bash
./venv/Script/Activate
```

(Linux)
```bash
./venv/bin/activate
```


Install dependencies

```bash
pip install -m requirements.txt
```

Create a .env with the following information on your root directory

```bash
[DEFAULT]
DISCORD_TOKEN=
PINECONE_API_KEY=
PINECONE_ENV=
OPENAI_API_KEY=
ALLOWED_USERS=
TARGET_USER=
LOG_FOLDER=
LOG_FILE=
TIME_TO_ANSWER=
```

Run the app

```bash
python main.py 
```
