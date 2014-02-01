import urllib
import urllib2
import urlparse

ENDPOINT_SANDBOX = "https://api-3t.sandbox.paypal.com/nvp"


class ExpressCheckout(object):

    VERSION = "109.0"

    def __init__(self, username, password, signature, sandbox=False):
        self.username = username
        self.password = password
        self.signature = signature
        if sandbox:
            self.endpoint = ENDPOINT_SANDBOX

    def _post_data(self, url, data):
        """ Posts data to a given url

            params:
                url: a string containing the url
                data: a string or a dict containing data
                    if string, must be urlencoded
        """
        if type(data) == dict:
            data = urllib.urlencode(data)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        return response.read()

    def _validate_field(self, field, value):
        """ Validates the value given the field.
        field: String (amount, currency_id)
        value: String

        currency_id:
            Must be a valid one of those specified at the documentation:
            https://developer.paypal.com/docs/classic/api/currency_codes/ 

        amount:
            Regardless of the specified currency, the format must have
            a decimal point with exactly two digits to the right and an 
            optional thousands separator to the left, which must be a 
            comma.
        """

        CURRENCY_IDS = ["AUD", "BRL", "CAD", "CZK", "DKK", "EUR", "HKD",
            "HUF", "ILS", "JPY", "MYR", "MXN", "NOK", "NZD", "PHP", "PLN",
            "GBP", "RUB", "SGD", "SEK", "CHF", "TWD", "THB", "TRY", "USD"
        ] 

        if field == "amount":
            if "{0:.2f}".format(float(value)) == value:
                return True
            else:
                return False
        elif field == "currency_id":
            return True if value in CURRENCY_IDS else False

    def _set_express_checkout_request(self, amount, currency_id,return_url,
            cancel_url, method="SetExpressCheckout"):
        """ Creates a proper request to be posted """
        if self._validate_field("amount", amount) and\
            self._validate_field("currency_id", currency_id):

            obj_for_request = {
                "METHOD": "SetExpressCheckout",
                "VERSION": self.VERSION,
                "USER": self.username,
                "PWD": self.password,
                "SIGNATURE": self.signature,
                "PAYMENTREQUEST_0_AMT": amount,
                "PAYMENTREQUEST_0_CURRENCYCODE": currency_id, 
                "RETURNURL": return_url,
                "CANCELURL": cancel_url,
                "PAYMENTREQUEST_0_PAYMENTACTION": "Sale" 
            }
            return urllib.urlencode(obj_for_request)
        else:
            raise Exception("the amount field is not valid")

    def _set_get_express_checkout_details_request(self, token):
        """ Creates a proper request to be posted """
        obj_for_request = {
            "USER": self.username,
            "PWD": self.password,
            "SIGNATURE": self.signature,
            "VERSION": self.VERSION,
            "TOKEN": token,
            "METHOD": "GetExpressCheckoutDetails"
        }
        return urllib.urlencode(obj_for_request)

    def _set_do_express_checkout_payment_request(self, payerid, token, amount):
        """ Creates a proper request to be posted """
        obj_for_request = {
            "USER": self.username,
            "PWD": self.password,
            "SIGNATURE": self.signature,
            "VERSION": self.VERSION,
            "PAYMENTREQUEST_0_PAYMENTACTION": "Sale",
            "PAYERID": payerid,
            "TOKEN": token,
            "PAYMENTREQUEST_0_AMT": amount,
            "METHOD": "DoExpressCheckoutPayment"
        }
        return urllib.urlencode(obj_for_request)

    def _set_create_recurring_payments_profile(self, method, profilestartdate, 
            desc, billingperiod, billingfrequency, amt, currencycode, acct, 
            email, street, street2, city, state, countrycode, zip_code):
        obj_for_request = {
            "METHOD": method,
            "PROFILESTARTDATE ": profilestartdate,
            "DESC ": desc,
            "BILLINGPERIOD ": billingperiod,
            "BILLINGFREQUENCY ": billingfrequency,
            "AMT ": amt,
            "CURRENCYCODE ": currencycode,
            "ACCT ": acct,
            "EMAIL ": email,
            "STREET ": street,
            "STREET2" : street2,
            "CITY" : city,
            "STATE" : state,
            "COUNTRYCODE" : countrycode,
            "ZIP": zip_code,
        }
        return urllib.urlencode(obj_for_request)


    def setExpressCheckout(self, amount, currency_id, return_url, cancel_url, 
                method="SetExpressCheckout"):
        """ Performs the setExpressCheckout request and returns the
            response in a python dict"""
        data = self._set_express_checkout_request(amount, currency_id, \
            return_url, cancel_url, method)
        return urlparse.parse_qs(self._post_data(self.endpoint, data))

    def getExpressCheckoutDetails(self, token):
        """ Performs the GetExpressCheckoutDetails request and returns
            the response in a python dict """
        data = self._set_get_express_checkout_details_request(token)
        return urlparse.parse_qs(self._post_data(self.endpoint, data))

    def doExpressCheckoutPayment(self, payerid, token, amount):
        """ Performs the DoExpressCheckoutPayment request and returns
            the response in a python dict """
        data = self._set_do_express_checkout_payment_request(payerid, token,\
            amount)
        return urlparse.parse_qs(self._post_data(self.endpoint, data))

    def CreateRecurringPaymentsProfile(self, method, profilestartdate, 
            desc, billingperiod, billingfrequency, amt, currencycode, acct, 
            email, street, street2, city, state, countrycode, zip_code):
        """ Sends the request for creating a recurring payments
            profile """
        data = self._set_create_recurring_payments_profile(method, 
            profilestartdate, desc, billingperiod, billingfrequency, amt, 
            currencycode, acct, email, street, street2, city, state, 
            countrycode, zip_code)
        return urlparse.parse_qs(self._post_data(self.endpoint, data)) 


def main():
    username = "ciro9758_api1.gmail.com"
    password = 1390922883
    signature = "AFcWxV21C7fd0v3bYYYRCpSSRl31AFdl6Gwn9pQHqzliaz6mNHjRfG.k"

    ec = ExpressCheckout(username,password,signature,True)
    response =  ec.setExpressCheckout("20.00","BRL","http://cirocosta.com/return",\
        "http://cirocosta.com/cancel")
    print response
    if response['ACK'] == ["Success"]:
        token = response['TOKEN']
        reresponse = ec.getExpressCheckoutDetails(token[0])
        print reresponse


if __name__ == "__main__":
    main()