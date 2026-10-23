class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        result = ""
        for s in strs:
            res.append(f"{len(s)}#{s}")

        result = "".join(res)
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        i =0 
        j = 0
        decoded_strs = []
        while i <len(s):
            length= ""
            j=i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])

            i = j+1
            temp_word = s[i:i+length]
            decoded_strs.append(temp_word)

            print(decoded_strs)
            i = i+length
            
        return decoded_strs
