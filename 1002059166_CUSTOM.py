import numpy as np

# Concatenate first and last name
first_name = "sravan"
last_name = "chandaka"
concatenated_name = first_name + last_name
#print(concatenated_name)

# Set of semi-matches
semi_matches = set(concatenated_name)

# Create custom substitution dictionary
S = {}
for c in "abcdefghijklmnopqrstuvwxyz":
    S[c] = {}
    for d in "abcdefghijklmnopqrstuvwxyz":
        if c == d:
            S[c][d] = 2  # match
        elif c in concatenated_name and d in concatenated_name:
            S[c][d] = 1  # semi-match
        else:
            S[c][d] = -1  # mismatch

# Write S to file
with open("1002059166_S.txt", "w") as f:
    # write header row
    f.write("[['_'")
    for c in "abcdefghijklmnopqrstuvwxyz":
        f.write(", '{}'".format(c))
    f.write("],\n")
    # write each row of the matrix
    for c in "abcdefghijklmnopqrstuvwxyz":
        f.write("[ '{}'".format(c))
        for d in "abcdefghijklmnopqrstuvwxyz":
            f.write(", '{:2}'".format(str(S[c][d])))
        f.write("],\n")
    f.write("]")

# Pretty print S
#S_list = [['_'] + list(S.keys())] + [[k] + list(v.values()) for k, v in S.items()]
#print(f"S= {S_list}")
#print(np.matrix(S_list))



class Solution:
    def local_alignment(self, sequence_A: str, sequence_B: str, substitution: dict, gap: int) -> [tuple]:
        # initialize matrix
        n, m = len(sequence_A), len(sequence_B)
        D = [[0] * (m+1) for i in range(n+1)]
        arrow = [['' for j in range(m+1)] for i in range(n+1)]
        outMatrix = []
        out0 = [' ', ' ']
        for j in range(m):
            out0.append(sequence_B[j])
        outMatrix.append(out0)
        out1 = [' ']
        for j in range(m+1):
            out1.append(str(D[0][j]) + ' ')
        outMatrix.append(out1)
        
        # fill matrix
        max_score = 0
        max_values = []
        for i in range(1, n+1):
            out1 = [sequence_A[i-1], '0']
            for j in range(1, m+1):
                match = D[i-1][j-1] + substitution[sequence_A[i-1]][sequence_B[j-1]]
                delete = D[i-1][j] + gap
                insert = D[i][j-1] + gap
                D[i][j] = max(0, match, delete, insert)
                if D[i][j] == match:
                    arrow[i][j] += '↖'
                if D[i][j] == delete:
                    arrow[i][j] += '↑'
                if D[i][j] == insert:
                    arrow[i][j] += '←'
                if D[i][j] > max_score:
                    max_score = D[i][j]
                    max_values = [(i,j)]
                elif D[i][j] == max_score:
                    max_values.append((i,j))
                out1.append(str(D[i][j])+arrow[i][j])
            outMatrix.append(out1)
        
                # print matrix with arrows and headers
      #  print("Directional Matrix:")
       # print(f"         |{'      '.join(sequence_B)}")
        #for i in range(n+1):
         #   print(f"+{'-'*3}+{'-'*2}" * (m+1) + "+")
          #  if i == 0:
           #     print(" ", end="")
            #else:
             #   print(sequence_A[i-1], end=" ")
            #for j in range(m+1):
             #   print(f"|{D[i][j]:>3}{''.join(arrow[i][j]):>2}", end=" ")
               

            #print("|")
        #print(f"+{'-'*3}+{'-'*2}" * (m+1) + "+")
        
        with open("1002059166_D.txt","w", encoding='utf-8') as f:
            for i in range(n+2):
                f.write('\t'.join([outMatrix[i][j] for j in range(m+2)]) + '\n')


        
        # traceback
        
        def trace(max_index):
            alignments = []
            stack = [(max_index[0], max_index[1], "", "")]
            while stack:
                i, j, seqA, seqB = stack.pop()
                if D[i][j] == 0:
                    alignments.append((seqA[::-1], seqB[::-1]))
                    continue
                if i > 0 and j > 0 and D[i][j] == D[i-1][j-1] + substitution[sequence_A[i-1]][sequence_B[j-1]]:
                    stack.append((i-1, j-1, seqA + sequence_A[i-1], seqB + sequence_B[j-1]))
                if i > 0 and D[i][j] == D[i-1][j] + gap:
                    stack.append((i-1, j, seqA + sequence_A[i-1], seqB + "-"))
                if j > 0 and D[i][j] == D[i][j-1] + gap:
                    stack.append((i, j-1, seqA + "-", seqB + sequence_B[j-1]))
                
            return alignments
        
        tup = []
        
        for v in max_values:
            tup.append(trace(v))
        return tup


# Test the local alignment function with the concatenated name and pangram
# Run local alignment function with custom S and gap penalty of -2

solution = Solution()
sequence_A = concatenated_name
sequence_B = "thequickbrownfoxjumpsoverthelazydog"
gap = -2
alignments = solution.local_alignment(sequence_A, sequence_B, S, gap)
#print(D)
for alignment in alignments:
    print(alignment)

# Write matrix D to file
# Open file for writing




