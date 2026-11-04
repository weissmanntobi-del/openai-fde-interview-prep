import unittest
from examples.eval_lab.run_eval import evaluate
from examples.eval_lab.policy import propose


class EvalLabTests(unittest.TestCase):
    def test_fixtures_load(self):
        report = evaluate()
        self.assertEqual(report['total'], 8)
        self.assertEqual(report['passed'], 7)  # exercise: baseline has one known failure

    def test_boundary_amount(self):
        self.assertEqual(propose({'amount':100,'has_receipt':True,'fraud_flag':False}), 'approve')
        self.assertEqual(propose({'amount':101,'has_receipt':True,'fraud_flag':False}), 'review')

    def test_missing_receipt(self):
        self.assertEqual(propose({'amount':10,'has_receipt':False,'fraud_flag':False}), 'review')

    def test_no_money_movements(self):
        self.assertIn(propose({'amount':5,'has_receipt':True,'fraud_flag':False}), {'approve','review','deny'})
        # A proposed 'approve' is ONLY a label, never an executed tool call.


if __name__ == '__main__':
    unittest.main()
