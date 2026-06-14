class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def chars_counts(s: str):
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            counts = {c: 0 for c in alphabet}
            for c in s:
                counts[c] += 1
            return tuple(counts.values())
        
        d = {}
        for s in strs:
            counts = chars_counts(s)
            if counts in d:
                d[counts].append(s)
            else:
                d[counts] = [s]

        return list(d.values())