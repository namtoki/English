# TODAY

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
