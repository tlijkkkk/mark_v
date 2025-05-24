from typing import List


class Solution:
    def divide_players_into_teams_equal_skill(self, skill: List[int]) -> int:
        skill_sorted = sorted(skill)

        i = 0
        j = len(skill_sorted) - 1
        equal_score = skill_sorted[i] + skill_sorted[j]
        chemistry = 0

        while i < j:
            if skill_sorted[i] + skill_sorted[j] != equal_score:
                return -1
            chemistry += skill_sorted[i] * skill_sorted[j]
            i += 1
            j -= 1

        return chemistry

        