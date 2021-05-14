#리스트실습
li = [3, 1, "배가", 4, "고파요", 5, 1]

#리스트 인덱싱
print(li[2])

#리스트 슬라이싱
print(li[2:5])

#리스트 길이를 구해주는 내장함수 : len(리스트 변수명)
print(len(li))

#리스트를 오름차순으로 정렬하는 내장함수 : 리스트변수명.sort()
li2=[3,1,4,5,2]
li2.sort() #여기서 정렬 이미 끝남(원본 리스트 자체를 바꿈)(리스트에서만)
print(li2.sort()) #None반환

#sorted
print(sorted(li2)) #오름차순 반환(리스트, 튜플, 딕셔너리 사용가능)
print(li2)#원본리스트 변하지x

#깜짝퀴즈: sort()로 내림차순 하는법을 알아보도록 하자
#여기에 코드 적기(print문 사용)
print(sorted.reverse)

#리스트 내의 특정 원소 인덱스를 반환하는 함수 : 리스트변수.index()
print(li.index("배가"))

#리스트 내의 특정 원소의 개수를 세어주는 함수 : 리스트변수.count(요소)
print(li.count(1))



