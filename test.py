import requests
import unittest

rest_site = 'https://test-vaccinecodeset.cdc.gov/SymedicalDistributionREST/api/distributionext/'
mnemonic = 'TEST_JDI_1'

class TestSymedical(unittest.TestCase):

    def test_loop_1(self):
        # unsubscribe then resubscribe to make test repeatable
        self.unsubscribe()
        self.subscribe()

    def test_available(self):
        response = requests.get(rest_site+'available/'+mnemonic)
        with open('fixtures/available.txt', 'r') as f:
            expected = f.read().strip()
        actual = response.text
        self.assertEqual(expected, actual)
        self.assertEqual(200, response.status_code)

    def test_pending(self):
        response = requests.post(
            rest_site+'pending/'+mnemonic,
            json={},
        )
        with open('fixtures/pending.txt', 'r') as f:
            expected = f.read().strip()
        actual = response.text
        self.assertEqual(expected, actual)
        self.assertEqual(200, response.status_code)

    def test_downloadstate(self):
        json = {
            "distributionGroupMnemonic": mnemonic,
            "distributionPackageUID": "b554c854-ce66-e911-a18a-0e9e89df70ac",
        }
        response = requests.post(
            rest_site+'downloadstate',
            json=json,
        )
        with open('fixtures/standard.txt', 'r') as f:
            expected = f.read().strip()
        actual = response.text
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, actual)

    def test_applystate(self):
        json = {
            "distributionGroupMnemonic": mnemonic,
            "distributionNodeUID": "24cea19d-075b-e911-85f9-5ef1864b1132",
            "distributionPackageUID": "b554c854-ce66-e911-a18a-0e9e89df70ac",
        }
        response = requests.post(
            rest_site+'applystate',
            json=json,
        )
        with open('fixtures/standard.txt', 'r') as f:
            expected = f.read().strip()
        actual = response.text
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, actual)

    def unsubscribe(self):
        json = {
            "distributionGroupMnemonic": mnemonic,
            "distributionPackageUID": "b554c854-ce66-e911-a18a-0e9e89df70ac",
            "userName": "chris"
        }
        response = requests.post(
            rest_site+'unsubscribe',
            json=json,
        )
        with open('fixtures/standard.txt', 'r') as f:
            expected = f.read().strip()
        actual = response.text
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, actual)

    def subscribe(self):
        json = {
            "distributionGroupMnemonic": mnemonic,
            "distributionNodeUID": "24cea19d-075b-e911-85f9-5ef1864b1132",
            "distributionPackageUID": "b554c854-ce66-e911-a18a-0e9e89df70ac",
            "userName": "chris"
        }
        response = requests.post(
            rest_site+'subscribe',
            json=json,
        )
        with open('fixtures/standard.txt', 'r') as f:
            expected = f.read().strip()
        actual = response.text
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
