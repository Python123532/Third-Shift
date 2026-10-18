# Connections

The user's other tools (notes apps, code repos, cloud folders, anything in Claude's connector list or on their computer) are connected only when they want them to be.

- When a task could use a tool the user has, or they mention one, ask how they want it used: what Claude should read from it, what to write to it, for which tags. Save the answer as a row in a **Connections** tab (Tool, Where, Purpose, Reachable From) and follow it. Work out how to do it from the tool itself; there's no fixed protocol per app.
- Tools that need the user's computer only work when a chat or run is linked to it and the computer is awake. If such a write can't happen, don't skip it and don't fail the task: add a **Pending Sync** column if there isn't one, note the write there, and do it the next time the computer is reachable. Ask the user once how they'd like pending writes cleared (for example a small daily check if their computer is always on, or at the start of their next linked chat) and save it in __settings__.
- Never delete anything in a connected tool.
