PayPal Hackathon related
===

ExpressCheckout
---

![setExpressCheckout](https://www.paypalobjects.com/webstatic/en_US/developer/docs/ec/SandboxECUX.gif)

**setExpressCheckout**
```
# SPECIFY THAT WE ARE DEALING WITH THE SETEXPRESSCHECKOUT
METHOD=SetExpressCheckout
VERSION=XX.0

# SPECIFY OUR CREDENTIALS
USER=sdk-three_api1.sdk.com
PWD=QFZCWN5HZM8VBG7Q
SIGNATURE=A-IzJhZZjhg29XQ2qnhapuwxIDzyAZQ92FRP5dqBzVesOkzbdUONzmOU

# specify the amout and also the currency
PAYMENTREQUEST_0_AMT=amount
PAYMENTREQUEST_0_CURRENCYCODE=currencyID

# Return and also cancel URL if it fails
RETURNURL=return_url
CANCELURL=cancel_url

# Specify the payment action
PAYMENTREQUEST_0_PAYMENTACTION=Sale


# if setExpressCheckout was successful
https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=callback_function&token=TOKEN_VALUE
```

**getExpressCheckoutDetails**

