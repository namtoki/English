# TODAY

---

## Touch

## Spatial Audio

From a software perspective, I'll leave this up to the UX team.
At the end of the day, it all comes down to what users find easiest to use based on your research.
There shouldn't be any technical limitations regardless of which option you choose.
So, I'm good with whatever you decide.

## Auracast

As mentioned in the Jira ticket,
Eastech is asking whether music playback should be able to interrupt Auracast playback.

Here's where we stand:
We originally decided to follow the same spec as the C-series,
meaning music playback cannot interrupt Auracast.
The broadcast stays connected unless the user explicitly chooses to leave.

However, Eastech is now suggesting we allow music to interrupt Auracast.
Their reasoning is that the Airoha SDK v5.7.0 used in Perl2 already works this way,
and they're finding it difficult to implement the behavior we originally specified.

Just giving you a heads-up on this.

The software team is currently looking into how difficult it would be to stick with the original spec.

That said,
if it turns out to be too challenging from a software perspective,
would it be okay to go with the behavior where music playback can interrupt Auracast?
