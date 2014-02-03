PayPall ExpressCheckout Python SDK [![Build Status](https://travis-ci.org/cirocosta/paypal-expresscheckout-python.png)](https://travis-ci.org/cirocosta/paypal-expresscheckout-python)
===

> A quick/simple lib for using [ExpressCheckout](https://developer.paypal.com/webapps/developer/docs/classic/express-checkout/gs_expresscheckout/)

QuickStart
---
Just copy `src/paypal_ec.py` file to your utils directory and import the library.
There is a code example commented at the end of the library (*function main*).


Using
---

1.	Initialize the `ExpressCheckout` with your sandbox user credentials:
go to [PayPal app acounts](https://developer.paypal.com/webapps/developer/applications/accounts), select the probfile of one if created, then get the *api credentials*.

2.	Execute the method that you want with the parameters it requires: **setExpressCheckout**, **getExpressCheckoutDetails**, **doExpressCheckoutPayment**.

3.	Get the response and do whatever you want with it.


*ps.: responses will always be a python dict so that you are able to manage it the way you want.* 


Hacking
---
For properly configuring the dependencies:

```bash
$ pip install virtualenv
$ virtualenv .env
$ pip install -r requirements.txt
$ source .env/bin/activate
$ nosetests --verbose 
```  

Contributing
---
Just fork the repo, test/document it and then submit your PR. PR are **awesome**.

