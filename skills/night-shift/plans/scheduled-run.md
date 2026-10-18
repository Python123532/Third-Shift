# Scheduled Run plan

Follow these steps in order. Nobody is watching: never ask the user anything. If something is unclear, write the question in the task's Notes, set Needs review, and move on.

## 1. Quick check (before anything else)
1. Find the sheet (use the ID in the scheduled task's prompt if given). If it can't be reached, stop; the final message says so.
2. Read __settings__. Get the current time in its Timezone.
3. **Outside Offline Mode:** add one Run Reviews row 'Started outside Offline Mode at (time); check Run Times and Offline Mode.' and stop.
4. **First or regular run:** first if the prompt says so, or if the time is within 60 minutes after the first Run Time. Otherwise regular.
5. Read only the queue columns (plans/queue-rules.md) and build the queue. **Regular run with an empty queue:** stop now with a one-line final message. Write nothing.

## 2. Work the queue
For each task in order:
1. Before each milestone, check the time. If less than 60 minutes remain in Offline Mode, go to step 4.
2. Read that task's full row, its Standards rows, and its Spec Doc if any.
3. **Effort S:** every milestone. **Effort M:** only the next unfinished one.
4. When a task finishes, any task waiting on it whose Depends On is now all Finished joins the end of its Priority group in this run.

After every milestone:
1. Re-read the row. If Last Updated changed, start from the newer row.
2. Update Milestones, Last Status (In progress, or Finished after the last milestone), and Last Updated.
3. Add a short Log row (Run Type Scheduled).
4. Do any writes the task's Connections call for, or note them in Pending Sync (plans/connections.md).
5. If Finished: link in Output Link and rate it (SKILL.md, Task rule 6). If it was the last unfinished subtask, finish the parent (Task rule 7).

If something fails (a connector drops, a file is missing, the same call fails twice): save what's done, write in Notes what failed and where, set Needs review, go to the next task. Never retry a failing call more than twice.

## 3. Record the run
Add one Run Reviews row (create the tab with these headers if needed): Date, Run, Tasks Worked, Milestones Done, Output Links, What Met the Spec, Problems or Gaps, Facts to Double-Check, Claude Rating, Why That Rating, Your Notes.
- Date 'yyyy-mm-dd hh:mm'. Run 'First' or 'Regular'. Claude Rating: one whole number 1 to 10 for the run, against the Specs worked, or 'n/a'. Why That Rating: a reason for each point below 10. Your Notes: blank.
- Keep each cell to one or two short lines. Format: plans/examples.md.

## 4. Final message
- **First run:** clear any Pending Sync entries whose tool is reachable now (plans/connections.md), then write the digest (plans/digest.md), starting with one line on what this run did. It goes out as the run's notification.
- **Regular run:** two to four lines on what was done and what's next.
