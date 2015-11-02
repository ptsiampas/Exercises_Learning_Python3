# 10.6. Exercises
1. Add some new key bindings to the first sample program:
  * Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
  * Pressing keys + or - should increase or decrease the width of tess’ pen. Ensure that the pen size stays between 1 and 20 (inclusive).
  * Handle some other keys to change some attributes of tess, or attributes of the window, or to give her new behaviour that can be controlled from the keyboard.

2. Change the traffic light program so that changes occur automatically, driven by a timer.

3. In an earlier chapter we saw two turtle methods, hideturtle and showturtle that can hide or show a turtle. This suggests that we could take a different approach to the traffic lights program. Modify the program so that we create three separate turtles for each of the green, orange and red lights, and instead of moving tess to different positions and changing her color, we just make one of the three turtles visible at any time. Once you’ve made the changes, sit back and ponder some deep thoughts: you’ve got two programs, both seem to do the same thing. Is one approach somehow preferable to the other? Which one more closely resembles reality  i.e. the traffic lights in your town?

4. Now that you’ve got a traffic light program with different turtles for each light, perhaps the visibility / invisibility trick wasn’t such a great idea. If we watch the traffic lights, they turn on and off  but when they’re off they are still there, perhaps just a darker color. Modify the program now so that the lights don’t disappear: they are either on, or off. But when they’re off, they’re still visible.

5. Your traffic light controller program has been patented, and you’re about to become seriously rich. But your new client needs a change. They want four states in their state machine: Green, then Green and Orange together, then Orange only, and then Red. Additionally, they want different times spent in each state. The machine should spend 3 seconds in the Green state, followed by one second in the Green+Orange state, then one second in the Orange state, and then 2 seconds in the Red state. Change the logic in the state machine.