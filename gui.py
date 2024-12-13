import tkinter as tk
from tkinter import messagebox
from logic import is_valid_user_id, submit_vote, get_vote_counts

# GUI Function to handle vote submission when the button is clicked
def on_vote_button_click(user_id_entry, candidate_var, votes, voted_users, counts_label):
    user_id = user_id_entry.get()
    if not is_valid_user_id(user_id):
        messagebox.showerror("Error", "Invalid User ID! Please enter a valid 6-character alphanumeric ID.")
        return
    
    if candidate_var.get() == 0:
        messagebox.showerror("Error", "Please select a candidate.")
        return

    status, message = submit_vote(user_id, candidate_var.get(), votes, voted_users)
    if status == "Error":
        messagebox.showerror("Error", message)
    else:
        messagebox.showinfo("Success", message)
        # Update vote counts display
        counts_label.config(text=get_vote_counts(votes))

# Function to create the voting interface
def create_voting_interface(root, votes, voted_users):
    # Label for instructions
    instructions_label = tk.Label(root, text="Enter your 6-character User ID and vote for a candidate.", fg="#0000FF")
    instructions_label.pack(pady=10)

    # Entry box for user ID
    user_id_label = tk.Label(root, text="User ID (6 characters):")
    user_id_label.pack()

    user_id_entry = tk.Entry(root, width=30)
    user_id_entry.pack(pady=5)

    # Radio buttons for selecting a candidate
    candidate_var = tk.IntVar()

    candidate_label = tk.Label(root, text="Select Candidate:")
    candidate_label.pack(pady=5)

    candidate1_button = tk.Radiobutton(root, text="John", variable=candidate_var, value=1)
    candidate1_button.pack()

    candidate2_button = tk.Radiobutton(root, text="Jane", variable=candidate_var, value=2)
    candidate2_button.pack()

    # Submit Vote button
    submit_button = tk.Button(root, text="Submit Vote", command=lambda: on_vote_button_click(user_id_entry, candidate_var, votes, voted_users, counts_label), bg="#4CAF50", fg="white")
    submit_button.pack(pady=15)

    # Label to display the vote counts
    counts_label = tk.Label(root, text="John: 0 | Jane: 0 | Total: 0", fg="#0000FF")
    counts_label.pack(pady=10)

    # Exit button
    exit_button = tk.Button(root, text="Exit", command=root.quit, bg="#f44336", fg="white")
    exit_button.pack(pady=10)

    return user_id_entry, candidate_var, counts_label

