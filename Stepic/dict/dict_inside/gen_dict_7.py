words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {words[c]: [ord((words[c])[j]) for j in range(len(words[c]))] for c in range(len(words))}

print(result)

#ord('A')
