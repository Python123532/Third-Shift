# TASK create (description)

Build a new task with the user until every core column has a value, then save it.

1. Fill in what the user already said. Ask only about what's missing or unclear, with clickable choices where possible, at most 4 questions per card. Don't re-ask anything.
2. Don't add scope the user didn't ask for.
3. Write Spec as the three labeled lines and Milestones as 2 to 5 steps. Match the format in plans/examples.md.
4. **Dated work** (an event, test, meeting): unless the user gave both, ask when the event is and when the output is due. Suggest a Due 3 days before the event. Put the event date in 'What:' and the due date in Due. Never use the event date as Due without asking.
5. **Repeating work** (the user says weekly, every few days, etc.): set Repeat ('daily', 'weekly', or 'every N days') and Due to the first run date (SKILL.md, Task rule 8).
6. **Effort L:** propose a split before saving (plans/split.md).
7. **Standards:** show which will apply. If the Tag has none, ask what good work looks like for this kind of task: 2 or 3 short options based on the task, plus 'write my own' and 'skip'. Save the answer as a Standards row (create the tab if needed). On 'skip', save nothing and don't ask again for that Tag.
8. If one of the user's tools would help, follow plans/connections.md.
9. If the task's files are somewhere a scheduled run can't reach (inside a chat, or a computer that isn't connected), say so and ask where to put them.
10. Save with Last Status 'Not started', Ratings blank, Runs 'Daily queue' unless the user chose otherwise. Show the saved row.
