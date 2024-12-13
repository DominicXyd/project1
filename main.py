import tkinter as tk
from gui import create_voting_interface
from logic import get_vote_counts

# Initialize the Tkinter root window
root = tk.Tk()
root.title("Voting System")

# Initialize variables to store votes and users who have voted
votes = {"John": 0, "Jane": 0}
voted_users = set()

# Create the voting interface
user_id_entry, candidate_var, counts_label = create_voting_interface(root, votes, voted_users)

# Initialize the display with the current vote counts
counts_label.config(text=get_vote_counts(votes))

# Main loop for the Tkinter GUI
root.mainloop()

