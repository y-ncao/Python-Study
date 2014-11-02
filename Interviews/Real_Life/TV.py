# Interview with TrueVault
# from truevault import truevault
api_key = '349713ce-6405-4b8e-b6ad-6ef7668f1c1f'
vault_id = '23d563f0-3be7-4b3a-865a-dfce1cb2db71'
import requests
from requests.auth import HTTPBasicAuth

class TrueVault_API(object):
    def __init__(self, key):
        self.valut_list = []
        self.key = key

    def Vault(self, id):
        return Vault_Class(id, self.key)

class Vault_Class(object):
    def __init__(self, id=None, key=None, name=None):
        r = requests.get('https://api.truevault.com/v1/vaults/%s' % id, auth=HTTPBasicAuth(api_key, ''))
        print r
        """
        if r.status_code == 200:
            pass
        else:
            r = requests.get('https://api.truevault.com/v1/vaults/%s' % id)
        """
        response = r.json()
        self.vault = response.get('vault', None)
        self.name = None
        if self.vault:
            self.id = self.vault.get('id')
            self.name = self.vault.get('name')


    def Document(self, doc_id=None):
        return Document_Class(self.id, doc_id)

class Document_Class(object):
    def __init__(self, vault_id, doc_id=None):
        if doc_id is None:
            r = requests.post('https://api.truevault.com/v1/vaults/%s/documents' % vault_id, auth=HTTPBasicAuth(api_key, ''))
            response = r.json()
            print response
            self.id = response.get('document_id')
        """
        r = requests.get('https://api.truevault.com/v1/vaults/%s/documents' % vault_id, auth=HTTPBasicAuth(api_key, ''))
        response = r.json()
        self.id = response.get('document_id')
        """
    def save(self):
        if self.doc is None:
            pass


my_tv = TrueVault_API(api_key)

test_vault = my_tv.Vault(vault_id)

print test_vault.name


new_document = test_vault.Document()


print new_document.id # something
"""
existing_doc = test_vault.Document(new_document.id)
new_document.id == existing_doc.id

doc = my_tv.Vault(some_id).Document(doc_id)
"""
