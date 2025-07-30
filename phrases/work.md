# WORK

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
---

## 実績 (Track record)
> So while I've been in touch with Mimi,
> I found out that they actually don't have any `track record` of implementing Voice Clarity into the Airoha SDK.

>   but for the main Personalization feature,
>   it looks like they've got the implementation process pretty well established,
>   so I don't think we need to worry about that part.

>   However, I'm feeling a bit uncertain about whether Voice Clarity is actually feasible,

> so I've just started following up on this.

## 段取りする (set things up)
> Specifically,
> We're `setting things up` to pass along some Airoha documentation to Mimi
> so they can check whether Airoha SDK has all the necessary technical components and report back to us.

>   At the same time,
>   we're going to deepen our understanding of Airoha's Audio Processing flow and source code architecture on our end,
>   so we can verify the validity of their report.

>   For example,
>   understanding Airoha's Audio Flow like this.
>   I'll drop a link later.
>   And right now I'm looking at the DSP source code to see exactly how this flow is implemented in software.

# Technical Meeting

## Premise

`First, let me share our high-level understanding, and please correct me if anything is inaccurate.`
Our understanding is that we'd like to adopt two components from your solution:
Sound Personalization and Voice Clarity.
For Sound Personalization, you have previous experience implementing it on the Airoha SDK and have integration guides available.
However, for Voice Clarity, you haven't implemented it on an SoC before.
`Is this understanding correct?`

## 専用の
> `You're concerned` it might affect screens that `are dedicated to` other products like C500 or PerL1, aren't you?

## 見る限り (From / Based on / As far as), せずに (without V-ing)
> `From what I can see in` the source code,
> `it looks like` they're hardcoding screens for each combination of flags - like "denon or nura" and "Airoha or not"
> so `it seems like` we could implement this `without` affect`ing` screens for other products.
> Matsumoto-san, please correct me if I'm wrong. Or should we set aside some time to estimate the implementation effort?

> Regarding the hearing test screen,
> `from what I can see in` Mimi's documentation, `it looks like` we can build our own custom UI,

## CC した
> but I'm checking with Mimi just to be sure. `I've cc'd` you on the email, May-san,
> so you should have received it. Let me continue investigating this.

## そういうもんだと
> so I was assuming `that's just how it is`.

## のようにも見える, 整理する
> But some documentation `makes it seem like` Passthrough is part of ANC functionality,
> so I think we need to `sort this out`.
> Let me check this.

## 考えは変わっていなくて
> Regarding tip recommendation,
> `my understanding hasn't changed` - we'd still do our best effort to find some solution during the development phase if possible.
> However, I heard that the PS team's research shows this feature doesn't seem to have much value
> when they looked at other products out there.
> So given that, I think we might be okay with dropping it at this point.

> Either way, I don't think we can finish the feasibility study and effort estimation before BCR.

## こういった考えから
> From an acoustic standpoint, we might be able to put together some kind of logic,
> but software-wise, I think we need to actually play around with the real hardware
> and observe how each variable changes during sealing checks when we attach various sized tips.
> `At this point in our understanding,` we'll be assessing feasibility in the development phases after BCR.

The current button maps to position 30 on the bottom bar, while the adjacent button maps to position 60.
When the 30 button is active and we manually change the bar value from 30 to 60,
shouldn't the UI update to reflect this by showing the 60 button in the selected gray state?

---

## UX spec

In terms of RFQ blockers,
I don't think there's anything we need to follow up on here.
There are still some TODOs for the engineering team to work on,
but I don't think they'll impact the RFQ.

About the Voice mode described in Noise Controls,
the engineering team (not only Software team) needs to do a study on what technical elements could be used to achieve it.

---

## EQ

### 他社のプリセットについて聞かれたら
Wasn't the PS team looking into that? Sorry if I'm wrong.

### どっちが良いか聞かれたら
From a software perspective, easier implementation would be better.
Matsumoto-san, do you have any sense at this point which approach would be easier?

Since either approach is the same, I'll leave it up to UX and PS to decide.

### Delete 直後ってどうなるの？
What EQ setting should the system be set right after deletion?
How about having it set to Default? it is better. I think.

I mean, that would reduce complexity, right?

---

## Quick Setup

I'm in favor of it since it reduces implementation effort.

Didn't we have users enter their birth year when signing up for the app? Either way though.

---

