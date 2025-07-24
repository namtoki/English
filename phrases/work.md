# TODAY

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

## Sleep Timer

I've given my comments from the embedded perspective,
so Matsumoto-san, could you please comment from the app perspective?

### Second device
I think this is a yes.
Even when there's only one connected device,
the App needs to sync the sleep timer status with the connected device when it launches.

I mean,
when you start the sleep timer in the app, close the app, and then reopen it right away,
it would be better if the sleep timer progress could be retrieved from the device, right?

### 左から 2 つ目
Based on my earlier comment, this would also be No, No, Yes, I think.

### 左から 3 つ目
Basically,
I think the timer should continue for everything except phone calls, which are a strong wake-up action.
With that in mind, timer continuation would be better here, right?

### 左から 3 つ目 一番下
I think
both when the Sleep Timer expires and when it's in the case,
it enters a strong power-saving mode with Bluetooth turned off.
With that in mind, if it's already been put in the case, I think we should consider that
the goal of entering power-saving mode has already been achieved.
So I think resetting it here would be good.

### その右
Considering that it transitions to a strong power-saving mode with Bluetooth turned off,
playback from another source device wouldn't be possible either, 
so I don't think this use case exists.

### 一番右
I mean,
someone who answers the phone isn't planning to sleep, right?

---
