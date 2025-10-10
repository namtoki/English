
## EQ

### Sync 説明しろと言われたら

Since we're already communicating with the UX team on Teams and Figma, I think we can skip the explanation here.

I think the key thing is to present what benefits there are in syncing data between PerL2 Standard and PerL2 Pro, and specifically what kind of data we want to sync. That's what I'd like to know first.
Technically, we know that if we properly sync data between Server/App/Buds, there shouldn't be any issues, but it does add some complexity and there's a chance we could introduce bugs, so we need to weigh that against the benefits.
What specific data are we looking to sync, and what's the user value proposition here?

#### 全体
This page `explains` how to achieve synchronization of buds control data between `multiple` pairs of buds,
particularly between PerL2 Standard and PerL2 Pro.

To `tackle` this, I will `break this down into` three steps:

#### ①
First, I'll show that synchronization is `simple` when the data is stored in the buds.
Second, I'll demonstrate that even when data is not stored in the buds, it's not a problem.
Finally, I'll show that the only `real challenge` is the `translation algorithms` between Standard and Pro.

I've written a lot of things here, but I'll focus on the main points.

First, `as background,` the Airoha chip has non-volatile memory `where` almost all buds control data is stored.
You can read and write this data using APIs available in the Airoha SDK.

For example, you can retrieve EQ parameters like frequency, gain, and other settings `using` the getAllEQSettings() function,
and you can set them `using` the setEQSetting() function.

Almost all buds control data has its own `dedicated` API.

`Given this foundation,` when you want to synchronize buds control data,
you can do so if the app always caches the buds data.

`Now, what happens when` you want to synchronize data while switching between mobile devices?
Even in this case, it's possible if the buds control data is synced from the app to the server.

Also, even when you only switch mobile devices,
it's not a problem as long as the Buds' information is stored on the server through the app.

The key point is that we just need to properly identify
which data should be shared across multiple devices and store that data on the server.

#### ②
And This explains situations like Custom EQ, where not all slots are stored on the Buds,
but since it's essentially the same as what I explained earlier, I'll skip this part.

---

## Sleep Timer

### Follow-up

#### 導入
To think about this topic, you need to `organize` the power states.

#### 自分のページの全体を見せる
This is the page where I consolidated what types of power states there are, what they are, and things like that.
At the end, I propose which power state the buds should enter when the sleep timer expires.

#### 1 枚目
So first, this is a table written on the UX specification page.
In this table, you can see expectations `for` how the buds should behave in terms of power status transitions.

#### 2 枚目
If you visualize this, this would look `something like this`.

#### 3 枚目
And you have to define each power state name, for example, like this.
Now you should consider the following:
What they are at the system level - I mean, how much power each power state consumes, what regions are disabled, and so on.

#### 4 枚目
So this is a rough image of that, based on what I heard from Eastech's engineer.
In this diagram, green boxes indicate they are powered on, and gray boxes indicate they are powered off.
And the most important thing, I think, is that Standby and Power OFF are almost the same in terms of power consumption,
and the only difference is that IR sensor and PUI are enabled in Standby.

And now, which power state should the buds enter when the sleep timer expires?
The options are Standby, Power OFF, or something else.

#### 5 枚目
I suggest Power OFF because this mode disables PUI and IR sensor, and you would want the buds to save power consumption.
From this perspective, Power OFF is the most suitable option.
This is my analysis.

### それをベースに考えると

Based on this, I putted some comments in this page.
And what I want to discuss is this question.
if the power state the buds enter when sleep timer expired is PowerOFF, this is not same as Standby.
So I think in this case the timer should still be running while they are in Standby mode.
Because Standby mode enables IR sensor and PUI, right?

---

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


## Airoha

## Mimi

### Walk through hearing test flow

#### Login

Looking at `the reason why` Login is marked as Optional,
`I think it's because` the Mobile SDK has a specific `mechanism` built in.

When you read through the Mobile SDK documentation,
there's `something called` Anonymous User Authentication.
With this feature, users don't need to `explicitly` log in.
The system generates a random login ID,
so you'd need to store that value on Masimo's server side and manage it by linking it to the Denon Account.

#### Internet Connection

I thought I've shared this condition.
The calculation of personalization profile is conducted on the Mimi server side.

## Sound Personalisation settings

## Review of our initial concepts
    Share our early thinking around the Sound Personalisation page and gather your feedback

## Custom UI constraints
    What can/can’t be customised in the SDK
    Building our own custom UI based on the SDK APIs

## Low Battery Mode

Low Battery Mode is designed to enter a low power state when the Buds' battery drops below a certain threshold, right?

First, I understand that we haven't reached a conclusion on whether to proceed with a specification
that differs from PerL1, where the device enters low-power state only after falling below a threshold.

Personally, I have no particular objection as long as this feature is not enabled by default.

  If it were the default, we would need to reconsider the playback time specifications.
  
  If we were to set a number higher than the current 7 hours based on this low power mode assumption,
  this is not what users would expect.
  
  On the other hand, if we maintain the 7-hour spec notation with Auto Low power mode OFF,
  it would be questionable to use spec notation based on a non-default setting.
  
  Therefore, being off by default becomes a condition.

Second, I believe the threshold hasn't been determined yet,
but please proceed with it as TBC (To Be Confirmed).

How about we make this decision during the development phase?
Because not having this determined shouldn't particularly impact ODM's effort,

  I think it has the aspect that you can't decide what percentage it should be without actually implementing and testing it.
  
  There are predictions for playback time extension effects,
  such as approximately 1 hour at 30% or approximately 2 hours at 60%.
  However, considering major features like Personalization and Spatial Audio, the effects could be even greater,
  which makes it difficult to determine the exact percentage at this point.

  Actually, I think it might be better for the user experience to align the threshold with Case LED pattern.

## Onboarding draft flow - Questions for Steve & PS team

## Sleep timer - Prototype run through and key use cases

## Swipe function - Share usability test results

## Mimi

### Question from me
Yeah, yeah.
As for the question I asked this week,
to begin with,

I'd like to know whether Voice Clarity can be enabled during calls — putting aside whether this is useful or not.

Supposing that Voice Clarity is enabled during a call, is there any chance that some user experiences would be improved compared to when Voice Clarity is off? Of course, I understand that the current version of Voice Clarity doesn't denoise incoming signals during decoding. However, even without that feature, Voice Clarity still has Natural Ambience feature: it removes environmental noise around the wearer, and it minimizes self-voice amplification using some algorithm, right?

So I assume that even with just Natural Ambience feature, there would be some effectiveness in terms of call experience.
Does that make sense?

I understand that we can only determine whether there's any effectiveness during phone calls by actually testing it in real use scenarios.

### SoW

I have some comments.
First, as for Sound Personalization,
at Implementation section, I can see the sentence "Note: the hearing test-flow itself can only be themed as described above".
Does this mean that API-based integration cannot provide the same level of functionality/customization?

## Federated Login

As for federated login,

while this feature isn't currently supported by the Nura Server (AWS EC2-based),
the Denon Headphone App source code shows some federated login APIs.

I've inquired about feasibility and implementation effort to the server team, but the team hasn't responded yet.

Since they've answered other questions, this may be a particularly complex issue for them.
So, it might require significant development effort from both app and server teams.

## 6 digits

The 6-digit login system is known as a "passwordless method" or "one-time password" (OTP).

To me, in my opinion, this method is perfectly valid.

It's actually becoming popular in the SaaS industry
  —platforms like Slack, Notion, Udemy and etc use OTP authentication.

The main benefit is that users don't need to remember complex passwords.
This isn't an outdated method;
it's actually a current best practice in the first place.

The effort required to switch to a password-based method doesn't justify the benefits at all.

## Spatial Audio


## Intro

Hello, my name is Toshiyuki Tanamura, and I usually go by Tana `short for` Tanamura.

I've been at this company for about two years.
Before joining here, I was involved in developing storage software, drone software, and a little bit Android applications.

Now I've `been working on` headphone product development, specifically PerL2, which is the successor to PerL1.
I'm a member of the Software Project Management team. We have another member in Shirakawa,
so our team consists of two people including myself.

This is Denon & Marantz's first attempt at developing TWS headphones `in-house`,
so this project is quite challenging for us.

I think there are two key points:

First,
and this isn't software related,
PerL1 has a critical downside: it's too big and heavy.
Our mechanical engineers and designers are `addressing` this,
and PerL2 will be much more compact compared to PerL1.

Second,
this is software-related:
the personalization functionality called AAT in PerL1.
As you know, the AAT technology belongs to the Nura team, which was originally `a separate company`
but merged with us recently.

That team will remain on the Masimo side after the Harman merger `concludes`.

So we need to find an alternative solution or develop one ourselves.
and, we ended up deciding to adopt a third-party vendor solution called Mimi.

These are the two key challenges, I believe.

At the same time,
I see this project as our first step toward developing TWS headphones in-house.
In this project, an ODM vendor will design and implement almost all the software,
but we're planning to have them share the source code with us.
This will allow us to dive deep into the TWS headphone software world.

I'm excited to `get our hands on it soon`."

## Intro

Apparently, most members are absent today
because many Pi6 meetings are being held this week.

I think most members, including Sagawa-san, Saito-san, and Fujise-san, are attending one of those meetings.
On a side note, some UK members seem to have come to the Japan office.

## Stance

If you have something you want to figure out whether it's feasible or not,
we - the software team - are happy to support you.

## Widget

Yeah, as I mentioned to the UX team and PS team in the Jira ticket,
I've done some feasibility study for showing the sleep timer widget.
So what is the widget?
To recap, in the Figma, the UX team requests a widget that looks like this.

And it is definitely feasible to just show the widget,
but if you think about it, this feature requires communicating with the buds to show the widget
because the timer runs on the buds side and some other device might change the timer.

The app can communicate with the buds if the app's state is Foreground or Background,
but if the app is terminated after the sleep timer runs,
it is not feasible for the app to communicate with the buds, you know what I mean?

So we have no choice but to use the device's local timer instead of the timer in the buds,
at least when the app is terminated.
Of course it is feasible when the app is in Foreground or Background.
But I think it is better to keep the design simple in order to reduce the possibility of bugs.

So I'm recommending that the widget be achieved by using the device's local timer,
even if the app is alive.
