# Scheduled Run plan

Follow these steps in order, every scheduled run. Nobody is watching: never stop to ask the user anything. If something is unclear, write the question in the task's Notes, set its Last Status to Needs review, and move on to the next task.

## 1. Find the sheet
Find the 'Task Manager' sheet (see 'The sheet' in SKILL.md). Read Tasks and __settings__, plus Standards and Connections if they exist. If the sheet can't be reached, stop. The run's final message says the sheet couldn't be reached.

## 2. Decide which run this is
This is the **first run of Offline Mode** if the scheduled task's prompt says so. If the prompt doesn't say, it's the first run when the current time (in the Timezone from __settings__) is within 60 minutes after the first time in Run Times. Every other run is a regular run.

## 3. First run only: close out the previous cycle
Do these before any task work:
1. List tasks that have been Needs review for more than 2 days, and tasks In progress whose Last Updated is more than 3 days old. They go in the digest under 'Stuck'.
2. If a Pending Sync column exists and has entries, list them for the digest. Clear any whose tool is reachable from this run (see plans/connections.md).
3. Write the digest as defined under 'TASK digest' in SKILL.md, covering everything since the previous digest. It becomes this run's final message.

## 4. Build the queue
Include a task only if:
- its Last Status is Not started or In progress,
- its Runs is Daily queue,
- every task in its Depends On (if that column exists) is Finished, and
- it isn't a parent with subtasks (other rows use its ID plus a letter, such as T-005a). The subtasks run instead.

Set these to Needs review, with a Notes line saying why, and leave them out:
- a task with Spec, Milestones, or Effort empty, or a Spec missing its 'What:' or 'Output:' line,
- a task with Effort L that hasn't been split.

Order the queue by Priority (High, then Med, then Low), then by Due (earliest first, blank last), then by ID.

## 5. Work the queue
For each task in order:
1. Read its Standards and its Spec Doc if it has one.
2. **Effort S:** do every milestone. **Effort M:** do only the next unfinished milestone.
3. Before starting a milestone, check the time. If less than 60 minutes remain before Offline Mode ends, stop working the queue and go to step 7.

## 6. After every milestone
1. Re-read the task's row. If Last Updated changed since you read it, start from the newer row.
2. Update Milestones (progress line plus steps), Last Status (In progress, or Finished if the last milestone is done), and Last Updated.
3. Add a Log row: Run Type Scheduled, What Was Done, Stopped At.
4. Do any writes the task's Connections call for, or note them in Pending Sync (see plans/connections.md).
5. If the task is now Finished, put the link in Output Link and rate it (SKILL.md, Task rule 6).

## 7. If something fails
If a connector drops, a file is missing, or the same tool call fails twice:
1. Save what's done.
2. Write in Notes what failed and at which step.
3. Set Last Status to Needs review.
4. Go to the next task.

Never retry the same failing call more than twice.

## 8. Record the run
Add one row to the Run Reviews tab (create it with these headers if it doesn't exist):

Date, Run, Tasks Worked, Milestones Done, Output Links, What Met the Spec, Problems or Gaps, Facts to Double-Check, Claude Rating, Why That Rating, Your Notes

- **Run:** 'First' or 'Regular'.
- **Your Notes:** stays blank for the user.
- If nothing ran, still add the row and say why the queue was empty.
- See plans/examples.md for a filled-in row.

## 9. Final message
- **First run:** the digest from step 3, plus one line on what this run worked on.
- **Regular run:** two to four lines on what was done and what's next.
