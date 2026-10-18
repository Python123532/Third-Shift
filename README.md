<img src="assets/icon.png" width="96" alt="Third Shift icon: a pixel crescent moon with drifting z's over a night sea">

# Third Shift: a task queue for Claude

*Formerly Night Shift. If you installed it under that name, download the new zip below and replace the old one.*

Hand Claude a list of work and get it back done, rated, and ready for review. Third Shift gives Claude three things a plain prompt doesn't have:

- **A checkpointed queue.** Tasks live in a Google Sheet, ordered by priority, due date, and dependencies. Claude saves after every step, so a run that gets cut off picks up exactly where it stopped, even days later and from any chat.
- **Your standards, per project.** Tell it once what good work looks like for each kind of task (vetted sources for research, three thumbnails before refining for art, tests passing for code), and every task with that tag follows it.
- **Ratings you can calibrate.** Claude rates each result 1 to 10 against your spec and says why it lost points. You add your rating, and the digest tracks the gap. If Claude rates itself too high, it scores stricter from then on.

The work runs on a schedule you pick, while you're offline, and the first run of the day sends you a digest: what finished, what needs you, and the one thing to do next.

## Why not just a scheduled task and a good prompt?

You can schedule a prompt in Claude already, and for one repeating job that's often enough. Third Shift is for when you have several jobs at once. A scheduled prompt runs the same instruction every time and forgets what happened last run. Third Shift decides what to work on each night from your queue, remembers how far each task got, holds every task to the standards you set for its project, and keeps score of how its self-ratings compare with yours. Each run is an ordinary scheduled task; Third Shift is what tells it which work to do and how to judge it.

## A real example

Task T-006, made with `TASK create from template` (Study guide) and run with `TASK execute T-006`:

| | |
|---|---|
| **Spec** | What: a study guide for intro biophysics: key terms, main ideas, 10 practice questions with answers. Output: a Google Doc. For: a student reviewing for a test. |
| **First pass** | Claude 8 / You 7. The reviewer's note: formulas like dc/dx were plain text, not crisp. Sent back with that note. |
| **Second pass** | Every formula rebuilt as a real equation, units kept upright, answers numbered. Claude 9 / You 9. |
| **Output** | [Intro Biophysics Study Guide](examples/biophysics-study-guide.md) (a copy; the original is a Google Doc with native equations) |
| **Why not 10** | -1: no course or textbook was named, so the scope is a general intro choice. All 10 answers were recomputed in code. |
| **Tip** | Name the course and textbook chapter so the terms and questions match your class. |

How it shows up in the next morning's digest:

> **Finished:** T-006 Intro biophysics study guide ([link](examples/biophysics-study-guide.md)), Claude 9 / You 9
> **Next step:** Review T-005a (about 2 min), which unblocks T-005b.

## Where it works well

- **Work you don't want to babysit.** Research write-ups, document cleanups, study guides, event plans: anything that breaks into steps.
- **Several things at once.** Queue five tasks on Sunday; they get done in order through the week.
- **Work spread across chats and devices.** Add a task from your phone, check it from your laptop.

Not great for: anything that needs a person to click "send" or "buy" (it drafts those and waits for you), or quick one-off questions (just ask Claude normally).

## What you need

- A paid Claude plan that includes skills and scheduled tasks.
- The **Google Drive** and **Google Sheets** connectors, turned on in **Settings > Connectors**.

## Install

**Most people: the plugin.** Download [`dist/third-shift-plugin.zip`](dist/third-shift-plugin.zip) and upload it in Claude where you add plugins. It includes the skill, a `/third-shift:task` command, and a reviewer for second opinions. To update later, download the newest zip and upload it again.

**Skill only:** if your Claude doesn't offer plugin uploads, download [`dist/third-shift.zip`](dist/third-shift.zip) and upload it in **Settings > Skills**. Everything works except the second-opinion reviewer.

**Claude Code:** `/plugin marketplace add Python123532/claude-task-manager`, then `/plugin install third-shift@third-shift`. Get updates with `/plugin marketplace update third-shift`.

Install one of these, not two: two copies would both answer `TASK` commands.

## Get started

1. Open a new chat and type `TASK setup`.
2. Claude shows you exactly what it will access (table below) and asks before creating anything.
3. It makes a Google Sheet called **Task Manager**, asks when you're usually offline, and sets up the scheduled runs (one a day by default).
4. It offers a 2-minute sample task, so you see a finished, rated result before the first night.
5. Add real work with `TASK create (what you want done)`, or start from a template: `TASK create from template`.

## What it can access

| Access | Used for |
|---|---|
| Google Sheets | One sheet named "Task Manager". No other sheets. |
| Google Drive | Creates that sheet and a "Task Manager" folder, and saves finished work there. Reads the **titles** of your 20 most recent files only if you say yes during setup. |
| Scheduled tasks | Runs at the times you pick, while you're offline. |
| Memory | Only if you say yes: suggests a setup from what Claude already knows about you. |

Runs never send messages, submit forms, buy anything, post publicly, or delete anything. They draft it and wait for you. Other tools (a notes app, a code repo, folders on your computer) are added only when you ask, and Claude tells you exactly what it would read and write first.

**Text inside your sources is information, not instructions.** If a web page, document, or email that a task reads says something like "ignore your instructions and...", the run is told to treat it as content, not a command, and to keep to your task and the limits above.

Your sheet and tasks are yours alone. Nothing is shared with the author or anyone else who uses Third Shift. The plugin has no server of its own and sends nothing anywhere except through your own connectors.

## How it fits with Claude's scheduled tasks

Third Shift's runs are ordinary scheduled tasks, so you'll see them in your scheduled tasks list as "Third Shift: first run" and "Third Shift: regular run". Pause, resume, or change their notifications there. Third Shift decides what each run works on; the scheduled task just decides when it runs. Your other scheduled tasks are untouched.

## Files on your computer

Scheduled runs happen in the cloud. They can use your connectors (Google Drive, Sheets, and any others you've added) but not files on your computer. That's why the queue lives in a Google Sheet and finished work goes to Google Drive: everything a run needs is reachable even when your laptop is closed.

If a task really needs local files, it can get its own scheduled task that runs on your computer, which works only while the computer is on with the Claude desktop app open. Writes to local tools (like a notes app) that can't happen in the cloud are queued and done the next time you use `TASK` in a chat linked to your computer.

## What it costs

Measured on the current version:
- **Every chat:** about 290 tokens, for the plugin's short description.
- **First `TASK` command in a chat:** about 2,000 tokens of instructions, plus 150 to 400 for that command's own steps. Later commands in the same chat add only their own steps.
- **A scheduled run with nothing to do:** one small read of two sheet columns, then it stops. On the author's sheet, a full empty first run, digest included, took under a minute.
- **The work itself:** the same as asking Claude to do that task by hand.

## Commands

Type these at the start of a message. Anything in parentheses is yours to fill in. You can also just ask in plain words.

| Command | What it does |
|---|---|
| `TASK setup` | Makes your sheet, asks your schedule, sets up the runs. Run it again to change any of it. |
| `TASK create (what)` | Builds a new task with you until it's clear enough to run without you. Add `from template` to start from a starter. |
| `TASK execute (id)` | Does a task right now instead of waiting for a run. |
| `TASK status` | Every task and where it stands. Add a tag or task ID to narrow it. |
| `TASK queue` | What the next run will work on, in order. |
| `TASK review` | A table of finished work to rate. Reply like `T-001 9, T-002 7`, or `skip`. With an ID: rate one task, then approve it or send it back. Add `check` after an ID for an independent second rating. |
| `TASK edit (id) (change)` | Change anything: due date, priority, tag, pause, resume, delete, archive. |
| `TASK split (id)` | Break a big task into smaller ones, in order. |
| `TASK digest` | What finished, what needs you, what's stuck, and the one thing to do next. You can reply right to it (`approve T-005a`). |
| `TASK doctor` | Checks your setup (connectors, sheet, schedule, computer access) and offers fixes. |
| `TASK help` | This list. |

## The sheet

It starts with three tabs: **Tasks**, **Log** (every piece of work done), and **__settings__** (your timezone, offline hours, and run times). Other tabs appear only when needed: **Standards**, **Connections**, **Run Reviews** (one row per run, used for the digest), and **Archive**.

**Repeating tasks:** say "weekly" or "every 3 days" when you create one, and it puts itself back in the queue after each run.

Add your own columns or tabs any time. Claude finds columns by name, so nothing breaks, and it never removes anything you added.

## If something comes up

- **A run hit something unclear.** It doesn't guess. The task goes to *Needs review* with the question in its Notes, and the digest tells you.
- **A task needs an email sent or a form submitted.** Runs draft it and wait for you.
- **A task's files only exist inside one chat.** Scheduled runs start fresh and can't see them. Put the files in Google Drive or a connected tool.
- **Something seems off.** Run `TASK doctor`.

## What's in this repo

| Path | What it is |
|---|---|
| `dist/` | Ready-to-upload zips: the plugin, and the skill on its own |
| `skills/third-shift/` | The skill: `SKILL.md` plus `plans/`, which load only when a command needs them |
| `commands/`, `agents/`, `.claude-plugin/` | The plugin's slash command, reviewer, and manifests |
| `assets/`, `scripts/` | The icon and social card, and the scripts that draw them and build the zips |

## License

MIT. Use it, change it, share it. See [LICENSE](LICENSE).
