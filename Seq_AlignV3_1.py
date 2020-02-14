import sys

stdoutOrigin = sys.stdout
sys.stdout = open("results.txt", "w")

match = 6
mismatch = -4
gap = -3

seq1 = "CGAUCAC"
seq2 = "CAUCGAC"
seq1Length = len(seq1)
seq2Length = len(seq2)
#print(seq1Length)
#print(seq2Length)
seq1_ = 0
seq2_ = 0

M = [[0 for i in range(len(seq1) + 1)] for j in range(len(seq2) + 1)]
MO = [["S" for w in range(len(seq1) + 1)] for v in range(len(seq2) + 1)]

for i in range(1, seq1Length + 1):
    M[0][i] = i * gap

for i in range(1, seq2Length + 1):
    M[i][0] = i * gap
# the y var moves left to right while the x var moves up and down
for x in range(1, seq2Length + 1):
    for y in range(1, seq1Length + 1):
        let1 = seq1[seq1_]
        let2 = seq2[seq2_]
        #print(let1, let2)

        if (let1 == let2):
            hold = M[x - 1][y - 1]
            hold += match
            M[x][y] = hold
        else:
            hold = M[x - 1][y - 1]
            hold += mismatch
            M[x][y] = hold
        MO[x][y] = "D"

        temp = M[x][y - 1] + gap
        if temp > M[x][y]:
            M[x][y] = temp
            MO[x][y] = "L"

        temp = M[x - 1][y] + gap
        if temp > M[x][y]:
            M[x][y] = temp
            MO[x][y] = "U"
        seq1_ += 1
    seq1_ = 0
    seq2_ += 1

alignScore = M[seq2Length][seq1Length]
# print(alignScore)

for row in M:
    print(row)
print()

for row in MO:
    print(row)
print()

x = seq2Length
y = seq1Length

#character lists to hold the reversed characters of the trace back
seq1Final = []
seq2Final = []

#Initialize backtrack_ so that the while loop can start
backtrack_ = "I"

while (backtrack_ != "S"):
    backtrack_ = MO[x][y]
    #print(backtrack_)
    if backtrack_ == "D":
        x -= 1
        y -= 1
        seq1Final.append(seq1[y])
        seq2Final.append(seq2[x])
    elif backtrack_ == "L":
        y -= 1
        seq2Final.append("-")
        seq1Final.append(seq1[y])
    elif backtrack_ == "U":
        x -= 1
        seq1Final.append("-")
        seq2Final.append(seq2[x])
#print(seq1Final)
#print(seq2Final)

seq1Print = []
seq2Print = []

for i in range(0, len(seq1Final)):
    seq1Print.append(seq1Final.pop())

for i in range(0, len(seq2Final)):
    seq2Print.append(seq2Final.pop())

print(seq1Print)
print(seq2Print)
print("Optimal alignment score is: " + alignScore.__str__())

sys.stdout.close()
sys.stdout = stdoutOrigin