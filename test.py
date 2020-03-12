import numpy as np

n = np.array(
    [[["A"],
     ["A"],
     ["A"]],
    [["B"],
     ["B"],
     ["B"]],
    [["C"],
     ["C"],
     ["C"]]])

print(n)
print()
print("================================================================================")
print()
for r in range(3):
    np.random.shuffle(n[r,:,:])
print(n)