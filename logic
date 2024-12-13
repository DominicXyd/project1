import re
import time

# File to store votes
VOTE_FILE = "votes.txt"

# Function to validate user ID (should be alphanumeric and of length 6)
def is_valid_user_id(user_id):
    return bool(re.match(r'^[a-zA-Z0-9]{6}$', user_id))

# Function to submit a vote
def submit_vote(user_id, candidate, votes, voted_users):
    # Check if user has already voted
    if user_id in voted_users:
        return "Error", f"User ID {user_id} has already voted!"
    
    # Add user to the set of voted users
    voted_users.add(user_id)

    # Increment the candidate's vote
    if candidate == 1:
        votes["John"] += 1
        message = "Voted for John!"
    elif candidate == 2:
        votes["Jane"] += 1
        message = "Voted for Jane!"

    # Save vote to file with user ID and timestamp
    with open(VOTE_FILE, "a") as f:
        f.write(f"{user_id},{candidate},{time.ctime()}\n")

    return "Success", message

# Function to display vote counts
def get_vote_counts(votes):
    total_votes = votes["John"] + votes["Jane"]
    return f"John: {votes['John']} | Jane: {votes['Jane']} | Total: {total_votes}"

