import os
import random
import datetime

# 🔹 Change this to your AI-Prompt-Engineer repository path
REPO_PATH = os.path.expanduser("/Users/allan/Downloads/drstone-genius04")  # Update if needed

# 🔹 Number of commits to generate
NUM_COMMITS = random.randint(100, 250)  # Random between 100-250 commits

# 🔹 Your GitHub username & email
GIT_USERNAME = "drstone-genius04"
GIT_EMAIL = "kingallan.10@gmail.com"

# 🔹 AI-Prompt-Engineer Specific Commit Messages
COMMIT_MESSAGES = [
    "Testing new prompt strategies",
    "Optimized GPT prompt formatting",
    "Updated README with prompt engineering guidelines",
    "Enhanced system prompt clarity",
    "Added temperature & max token adjustments",
    "Improved prompt chaining for coherent responses",
    "Refactored prompt generation function",
    "Fixed token limit issues in long prompts",
    "Implemented few-shot examples for better AI context",
    "Updated dataset with more diverse prompts",
    "Tested new prompting strategies",
    "Added regex filtering for cleaner inputs",
    "Optimized function for efficient prompt generation",
    "Enhanced zero-shot prompt effectiveness",
    "Updated example outputs for different LLM models",
    "Improved AI reasoning prompts",
    "Added interactive prompt testing module",
    "Fixed API call issues in prompt execution",
    "Documented best practices for prompt engineering",
    "Refactored user input validation in prompts",
]

# Function to create and push commits
def make_commit(commit_date, commit_message):
    os.chdir(REPO_PATH)  # Move to repo folder

    # Create or update a dummy file
    with open("commit_log.txt", "a") as file:
        file.write(f"{commit_date}: {commit_message}\n")

    # Add changes to Git
    os.system("git add .")
    os.system(f'GIT_AUTHOR_DATE="{commit_date}" GIT_COMMITTER_DATE="{commit_date}" git commit -m "{commit_message}"')

# Set Git username and email
os.system(f'git config user.name "{GIT_USERNAME}"')
os.system(f'git config user.email "{GIT_EMAIL}"')

# Get the current branch name
branch_name = os.popen("git rev-parse --abbrev-ref HEAD").read().strip()

# Generate commits spread randomly across the year
start_date = datetime.datetime.now() - datetime.timedelta(days=365)
for _ in range(NUM_COMMITS):
    random_days = random.randint(1, 365)  # Choose a random day in the past year
    random_time = datetime.timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
    commit_date = start_date + datetime.timedelta(days=random_days) + random_time
    commit_message = random.choice(COMMIT_MESSAGES)  # Choose a random commit message

    make_commit(commit_date.strftime("%Y-%m-%dT%H:%M:%S"), commit_message)

# Push all commits to GitHub
os.system(f"git push origin {branch_name}")