import subprocess

def get_llm_recommendation(context):
    cmd = ['ollama', 'run', 'llama3']
    prompt = f"""
    You are a recommendation expert. Based on the following context, suggest 3 personalized products:\n\n{context}
    """
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=prompt)
    if stderr:
        print("LLM Error:", stderr)
    return stdout.strip()
