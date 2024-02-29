import numpy as np

def local_alignment_with_matrix(s1, s2, S, gap_penalty):
    n, m = len(s1), len(s2)
    D = np.zeros((n+1, m+1), dtype=int)
    max_score = 0
    alignments = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            match = D[i-1,j-1] + S[s1[i-1]][s2[j-1]]
            delete = D[i-1,j] + gap_penalty
            insert = D[i,j-1] + gap_penalty
            D[i,j] = max(match, delete, insert, 0)
            if D[i,j] > max_score:
                max_score = D[i,j]
                alignments = [(i, j)]
            elif D[i,j] == max_score:
                alignments.append((i, j))
    results = []
    for end_i, end_j in alignments:
        i, j = end_i, end_j
        local_s1, local_s2 = '', ''
        while D[i,j] != 0:
            if D[i-1,j-1] + S[s1[i-1]][s2[j-1]] == D[i,j]:
                local_s1 = s1[i-1] + local_s1
                local_s2 = s2[j-1] + local_s2
                i -= 1
                j -= 1
            elif D[i-1,j] + gap_penalty == D[i,j]:
                local_s1 = s1[i-1] + local_s1
                local_s2 = '-' + local_s2
                i -= 1
            elif D[i,j-1] + gap_penalty == D[i,j]:
                local_s1 = '-' + local_s1
                local_s2 = s2[j-1] + local_s2
                j -= 1
        results.append((max_score, local_s1, local_s2, D))
    return results

# Concatenate first and last name
first_name = "sravan"
last_name = "chandaka"
concatenated_name = first_name + last_name
print(concatenated_name)

# Set of semi-matches
semi_matches = set(concatenated_name)

# Create custom substitution dictionary
S = {}
for c in semi_matches.union(set("abcdefghijklmnopqrstuvwxyz")):
    S[c] = {}
    for d in semi_matches.union(set("abcdefghijklmnopqrstuvwxyz")):
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
    for c in S.keys():
        f.write(", '{}'".format(c))
    f.write("],\n")
    # write each row of the matrix
    for c in S.keys():
        f.write("[ '{}'".format(c))
        for d in S[c].values():
            f.write(", '{:2}'".format(str(d)))
        f.write("],\n")

# Pretty print S
S_list = [['_'] + list(S.keys())] + [[k] + list(v.values()) for k, v in S.items()]
print(f"S={S_list}")
print(np.matrix(S_list))


# Test the local alignment function with the concatenated name and pangram
# Run local alignment function with custom S and gap penalty of -2
s1 = concatenated_name
s2 = "thequickbrownfoxjumpsoverthelazydog"
max_score, local_s1, local_s2, D = local_alignment_with_matrix(s1, s2, S, -2)

# Write matrix D to file
with open("1002059166_D.txt", "w") as f:
    for row in D:
        f.write(" ".join([str(x) for x in row]) + "\n")

# Print output tuple
print("Maximum score:", max_score)
print("Local alignment:")
print(local_s1)
print(local_s2)

solution = Solution()
sequence_A = concatenated_name
sequence_B = "thequickbrownfoxjumpsoverthelazydog"
gap = -2
alignments = solution.local_alignment(sequence_A, sequence_B, S, gap)

for alignment in alignments:
    print(alignment)
    print()

