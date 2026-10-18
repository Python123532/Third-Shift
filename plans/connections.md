# Connections plan

Read this when a task could use one of the user's other tools (a notes app, a code repo, a cloud folder, anything in Claude's connector list, or a folder on their computer), or when the user mentions one.

## 1. Ask before using a tool
The first time a tool comes up, ask the user, with clickable choices where possible:
1. What should Claude read from it? (nothing, context for tasks, specific files or pages)
2. What should Claude write to it? (nothing, a note per task, a log line after each run, the finished output, other)
3. For which tags?

Save the answer as a row in a Connections tab (create it if it doesn't exist) with these columns:
- **Tool**
- **Where:** a folder path, page, repo, or Drive folder
- **Purpose:** what to read and write, in the user's words
- **Tags**
- **Reachable From:** Cloud if it's a connector, Computer if it's only on the user's machine

Follow that row from then on. Work out how to use the tool from the tool itself. There's no fixed method for any app.

## 2. Tools on the user's computer
These work only when the chat or run is linked to the user's computer and it's awake with the Claude desktop app open.

If a write to one can't happen now:
1. Don't skip it, and don't fail the task.
2. Add a Pending Sync column to Tasks if it doesn't exist.
3. Write the pending write in that task's cell, for example 'Notes app: task note'.

The first time a pending write happens, ask the user how they'd like pending writes cleared, and save the answer as a Pending Sync row in __settings__:
- **Daily check:** their computer is always on. Create a small daily scheduled task that requires their computer, set inside Offline Mode after the last Run Time. It reads only the Pending Sync column, stops right away if it's empty, and otherwise does the writes and clears them.
- **Next linked chat:** clear pending writes at the start of the next TASK command in a chat linked to their computer.
- **Cloud copy:** their folder is also synced to a cloud place Claude can reach (such as a GitHub repo or a Drive folder). Write to the cloud copy instead, so nothing is pending.

## 3. Conflicts
If the same task detail was changed both in the sheet and in a connected tool, ask the user once which should win and save the answer as a Tiebreak row in __settings__:
- **Newest edit wins:** use the later change, and write what was overwritten in the Log so it can be restored from version history.
- **Sheet wins:** changes to Last Status, Priority, Effort, Milestones, or Ratings made outside the sheet are shown to the user in 'TASK review' instead of applied.

## 4. Never
- Never delete a file, note, page, or anything else in a connected tool.
- Unattended runs follow SKILL.md 'Safety' in every tool.
