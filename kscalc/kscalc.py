import score_guess
print score_guess
from score_guess import score_guess
import scipy.optimize as so


a = """ATGTCGGGGCGCGGCAAGGGCGGCAAGGGGCTCGGCAAGGGCGGCGCGAAGAGGCATCGC
AAGGTGCTCCGCGACAACATCCAGGGCATCACCAAGCCGGCGATCCGGAGGCTGGCGAGG
AGGGGCGGCGTGAAGCGCATCTCCGGGCTGATCTACGAGGAGACCCGCGGCGTGCTCAAG
ATCTTCCTCGAGAACGTCATCCGCGACGCCGTCACCTACACGGAGCACGCCCGCCGCAAG
ACCGTCACCGCCATGGACGTCGTCTACGCGCTCAAGCGCCAGGGCCGCACCCTCTACGGC
TTCGGCGGCTGA"""
b = """ATGTCAGGTCGTGGAAAAGGAGGCAAGGGGCTCGGTAAGGGAGGAGCGAAGCGTCATCGG
AAAGTTCTCCGTGATAACATTCAGGGAATCACTAAGCCGGCTATCCGGCGTCTTGCGAGA
AGAGGTGGAGTGAAGAGAATCAGCGGGTTGATCTACGAGGAGACCAGAGGCGTTTTGAAG
ATCTTCTTGGAGAACGTTATTCGCGATGCTGTGACGTACACTGAGCACGCCAGGCGGAAG
ACGGTGACCGCCATGGATGTTGTTTACGCCCTTAAGAGGCAGGGAAGGACTCTGTACGGG
TTCGGTGGTTAA"""

a = """ATGGCGGCGGCGGCGGCGGCGGCGGGGTACAGGGCGGAGGAGGAGTACGACTACCTGTTCAAGGTGGTGCTGATCGGGGACAGCGGCGTGGGGAAGTCGAACCTGCTGTCGCGGTTCGCGCGGGACGAGTTCAGCCTGGAGACCAGGTCCACCATCGGCGTCGAGTTCGCCACCAAGACCGTCCGCGTCGACGACAGGCTCGTCAAGGCCCAGATCTGGGACACCGCCGGCCAAGAGAGGTACCGCGCCATCACGAGCGCCTACTACCGCGGCGCGGTGGGCGCGCTGGTGGTGTACGACGTGACGCGCCGCATCACGTTCGAGAACGCGGAGCGGTGGCTCAAGGAGCTCCGCGACCACACGGACGCCAACATCGTCGTCATGCTCGTGGGCAACAAGGCCGACCTGCGCCACCTCCGCGCCGTCCCCGCGGAGGACGCCAGGGCGTTCGCCGAGGCGCACGGGACCTTCTCCATGGAGACGTCGGCGCTGGAGGCCACCAACGTGGAGGGCGCCTTCACCGAGGTGCTCGCGCAGATCTACCGCGTCGTCAGCCGGAACGCGCTCGACATCGGCGACGACCCCGCCGCGCCGCCCCGGGGGCGGACCATCGACGTCAGCGCCAAGGATGACGCCGTCACCCCCGTGAACAGCTCAGGGTGCTGCTCGTCTTGA"""
b = """---------------ATGGCGTCGGGGTACCGCGCGGAGGAGGAGTACGACTACCTGTTCAAGGTGGTGCTGATCGGGGACAGCGGCGTGGGCAAGTCGAACCTGCTGTCGCGGTTCGCCAGGGACGAGTTCAGCCTCGAGACCAGGTCCACCATCGGCGTCGAGTTCGCCACCAAGACCGTCCAGGTCGACGACAAGCTCGTCAAGGCGCAGATCTGGGACACCGCCGGGCAGGAGAGGTACCGCGCCATCACGAGCGCATACTACCGCGGCGCGGTGGGCGCGCTGGTGGTGTACGACGTGACCCGCCGCATCACCTTCGACAACGCCGAGCGCTGGCTGCGGGAGCTGCGGGACCACACGGACGCCAACATCGTGGTCATGCTGGTGGGCAACAAGGCCGACCTGCGCCACCTCCGCGCCGTGACGCCCGAGGACGCCGCGGCCTTCGCGGAGCGGCACGGCACCTTCTCCATGGAGACGTCGGCGCTGGACGCCACCAACGTCGACCGCGCCTTCGCCGAGGTGCTCCGCCAGATCTACCACGTCGTCAGCCGGAACGCGCTCGACATCGGGGAGGACCCCGCCGCGCCGCCCAGGGGAAAGACCATCGACGTCGGCGCCGCCAAGGACGAGGTCTCCCCCGTGAATACGGGCGGCTGCTGCTCGGCTTAG"""


def mleks(_seqa, _seqb):

    # we only look at the 3rd basepair.
    seqa = _seqa[2::3].upper()
    seqb = _seqb[2::3].upper()

    ab = [sab for sab in zip(seqa, seqb) if not "-" in sab]
    seqa = "".join([s[0] for s in ab])
    seqb = "".join([s[1] for s in ab])

    D = sum([aa != bb for aa, bb in zip(seqa, seqb)])

    seqab = seqa + seqb
    slen = len(seqab)/2

    scores = {}
    # give the optimizer the best guess from this range.
    for guess in (0.3, 0.5, 0.75, 1.1, 1.5):
        scores[guess] = score_guess(guess, seqab, D, slen)

    best_guess = sorted(scores.items(), key=lambda a: (a[1], a[0]))[0][0]
    def fnopt(ks_guess):
        return score_guess(ks_guess[0], seqab, D, slen)
    r = so.fmin(fnopt, best_guess, args=(), disp=True, 
                xtol=0.1, maxfun=20)
    return r[0]


print mleks(a.replace("\n", ""), b.replace("\n", ""))
print "trying again"
print mleks(a.replace("\n", ""), b.replace("\n", ""))
print "trying again"
print mleks(a.replace("\n", ""), b.replace("\n", ""))