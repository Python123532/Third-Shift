<img src="assets/icon.png" width="96" alt="Night Shift icon: a pixel crescent moon with drifting z's over a night sea">

# Night Shift: a task queue for Claude

Hand Claude work, and it gets done while you're offline. Night Shift keeps your tasks in a Google Sheet that every chat can see. Claude works through them on a schedule you pick, saves after every step, rates its own work honestly, and you review the results when you're back.

It starts small on purpose. Your schedule, what "good work" means to you, and which of your tools it uses are all set up by asking you, and saved in your sheet.

## Light on tokens

It only loads the instructions a command needs, reads only the sheet columns it needs, and a scheduled run with nothing to do stops after one small check. The cost that's left is the actual work on your tasks.

## Where it works well

- **Work you don't want to babysit.** Research write-ups, document cleanups, study guides, event plans, code upkeep: anything that can be broken into steps. Claude saves after each step and picks up where it left off on the next run.
- **Work spread across chats and devices.** Add a task from your phone, check it from your laptop. The sheet is the one place everything lives.
- **An honest feedback loop.** Claude rates its work 1–10 against what you asked for and says what to specify better next time. You add your own rating, and the gap tells you how far to trust its self-ratings.

Not great for: anything that needs a person to click "send" or "buy" (it drafts those and waits for you), or quick one-off questions (just ask Claude normally).

## What you need

- A Claude plan that includes skills and scheduled tasks.
- The **Google Drive** and **Google Sheets** connectors, turned on in **Settings > Connectors**.

## Install

**In the Claude app (most people):**
1. Download [`dist/night-shift.zip`](dist/night-shift.zip) from this repo.
2. In Claude, go to **Settings > Skills**, choose **Upload a skill**, and upload the zip.

**In Claude Code:** run `/plugin install night-shift --marketplace Python123532/claude-task-manager`. This adds a `/night-shift:task` slash command and a reviewer for second opinions.

Use one or the other, not both.

## Get started

1. Open a new chat and type `TASK setup`.
2. Claude shows you exactly what it will access (table below) and asks before creating anything.
3. It makes a Google Sheet called **Task Manager**, asks when you're usually offline, and sets up the scheduled runs (one a day by default).
4. Make sure push notifications are on for the first run of the day (setup turns them on; you can check in your scheduled tasks). That run ends by sending you a digest: what finished, what needs you, and what's stuck.
5. Add your first task: `TASK create (what you want done)`.

## What it can access

| Access | Used for |
|---|---|
| Google Sheets | One sheet named "Task Manager". No other sheets. |
| Google Drive | Creates that sheet and a "Task Manager" folder, and saves finished work there. Reads the **titles** of your 20 most recent files only if you say yes during setup. |
| Scheduled tasks | Runs at the times you pick, while you're offline. |
| Memory | Only if you say yes: suggests a setup from what Claude already knows about you. |

Runs never send messages, submit forms, buy anything, post publicly, or delete anything. They draft it and wait for you. Other tools (a notes app, a code repo, folders on your computer) are added only when you ask, and Claude tells you exactly what it would read and write first.

Your sheet and tasks are yours alone. Nothing is shared with anyone else who uses Night Shift.

## Commands

Type these at the start of a message. Anything in parentheses is yours to fill in. You can also just ask in plain words.

| Command | What it does |
|---|---|
| `TASK setup` | Makes your sheet, asks your schedule, sets up the runs. Run it again to change any of it. |
| `TASK create (what)` | Builds a new task with you until it's clear enough to run without you. |
| `TASK execute (id)` | Does a task right now instead of waiting for a run. |
| `TASK status` | Every task and where it stands. Add a tag or task ID to narrow it. |
| `TASK queue` | What the next run will work on, in order. |
| `TASK review` | A table of finished work to rate. Reply like `T-001 9, T-002 7`, or `skip`. With an ID: rate one task, then approve it or send it back. Add `check` after an ID for an independent second rating. |
| `TASK edit (id) (change)` | Change anything: due date, priority, tag, pause, resume, delete, archive. |
| `TASK split (id)` | Break a big task into smaller ones, in order. |
| `TASK digest` | What finished, what's in progress, what needs you, what's stuck. |
| `TASK help` | This list. |

## The sheet

It starts with three tabs: **Tasks**, **Log** (every piece of work done), and **__settings__** (your timezone, offline hours, and run times). Other tabs appear only when needed:

- **Standards**: what good work looks like for each kind of task. A researcher might want vetted sources; an artist might want three thumbnails before refining. Claude asks the first time a tag has none.
- **Connections**: the tools you've connected and what each is for.
- **Run Reviews**: one row per scheduled run, used for the digest.
- **Archive**: finished tasks you've archived.

Add your own columns or tabs any time. Claude finds columns by name, so nothing breaks, and it never removes anything you added.

## If something comes up

- **A run hit something unclear.** It doesn't guess. The task goes to *Needs review* with the question in its Notes, and it shows up in your digest.
- **A task needs an email sent or a form submitted.** Runs draft it and wait for you.
- **A task needs your computer and it was off.** The work is noted and done the next time your computer is reachable. Claude asks you once how you'd like that handled.
- **A task's files only exist inside one chat.** Scheduled runs start fresh and can't see them. Put the files in Google Drive or a connected tool.
- **The ratings seem too generous.** Compare Claude's numbers with yours over a few tasks, and tell it in `TASK review`.

## What's in this repo

| Path | What it is |
|---|---|
| `dist/night-shift.zip` | The skill, ready to upload in Settings > Skills |
| `dist/night-shift-plugin.zip` | The full plugin, ready to upload as a plugin |
| `skills/night-shift/` | The skill's source: `SKILL.md` plus `plans/`, which load only when needed |
| `commands/`, `agents/`, `.claude-plugin/` | The plugin: the slash command, the reviewer, and manifests |
| `assets/`, `scripts/` | The icon and social card, and the scripts that draw them and build the zip |

## License

MIT. Use it, change it, share it. See [LICENSE](LICENSE).
