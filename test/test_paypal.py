import unittest
import paypal

class TestExpressCheckout(unittest.TestCase):

    def setUp(self):
        self.ec = paypal.ExpressCheckout("sdk-three_api1.sdk.com",
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

    # def test_set_express_checkout_request(self):
    #     sample_true = """
    #         METHOD=SetExpressCheckout
    #         VERSION=XX.0
    #         USER=sdk-three_api1.sdk.com
    #         PWD=QFZCWN5HZM8VBG7Q
    #         SIGNATURE=A-IzJhZZjhg29XQ2qnhapuwxIDzyAZQ92FRP5dqBzVesOkzbdUONzmOU
    #         PAYMENTREQUEST_0_AMT=20.00
    #         PAYMENTREQUEST_0_CURRENCYCODE=BRL
    #         RETURNURL=http://www.meuurl.com/retorno
    #         CANCELURL=http://www.meuurl.com/cancel
    #         PAYMENTREQUEST_0_PAYMENTACTION=Sale
    #     """
    #     should_be_correct = self.ec.set_express_checkout_request("20.00", "BRL",
    #         "http://www.meuurl.com/retorno", "http://www.meuurl.com/cancel")
    #     self.assertEqual(sample_true, should_be_correct)



if __name__ == "__main__":
    unittest.main()