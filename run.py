import requests
rest_site = 'https://test-vaccinecodeset.cdc.gov/SymedicalDistributionREST/api/distributionext/'
#rest_site = 'https://vaccinecodeset.cdc.gov/SymedicalDistributionREST/api/distributionext/'
mnemonic = 'TEST_JDI_1'
#mnemonic = 'AIRA_JDI'
response = requests.get(rest_site+'available/'+mnemonic)

#print(response.text)

package_uids = []
for k in response.json()['PackageItems']:
    package_uids.append(k['PackageUID'])

for package_uid in package_uids:
    print(package_uid)
    json = {
        "distributionGroupMnemonic": "TEST_JDI_1",
        "distributionPackageUID": package_uid,
        "distributionNodeUID": "0e826259-5e5c-e911-85f9-3eb3d3152801",
        "userName": "chris",
        "ApplyStateID": 2,
    }

    print("downloadstate")
    response = requests.post(
        'https://test-vaccinecodeset.cdc.gov/SymedicalDistributionRESTTest/api/distributionext/downloadstate',
        json=json,
    )
    print(response.json())

    print("unsubscribe")
    response = requests.post(
        'https://test-vaccinecodeset.cdc.gov/SymedicalDistributionRESTTest/api/distributionext/unsubscribe',
        json=json,
    )
    print(response.json())

    print("applystate")
    response = requests.post(
        'https://test-vaccinecodeset.cdc.gov/SymedicalDistributionRESTTest/api/distributionext/applystate',
        json=json,
    )
    print(response.json())

    print("subscribe")
    response = requests.post(
        'https://test-vaccinecodeset.cdc.gov/SymedicalDistributionRESTTest/api/distributionext/subscribe',
        json=json,
    )
    print(response.json())

print("pending")
response = requests.post(
    #'https://test-vaccinecodeset.cdc.gov/SymedicalDistributionRESTTest/api/distributionext/pending/TEST_JDI_1',
    'https://test-vaccinecodeset.cdc.gov/SymedicalDistributionREST/api/distributionext/pending/TEST_JDI_1',
    json=json,
)
print(response.json())
for pack in response.json()['Packages']:
    print(pack.keys())
    print(pack['PackageName'])
