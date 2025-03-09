# Meeting

## 20250310

Small Talk
> Hey, can you hear me?
> Good.
> Did you have a good weekend?

Start
> (Okay,)
> I think we’ve `got everyone here`. Let’s get started.

Preface
> The main purpose of today’s meeting is to `address` each other’s questions,
> but
> I also see this as an opportunity for us to get to know each other for future collaboration.
>
> (Of course,)
> we’ll `go over` the Excel file you answered the other day,
> but
> we also want to clarify as much as possible any unanswered parts from this Q&A list.
>
> And `feel free to` discuss anything else as well!
>
> Any questions?

Introduction
> (Alright,)
> (first,)
> let us introduce ourselves from the Masimo side.
>
> (That said,)
> it’ll just be a quick intro where we show our faces, mention our names, and briefly share our background related to TWS.
>
> ...
>
> (So,)
> (as for our background in TWS development,)
> Kuroishi-san and I have some experience with Qualcomm, though we can’t share specific product details.
>
> (As for Airoha,)
> we’re just getting started with it.
> We’ve been `going through` the documentation and SDK, (and recently,) we’ve been trying to get the EVK up and running.
>
> (That said,)
> everyone here has experience working on our AV receivers and HiFi products, of course.
>
> (`And with that,`)
> could you guys from the Eastech side introduce yourselves?
> Just your names and faces `are totally fine`!

Dive
> Okay, let’s `jump into` the main topic.

```
💬 「では、この点についてもう少し詳しく説明していただけますか？」
👉 "Could you elaborate on this point?"

💬 「この回答の背景を少し補足していただけますか？」
👉 "Could you provide some additional context for this answer?"

💬 「この点について、何か補足や修正すべきことはありますか？」
👉 "Is there anything to add or revise regarding this point?"

💬 「この回答について、ご意見や追加の質問はありますか？」
👉 "Does anyone have any comments or follow-up questions on this?"
```

Q&A Overview
> (First off,)
> I just realized that
>   there were some questions in the Q&A sheet that we hadn’t responded to.
> My apologies for that.
>
> I'll answer them now.
>
> ...

Move on to Core questions
> So let's move on to "Core Questions"

Bluetooth
> And
> `Let's start with the first question`, the Bluetooth versions,
> `The response to this question was` 6.0.
>
> So
> (from this answer,)
> it sounds like the SDK version is based on 5.5. Is that right?
>
> Good.
>
> And
> the following questions are mostly about the Profile and Codecs.
>
> Kato-san, do you have any thoughts on these?
> We don’t actually need LC3-SuperWideBand to work `over` Classic in the first place, right?
> And there's no specific need to support PXP either, correct?
>
> 加藤さんのターン
>
> Got it.
>
> 〇〇san,
> We asked this question,
> but
> it's not that
>   we specifically want LC3-SWB to be supported on Bluetooth Classic.
> `As long as` it works with BLE, that's fine.
> We `just wanted to` check if Classic could support it too by verifying the HFP version, just to be sure.
> 
> and
> PXP isn't something we need to handle at this point.
>
> My bad for bringing it up.
>
> (By the way,)
> is there a way to check a list of supported profiles somewhere?
> Would it be in the **SDK documentation** or something?
>
> And
> the next few questions seem pretty clear-cut.
> Kato-san, do you want to add anything?
> 
> (Yeah, as far as I know,)
> there aren't really any earbuds or headphones that officially support **AAC-ELD**, right?
> I think it's safe to say it's **not supported**, and that shouldn't be an issue.
> What do you think, Kato-san?
>
> Alright,
> This is an area I was also curious about.
> Regarding **line 16**,
>
> let me clarify the question.
> This means that,
> **If a user buys the product and later loses one of the buds,
> can we send the user a replacement bud and have them pair it with the remaining one by themselves?**
>
> (`From what I understand`,)
> this would be difficult due to **LE Audio-related keys** or something like that.
> Does that sound right?
> What do you think?

ANC
> And
> `Let's move on to the next topic`, ANC.
> `The response to this question was` "4 modes".
>
> I checked the Android SDK `on my end`,
> and yeah,
> it does seem like the implementation assumes four ANC modes.
>
> I don’t have any more questions, but does anyone have any comments?

Call Quality
> `Let's move on to the next topic`, Call Quality.
>
> So
> (for call quality,)
> `it just comes down to` microphones placement design and parameter tuning in the config tool, right?
> Got it.

Talk Through
> So
> `Let's move on to the next topic`, Transparency.
>
> (Regarding the first question,)
> I realize our `terminology` we used might have been a bit unclear,
> so
> let me clarify.
>
> `When we say 'effectiveness,' we mean that`
>   if you lower it, external sound gets blocked more and Talk Through gradually turns off.
>   (On the other hand,)
>   if you increase it, more external sound comes through, essentially reaching a 100% Talk Through state.
> `This is the same as what` you refer to as 'gain,' right?
>
> So
> `when we said 'dynamically adjust' here, we meant that`
>   the gain automatically changes based on the external environment.
> (From what you told us,)
> this corresponds to the 'vivid passthrough' feature, right?
>
> (If that’s the case,)
> would it be possible to support both static passthrough and dynamic passthrough,
>   (allowing the user to switch between them via the smartphone app?)
> (And of course,)
> in the case of static passthrough, the gain should still be adjustable.
>
> So
> (about the second question,)
> Airoha's team said
>   that they haven’t implemented this feature yet
>   and
>   that it's still in development.
> But
> you guys mentioned that it’s possible to implement using the VAD module.
>
> this is great.
> 
> Have you actually done this before, or is it just theoretically possible?
> Have you modified the SDK and worked on controlling the VAD module, or is this `more of` a conceptual idea?

Spatial Audio
> Next, Spatial Audio
> So
> `just to confirm, does this mean that`
>   you’ve tried implementing Savitech’s Spatial Audio library,
>   but
>   you haven’t actually released any products with Spatial Audio yet?
>
> And
> The proposal mentioned using either Dirac or Dolby.
> `would this be` your first time working on something like this?
> `Would it be` a challenging project for you?
> Or,
> (since you already know that a TDK G-sensor is required,)
> does that mean you've actually implemented both Dolby and Dirac for some test?

EQ
> So
> `Let's move on to the next topic`, EQ.
>
> 28 slots is a lot more than I expected!
> (`Just out of curiosity,`)
> have there actually been cases where all 28 slots were used?

Ear fitting
> So
> `Let's move on to the next topic`, Ear fitting.
>
> (`First off,`)
> I want to apologize for the mistake.
> I wrote 'IMU,' but I actually meant 'IR sensor.'
> (Basically,)
> `what I was asking` is whether IR sensors or capacitive sensors are typically used for proximity detection
>   to check if the buds are in the ear, right?
> (Regarding this,)
> I saw that HX3009 was proposed in the proposal, so I think we were on the right track.
>
> But
> You wrote 'Airoha provides a similar method by Mic,'
> and
> `that got me wondering.`
> does this mean the microphone is used
>   not just to check if the buds are in the ear,
>   but to confirm they’re properly fitted for ANC and other features to work correctly?
> I think the document that covers this is probably Fit_Detection_Feature.pptx,
> (but right now,)
> it doesn’t seem to be accessible to us on MediaTek Online.

Touch
> And
> `Let's move on to the next topic`, Touch and Swipe button
>
> Kuroishi-san, do you have any other inputs?
>
> (Regarding the two middle questions,)
> (to be precise,)
> we’re asking
>   whether functions like play, pause, next track, and previous track can be mapped to any tap or swipe gestures.
> `To break it down,`
>   the first question is whether users can customize these mappings via the smartphone app.
>   The second question is whether actions can be assigned specifically to the left or right bud.
>     For example, tapping the left bud once to play/pause music and tapping the right bud once to toggle ANC.

Motion Capture
> And Motion Capture
>
> Kuroishi-san, do you have any other inputs?

Case Communication
> Kuroishi-san, do you have any other inputs?
>
> (By the way,)
> I assume that the Case protocol is basically defined by Airoha,
>      and that the available commands are also predefined, right?
> But
> is it possible to create custom commands and define your own communication if needed?

Conclusion
> I think we've covered everything on the agenda.
> but
> Before we wrap up, does anyone have any final questions or comments?
> If not, we'll call it a day here.
>
> Alright, thanks again, everyone, for your time and participation!
> and see you next time!

## 20250306

### Transparency

Me
> (As I shared last week,)
> it’s just that I'll continue digging into its feasibility by the end of MS3.

Me
> Do you want me to explain it again?
> Sure.

Me
> (In the last meeting,)
> I reported that
>   Airoha doesn’t support transitioning to Transparency Mode via Voice Trigger for now.
>
> So
> I’ll also ask ODM vendors if they can implement it and how to implement it.
>
> and
> Eastech has already confirmed they can,
> and
> (given Airoha’s chip architecture includes a hardware accelerator for voice detection,)
> it should be possible (at the end of the day).
> 
> And
> I’ll keep checking with Airoha on when they might support this,
> Also
> I'm working on getting confirmation from ODM vendors regarding feasibility of it.

## 20250303

### Voice Prompt / TTS

Me
> (If I had to say,)
> who has the ball for deciding which service to use for Voice Prompt?
> 
> (In the meeting,)
> we concluded that the only way to decide on a TTS service is to check with native speakers.
> 
> I don’t think
>   the software team is in a position to take the lead anymore.
> Reaching out to native speakers of different languages in the company and running evaluations
> isn’t really software development anymore, is it?
> 
> I strongly believe the UX team should `take care of` this task.
> Should we create a Jira task for it and assign it to you?

### LE Audio

Me
> So this is a feature where S V when ___ happens, right?
> 
> You talked about this before, right?
> what did we decide at that time?
> Apologies, I didn’t have the opportunity to do the handover from XXXX-san.
> I can't say for sure` without checking, but..

### Transparency

Me
> Should the focus be on natural ambient sound passthrough
>                     or
>                     on making face-to-face conversations easier?
> or
> should multiple modes be provided to accommodate both?

Me
> `I assume` one of them is a typo,
> but
> (in Chapter 4's GIVEN WHEN THEN part,) `it says` 'THEN pause audio,'
> (while in Chapter 5, Section 2,) `it says` 'lower the media volume.'
> Which one is correct?

### Startup

Me
> If the only goal is to speed up login, I don’t think it’s necessary.
