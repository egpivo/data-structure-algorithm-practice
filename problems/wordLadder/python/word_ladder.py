from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Find the shortest transformation sequence from beginWord to endWord.
        Uses BFS with pattern matching optimization.
        Time Complexity: O(M * N) where M is word length, N is wordList size
        Space Complexity: O(M * N)
        """
        if endWord not in wordList:
            return 0
        
        length = len(beginWord)
        words = set(wordList)
        words.add(beginWord)

        # Create pattern buckets: "h*t" -> ["hot", "hit", "hat", ...]
        buckets = defaultdict(list)
        for word in words:
            if len(word) != length:
                continue
            for i in range(length):
                pattern = word[:i] + "*" + word[i+1:]
                buckets[pattern].append(word)

        q = deque([(beginWord, 1)])
        seen = {beginWord}

        while q:
            w, step = q.popleft()

            if w == endWord:
                return step
            
            # Explore all patterns for current word
            for i in range(length):
                pattern = w[:i] + "*" + w[i+1:]
                
                # Process all words matching this pattern
                for neighbor in buckets[pattern]:
                    if neighbor not in seen:
                        seen.add(neighbor)  # Mark as seen before adding to queue
                        q.append((neighbor, step + 1))
                
                # Optimization: delete pattern after processing to avoid revisiting
                # This works because BFS guarantees shortest path
                del buckets[pattern]
        
        return 0


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Standard case
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    result1 = solution.ladderLength(beginWord1, endWord1, wordList1)
    print(f"Test 1: {result1} (Expected: 5)")
    assert result1 == 5, "Test 1 failed"
    
    # Test case 2: No transformation possible
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    result2 = solution.ladderLength(beginWord2, endWord2, wordList2)
    print(f"Test 2: {result2} (Expected: 0)")
    assert result2 == 0, "Test 2 failed"
    
    # Test case 3: Begin word equals end word
    beginWord3 = "a"
    endWord3 = "a"
    wordList3 = ["a", "b", "c"]
    result3 = solution.ladderLength(beginWord3, endWord3, wordList3)
    print(f"Test 3: {result3} (Expected: 1)")
    assert result3 == 1, "Test 3 failed"
    
    # Test case 4: Direct transformation (one step)
    beginWord4 = "hit"
    endWord4 = "hot"
    wordList4 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result4 = solution.ladderLength(beginWord4, endWord4, wordList4)
    print(f"Test 4: {result4} (Expected: 2)")
    assert result4 == 2, "Test 4 failed"
    
    # Test case 5: Longer transformation
    beginWord5 = "red"
    endWord5 = "tax"
    wordList5 = ["ted","tex","red","tax","tad","den","rex","pee"]
    result5 = solution.ladderLength(beginWord5, endWord5, wordList5)
    print(f"Test 5: {result5} (Expected: 4)")
    assert result5 == 4, "Test 5 failed"
    
    # Test case 6: End word not in wordList
    beginWord6 = "hit"
    endWord6 = "xyz"
    wordList6 = ["hot","dot","dog","lot","log"]
    result6 = solution.ladderLength(beginWord6, endWord6, wordList6)
    print(f"Test 6: {result6} (Expected: 0)")
    assert result6 == 0, "Test 6 failed"
    
    print("\nAll test cases passed!")
