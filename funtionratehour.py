hrs = input("Enter Hours:")
hrf = float(hrs)
rats = input("Enter rate:")
ratf = float(rats)

def computepay(hrf,ratf):
	if hrf > 40 :
		reg = hrf * ratf
		otp=(hrf-40.0)*(ratf*0.5)
		total = reg + otp
        	return total
	elif hrf <= 40 :
    	total = hrf*ratf


p = computepay(hrf,ratf)
print("Pay",p)
