# TASK doctor

A health check. Read only what each check needs, change nothing yet, then show one table: Check, Status (OK or Problem), Fix.

1. **Connectors:** Google Drive and Google Sheets respond.
2. **Sheet:** exactly one 'Task Manager' sheet; Tasks, Log, and __settings__ tabs exist; all 13 core columns are present (header row only). List missing columns and old names that look like a core column (for example 'Objective' for Spec, or a run rule like 'OWN SCHEDULE' written in Notes instead of Runs).
3. **Settings:** Timezone, Offline Mode, and Run Times are filled in, and every Run Time is inside Offline Mode.
4. **Scheduled runs:** if you can list scheduled tasks, check there is one per Run Time, each enabled, each naming this sheet's ID, and the first one has push notifications on. Own schedule tasks have their own scheduled task.
5. **Computer access:** for each Connections row or Own schedule task that needs the user's computer, whether that computer and folder are reachable right now (if this session can check).
6. **Backlog:** count of Pending Sync entries, and tasks Stuck for more than 2 days (plans/digest.md).

Then ask which fixes to make. Make only those. Never delete a row, column, tab, or scheduled task; rename or move things only with a yes. Anything needing the user's hands (re-linking a folder, turning on a notification) goes in the table as a short step for them.
