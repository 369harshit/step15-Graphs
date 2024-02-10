from collections import deque
def findLadders(startWord, targetWord, wordList):
    wordSet = set(wordList)
    if targetWord not in wordSet:
        return []

    result = []
    queue = deque([(startWord, [startWord])])

    while queue:
        currentWord, path = queue.popleft()

        for i in range(len(currentWord)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = currentWord[:i] + char + currentWord[i+1:]

                if nextWord == targetWord:
                    result.append(path + [targetWord])
                elif nextWord in wordSet:
                    wordSet.remove(nextWord)
                    queue.append((nextWord, path + [nextWord]))

    return result

# Example usage
startWord = "der"
targetWord = "dfs"
wordList = {"des", "der", "dfr", "dgt", "dfs"}

result = findLadders(startWord, targetWord, wordList)
for path in result:
    print(" ".join(path))
