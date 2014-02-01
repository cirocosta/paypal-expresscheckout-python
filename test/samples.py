USER = "sdk-three_api1.sdk.com"
PWD = "QFZCWN5HZM8VBG7Q"
SIGNATURE ="A-IzJhZZjhg29XQ2qnhapuwxIDzyAZQ92FRP5dqBzVesOkzbdUONzmOU"
VERSION = "109.0"

sample_set_express_checkout_request = {
    "METHOD": "SetExpressCheckout",
    "VERSION": VERSION,
    "USER": USER,
    "PWD": PWD,
    "SIGNATURE": SIGNATURE,
    "PAYMENTREQUEST_0_AMT": "20.00",
    "PAYMENTREQUEST_0_CURRENCYCODE": "BRL", 
    "RETURNURL": "http://myurl.com/return",
    "CANCELURL": "http://myurl.com/cancel",
    "PAYMENTREQUEST_0_PAYMENTACTION": "Sale" 
}

sample_get_express_checkout_details_request = {
    "USER": USER,
    "PWD": PWD,
    "SIGNATURE": SIGNATURE,
    "VERSION": VERSION,
    "TOKEN": "um_token",
    "METHOD": "GetExpressCheckoutDetails"
}

sample_do_express_checkout_payment_request = {
    "USER": USER,
    "PWD": PWD,
    "SIGNATURE": SIGNATURE,
    "VERSION": VERSION,
    "PAYMENTREQUEST_0_PAYMENTACTION": "Sale",
    "PAYERID": "payerid",
    "TOKEN": "um_token",
    "PAYMENTREQUEST_0_AMT": "20.00",
    "METHOD": "DoExpressCheckoutPayment"
}