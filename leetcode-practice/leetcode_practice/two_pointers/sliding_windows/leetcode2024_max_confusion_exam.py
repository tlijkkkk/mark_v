class Solution:
    def max_confusion_exam(self, answer_key: str, k: int) -> int:
        i = 0
        t_count = 0
        f_count = 0
        result = 0

        for j in range(len(answer_key)):
            if answer_key[j] == 'T':
                t_count += 1
            else:
                f_count += 1

            while min(t_count, f_count) < k:
                if answer_key[i] == 'T':
                    t_count -=  1
                else:
                    f_count -= 1
                i +=1
            
            result = max(result, j - i + 1)
        
        return result

