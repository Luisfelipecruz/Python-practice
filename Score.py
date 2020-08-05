scoreS = input("Enter Score: ")
try:
	scoreF = float(scoreS)
except:
    scoreF = -1
if scoreF >= 0.9:
	print ('A')
elif scoreF >= 0.8:
	print ('B')
elif scoreF >= 0.7:
	print ('C')
elif scoreF >= 0.6:
	print ('D')
elif scoreF < 0.6:
	print ('F')
