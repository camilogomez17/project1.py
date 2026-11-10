# Reflections

> These are draft responses based on the current implementation. Review them
> and revise the wording so it accurately describes your own experience
> before submitting.

## 1. Share one aspect of building this project you found challenging and how you overcame it.

One challenging part was keeping the game history and statistics consistent
when a record is edited or deleted. I addressed this by storing each round as
a dictionary inside one list, then using dedicated functions to add, update,
and remove records. Statistics are calculated from the current list instead
of being maintained as separate counters. This avoids counters becoming
incorrect after a record changes.

## 2. Share one technical concept that you gained a deeper understanding of through building this project. Explain that concept in simple terms and explain how it is used in your project.

I gained a better understanding of lists of dictionaries. A list stores
multiple records in order, and each dictionary groups related values under
named keys. In this project, each dictionary represents one game and stores
the player's choice, the computer's choice, the result, and the time played.
The program loops through the list to display history and calculate
statistics, and uses a list index to edit or remove a particular record.
