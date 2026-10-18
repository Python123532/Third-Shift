# TASK digest

A summary of everything since the last digest. Build it from the Run Reviews rows since then and these Tasks columns only: ID, Name, Last Status, Milestones (progress line only), Output Link, Ratings, Notes (first line), Runs, Depends On, Repeat, Last Updated. Don't read the Log.

Four short groups:
1. **Finished:** with Output Link and Ratings.
2. **In progress:** with milestone progress.
3. **Needs you:** Needs review tasks, with the question or draft that's waiting.
4. **Stuck:** with why. Includes Needs review for more than 2 days, In progress untouched for more than 3 days, and, right away, any task whose Depends On points to a Needs review or Stuck task (name what it waits on).

Leave out Paused, Manual only, and parent tasks.

Then, in this order:
1. **Next step:** the one action that would unblock the most work, with a time estimate and what it unblocks, e.g. 'Review T-005a (about 2 min), which unblocks T-005b.' Say they can reply right here ('approve T-005a', 'T-005a: (changes)').
2. **Calibration** (only when 3 or more tasks have both numbers): average Claude minus You over the last 10 rated tasks, e.g. 'Claude rates itself +1.2 above you.' Save it as a Rating Gap row in __settings__.
3. One line listing tasks whose Ratings show 'You -' (not 'You skip') and 'Reply TASK review to rate them.' If nothing changed since the last digest, say so in one line.
