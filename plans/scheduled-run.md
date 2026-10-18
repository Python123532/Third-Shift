# Scheduled Run plan

Follow these steps in order, every scheduled run. Nobody is watching: never stop to ask the user anything. If something is unclear, write the question in the task's Notes, set its Last Status to Needs review, and move on to the next task.

## 1. Find the sheet
Find the 'Task Manager' sheet (see 'The sheet' in SKILL.md). If the scheduled task's prompt gives a sheet ID, use that sheet. Read Tasks and __settings__, plus Standards and Connections if they exist. If the sheet can't be reached, stop. The run's final message says the sheet couldn't be reached.

## 2. Decide which run this is
1. **Check Offline Mode.** Get the current time in the Timezone from __settings__. If it is outside Offline Mode, do no task work: add one Run Reviews row (step 8) saying 'Started outside Offline Mode at (time). Run Times and Offline Mode may not match; check __settings__ and the scheduled tasks.', and make that the final message. Stop.
2. **First or regular.** This is the **first run of Offline Mode** if the scheduled task's prompt says so. If the prompt doesn't say, it's the first run when the current time is within 60 minutes after the first time in Run Times. Every other run is a regular run.

## 3. First run only: close out the previous cycle
Do these before any task work. Keep the lists for the digest in step 9; don't write the digest yet.
1. List tasks that have been Needs review for more than 2 days, tasks In progress whose Last Updated is more than 3 days old, and any task whose Depends On points to a task that is Needs review or Stuck (no waiting period). They go in the digest under 'Stuck'.
2. If a Pending Sync column exists and has entries, list them for the digest. Clear any whose tool is reachable from this run (see plans/connections.md).

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
1. Before starting each milestone, check the time. If less than 60 minutes remain before Offline Mode ends, stop working the queue and go to step 8.
2. Read the task's Standards and its Spec Doc if it has one.
3. **Effort S:** do every milestone. **Effort M:** do only the next unfinished milestone.
4. After a task's work is saved, re-check the queue rules for tasks that depended on it. A task whose Depends On just became all Finished joins the end of its Priority group in this run.

## 6. After every milestone
1. Re-read the task's row. If Last Updated changed since you read it, start from the newer row.
2. Update Milestones (progress line plus steps), Last Status (In progress, or Finished if the last milestone is done), and Last Updated.
3. Add a Log row: Run Type Scheduled, What Was Done, Stopped At.
4. Do any writes the task's Connections call for, or note them in Pending Sync (see plans/connections.md).
5. If the task is now Finished, put the link in Output Link and rate it (SKILL.md, Task rule 6).
6. If the task is a subtask and all its siblings are now Finished, set the parent to Finished and put links to the subtask outputs in the parent's Notes.

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

- **Date:** 'yyyy-mm-dd hh:mm' in the user's timezone.
- **Run:** 'First' or 'Regular'.
- **Claude Rating:** one whole number from 1 to 10 for the run as a whole, judged against the Specs of the tasks worked. Write 'n/a' if nothing was worked.
- **Why That Rating:** the reason for every point below 10.
- **Your Notes:** stays blank for the user.
- If nothing ran, still add the row and say why the queue was empty.
- See plans/examples.md for a filled-in row.

## 9. Final message
- **First run:** write the digest now, as defined under 'TASK digest' in SKILL.md, covering everything since the previous digest, including this run's work. Use the Stuck and Pending Sync lists from step 3, and re-check them against the current sheet. Start it with one line on what this run did.
- **Regular run:** two to four lines on what was done and what's next.
