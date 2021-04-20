def areAnagram(str1, str2):
    count=0
    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        return 0
    for i in range(0, n1):
        if str1[i] == str2[i]:
            count=count+1
    return count
str1 = "c671b3e40d412de3ac22caf369719d30"
str2 = "7b490fc7f093550ea6998f9acbf4d822"
num=areAnagram(str1, str2)
print("Common points in before and after MD5 hashes  are : ",num)
str11="90f3e61afe7a048a3d55e8ca967739f75891404383055acf0a1dc472692c5661"
str22="9eb5b3a5673d1ae79cb1075417df8d73a96a04c55fbd9be2cbb9175ab7279204"
num1=areAnagram(str11, str22)
print("Common points in before and after SHA256 hashes are : ",num1)
