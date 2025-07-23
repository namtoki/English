# TODAY

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
