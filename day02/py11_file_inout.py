# py11_file_inout.py - 파일 입출력

# 쓰기
# a(추가), r(읽기), w(쓰기)
f = open('./day2/textfile.txt', mode='w',encoding='utf-8')
# 아무것도 안함
f.write('저는 한국사람입니다.\n')
f.write('남자입니다.')
f.close()

print('텍스트파일이 생성되었습니다')
