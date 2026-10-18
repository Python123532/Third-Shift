# Setup plan

The first-run interview, run by 'TASK setup'. Re-running it lets the user change anything here.

Use clickable multiple-choice questions where possible (at most 4 per card). Ask only what the core needs; standards and tool connections get set up later, the first time they come up.

1. **Find or create the sheet.** Search the user's Drive for a spreadsheet called 'Task Manager' that they own. If there isn't one, create it with the core tabs and columns from SKILL.md: dropdowns for Priority, Effort, Last Status and Runs, and 1-10 limits on the two rating columns.

2. **Ask the schedule:**
   - their timezone,
   - when they're busy (when runs may happen),
   - when they use Claude themselves (protected time),
   - what times they'd like the runs.
   Save the answers in __settings__.

3. **Offer to create the scheduled runs.** Each scheduled task's prompt tells Claude to load this skill, follow the Scheduled Run plan, and says whether it's the day's last run. Include the sheet's ID and a fallback: if the skill isn't available, add one Run Reviews row saying so and stop.

4. **Close** with a short summary of what was set up, and say that standards and tool connections get set up as they come up and that anything can be changed by just asking.
