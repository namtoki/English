# TODAY

## Hearing test: Concepts walk through

---

## Onboarding: Flow walk through & open questions

---

## EQ

### 仕様的なことを聞かれたら

I`'m in favor of` ... because that reduces implementation effort.

### Sync 説明しろと言われたら

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
