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
> about the Bluetooth versions,
> thanks for the answers.
>
> Kato-san, do you have any thoughts on this?
> We don’t actually need LC3-SuperWideBand to work `over` Classic, right?
> And there's no specific need to support PXP either, correct?
>
> 加藤さんのターン
>
> Got it.
>
> 〇〇san,
> I asked those questions,
> (but just to clarify,)
> there's no actual requirement to support LC3-SWB on Classic,
> and
> PXP isn't something we need to handle at this point.
> My bad for bringing it up.
> 
> (By the way,)
> is there a way to check a list of supported profiles somewhere?
> Would it be in the **SDK documentation** or something?
>
> (Yeah, as far as I know,)
> there aren't really any earbuds or headphones that officially support **AAC-ELD**, right?
> I think it's safe to say it's **not supported**, and that shouldn't be an issue.
> What do you think, Kato-san?
>
> Alright,
> this is my last question about Bluetooth.
> Regarding **line 16**,
>
> let me clarify the question.
> **If a user buys the product and later loses one of the buds,
> can we send the user a replacement bud and have them pair it with the remaining one by themselves?**
>
> From what I understand,
> this would be difficult due to **LE Audio-related keys** or something like that.
> Does that sound right? What do you think?

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
