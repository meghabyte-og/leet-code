from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        root = TrieNode()

        # returns True if idx1 is a better choice than idx2
        def better(idx1, idx2):
            if idx2 == -1:
                return True

            if len(wordsContainer[idx1]) < len(wordsContainer[idx2]):
                return True

            if len(wordsContainer[idx1]) == len(wordsContainer[idx2]):
                return idx1 < idx2

            return False

        for i, word in enumerate(wordsContainer):
            rev = word[::-1]

            node = root

            if better(i, node.best_index):
                node.best_index = i

            for ch in rev:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if better(i, node.best_index):
                    node.best_index = i

        ans = []

        # Process queries
        for word in wordsQuery:
            rev = word[::-1]

            node = root
            res = root.best_index

            for ch in rev:
                if ch not in node.children:
                    break

                node = node.children[ch]
                res = node.best_index

            ans.append(res)

        return ans