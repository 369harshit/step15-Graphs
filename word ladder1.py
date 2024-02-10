from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])

    while queue:
        currentWord, length = queue.popleft()

        for i in range(len(currentWord)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = currentWord[:i] + char + currentWord[i+1:]

                if nextWord == endWord:
                    return length + 1

                if nextWord in wordSet:
                    wordSet.remove(nextWord)
                    queue.append((nextWord, length + 1))

    return 0

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

result = ladderLength(beginWord, endWord, wordList)
print(result)
