# Assignment 3 - Writeup

Assignment 3 is all about creating this natural language query system.  In order to do so, you have to write a lot of functions to retrieve infomation.  You will also have to write a function to return answers from a pattern-action list.  There is a lot of work to accomplish in this assignment, but this portion is intended for you to write about what you accomplished.

## Reflection Questions
1. In your own words describe the `search_pa_list` function.
The 'search_pa_list function takes a list of strings as inputs. It iterates through a list, and for every iteration it tries to match patterns from the list to the input. It does this using the match() function. If a match is found, it calls a function and returns the info. If there are not matches, it returns another string output. 


2. What movie did you add to the `movies.py` file?  What year was it made? Any specific reason you added that movie?
I added the movie "pulp fiction" made in 1994 because I think that movie is very funny and deserves a spot. Many people would consider pulp fiction to be a classic because of its actors and how funny it is. 


3. What pattern / action did you add to the paList data structure?  Why do you think that is a useful pattern / action?
I added the pattern/action pair "movies in the genre _" linked to the movies_by_genre function. This pattern allows users to search for movies belonging to a specific genre, making it useful for exploring the movie database based on genre preferences. It provides a convenient way for users to find movies that match their genre interests.


4. What is chatbot would you create that would be like this?  Describe why you would create it and what it would do.
I would create a chatbot that would be used to filter out information from all over the internet. You could enter in information and it could spot any fake news or test to see if something is legit or not. This would be very complex but I think it could be very useful for people to use. 


5. What was the most difficult portion of this assignment?
The most difficult part of this assignment was writing the new asserts because I ran into some unique problems while trying to incorporate them. 

6. Did you write a new assert for your pattern action?
Yes, I added a new assert. 


