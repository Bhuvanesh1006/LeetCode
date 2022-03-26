class Solution:
    def defangIPaddr(self, address: str) -> str:
        replacedadd=address.replace(".","[.]")
        return replacedadd
                