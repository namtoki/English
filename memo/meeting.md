# Meeting

## 20250327

導入
> I `figured` we have a bunch of assignments out of Use Case Study,
> `so` I added a row to track our progress.
>
> We're `keeping track of` those assignments as child issues under this Jira issue,
> `and` this is about how much we've had so far.
>
> > 目的のところ聞かれたら
> > `The reason` I’m writing this here is to `make it clear` what this work is leading to,
> >   `so that` we can always stay aware of where we are in the process.
> > If I’ve misunderstood anything, please feel free to share the right direction!

今日の議題
> Today’s agenda has three items — all just progress updates.
>
> `And` the first two are related to the Fit test for Use Case Study 1, and the last one is about Re-married Mode for Use Case Study 9.
>
> They’ve all moved from TODO to IN PROGRESS.

説明が必要か？
> Each of these issues has some `progress summarized`    like this
> would it be helpful if I gave a `quick rundown` here?

Fit test アルゴリズム
> So, first off, "Clarify fit test algorithm with Airoha Bluetooth chips"
>
> This task is about checking whether, when switching the chipset from Qualcomm to Airoha, we can have a standalone Fit test feature separate from the Personalization feature.
> That's what we were asked to look into.
>
> `And` So far, it looks like this is feasible — `mainly because` the Airoha SDK comes with its own Fit test feature.
>
> > マウスオーバーで示しながら
> This diagram shows the Fit test block diagram, taken from this PowerPoint file.
> We got it from Eastech, by the way.
>
> > 図を大きくしてから
> `the way it works is`: sound is played from the speaker, `and` picked up by the feedback mic, `and then` it runs its own air leakage detection algorithm.
>
> `That said,` there’s a chance the Personalization libraries might have their own built-in Fit test features, and I know Audiodo & Audiara have the feature.
> `So` I’m planning to `keep checking in with` companies like Audiara and Audiodo to see what they say about that.
>
> > レコメンド機能について聞かれたら
> > Ah yeah, I’ll cover that in the next issue — gonna talk about it right after this.

Fit test レコメンド
> Let's move on to this.
>
> This task is about ear tip recommendation.
>
> `And` the Airoha's Fit test, as I said, actually, doesn’t include any kind of recommendation feature.
> `Basically,` when you think of it as an API, it only returns two values — either 'Good' or 'Not Good'.
>
> That said, I want to look into whether it’s really impossible or if there’s some way to `tweak` it.
> I’ll be checking the SDK myself, and also talking with Airoha and the ODM vendors about it.

Re-married
> And the last one is here.
>
> This task mainly focuses on whether the users can remarry by themselves.
>
> so far,
> this looks feasible, but it’s a bit of a challenge.
>
> Technically, it seems possible — but none of the JDM vendors we’ve talked to have actually implemented this before.
>
> The key thing here is something called SIRK — both buds need to have the same key to pair up.
> This comes from how BLE is designed to treat two devices as one, unlike BR/EDR, which doesn’t have this kind of mechanism.
>
> `And` There is an API to sync the SIRK between the left and right buds — and we’re probably going to need to call that API either from the charging case or from the smartphone app.
>
> `And` I think the UX team is currently working through this part of the story, so thanks in advance for continuing to explore that.
> but at the same time, from the software side, we’ll stay ready to support whichever direction the spec ends up going.
>
> Just a heads-up — there's still a chance that, after digging a bit deeper, we might find out it's actually not feasible.
> `So` just keep that in mind.
>
> > 何か聞かれたら
> > To be honest, I'm not super familiar with it yet
> > I'm still getting up to speed.
> > But I’m working on it and aiming to get a full grasp of everything soon.
> > After that I'll get back to you.

## 20250313

Conduct RFI
> First and foremost,
> they have more experience with Airoha chip development than us,
> so
> we mainly evaluated them based on how easy it is to communicate with them
>                                   and
>                                   whether they have a lot of information that isn’t covered in Airoha’s official documentation.
>
> And
> if we still need to assess which one is technically better,
> I think we need to build our own technical knowledge of Airoha by working with like the evaluation kit ourselves,
> and then `use that foundation to` have deeper technical discussions with them.

SoC selection
> To add to that,
> both SoCs basically have the features we need,
>
> so
> the deciding factor will mostly `come down to` cost.
> but
>
> That said,
> there are some differences, like the version of ANC they use, but whether those differences are significant is something we can only determine through actual testing.
> We still need to figure out how to handle these smaller differences and summarize our approach moving forward.
> 
> and
> Right now,
> all that information is a bit `all over the place`,
> so I’d appreciate some time to tidy up and put everything together.
>
> We're particularly concerned about the Flash size, since features like voice trigger and voice prompt support could take up a lot of space.
> That said, we don’t have all the details organized yet, so I’d like to discuss this in more detail next time.

## 20250311

Small Talk
> Hey, can everyone hear me?
> Good.
> How's it going?
>
> I think everyone will be here soon, so please wait a moment.

Start
> `Is everyone` from your side `here`?
> 
> (Okay,)
> `I think we’ve got everyone here`.
> > but Our product lead, Saito, will be joining us late."
> Let’s get started.

Preface
> So,
> Thank you all `for being here`.
>
> The main purpose of today’s meeting is to `address` each other’s questions,
> but
> I also see this as an opportunity for us to `get to know` each other for future collaboration.
>
> (Of course,)
> we’ll `go over` the Software Core Questions you've answered the other day.
>
> but
> I would like to `proceed while` (occasionally) referring to the Feasibility Study materials you have submitted.
>
> And `feel free to` discuss anything else as well!

Introduction
> (Alright,)
> (so,)
> let us introduce ourselves from the Masimo side.
>
> (`That said,`)
> `it’ll just be` a quick introduction `where` we show our faces, mention our names, and briefly share our background related to TWS.
>
> ...
>
> (And,)
> (as for our background in TWS development,)
> Kuroishi-san and I have some experience with Qualcomm, though we can’t share specific product details.
>
> (As for Airoha,)
> we’re just `getting started with` it.
>
> and
> in order for us to gain a deeper technical understanding,
> We’ve been `going through` the documents and SDK source code, (and recently,) we’ve been trying to `get` the EVK `up and running`.
>
> (`That said,`)
> everyone here has experience developing some audio equipments, like AV receivers and HiFi products, of course.
>
> (`And with that,`)
> could you guys from the Fujikon side introduce yourselves?
> Just your names and faces `are totally fine`!

Dive
> Okay, let’s `jump into` the main topic.

```
👉 "Could you elaborate on this point?"

👉 "Could you provide some additional context for this answer?"

👉 "Is there anything to add or revise regarding this point?"

👉 "Does anyone have any comments or follow-up questions on this?"
```

Bluetooth
> And
> `Let's start with the first question`, the Bluetooth versions,
> `The response to this question was` 6.0.
>
> and it was really helpful that you also wrote the SDK version.
>
> And
> the following questions are mostly about the Profile and Codecs
> and
> answers are clear-cut.
>
> But
> (`just to add one more thing,`)
> > You don't have to support LC3-SuperWideBand `over` Bluetooth Classic in the first place.
> > Supporting LC3-SuperWideBand over BLE is fine.
> And there's no specific need to support PXP either.
>
> So
> My apologies for bringing it up.
>
> (By the way,)
> is there a way to check a list of supported profiles somewhere?
> Would it be in the **SDK source code**, **documents available from MediaTek Online** or something?
>
> Oh, I see! That makes sense. Got it!
>
> And
> the next few questions also seem clear-cut.
> I'll skip these items since there are quite a few questions.
> 
> > (Yeah, as far as I know,)
> > there aren't really any earbuds or headphones that officially support **AAC-ELD**, right?
> > I think it's safe to say it's **not supported**, and that shouldn't be an issue.
> > Kato-san, Is there anything to add or revise regarding this point?"
>
> > Alright,
>
> but
> Regarding **line 11**,
> You said the default is 2, but can it go up to like 4 or 5?
> I saw 4 mentioned in the datasheet.
>
> If there are more than three devices,
> does it get unstable or something?
> Are there any restrictions or anything like that?
>
> and
> Regarding **line 16**,
> This is an area I was also curious about.
>
> let me clarify the question.
> This means that,
> **If a user buys the product and later loses one of the buds,
> can we send the user a replacement bud and have them pair this with the remaining one by themselves?**
>
> (`From what I understand`,)
> this would be difficult due to **LE Audio-related keys**, SIRK, or things like that.
> Does that sound right?
> What do you think?

ANC
> And
> `Let's move on to the next topic`, ANC.
> `The response to this question was` "4 modes".
>
> and
> I checked the Android SDK `on my end`,
> and yeah,
> it does seem like the implementation assumes four ANC modes.
>
> So, when you say "4 modes,"
> I guess it's coming from something like this, right?
>
> And
> (`while we're at it,`)
> (if you happen to know,)
> there seem to be three modes for each: Passthrough, Hybrid Passthrough, and Vivid Passthrough.
> Does that mean each of them can have up to three modes?
>
> Also,
> (sorry if this is a basic question,)
> but
> what's the difference between Hybrid Passthrough and regular Passthrough? And which one would be better to use?
>
> I don’t have any more questions, but does anyone have any comments?

Call Quality
> `Let's move on to the next topic`, Call Quality.
>
> So,
> `would it be fair to say`
>   that your company has a strong expertise in ANC tuning for products using ADI chips,
>   and
>   that knowledge could also be valuable for ANC tuning on Airoha BT chips?
>
> So
> (at the end of day,)
> `it just comes down to` designing microphones placement and tuning parameter in the config tool, right?
>
> Got it.
>
> And the next question.
>
> You guys recommend using analog microphones in terms of size and performance.
> (From my experience,)
> (though it's limited,)
> I found it quite unique to have all the microphones are analog.
>
> and
> This is mentioned on page 44 of this document.
>
> so
> (From an acoustic perspective,)
> are there any downsides to this?
> for example, power consumption, or something like that.

Talk Through
> So
> `Let's move on to the next topic`, Transparency.
>
> and
> `when we said 'dynamically adjust' here, we mean that`
>   the gain automatically changes based on the external environment.
>
> you said "It cannot be dynamically adjusted."
> but
> this(, If I'm not mistaken,) corresponds to the 'vivid passthrough' feature, right?
> Do you have the experience of using vivid passthrough?
>
> and the next answer is ~~~~. Yeah,
> in the case of static passthrough, the gain should be adjustable.
>
> And
> (as for this question,) (you said checking with SoC vendor)
> Airoha team said
>   that they haven’t implemented this feature yet
>   and
>   that it's still in development.
> But
> I think it’s possible to implement using the VAD module.
> VAD module is mentioned in datasheet, like here.
> Do you think about this?
> Is it possible to implement some voice trigger feature?
>
> this is great.
> 
> > Have you actually done this before, or is it just theoretically possible?
> > Have you modified the SDK and worked on controlling the VAD module, or is this `more of` a conceptual idea?

Spatial Audio
> Next, Spatial Audio
> 2 つのクエスチョンを一気に読み上げる
> So
> This was also mentioned in the table of the Feasibility Study document, right?
> 資料見せる
> Just to confirm,
> does this mean that you have a experience integrating this THX 3rd party into an Airoha BT chip before?
> Or
> is it `just saying that,` while there’s no actual experience, it’s theoretically possible to implement?

EQ
> So
> `Let's move on to the next topic`, EQ.
>
> 4 slots is fewer than I expected.
>
> Is this the number of subsets?
> So there are only 4 subsets, but there are actually more PEQ patterns that can be assigned to those 4, right?
>
> Good. Here I have no additional question.

Ear fitting
> So
> `Let's move on to the next topic`, Ear fitting.
>
> (`First off,`)
> I want to apologize for the mistake.
> I wrote 'IMU,' but I actually mean 'IR sensor.'
> (and Basically,)
> `what I was asking` is whether IR sensors or capacitive sensors are typically used for proximity detection
>   to check if the buds are in the ear.
> (And)
> I saw that an IR sensor was proposed in your proposal, so I think we were on the right track.
>
> And
> Good to know that Airoha 1592 (Perl Pro 2) could do it with FB mic. It checks air leakage to assess the fitting.
> but
> Just to double-check,
> are you saying that this can't be done with the 1577?
>
> Is that mentioned in any document?"

Touch
> And
> `Let's move on to the next topic`, Touch and Swipe button
>
> I don't have any particular comments on this topic since it's pretty `straightforward`.
>
> (Regarding the two middle questions,)
> (to be precise,)
> we’re asking
>   whether functions like play, pause, next track, and previous track can be mapped to any tap or swipe gestures.
> `To break it down,`
>   the first question is whether users can customize these mappings via the smartphone app.
>   The second question is whether actions can be assigned specifically to the left or right bud.
>     For example, tapping the left bud once to play/pause music and tapping the right bud once to toggle ANC.
>
> Kuroishi-san, do you have any other inputs?

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

Sound Dose
> Actually,
> the **Sound Dose** feature hasn’t been officially confirmed yet, and it’s probably not going to be included.
>
> But
> I’m asking about it here just in case.
> and
> this is an interesting answer.
> to be honest,
> it depends on what exactly this feature involves,
> but either way,
> I think a 3rd party would be needed.
>
> and
> You guys said 'Yes,'
> but
> does that mean it can be achieved using a 3rd party solution,
> or
> are you saying it can be done through an in-house implementation?  
>
> And
> is this something that's theoretically possible,
> or
> do you have some experience of implementing it before?

Power
> Let's move on to Power
>
> Kuroishi-san, do you have any other inputs?

Voice Prompt
> Let's move on to Voice Prompt
>
> I think we’ve already asked about this in the Q&A list as well.
> Kuroishi-san, would it be okay if I leave this to you to handle?
> 
> 容量の換算方法、
> (Right now,)
> we're planning to support multiple languages.
> The idea is that (when the language setting is changed in the smartphone app,) the audio files will be downloaded from the server to the phone, and then from the phone to the buds.
>
> First,
> I’d like to know if this is even possible.  
> Also,
> based on your experience, do you have a rough idea of how many bytes of audio data can be stored on the buds at this stage?
> Just an estimate is fine.

App
> `What we’re mainly concerned about` is that
>   things might get complicated when the app is connected in single mode.
>
> For example,
> let’s say you are using one bud whose ANC Gain is set to like Level 4 out of 10, and then the other bud gets used later
> in this case,
> I think this Gain Level 4 setting needs to be synced with the other bud.
> but
> Considering the timing of this synchronization, it seems like the design and implementation could get quite complicated.
> What do you think?"
> 
> Would that work smoothly without any issues?

Conclusion
> I think we've covered everything on the agenda.
> but
> Before we wrap up, does anyone have any final questions or comments?
> If not, we'll call it a day here.
>
> Alright, thanks again, everyone, for your time and participation!
> and see you next time!

## 20250310

Small Talk
> Hey, can you hear me?
> Good.
> Did you have a good weekend?

Start
> (Okay,)
> Is everyone from your side here?" 
> 
> I think we’ve `got everyone here`. Let’s get started.
> Thank you all for being here.

Preface
> The main purpose of today’s meeting is to `address` each other’s questions,
> but
> I also see this as an opportunity for us to `get to know` each other for future collaboration.
>
> (Of course,)
> we’ll `go over` the Excel file you answered the other day,
> but
> we also want to clarify (as much as possible) any unanswered parts from this Q&A list.
>
> And `feel free to` discuss anything else as well!

Introduction
> (Alright,)
> (first,)
> let us introduce ourselves from the Masimo side.
>
> (`That said,`)
> `it’ll just be` a quick introduction `where` we show our faces, mention our names, and briefly share our background related to TWS.
>
> ...
>
> (So,)
> (as for our background in TWS development,)
> Kuroishi-san and I have some experience with Qualcomm, though we can’t share specific product details.
>
> (As for Airoha,)
> we’re just `getting started with` it.
> We’ve been `going through` the documentation and SDK, (and recently,) we’ve been trying to get the EVK up and running.
>
> (`That said,`)
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
> (`First off,`)
> I just realized that
>   there were some questions in the Q&A sheet that we hadn’t responded to.
> My apologies for that.
>
> I'll answer them now.
>
> For this first question about "First time,"
> it specifically `refers to` when the buds are in a factory-default state and have never been paired before.
> `This means that`
>   when you open the case lid for the first time after unboxing,
>     that’s considered the "First time."
>   Once they’ve been paired,
>     they won’t go back to the "First time" state unless you perform a factory reset.
>
> And
>   Even if you delete all paired devices from the list, the buds will still go into the 3-minute pairing mode mentioned here.
> 
> As for the next question,
> our wording wasn’t quite right.
> `What we actually mean is that`
>   when the Buds are in the case, we want buds to optimize for faster recharging (while making sure they don’t actively engage in pairing behavior).
>   In other words, they shouldn’t respond to things like Bluetooth Classic **inquiry** requests.
>
> Let's moving on,
> As it's written here,
> We're still discussing this with the spec owner, but there's a chance it may not be included in the specifications.
>
> but
> If we end up deciding to include it after all, we'll let you know again.
>
> And
> (for the remaining questions about the buttons and LED,)
> (as you can see,)
> we want to have two buttons on the case.
> The **Amber LED** mentioned for updates refers to the **case LED**.
>
> **Button 1** `is mainly for` pairing,
> while
> **Button 2** is designed to be harder to press,
> if you want to press it, you’d need something like a pen tip
> and `is primarily for` factory resets.

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
> and
> PXP isn't something we need to handle at this point.
>
> My bad for bringing it up.
>
> (By the way,)
> is there a way to check a list of supported profiles somewhere?
> Would it be in the **SDK documentation** or something?
>
> Oh, I see! That makes sense. Got it!
>
> And
> the next few questions also seem pretty clear-cut.
> Kato-san, do you want to add anything?
> 
> (Yeah, as far as I know,)
> there aren't really any earbuds or headphones that officially support **AAC-ELD**, right?
> I think it's safe to say it's **not supported**, and that shouldn't be an issue.
> Kato-san, Is there anything to add or revise regarding this point?"
>
> Alright,
>
> but
> Regarding **line 16**,
> This is an area I was also curious about.
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
> and
> I checked the Android SDK `on my end`,
> and yeah,
> it does seem like the implementation assumes four ANC modes.
>
> So, when you say "4 modes,"
> I guess it's coming from something like this, right?
>
> And
> (while we're at it,)
> (if you happen to know,)
> there seem to be three modes for each: Passthrough, Hybrid Passthrough, and Vivid Passthrough.
> Does that mean each of them can have up to three modes?
>
> Also,
> (sorry if this is a basic question,)
> but
> what's the difference between Hybrid Passthrough and regular Passthrough? And which one would be better to use?
>
> I don’t have any more questions, but does anyone have any comments?

Call Quality
> `Let's move on to the next topic`, Call Quality.
>
> Your answer is clear-cut.
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
> in the case of static passthrough, the gain should be adjustable.
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
>
> Good. Here I have no additional question.
>
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
> I think the document that covers this is probably Fit_Detection_Feature.pptx you referred to,
> (but right now,)
> it doesn’t seem to be accessible to us on MediaTek Online.
>
> So
> `Looks like` I should ask Airoha to make this document available for download.

Touch
> And
> `Let's move on to the next topic`, Touch and Swipe button
>
> I don't have any particular comments on this topic since it's pretty `straightforward`.
>
> (Regarding the two middle questions,)
> (to be precise,)
> we’re asking
>   whether functions like play, pause, next track, and previous track can be mapped to any tap or swipe gestures.
> `To break it down,`
>   the first question is whether users can customize these mappings via the smartphone app.
>   The second question is whether actions can be assigned specifically to the left or right bud.
>     For example, tapping the left bud once to play/pause music and tapping the right bud once to toggle ANC.
>
> Kuroishi-san, do you have any other inputs?

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

Sound Dose
> Actually,
> the **Sound Dose** feature hasn’t been officially confirmed yet, and it’s probably not going to be included.
>
> But
> I’m asking about it here just in case.  
>
> So,
> the exact specs for **Sound Dose** haven’t been decided yet,
> but
> if they do get finalized, I think the main question will be whether it’s possible to implement it or not.
>
> So
> Kuroishi-san, do you have any other inputs?

Power
> Let's move on to Power
>
> Kuroishi-san, do you have any other inputs?

Voice Prompt
> Let's move on to Voice Prompt
>
> I think we’ve already asked about this in the Q&A list as well.
> Kuroishi-san, would it be okay if I leave this to you to handle?
> 
> 容量の換算方法、
> (Right now,)
> we're planning to support multiple languages.
> The idea is that (when the language setting is changed in the smartphone app,) the audio files will be downloaded from the server to the phone, and then from the phone to the buds.
>
> First,
> I’d like to know if this is even possible.  
> Also,
> based on your experience, do you have a rough idea of how many bytes of audio data can be stored on the buds at this stage?
> Just an estimate is fine.

App
> `What we’re mainly concerned about` is that
>   things might get complicated when the app is connected in single mode.
>
> For example,
> let’s say one bud has **ANC Gain set to Level 4**, and then the other bud gets used later—
>   **which setting will take priority?**
>
> Also,
> I assume there will be some kind of **sync communication** between the two buds when this happens.
> Would that work smoothly without any issues?

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
