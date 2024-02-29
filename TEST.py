s = 1002059166_NW()
seq_A = "gata"
seq_B = "ctag"
substitution = {'a': {'a':1,'t':-1,'c':-1,'g':-1}, 't': {'a':-1,'t':1,'c':-1,'g':-1}, 'c': {'a':-1,'t':-1,'c':1,'g':-1}, 'g': {'a':-1,'t':-1,'c':-1,'g':1}}
gap = -2
alignments = s.global_alignment(seq_A, seq_B, substitution, gap)
print(alignments)
