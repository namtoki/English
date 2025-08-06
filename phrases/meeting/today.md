# TODAY

## Airoha

## Mimi

### Walk through hearing test flow

#### Login

Looking at the reason why Login is marked as Optional,
I think it's because the Mobile SDK has a specific `mechanism` built in.

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
