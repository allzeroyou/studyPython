#딕셔너리 실습
pairs={'유라':'눈치가 없다', '비비':'비누'}

#하나의 키 - value 쌍을 더 추가하는 방법 : 딕셔너리 변수[키]=value
print(pairs)
pairs['유라']='Night Running'
print(pairs)

#특정키 - value 쌍을 삭제하는 방법: del 변수 [키]
del pairs['비비']
print(pairs)

#key value값을 확인하는 방법 : 딕셔너리 변수.get(키)
print(pairs.get('유라'))