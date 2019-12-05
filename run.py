import requests
#rest_site = 'https://test-vaccinecodeset.cdc.gov/SymedicalDistributionREST/api/distributionext/'
rest_site = 'https://vaccinecodeset.cdc.gov/SymedicalDistributionREST/api/distributionext/'
#mnemonic = 'TEST_JDI_1'
mnemonic = 'AIRA_JDI'
#mnemonic = 'CA_DEV_TEST'
node_id = "2477d315-3d78-e911-85fc-4a5887b71b8c"
#node_id = "0e826259-5e5c-e911-85f9-3eb3d3152801"


response = requests.get(rest_site+'available/'+mnemonic)

print(response.text)

package_uids = []
for k in response.json()['PackageItems']:
    package_uids.append(k['PackageUID'])

json = {
    "distributionGroupMnemonic": mnemonic,
    "distributionNodeUID": node_id,
    "userName": "chris",
    "ApplyStateID": 2,
}

#for package_uid in package_uids:
#    print(package_uid)
#    json = {
#        "distributionGroupMnemonic": mnemonic,
#        "distributionPackageUID": package_uid,
#        #"distributionNodeUID": "0e826259-5e5c-e911-85f9-3eb3d3152801",
#        "distributionNodeUID": "2477d315-3d78-e911-85fc-4a5887b71b8c",
#        "userName": "chris",
#        "ApplyStateID": 2,
#    }
#
#    print("downloadstate")
#    response = requests.post(
#        rest_site+'downloadstate',
#        json=json,
#    )
#    print(response.json())
#
#    print("unsubscribe")
#    response = requests.post(
#        rest_site+'unsubscribe',
#        json=json,
#    )
#    print(response.json())
#
#    print("applystate")
#    response = requests.post(
#        rest_site+'applystate',
#        json=json,
#    )
#    print(response.json())
#
#    print("subscribe")
#    response = requests.post(
#        rest_site+'subscribe',
#        json=json,
#    )
#    print(response.json())

if json:
    print("pending")
    response = requests.post(
        rest_site+'pending/'+mnemonic,
        json=json,
    )
    print(response.json())
