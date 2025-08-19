
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
