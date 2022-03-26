s1 = int(input('enter the first side'))
s2 = int(input('enter the second side'))
s3 = int(input('enter the third side'))
if s1==s2 and s2==s3:
    print('equilateral triangle')
elif (s1==s2) and (s2!=s3) or (s2==s3) and (s2!=s1) or (s1==s3) and (s1!=s2):
    print('isoceles triangle')
elif s1!=s2 and s2!=s3 or s3!=s1:
    print('scalence triangle')
