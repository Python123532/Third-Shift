# Night Shift: a task queue for Claude

A Claude skill that gives you a task queue across every chat. You hand Claude work, it gets done on a schedule while you're busy, progress is saved after every step, Claude rates its own work honestly, and you review it when you're back.

The skill itself is small on purpose. It ships with only the core, and everything else is built around you as you use it: your schedule, what "good work" means to you, which of your tools it connects to, and any extra columns or tabs you want. Claude asks when something depends on you, saves the answer in your sheet, and follows it from then on.

## Where it works well

- **Work you don't want to babysit.** Research write-ups, document cleanups, code upkeep, anything that can be broken into steps. Claude saves after each step and picks up where it left off on the next run.
- **Work spread across chats and devices.** Start a task on your phone, check it from your laptop. The sheet is the single source of truth.
- **An honest feedback loop.** Claude rates its work 1-10 against the task's spec and your standards, says what to specify better next time, and you add your own rating. The gap between the two tells you whether to trust the self-ratings.

Less good for: anything that needs a person to click "send" or "buy" (it drafts those and waits for you), and quick one-off questions (just ask Claude normally).

## What you need

- A Claude plan that includes skills and scheduled tasks.
- The **Google Drive** and **Google Sheets** connectors (Settings > Connectors).
- Optional: any other connectors you want it to use, and the Claude desktop app if you want it to work with files on your computer.

## Setup

1. Zip the `SKILL.md` file and the `plans` folder together (or download the release zip). In Claude, go to **Settings > Skills**, choose **Upload a skill**, and upload the zip.
2. Open a new chat and type `TASK setup`.
3. Claude makes a Google Sheet called **Task Manager** in your Drive, asks (with your permission, and titles only) to look at your recent files so it can tailor itself to you, asks when you're offline, and sets up the scheduled runs. The first run each day also sends you a digest of everything since the last one.

That's it. Standards and tool connections get set up the first time they come up, and you can change anything by just asking.

## Commands

Type these at the start of a message. Anything else can be asked in plain words.

| Command | What it does |
|---|---|
| `TASK setup` | Makes your sheet, asks your schedule, sets up the runs. Re-run to change any of it. |
| `TASK create (what)` | Builds a new task with you until it's clear enough to run without you. |
| `TASK execute (id)` | Does a task now instead of waiting for a run. |
| `TASK status (tag or id)` | Every task and where it stands, or one task's full history. |
| `TASK queue` | What the next runs will work on, in order. |
| `TASK review (id)` | See a finished task, rate it, approve it or send it back. No ID: rate everything still unrated. |
| `TASK edit (id) (change)` | Change anything: due date, priority, tag, pause, resume, delete, archive. |
| `TASK split (id)` | Break a big task into smaller ones. |
| `TASK digest` | What finished, what's stuck, what needs you. |
| `TASK help` | The list. |

## The sheet

It starts with three tabs: **Tasks** (13 columns), **Log**, and **__settings__** (your timezone, Offline Mode, and Run Times). Other tabs appear only when you need them:

- **Standards**: what good work looks like, per tag. A researcher might want vetted sources and a lit review; an artist might want reference boards and thumbnails first. Claude asks the first time a tag has none.
- **Connections**: the tools you've connected and what each is for. Claude asks how you want a tool used before using it.
- **Run Reviews**: one row per scheduled run, used for the digest.
- **Archive**: finished tasks you've archived.

Add your own columns or tabs any time. Claude finds columns by name, so it won't break, and it never removes anything you added.

The **Runs** column says how each task gets worked on: *Daily queue* (the scheduled runs pick it up), *Own schedule* (it has its own scheduled task, for example one that needs your computer), or *Manual only* (it waits for `TASK execute`).

## If X happens

- **My computer was off.** Anything that needed your computer gets noted in a Pending Sync column and done the next time it's reachable. Claude asks you once how you'd like that handled.
- **A run hit something unclear.** It doesn't guess. The task goes to Needs review with the question in the Log, and it shows up in your digest.
- **A task needs an email sent or a form submitted.** Unattended runs never send, submit, buy, post, or delete. They draft it and wait for you.
- **The ratings look too generous.** Compare Claude Rating with your User Rating over a few tasks, and say so in `TASK review`.
- **A task's files only exist inside one chat.** Scheduled runs start fresh and can't see them. Put the files in Drive, a connected tool, or a folder on your computer.

## Sharing

Send people this repo. Everyone gets their own sheet through `TASK setup`, so nobody's tasks or settings mix.
