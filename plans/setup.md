# Setup plan

Run by 'TASK setup'. Re-running it lets the user change any answer. Use clickable multiple-choice questions where possible, at most 4 questions per card.

## 1. Find or create the sheet
Search the user's Drive for a spreadsheet named exactly 'Task Manager' that they own. Use an exact-title search (title equals 'Task Manager'), not a 'contains' search, which also matches files like 'Task Manager TEST' or 'Task Manager (old)'. If more than one exact match exists, ask which one.

- **If it exists:** use it. Don't change existing columns.
- **If it doesn't:** create it with the three core tabs and the exact columns from SKILL.md ('The sheet'):
  - dropdowns on Last Status, Priority, Effort, and Runs,
  - the header row frozen,
  - the first two columns (ID, Name) frozen.

## 2. Ask permission to learn from what the user already does
Ask this exact question as the question text of a choice card, with the answers 'Yes', 'No', and 'Tell me more':

> To tailor this to you, I can look at the titles of your 20 most recent Google Drive files and what I already remember about you. I'll only read titles, not the files themselves, and I won't save anything from them except a short summary of how you work (5 lines or fewer) that you can see and edit in your sheet. Is that OK?

- **Tell me more:** explain in two sentences what is read, what is saved, and where (the Profile row in __settings__). Then ask again.
- **No:** skip to step 4 and instead ask two questions:
  1. What kind of work do you mostly hand off? (research, writing, code, design, admin, other)
  2. What do you usually do with the results? (read once, edit and send, turn into slides or docs, other)

## 3. Learn and suggest (only if they said Yes)
1. Read the titles of the 20 most recent Drive files, plus whatever is already known about the user from memory. Read no file contents. Leave out the 'Task Manager' sheet, anything in the 'Task Manager' folder, and anything else this skill made (such as '(ID) (Name) spec' docs), and take the 20 most recent of what's left. Those show the skill, not the user.
2. Write a summary of how they work, 5 lines or fewer. Put the full summary inside the question text of a choice card ('Here's how you seem to work: (summary). Save it?'), with the answers 'Yes, save it', 'Change something', and 'Don't save it'. Don't show it outside the card. On 'Yes', save it to a Profile row in __settings__. On 'Change something', ask what to change, then show it again the same way.
3. Suggest **up to 3** ways the skill could fit what they do. Examples: a starting Standard for a tag they clearly use, an output format they produce often, a workflow such as turning a finished task's notes into a doc. Show them as a checklist card, with each suggestion's full wording in its answer text. Save only what they pick: Standards as Standards rows, anything else as a __settings__ row in their words.

## 4. Ask the schedule
Ask, then save each answer to __settings__ under these exact names:
1. **Timezone:** offer the one their device or memory suggests, plus 'other'.
2. **Offline Mode:** when are they usually not using Claude? Save as 'h:mm AM - h:mm PM'.
3. **Run Times:** how many runs a day (1, 2, or 3), and at what times inside Offline Mode? Suggest times 1 to 15 minutes before the hour (such as 2:58 AM), since on-the-hour runs can be delayed. Save comma-separated in time order. Every Run Time must be inside Offline Mode; if one isn't, say so and ask again.

## 5. Create the scheduled runs
Offer to create one scheduled task per Run Time. Each task's prompt follows this template:

> Scheduled run of the user's Night Shift task queue ((First run of Offline Mode | Regular run)). Nobody is watching. Load the night-shift skill and follow plans/scheduled-run.md exactly. The sheet is the Google Sheet 'Task Manager', ID (sheet ID). If the night-shift skill isn't available in this session, add one row to the Run Reviews tab saying so, then stop.

- Mark the first Run Time's task as 'First run of Offline Mode' and turn on its push notification, so the digest reaches the user.
- Mark the others 'Regular run'.

## 6. Close
Tell the user, in four lines or fewer:
- what was set up,
- that Standards and tool connections get set up the first time they come up,
- that anything can be changed by asking,
- and suggest 'TASK create' to add the first task.
