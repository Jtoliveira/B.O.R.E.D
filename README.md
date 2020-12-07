# B.O.R.E.D
This is the repository for the B.O.R.E.D - Born Of Random Enterntainment Deficits application

It was made using Python (with Tkinter and sqlite3) and the BoredAPI, which consists of an API that returns activities to do when you're bored. I was bored, so i made an application that runs on Windows and fetches data from it. This is probably some of the ugliest code i've ever written.

The app stores user data in a database and might also eventually hold a user's list of activities. This was the original plan but i chose to take it on a simpler route.

## How to use it:

1. Run the executable
2. Fill the username and password fields and hit "Create User" (for first time users, ignore this step if you already created some credentials)
3. Click "Login"
4. Select the categories on the left and set the interval of price and accessibility you want (remember to re-choose the category if you change the intervals in between requests)
5. If the button "New Activity" is clicked without a change in the parameters, it will fetch an activity with the same options as the previous request
6. Be sure to click "Logout" when you're done using the application

[This dude](https://github.com/RafaelCS-Aula) chose the name
