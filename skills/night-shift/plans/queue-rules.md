# Queue rules

Read only these Tasks columns: ID, Last Status, Runs, Priority, Effort, Spec, Milestones, and Due and Depends On if they exist.

A task is in the queue only if:
- Last Status is Not started or In progress,
- Runs is Daily queue,
- every ID in its Depends On is Finished, and
- it isn't a parent (no other row uses its ID plus a letter).

Left out, and set to Needs review with a one-line Notes reason (scheduled runs only; 'TASK queue' just lists them as left out):
- Spec, Milestones, or Effort empty, or Spec missing 'What:' or 'Output:',
- Effort L that hasn't been split.

Order: Priority (High, Med, Low), then Due (earliest first, blank last), then ID.
