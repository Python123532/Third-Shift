# TASK review (ID, optional)

Ratings are always asked in plain words, never with a choice card. Replies to a digest ('approve T-005a', 'T-005a: change the intro', 'T-001 8') follow these same rules, as if they'd typed the matching TASK review.

- **No ID:** read only ID, Name, Last Status, Output Link, Ratings, and Notes. Show every task whose Ratings has 'You -' (Finished tasks and repeating tasks; not parents) as one table in a reply: Task (ID and Name), Output (clickable link), Claude (number), Why not higher (one line from Notes). Ask for a reply like 'T-001 9, T-002a 6', with an optional note after any number, or 'skip'.
  - **A number:** write it as the 'You' number. A note goes in Notes as a line starting 'You:'.
  - **skip** (one task or all): write 'You skip'. This command and the digest stop asking about it; 'TASK review (ID)' can still rate it.
  - **Nothing to rate:** say so in one line.
- **With an ID:** show its output link, Ratings, and Notes in a reply, and ask for their 1 to 10. Write it as the 'You' number. Then ask: approve, or send back with notes?
  - **Approve:** stays Finished.
  - **Send back:** add their notes as a new last milestone, set In progress, clear the 'You' number.
- **'TASK review (ID) check':** an independent second rating. If a Third Shift reviewer agent is available, give it the sheet ID and task ID. If not, review it yourself, reading only Spec, Spec Doc, Standards, and the output (not Ratings, Notes, or Log). Show the result beside Claude's rating and add 'Check: N/10' to Notes. Don't change Ratings.
- **A task in Needs review waiting on an answer:** save their answer in Notes and set In progress (or Not started if no milestone is done) so the next run picks it up.
