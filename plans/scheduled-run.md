# Scheduled Run plan

What every scheduled run does. Nobody is watching, so never stop to ask: if something is unclear, write the question in the Log, set the task to Needs review, and move on.

1. **Find the sheet.** Read Tasks, __settings__, and Standards and Connections if they exist. If the sheet can't be reached, stop and say so.

2. **Build the queue.** Take tasks with Last Status Not started or In progress, and Runs set to Daily queue. Then:
   - Skip tasks whose Depends On tasks aren't all Finished.
   - Skip parent tasks that have subtasks. A task has subtasks when other rows use its ID plus a letter (T-005a, T-005b); the subtasks are what run.
   - Set to Needs review, with a Log note saying why, any task missing Objective, Deliverable, Audience & Tone or Milestones, and any Effort L task that hasn't been split.
   - Order by Priority (High, Med, Low), then earliest Due (blank last).

3. **Work the queue** to 'TASK execute' standards: S tasks finish this run, M tasks get at most one milestone. Never start a step that probably won't finish before the user's protected time; stop at the last clean point and save.

4. **After every milestone:**
   - Re-read the task's row and follow the Last Updated rule.
   - Update Milestones, Last Status and Last Updated.
   - Add a Log row (Run Type Scheduled).
   - Do the task's Connections writes, or note them in Pending Sync.

5. **When a task finishes,** rate it as described under 'The sheet' in SKILL.md.

6. **If something fails mid-task** (a connector drops, a file is missing, a tool errors twice): save what's done, write what failed and where in the Log, set the task to Needs review, and move on to the next task. Never retry the same failing call in a loop.

7. **Add one row to Run Reviews** for this run (create the tab if it doesn't exist): Date, Run, Tasks Worked, Milestones Done, Output Links, What Met the Spec, Problems or Gaps, Facts to Double-Check, Claude Rating, Why That Rating, Your Notes (left blank for the user). Add it even if nothing ran, and say why the queue was empty.

8. **If this is the last run of the day, end with 'TASK digest'.** It's the last run if the scheduled task's prompt says so. If the prompt doesn't say, compare the current time with the run times in __settings__: if no other run is scheduled before the user's protected time starts, it's the last run.
