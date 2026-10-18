# Task Manager for Claude

A Claude skill that turns Claude into a task manager you can use from any chat. You hand it tasks, it works on them on a schedule while you're busy, and every chat sees the same list because the list lives in a Google Sheet in your Drive.

It also connects to the tools you already use (Notion, Obsidian, GitHub, Google Drive), so tasks show up where you keep your notes, and finished work lands in the right project folder.

## Where it works well

- **Recurring or long work you don't want to babysit.** Research write-ups, document cleanups, code upkeep. Claude splits a task into milestones, saves after each one, and picks up where it left off on the next run.
- **Work spread across several chats.** Start a task on your phone, check it from your laptop, review it later. The sheet is the single source of truth.
- **Keeping your notes up to date without doing it yourself.** Task notes, a log line in your daily note after each run, and outputs filed into the project folder.
- **Honest feedback loops.** Claude rates its own work 1-10 against the task's spec and says what to specify better next time. You add your own rating, and the gap between the two shows whether the self-ratings can be trusted.

Less good for: anything that needs a person to click "send" or "buy" (it drafts those and waits for you), and quick one-off questions (just ask Claude normally).

## What you need

- A Claude plan that includes skills and scheduled tasks.
- The **Google Drive** and **Google Sheets** connectors turned on (Settings > Connectors).
- Optional: **Notion** connector, **GitHub** connector, and the **Claude desktop app** on your computer if you want Obsidian or local folders.

## Setup

1. In Claude, go to **Settings > Skills**, choose **Upload a skill**, and upload `SKILL.md` from this repo.
2. Open a new chat and type `TASK setup`.
3. Claude will:
   - make a Google Sheet called **Task Manager** in your Drive (tabs and columns included),
   - list the connectors it can see, plus any Obsidian vaults or code folders on your computer if the desktop app is linked,
   - ask which ones to connect and what each one is for,
   - ask a few preferences (below),
   - offer to set up the scheduled runs.
4. Open `SKILL.md` and change the **Time** section to your own schedule. The one in the file is the author's (busy 2:30 AM to 8:00 PM Eastern).

## Commands

Type these at the start of a message.

| Command | What it does |
|---|---|
| `TASK setup` | First-run interview: connect tools, set preferences. Re-run any time. |
| `TASK create (what)` | Builds a new task with you, field by field, until it's clear enough to run alone. |
| `TASK execute (id)` | Does a task now instead of waiting for a scheduled run. |
| `TASK update (source)` | Reads what changed in your connected notes and refreshes Claude's context. Asks what to look for first. |
| `TASK status (tag)` | Every task and where it stands. |
| `TASK queue` | What the next scheduled runs will work on, in order. |
| `TASK review (id)` | See a finished task, rate it, approve it or send it back. |
| `TASK digest` | What finished, what's stuck, what needs you. |
| `TASK build (id) (what)` | Turns a task's notes into something new, like a summary or a product review. |
| `TASK edit (id) (change)` | Change any field: priority, due date, tag, pause, resume. |
| `TASK depends`, `split`, `archive`, `delete` | Manage a task. |
| `TASK log`, `sources` | History and citations for a task. |
| `TASK template (name)` | Save a task's structure to reuse. |
| `TASK help` | The full list. |

## Preferences asked in setup

- **Tiebreak.** If a task was changed in the sheet and in your notes app between syncs, either the newest edit wins, or changes to sheet fields (status, priority, due date) made in your notes come back to you as proposals in `TASK review`.
- **Write style.** Claude writes straight into your notes and folders, or keeps everything under a "Claude Log" heading so your own writing is never touched.
- **Auto update.** Off (you run `TASK update` when you want), or every few days.

## The sheet

The tabs you'll read: **Tasks**, **Log**, **Run Reviews**, **Templates**, **Archive**, **Connections**.

Each task also gets a workspace doc in your Drive folder `Task Manager/Tasks`, with a Spec tab, a Notes tab, and a tab for anything you make with `TASK build`. The finished deliverable stays separate and is linked from the sheet.

Tabs that start with `__` (`__settings__`, `__context__`, `__scanlog__`) are bookkeeping for Claude. You can ignore them. `__context__` holds a few lines per project summarizing your notes, so Claude reads those instead of your whole vault every time, and `__scanlog__` tracks which files changed so unchanged files are never re-read.

## If X happens

- **My computer was asleep or the desktop app was closed.** Anything that needed your computer (Obsidian, local folders) is written into the task's **Pending Sync** column. How it gets cleared depends on the Sync Mode you picked in setup: a small daily check if your computer is always on, a cloud copy of your vault (Obsidian Git or a Drive/Dropbox folder) so no computer is needed, or the next time you use Claude on that computer. Cloud tools like Notion and Drive aren't affected. A task that runs entirely on your computer just skips that run and logs it.
- **A connector isn't turned on.** That connection shows as Broken in the Connections tab. Turn the connector on in Settings, then run `TASK setup` again.
- **I edited a task in my notes and in the sheet.** Your tiebreak setting decides. With "newest wins", the overwritten value is written to the Log so you can restore it from version history.
- **A scheduled run hit something unclear.** It doesn't guess. The task goes to **Needs review** with the question in the Log, and it shows up in your digest.
- **A task needs an email sent or a form submitted.** Unattended runs never send, submit, buy, post, or delete. They draft it and wait for you.
- **The ratings look too generous.** Compare Claude Rating with your own User Rating over a few tasks. If Claude keeps rating higher, tell it in `TASK review`.
- **A task's source files only exist in one chat.** Scheduled runs start fresh and can't see files inside other chats. Put the files in Drive, Notion, or a connected folder.

## Sharing with friends

Send them this repo. Everyone gets their own sheet and their own connections through `TASK setup`, so nobody's tasks mix. Don't point the skill at someone else's sheet.
