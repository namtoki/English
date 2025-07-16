

The current button maps to position 30 on the bottom bar, while the adjacent button maps to position 60.
When the 30 button is active and we manually change the bar value from 30 to 60,
shouldn't the UI update to reflect this by showing the 60 button in the selected gray state?

---

# 16 July 2025

## UI Concept

You
> `You're concerned` it might affect screens that `are dedicated to` other products like C500 or PerL1, aren't you?

> `From what I can see in` the source code,
> `it looks like` they're hardcoding screens for each combination of flags - like "denon or nura" and "Airoha or not"
> so `it seems like` we could implement this without affecting screens for other products.
> Matsumoto-san, please correct me if I'm wrong. Or should we set aside some time to estimate the implementation effort?

> May-san, could you give us some time to estimate the impact?

> Regarding the hearing test screen,
> `from what I can see in` Mimi's documentation, `it looks like` we can build our own custom UI,
> but I'm checking with Mimi just to be sure. I've `cc'd` you on the email, May-san,
> so you should have received it. Let me continue investigating this.

## ANC

### Why not have adaptive to cover both ANC and transparency?

> I think we need to `clarify` this.
> Airoha has a feature called "Adaptive ANC" but doesn't have one called "Adaptive Passthrough,"
> so I was assuming that's just how it is.
> But some documentation makes it seem like Passthrough is part of ANC functionality,
> so I think we need to `sort this out`.
> Let me check this.

### Are 5 level sufficient, acoustically for transitions would you recommend more?
### Would more levels be valuable?

> What do you think, acoustics team?

### Whether there's the opportunity for an additional preset mode, 'Voice': Could this be beamforming/conversational awareness?

> For this too, we need to figure out the basics
> like whether we use Airoha's Passthrough for both Aware and Voice with different fine-tuned settings,
> or use Airoha's Passthrough for Aware and Mimi's Transparency+ for Voice, etc.
> so, acoustics team, Should we discuss this together after the meeting?

### Is there enough differentiation considering SoC is the biggest difference from performance(ANC/Transparency)?

> What do you think, acoustics team?
> `I'll leave it up to you`, acoustic team.

## Sleep Timer

## Tip Recommendation

> Regarding tip recommendation,
> my understanding hasn't changed - we'd still do our best effort to find some solution during the development phase if possible.
> However, I heard that the PS team's research shows this feature doesn't seem to have much value
> when they looked at other products out there.
> So given that, I think we might be okay with dropping it at this point.

> Either way, I don't think we can finish the feasibility study and effort estimation before BCR.

> So what do you think, acoustic team?
> Are we good with that approach?"
