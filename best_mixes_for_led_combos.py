#!/usr/bin/python

#run#	CCT	CRI	R9	CQS	Duv	lm/Wvis	LPW	Blue (%W)	Blue dom (nm)	Verde (%W)	Verde dom (nm)	Deep red (%W)	Deep red dom (nm)	nvsl219B-V1-E90 (%W)	x	y	Gamut-CRI	Gamut-D65	GAI	TLCI Qa	TLCI d	R1	R2	R3	R4	R5	R6	R7	R8	R9	R10	R11	R12	R13	R14	R15	Q1	Q2	Q3	Q4	Q5	Q6	Q7	Q8	Q9	Q10	Q11	Q12	Q13	Q14	Q15	
#1	3953	98	97	96	-0.0027	271	96.7	6.00	475	1.50	508	0	660	92.40	0.3806	0.3711	1.048	0.839	82	99	-0.5	99	99	97	99	99	97	98	99	97	98	98	87	99	98	98	98	99	98	98	98	99	97	98	96	92	92	98	98	99	100	
import sys;

field_types = [int, int, int, int, int, float, float, float, float, int, float, int, float, int, float, float, float, float, float, int, int, float, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, str]
    
class Mix:
    cct = 0
    def __init__(self, lineText, lineFound):
        self.lineText = lineText
        self.lineFound = lineFound
        run, self.cct, self.cri, dummyR9, self.cqs, self.duv, lpwVis, self.lpw, self.intenBlue, self.dwlBlue, self.intenVerde, self.dwlVerde, self.intenRed, self.dwlRed, self.intenWhite, self.x, self.y, self.gaCRI, self.gaCQS, self.gaiE, self.tlci, self.tlciD, self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.r8, self.r9, self.r10, self.r11, self.r12, self.r13, self.r14, self.r15, self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9, self.q10, self.q11, self.q12, self.q13, self.q14, self.q15, junk = [field_types[i](l) for i, l in enumerate(lineText.split("\t"))]
        #print((parse(l) for l in lineText.split("\t")))
        #print(        str(type(self.cct)) + '\t' + str(type(self.cri)) + '\t' + str(type(self.cqs)) + '\t' + str(type(self.duv)) + '\t' + str(type(self.lpw)) + '\t' + str(type(self.intenBlue)) + '\t' + str(type(self.dwlBlue)) + '\t' + str(type(self.intenVerde)) + '\t' + str(type(self.dwlVerde)) + '\t' + str(type(self.intenRed)) + '\t' + str(type(self.dwlRed)) + '\t' + str(type(self.intenWhite)) + '\t' + str(type(self.x)) + '\t' + str(type(self.y)) + '\t' + str(type(self.gaCRI)) + '\t' + str(type(self.gaCQS)) + '\t' + str(type(self.gaiE)) + '\t' + str(type(self.tlci)) + '\t' + str(type(self.tlciD)) + '\t' + str(type(self.r1)) + '\t' + str(type(self.r2)) + '\t' + str(type(self.r3)) + '\t' + str(type(self.r4)) + '\t' + str(type(self.r5)) + '\t' + str(type(self.r6)) + '\t' + str(type(self.r7)) + '\t' + str(type(self.r8)) + '\t' + str(type(self.r9)) + '\t' + str(type(self.r10)) + '\t' + str(type(self.r11)) + '\t' + str(type(self.r12)) + '\t' + str(type(self.r13)) + '\t' + str(type(self.r14)) + '\t' + str(type(self.r15)) + '\t' + str(type(self.q1)) + '\t' + str(type(self.q2)) + '\t' + str(type(self.q3)) + '\t' + str(type(self.q4)) + '\t' + str(type(self.q5)) + '\t' + str(type(self.q6)) + '\t' + str(type(self.q7)) + '\t' + str(type(self.q8)) + '\t' + str(type(self.q9)) + '\t' + str(type(self.q10)) + '\t' + str(type(self.q11)) + '\t' + str(type(self.q12)) + '\t' + str(type(self.q13)) + '\t' + str(type(self.q14)) + '\t' + str(type(self.q15)))

    def __eq__(self, other):
        return self.cqs == other.cqs and self.cri == other.cri and self.tlci == other.tlci and self.gaCQS == other.gaCQS and self.gaiE == other.gaiE and self.gaCRI == other.gaCRI and self.lpw == other.lpw
    def __ge__(self, other):
        #extend to test all R and Q values
        return self > other or self == other
    def __gt__(self, other):
        #extend to test all R and Q values
        return self.cqs > other.cqs or self.cri > other.cri or self.tlci > other.tlci or self.gaCQS > other.gaCQS or self.gaiE > other.gaiE or self.gaCRI > other.gaCRI or self.lpw > other.lpw
    def __le__(self, other):
        #extend to test all R and Q values
        return self < other or self == other
    def __lt__(self, other):
        #extend to test all R and Q values
        return self.cqs < other.cqs or self.cri < other.cri or self.tlci < other.tlci or self.gaCQS < other.gaCQS or self.gaiE < other.gaiE or self.gaCRI < other.gaCRI or self.lpw < other.lpw
    
    def key(self):
        return (str(round(self.cct/50)*50))+'_'+str(self.dwlBlue)+'_'+str(self.dwlVerde)+'_'+str(self.dwlRed)
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return str(self.cct) + '\t' + str(self.cri) + '\t' + str(self.cqs) + '\t' + str(self.duv) + '\t' + str(self.lpw) + '\t' + str(self.intenBlue) + '\t' + str(self.dwlBlue) + '\t' + str(self.intenVerde) + '\t' + str(self.dwlVerde) + '\t' + str(self.intenRed) + '\t' + str(self.dwlRed) + '\t' + str(self.intenWhite) + '\t' + str(self.x) + '\t' + str(self.y) + '\t' + str(self.gaCRI) + '\t' + str(self.gaCQS) + '\t' + str(self.gaiE) + '\t' + str(self.tlci) + '\t' + str(self.tlciD) + '\t' + str(self.r1) + '\t' + str(self.r2) + '\t' + str(self.r3) + '\t' + str(self.r4) + '\t' + str(self.r5) + '\t' + str(self.r6) + '\t' + str(self.r7) + '\t' + str(self.r8) + '\t' + str(self.r9) + '\t' + str(self.r10) + '\t' + str(self.r11) + '\t' + str(self.r12) + '\t' + str(self.r13) + '\t' + str(self.r14) + '\t' + str(self.r15) + '\t' + str(self.q1) + '\t' + str(self.q2) + '\t' + str(self.q3) + '\t' + str(self.q4) + '\t' + str(self.q5) + '\t' + str(self.q6) + '\t' + str(self.q7) + '\t' + str(self.q8) + '\t' + str(self.q9) + '\t' + str(self.q10) + '\t' + str(self.q11) + '\t' + str(self.q12) + '\t' + str(self.q13) + '\t' + str(self.q14) + '\t' + str(self.q15)

best_mixes = dict()
lineFound = 2 #Line number in file
#skip the header
sys.stdin.readlines(1)[0]
print('CCT     CRI     CQS     Duv     LPW    Blue (%W)       Blue dom (nm)   Verde (%W)      Verde dom (nm)  Deep red (%W)   Deep red dom (nm)       nvsl219B-V1-E90 (%W)    x       y       Gamut-CRI       Gamut-D65       GAI     TLCI Qa TLCI d  R1      R2      R3      R4      R5      R6      R7      R8      R9      R10     R11     R12     R13     R14     R15     Q1      Q2      Q3      Q4      Q5      Q6      Q7      Q8      Q9      Q10     Q11     Q12     Q13     Q14     Q15')
tmp_lines = sys.stdin.readlines(100)
while tmp_lines:
    for lineText in tmp_lines:
      newMix = Mix(lineText, lineFound)
      lineFound +=1
      try:
          if best_mixes[newMix.key()] < newMix:
              best_mixes[newMix.key()] = newMix
      except KeyError:
          best_mixes[newMix.key()] = newMix
    tmp_lines = sys.stdin.readlines(100)
for val in best_mixes.values():
    print(val)