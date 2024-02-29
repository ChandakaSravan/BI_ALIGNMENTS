class Solution:
    def local_alignment(self, sequence_A: str, sequence_B: str, substitution: dict, gap: int) -> [tuple]:
        # initialize matrix
        n, m = len(sequence_A), len(sequence_B)
        D = [[0] * (m+1) for i in range(n+1)]
        arrow = [[[] for j in range(m+1)] for i in range(n+1)]
        
        # fill matrix
        max_score = 0
        max_values = []
        for i in range(1, n+1):
            for j in range(1, m+1):
                match = D[i-1][j-1] + substitution[sequence_A[i-1]][sequence_B[j-1]]
                delete = D[i-1][j] + gap
                insert = D[i][j-1] + gap
                D[i][j] = max(0, match, delete, insert)
                if D[i][j] == match:
                    arrow[i][j].append("↖")
                if D[i][j] == delete:
                    arrow[i][j].append("↑")
                if D[i][j] == insert:
                    arrow[i][j].append("←")
                if D[i][j] > max_score:
                    max_score = D[i][j]
                    max_values = [(i,j)]
                elif D[i][j] == max_score:
                    max_values.append((i,j))
        
                # print matrix with arrows and headers
        print("Directional Matrix:")
        print(f"         |{'      '.join(sequence_B)}")
        for i in range(n+1):
            print(f"+{'-'*3}+{'-'*2}" * (m+1) + "+")
            if i == 0:
                print(" ", end="")
            else:
                print(sequence_A[i-1], end=" ")
            for j in range(m+1):
                print(f"|{D[i][j]:>3}{''.join(arrow[i][j]):>2}", end=" ")
            print("|")
        print(f"+{'-'*3}+{'-'*2}" * (m+1) + "+")
        

        
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



#solution = Solution()

#sequence_A = 'TCGTGA'
#sequence_B = 'ATA'
#substitution = {
 #   'A': {'A': 4, 'G': -1, 'T': -1, 'C': -1},
  #  'G': {'A': -1, 'G': 4, 'T': -1, 'C': -1},
   # 'T': {'A': -1, 'G': -1, 'T': 4, 'C': -1},
    #'C': {'A': -1, 'G': -1, 'T': -1, 'C': 4}
#}
#gap = -3

#alignments = solution.local_alignment(sequence_A, sequence_B, substitution, gap)

#for alignment in alignments:
 #   print(alignment)




