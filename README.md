# ai_project3

As of now, there is only limited functionality within the program. The output is still messy, the GUI elements can get shuffled up sometimes, and exemplification and optimize are still only partially done. The program works by using an attribute class with the gui class to house an attribute along with their values, and having functionality of being able to return the correct value given a boolean value.
I have the original test files as well as the test files of my own instance. These files are a.txt(attributes file), c.txt(constraints file), penlog.txt(penalty logic file), posslog.txt(possibilistic logic), and qualilog.txt(qualitative choice logic)

Below you will find a rough description of the GUI buttons as they were designed to function, unfortunately I haven't quite made it there yet. I can generate feasible objects with existence, but exemplification and optimize still are only partially done, as I've been having trouble with them. 

INSTRUCTIONS FOR USE:
1. Click Load Instance
2. Enter the appropriate filenames and then click on the button saying "click me"
3. After entering attribute and constraint files, you need to enter 3 preference files and select their type via a radio button in order to submit each filename.
4. Finally you will be at the Home Screen, and can proceed to load another instance, generate feasible objects with existence, or partially exemplify or optimize the instance.

-----------------------------------------------------------------------------------------------------

The starting point is the GUI. That is what has to be designed first. It will feature multiple capabilities and buttons. There will be three buttons that are always visible. These are the "Create New Instance", "Load Instance", and "Quit". The three hidden buttons will be the instance options, "Existence", "Exemplification", and "(Omni)optimization". The hidden buttons will only appear after having selected an instance, or creating a new one.

/* - Button Functionality - */
	
1. Create New Instance
	Upon selection of create new instance, a new window will open that will prompt for the user to enter attribute name, and then the information associated with it. Upon creation of 8th attribute (at least 8 are needed for project), check to see if more attributes are desired, repeat if so until no more are desired, and then call create_constraints, which will essentially repeat this process with constraints, until they're all collected, and then call create_preferences.

2. Load Existing Instance
	Allows for user to enter file names that program will then open and parse them and populate the instance fields from the file data.

3. Existence
	This button will identify any objects from the attributes of the instance that satisfy the instance constraints.

4. Exemplification
	This generates two random objects and shows the preference that exists between the two (strict, equivalence, or incomparison) w.r.t T.

5. (Omni)optimization
	This button will first prompt to see if user wanted omnioptimization, or just normal optimization. If omni, find all optimal objects, if normal, just find one optimal object.

6. Quit
	Exits the program.
