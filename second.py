#문자열 실습

#1
likelion = "멋쟁이 사자처럼"
good = "은 좋은 동아리입니다."
print(likelion + good)
 
#2
print(likelion*3)

#3
print(likelion[0])

#4
print(likelion[3])

#5
print(likelion[4:6])

#6
print(len(likelion))

#7
lovelylikelion="멋쟁이 사자처럼은 사랑스러워"
print(lovelylikelion.count('사'))

#8
print(lovelylikelion.split())

#9
str='사과,바나나,포도'
print(str.split(,))


#10_특정 문자 인덱스를 찾아주는 내장함수 : find('문장'), index('문장')
print("find : ", lovelylikelion.find('랑'))
print("index : ", lovelylikelion.index('랑'))

#find와 index의 차이점
#오류가 발생했을 때, find는 -1을 반환, index는 ValueError라는 오류를 발생시킵니다
print("find: ",lovelylikelion.find('무'))
print("index: ",lovelylikelion.index('무'))

