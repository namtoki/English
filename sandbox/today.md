# TODAY

## Intro - Multi Point

Before we get to those topics,

we'd like to discuss the Multi point feature, as it seems there may be some misunderstandings or differences in our understanding.

So first things first, shall we discuss Multi point? Does that work for everyone?

Akane-san, Kuroishi-san, could you share some materials, or would it be okay if I share the Figma file?

## Touch control

Okay, so moving on to "Touch control."

Thank you, Vefa-san, for commenting on the Excel sheet attached to the Jira ticket.

As I understand it, Eastech is reviewing our request and will make a suggestion based on it.

So the ball is in Eastech's court. Please bear with us until they get back to us.

Is my understanding correct, or does anyone have any discussion points?

## Login

Okay, and before getting to the Sleep timer topic, I'd like to confirm how to move forward with the Login feature improvement.

Saito-san has shared with me that a unified account approach is under discussion, led by Zain, a Senior Product Manager, right?
And he will share some action items with us before long.

We should wait until then. Is my understanding correct?

That being said, I've asked the server team to estimate their effort if we move forward with the new login method.

## Sleep Timer

Okay, so next up is Sleep timer.

Tolu-san will be sharing some materials, right?

I've commented on that section in Figma and suggested an alternative flow,

but I think it would be best to have Tolu-san walk us through their flow first. Does that sound good to everyone?

> 自分の figma に移動

This is my suggested flow.

It's based on Tolu-san's flow, and initially, the steps are the same—setting up the Sleep timer on Device A and starting the timer.

However, I have two points.

> tolu の figma に移動

First,

when the app is launched on Device B, as Dilshard-san commented, Device B should receive notification from the Buds that the timer has started,

and the initial screen should display that the timer is running, as shown here.

> 自分の figma に移動

Given that, I think the subsequent screen transitions for Device B should reflect that the timer is already running,
as shown in these screens.

Then, if Device B subsequently changes the timer value,

I think Device A would be in the same situation as Device B,

so Device A's flow after this point should align with Device B's flow as well.

This is my second point.

I think it would be more consistent if Device A does not reset the timer that was set by Device B at this point.

This is because

Device B's flow doesn't reset the timer here,

and both Device A and Device B are in the same situation — their timers have been updated by another device.

Regardless of whether we reset the timer or not, I believe that at least,

Device A and Device B should behave the same way in this flow.

> ..

Next, this flow outlines the limitations of the Sleep timer.

The Sleep timer specification includes displaying a notification when one minute remains.

I believe there was a requirement that this notification should continue to work even after the app has been terminated by the user.

However, when the app is terminated, it cannot detect that the timer value has been changed by another device.

To be more precise,

communication with Bluetooth-connected devices is restricted.

Even more precisely,

this might be possible on Android, but iOS has limitations on processing when the app is terminated, so at least on iOS, it cannot be detected.

Given this,

if we consider the same flow as before:

after setting the timer on Device A, if the Device A app is terminated,

and then Device B changes the timer, Device A cannot detect this change.

However,

Device A continues counting with a timer on the mobile device side in order to display the "one minute remaining" notification even when terminated.

So what happens is, while the Buds will properly go to sleep based on the timer set by Device B,

Device A will trust its own timer and show the notification when it thinks there's one minute left, based on the mobile side timer.

This is a fairly rare case, so I think it's a minor issue.

But, I'm sharing this because it's a potential limitation to consider implementation constraints.
