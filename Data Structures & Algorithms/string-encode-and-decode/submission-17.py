class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            temp = f"{len(s)}#{s}"
            encoded_str = encoded_str+temp
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        print(len(s))
        while i <len(s)-1:
            temp_word = ""

            j=i
            len_s = ""
            while s[j] != "#":
                if j >=len(s):
                    break

                len_s = len_s+s[j]
                j+=1
            print("len_s, ",len_s)
            len_num = len(len_s)
            len_s = int(len_s)

            temp_word = s[i+len_num:i+len_num+len_s+1]
            decoded_strs.append(temp_word[1:])
            i = i+len_num+len_s+1
            print(decoded_strs)
            print(i)
        return decoded_strs
