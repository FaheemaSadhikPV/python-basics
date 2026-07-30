#COMPLEX TYPE
x=3+1j
com=1+0j
print(com)
print(x)
print(type(com))
print(type(x))

#NONE-to store null values  
x=None
print(x)
print(type(x))

#string
s1 = 'hello'
s2 = "world"
s3 = '''This is multiline'''
print(s1,s2)
print(s1+s2)
print(s3)

#Indexing & Slicing
s = 'python'
print('s[0]=',s[0])
print('s[-1]=',s[-1])
print('s[1:4]=',s[1:4])
print('s[:3]=',s[:3])
print('s[::2]',s[::2])
print('Reverse:',s[::-1])

#examples
Faheema = 'SOS|Faheema Sadhik PV|Data Science And Analytics|JULY2026|Morning|Offline'
print(Faheema[4:11]+Faheema[12:18]+Faheema[19:21]+Faheema[22]+Faheema[27]+Faheema[39]+Faheema[49:52]+Faheema[55:57]+Faheema[58]+Faheema[66])


game = 'i like car Racing'
print(game.upper())
print(game.lower())
print(game.title())
print(game.capitalize())
print(game.swapcase())
print(len(game))
print(game.find('z'))
print(game.find('i'))

#split
player = 'cr7-is-good'
print(player.split('-'))


#replace & translate
#replace example
print(player.replace('good','bad'))

#translate example
orig = 'aeiou'
tr = str.maketrans('aeiou','12345')
print('translate:','education'.translate(tr))

#line space
print("i am faheema\nfrom malappuram\nage 22\ngraduate")
print("faheema\tsadhik")

#type conversion
a="abc123"
x="123"
print(type(x))
 
y=int(x)
print(y)
print(type(y))

