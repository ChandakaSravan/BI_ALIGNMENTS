class Solution:
    def global_alignment(self, sequence_A: str, sequence_B: str, substitution: dict, gap: int) -> [tuple]:
        # initialize matrix
        n, m = len(sequence_A), len(sequence_B)
        D = [[0] * (m+1) for i in range(n+1)]
        for i in range(1, n+1):
            D[i][0] = D[i-1][0] + gap
        for j in range(1, m+1):
            D[0][j] = D[0][j-1] + gap
        
        # fill matrix
        for i in range(1, n+1):
            for j in range(1, m+1):
                match = D[i-1][j-1] + substitution[sequence_A[i-1]][sequence_B[j-1]]
                delete = D[i-1][j] + gap
                insert = D[i][j-1] + gap
                D[i][j] = max(match, delete, insert)
        
        # traceback
        alignments = []
        alignment = ["", ""]
        i, j = n, m
        while i > 0 or j > 0:
            if i > 0 and j > 0 and D[i][j] == D[i-1][j-1] + substitution[sequence_A[i-1]][sequence_B[j-1]]:
                alignment[0] = sequence_A[i-1] + alignment[0]
                alignment[1] = sequence_B[j-1] + alignment[1]
                i -= 1
                j -= 1
            elif i > 0 and D[i][j] == D[i-1][j] + gap:
                alignment[0] = sequence_A[i-1] + alignment[0]
                alignment[1] = "-" + alignment[1]
                i -= 1
            else:
                alignment[0] = "-" + alignment[0]
                alignment[1] = sequence_B[j-1] + alignment[1]
                j -= 1
            if i == 0 and j == 0:
                alignments.append(tuple(alignment))
            elif i == 0:
                alignments.append((alignment[0], "-" * j + alignment[1]))
            elif j == 0:
                alignments.append(("-" * i + alignment[0], alignment[1]))
        
        return alignments[::-1]

    s = Solution()
    seq_A = "gata"
    seq_B = "ctag"
    substitution = {'a': {'a':1,'t':-1,'c':-1,'g':-1}, 't': {'a':-1,'t':1,'c':-1,'g':-1}, 'c': {'a':-1,'t':-1,'c':1,'g':-1}, 'g': {'a':-1,'t':-1,'c':-1,'g':1}}
    gap = -2
    alignments = s.global_alignment(seq_A, seq_B, substitution, gap)
    print(alignments)

