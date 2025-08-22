class Solution:
    def natural_order_string_compare(self, str1: str, str2: str) -> int:
        i, j = 0, 0

        while i < len(str1) and j < len(str2):
            if str1[i].isdigit() and str2[j].isdigit():
                tmp = ""
                while i < len(str1) and str1[i].isdigit():
                    tmp += str1[i]
                    i += 1
                
                tmp2 = ""
                while j < len(str2) and str2[j].isdigit():
                    tmp2 += str2[j]
                    j += 1

                if int(tmp) < int(tmp2):
                    return -1
                elif int(tmp) > int(tmp2):
                    return 1
                
                continue
            
            if str1[i].isalpha() and str2[j].isalpha():
                if str1[i] < str2[j]:
                    return -11
                elif str1[i] > str2[j]:
                    return 11
            elif str1[i].isdigit():
                return -111
            else:
                return 111

            i += 1
            j += 1
        
        if i == len(str1) and j == len(str2):
            return 0
        elif i == len(str1):
            return -1111
        else:
            return 1111