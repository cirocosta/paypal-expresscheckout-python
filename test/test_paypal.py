import unittest
import paypal_ec
import samples
import urllib

# MISSING TESTS FOR CreateRecurringPaymentsProfile

class TestExpressCheckout(unittest.TestCase):
    """ Testing for the functions that are used just internaly.
        The public methods are doctested so that we provide a
        more rich documentation on how to use it """

    def setUp(self):
        self.ec = paypal_ec.ExpressCheckout("sdk-three_api1.sdk.com",
            "QFZCWN5HZM8VBG7Q", 
            "A-IzJhZZjhg29XQ2qnhapuwxIDzyAZQ92FRP5dqBzVesOkzbdUONzmOU",
            True)

    def tearDown(self):
        pass

    def test_validate_field(self):
        self.assertFalse(self.ec._validate_field("lol", "20.00"))
        self.assertTrue(self.ec._validate_field("amount", "20.00"))
        self.assertRaises(ValueError, self.ec._validate_field,"amount", "20,00")
        self.assertRaises(ValueError, self.ec._validate_field,"amount", "ahaha")

    def test_set_express_checkout_request(self):
        sample_true = samples.sample_set_express_checkout_request
        should_equal = self.ec._set_express_checkout_request("20.00","BRL",\
            "http://myurl.com/return", "http://myurl.com/cancel")
        self.assertEqual(urllib.urlencode(sample_true), should_equal)

    def test_set_get_express_checkout_details_request(self):
        sample_true = samples.sample_get_express_checkout_details_request
        sample_true = urllib.urlencode(sample_true)
        should = self.ec._set_get_express_checkout_details_request("um_token")
        self.assertEqual(sample_true, should)

    # def test_do_express_checkout_payment_request(self):
        # sample_true = sample_do_express_checkout_payment_request
        # TODO

if __name__ == "__main__":
    unittest.main()