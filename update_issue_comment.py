import os
import re
from github import Github

# Set your GitHub token here
github_token = os.getenv("GH_TOKEN")
g = Github(github_token)
repo = g.get_repo("Osiris-Team/Osiris-Team")
issue = repo.get_issue(number=4)

issue_body = issue.body
session_start = "<!--WORK_SESSIONS_START-->"
session_end = "<!--WORK_SESSIONS_END-->"
total_start = "<!--WORK_SESSIONS_TOTAL_START-->"
total_end = "<!--WORK_SESSIONS_TOTAL_END-->"

print("Issue Body:")
print(issue_body)

sessions_match = re.search(f"{session_start}(.*?){session_end}", issue_body, re.DOTALL)
if sessions_match:
    sessions_content = sessions_match.group(1)
    total_minutes = sum(map(int, re.findall(r"Took.*\((\d+)\s*min\)", sessions_content)))

    print("Sessions Content:")
    print(sessions_content)

    print("Total Minutes:")
    print(total_minutes)

    updated_total_content = f"{total_start}\nTotal work time: {total_minutes} min\n{total_end}"

    updated_issue_body = re.sub(f"{total_start}(.*?){total_end}", f"{updated_total_content}", issue_body, flags=re.DOTALL)

    print("Updated Issue Body:")
    print(updated_issue_body)

    issue.edit(body=updated_issue_body)
else:
    print("Sessions content not found.")
