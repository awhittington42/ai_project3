# ai_project3

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
