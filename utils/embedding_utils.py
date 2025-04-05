import subprocess
import json

def generate_embedding(text):
    # Replace 'mxbai-embed-large' with your Ollama embedding model
    cmd = ['ollama', 'run', 'mxbai-embed-large']
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=text)
    if stderr:
        print("Embedding Error:", stderr)
    try:
        output = json.loads(stdout)
        return output["embedding"]
    except Exception:
        return None
