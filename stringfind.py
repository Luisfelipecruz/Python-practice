text = "X-DSPAM-Confidence:    0.8475";

char= text.find(':')
numb= text[char+1 :]
num = numb.strip()

print(float(num))
