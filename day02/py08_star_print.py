# py08_star_print.py
# 별찍기

## 문자열에 사용할 수 있는 연산자는 +, * -> 추후 설명

## for문을 사용해서 콘솔에 아래와 같이 나오도록 구현하세요
'''
    *
   **
  ***
 ****
*****
'''
a = 5
for i in range(5):
    print(' ' * ((a - 1) - i), end='')
    print('*' * (i+1))
