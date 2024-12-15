with open("TestCaseInput.txt", "r") as f:
    tc = [line.strip().split(",") for line in f]
print(tc)

with open("TestCaseOutput.txt", "r", encoding="utf-8") as f:
    eo = [line.strip() for line in f]
f.close()
print(eo) 