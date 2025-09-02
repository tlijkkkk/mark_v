from typing import List, Dict
from collections import defaultdict
import re

class Solution:
    def find_dup_file_in_sys(self, paths: List[str]) -> List[List[str]]:
        map: Dict[str, List[str]] = defaultdict(list)
        for path in paths:
            parts: List[str] = path.split()
            root = parts[0]
            for i in range(1, len(parts)):
                m = re.match(rf"(.*)\((.*)\)", parts[i])
                map[m.group(2)].append(rf"{root}/{m.group(1)}")
        
        return [files for files in map.values() if len(files) > 1]

