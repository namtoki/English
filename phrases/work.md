# WORK

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
