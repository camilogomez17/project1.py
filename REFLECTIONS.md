# Reflections

1. Share one aspect of building this project you found challenging and how you
   overcame it.

One aspect of building this project I found challenging was understanding how code translates to logic and how we interpret that logic. It is hard to explain because of the abstraction behind programming. For example, we can model the game of rock, paper, scissors, as `result = (player move - computer move ) mod 3`. This is because the game of rock, paper, scissors is actually circular and can be represented using modular arithmetic. Although if you were to play this game in real life, your brain would do the pattern recognition for you. You naturally comprehend that rock beats scissors, scissors beat paper, and paper beats rock. And that depending on who plays what, you either win, tie, or lose. Mentally, we are abstracting the game, and our code is doing the same.

2. Share one technical concept that you gained a deeper understanding of
   through building this project. Explain that concept in simple terms and
   explain how it is used in your project.

I gained a deeper understanding of the technical concept called separation of concerns. This is where we separate data from logic. In simple terms it's keeping the operations of the project detached from the data being saved. It is used in my project by having separate files, `main.py` starts the app, `menu.py` handles the user's navigation, `logic.py` exclusively executes game rules, and `game_data.py` stores the stats and calculates winrate.

# AI Use On This App

I made the project twice, using implementer mode, and tutor mode. Creating the project this way forced me to individually construe the logic and user navigation. Writing out the code and creating the structure allowed me to see the fine details I did not see before. It allowed me to connect different systems and view different perspectives towards solving the same problem. Additionally, it created new dimensions of abstraction I had not previously seen nor imagined. In this test-driven-development, I applied the red-green-Refactor cycle. In my next project, I will use AI as a specialized tutor so I still own every line.

# AI Use On This App

I made the project twice, using implementer mode, and tutor mode. Creating the project this way forced me to individually construe the logic and user navigation. Writing out the code and creating the structure allowed me to see the fine details I did not see before. It allowed me to connect different systems and view different perspectives towards solving the same problem. Additionally, it created new dimensions of abstraction I had not previously seen nor imagined. In this test-driven-development, I applied the red-green-Refactor cycle. In my next project, I will use AI as a specialized tutor so I still own every line.