# TASK create (description)

Build a new task with the user until every core column has a value, then save it. If they ask for a template, or the request clearly matches one, use plans/templates.md first.

1. **Never assume what the task is.** If the description is only a name or a few words (e.g. "Pin13Update") or leaves out what to do, the scope, or the output, your first message is a plain-text question asking the user to type out in their own words what the task is: what to do, what's in and out of scope, and what they want back. Ask this before any multiple-choice card. Never infer the task's content from its name, existing tasks, the Tag, project files, or memory; those can be mentioned as context (e.g. "T-001 already covers X") but never used to fill in the answer. Wait for the reply, then continue.
2. Fill in what the user already said. Ask only about what's missing or unclear, with clickable choices where possible, at most 4 questions per card. Don't re-ask anything.
3. Don't add scope the user didn't ask for.
4. Write Spec as the three labeled lines and Milestones as 2 to 5 steps. Match the format in plans/examples.md.
5. **Dated work** (an event, test, meeting): unless the user gave both, ask when the event is and when the output is due. Suggest a Due 3 days before the event. Put the event date in 'What:' and the due date in Due. Never use the event date as Due without asking.
6. **Repeating work** (the user says weekly, every few days, etc.): set Repeat ('daily', 'weekly', or 'every N days') and Due to the first run date (SKILL.md, Task rule 8).
7. **Effort L:** propose a split before saving (plans/split.md).
8. **Standards:** show which will apply. If the Tag has none, ask what good work looks like for this kind of task: 2 or 3 short options based on the task, plus 'write my own' and 'skip'. Save the answer as a Standards row (create the tab if needed). On 'skip', save nothing and don't ask again for that Tag.
9. If one of the user's tools would help, follow plans/connections.md.
10. If the task's files are somewhere a scheduled run can't reach (inside a chat, or a computer that isn't connected), say so and ask where to put them.
11. Save with Last Status 'Not started', Ratings blank, Runs 'Daily queue' unless the user chose otherwise. Show the saved row.
