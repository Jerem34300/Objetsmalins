import os
import openai
from github import Github

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Retrieve environment variables
comment_body = os.getenv("COMMENT_BODY")
issue_number = int(os.getenv("ISSUE_NUMBER"))
repo_name = os.getenv("REPO")

# Generate a reply using OpenAI
prompt = f"Répond de manière courtoise et engageante au commentaire suivant : "{comment_body}""
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=150,
    temperature=0.7,
)
reply = response.choices[0].text.strip()

# Post the reply as a comment on the GitHub issue
gh = Github(os.getenv("GITHUB_TOKEN"))
repo = gh.get_repo(repo_name)
issue = repo.get_issue(issue_number)
issue.create_comment(reply)
