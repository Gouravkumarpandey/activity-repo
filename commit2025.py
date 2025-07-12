import os
import random
from datetime import datetime, timedelta

REPO_PATH = r"C:\Personal Project\gitcommit\activity-repo"
os.chdir(REPO_PATH)

# Set the date range: Jan 1, 2025 to Sep 30, 2025
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 9, 30)

# Number of commits per day (shuffled)
commits_per_day = [15, 20, 18, 10]
random.shuffle(commits_per_day)

# Pick random unique days within the date range
total_days = (end_date - start_date).days + 1
selected_day_offsets = random.sample(range(total_days), len(commits_per_day))
selected_days = [start_date + timedelta(days=offset) for offset in selected_day_offsets]

commit_count = 0
for day, num_commits in zip(selected_days, commits_per_day):
    print(f"Creating {num_commits} commits on {day.strftime('%Y-%m-%d')}...")
    for j in range(num_commits):
        # Randomize the time within that day
        random_hour = random.randint(0, 23)
        random_minute = random.randint(0, 59)
        random_second = random.randint(0, 59)
        commit_date = day.replace(hour=random_hour, minute=random_minute, second=random_second)

        with open("activity.txt", "a") as f:
            f.write(f"Commit {commit_count} at {commit_date}\n")
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        os.environ["GIT_AUTHOR_DATE"] = date_str
        os.environ["GIT_COMMITTER_DATE"] = date_str
        os.system("git add .")
        os.system(f'git commit --date="{date_str}" -m "Backdated commit {commit_count}"')
        commit_count += 1

# Clean up env vars
os.environ.pop("GIT_AUTHOR_DATE", None)
os.environ.pop("GIT_COMMITTER_DATE", None)
os.system("git push")
print(f"Done! Created {commit_count} commits (15+20+18+10=63) across 4 random days in Jan-Sep 2025.")
