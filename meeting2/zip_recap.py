llms = ["DeepSeek", "ChatGPT", "Claude", "Gemini", "Grok"]
costs = [6_500_000, 100_000_000, 12_000_000]

# for i in range(len(llms)):
#     print(llms[i], costs[i])

for model, cost in zip(llms, costs):
    print(model, cost)