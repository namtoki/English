# TODAY

## Sync

This is about the question that came up during yesterday's UX meeting when we were reviewing the EQ screen.

And this is just an update to let you know that I'm working on this in the Figma Space from the link.

I said yesterday that I'd share it today, but sorry, I didn't make it in time.

The basic flow is coming together, but I have this feeling like something's missing,
so I'm checking that right now.

---

## Sync

So first, let me explain the overall approach.
The system should manage data by splitting it into Device Data and Shared Data.

Device Data is what's stored on the Buds,
and

Shared Data is what we keep on servers, apps, buds depending the case.
here's the key insight from my analysis
I realized that some data actually needs to exist in each place.
We're calling this 'Shared Data,' and you can see it highlighted in red in these diagrams.
This includes things like Personalization Profile, Custom Custom EQ Parameters, and Active Custom EQ Parameters.

The critical thing about Shared Data is that we should add timestamp information to it.
This is super important because when there are conflicts - 
like when someone goes from offline to online, or switches devices - 
we can use these timestamps to figure out which version is the most recent.

---

Let me walk through the four scenarios we've mapped out:

First,
the Online scenario - pretty straightforward.
App gets data from both Buds and Server, user makes changes, App sync everything up.

Second,
Offline mode - here's where it gets interesting.
When users make changes offline, App cache them locally.
Then when the system come back online, App use those timestamps to make sure we're syncing the right version.

Third and fourth scenarios cover device switching - whether it's changing mobile devices or changing Buds.
In both cases, we rely on our timestamp system to resolve any conflicts.

Now, there's one more thing we need to address - 
and this is in the yellow box here.
For parameters that have different structures between PerL2 Pro and Standard, like the EQ settings,
we have two options: either treat them as completely separate parameters, or create conversion functions between them.

The beauty of this approach is that by using timestamps on our Shared Data,
we can handle pretty much any conflict scenario that comes up.
Does this make sense to everyone? Any questions about the flow or the timestamp logic?"
