class Solution:
    def global_alignment(self, sequence_A: str, sequence_B: str, substitution: dict, gap: int) -> [tuple]:
        # initialize matrix
        n, m = len(sequence_A), len(sequence_B)
        D = [[0] * (m+1) for i in range(n+1)]
        arrow = [[[] for j in range(m+1)] for i in range(n+1)]
        for i in range(1, n+1):
            D[i][0] = D[i-1][0] + gap
            arrow[i][0] = ["↑"]
        for j in range(1, m+1):
            D[0][j] = D[0][j-1] + gap
            arrow[0][j] = ["←"]
        
        # fill matrix
        for i in range(1, n+1):
            for j in range(1, m+1):
                match = D[i-1][j-1] + substitution[sequence_A[i-1]][sequence_B[j-1]]
                delete = D[i-1][j] + gap
                insert = D[i][j-1] + gap
                max_score = max(match, delete, insert)
                if max_score == match:
                    D[i][j] = match
                    arrow[i][j].append("↖")
                if max_score == delete:
                    D[i][j] = delete
                    arrow[i][j].append("↑")
                if max_score == insert:
                    D[i][j] = insert
                    arrow[i][j].append("←")
        
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
     
        
        alignments = []
        stack = [(n, m, "", "")]
        while stack:
            i, j, seqA, seqB = stack.pop()
            if i == 0 and j == 0:
                alignments.append((seqA[::-1], seqB[::-1]))
                continue
            if i > 0 and j > 0 and D[i][j] == D[i-1][j-1] + substitution[sequence_A[i-1]][sequence_B[j-1]]:
                stack.append((i-1, j-1, seqA + sequence_A[i-1], seqB + sequence_B[j-1]))
            if i > 0 and D[i][j] == D[i-1][j] + gap:
                stack.append((i-1, j, seqA + sequence_A[i-1], seqB + "-"))
            if j > 0 and D[i][j] == D[i][j-1] + gap:
                stack.append((i, j-1, seqA + "-", seqB + sequence_B[j-1]))
                
        return alignments
        
        
 
        
#s = Solution()
#seq_A = "gata"
#seq_B = "ctac"
#substitution = {'a': {'a':1,'t':-1,'c':-1,'g':-1}, 't': {'a':-1,'t':1,'c':-1,'g':-1}, 'c': {'a':-1,'t':-1,'c':1,'g':-1}, 'g': {'a':-1,'t':-1,'c':-1,'g':1}}
#gap = -2
#alignments = s.global_alignment(seq_A, seq_B, substitution, gap)
#print(alignments)
