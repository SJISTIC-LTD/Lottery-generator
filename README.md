# Lottery-generator
he word 'list' is a built-in type/function in Python. If you name your list 'list', you no longer have access to the built-in. This may cause problems if you are using/importing other people's code. Call your list something like 'numbers', which describes what's in the list.

Second, you need to define the list in the function, so that it gets reset every time the function is called. As it is, you always appending to the same list. That's why your output gets longer and longer each time.

Third, moving the definition inside the function will make it unavailable outside the function. You will need to use the return statement to return it from the function, and you will need to assign the function call on line 11 to a variable. Details on how to do this are in the functions tutorial link in my signature below.
