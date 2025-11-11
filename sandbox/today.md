# TODAY

This is feasible.

An inactive instance can load parameters when it becomes an active one.
However, it requires a specific trigger to load them, such as an explicit action like a button press or a screen transition.

This is the same with my suggested method in this ticket.
If the sleep timer has been set into the buds by an app, hereafter "App A," another device, for example "App B," can load the timer value on the buds when connected with it.

However, this is the behavior only when an app is actively connected to the buds.
Given that users might terminate the app right after starting the sleep timer,
it is difficult for "App A" to catch the new timer value set by "App B" after "App A" set the first timer value and was terminated by the user.
To be precise, this is technically possible on Android but not on iOS.

This is my point.

In that case, while the timer has not expired, it is still possible for "App A" to load the new timer value set by "App B" by actively reconnecting to the buds.
