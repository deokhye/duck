#%%
#1
#인덱스 0이랑 2의 공통점
import re

a= ['abbbbba', 'cddb', 'aerb', 'aeeeb', 'almnj']

p = re.compile('a..b')

for i in a:
    print(p.match(i))
    

#%%
#2
#1,3,4번째 출력
import re
a = ['abcd efghopqr-stuv', 'abcd-efgh', 'abc defghijk', 'ab cdhijk']

p = re.compile('a.+\s.+')

for i in a:
    print(p.match(i))

# %%
#3
#다 true, 주어만 프린트
import re
a= ["코끼리는 코끼리", "강아지는 강아지", "고양이는 고양이"]

p = re.compile(r'(?P<name>.+)는\s\1')

for i in a:
    matched = p.match(i)
    print(i)
    print(matched.group(1))


#%%
#4
#학점을 모두 4.5로
import re

a = ['김준태 - 학점 2.0', '이재화 - 학점 3.0', '최주원 - 학점 4.0']

# p = re.compile(r'(?P<rest>.+\s.\s).+')

# for i in a:
#     matched = p.match(i)
#     print(p.sub("\g<rest> 학점 4.5", i))

p = re.compile(r'(?P<rest>.+\s.\s).+')

for i in a:
    matched = p.match(i)
    print(p.sub("\g<rest> 학점 4.5", i))

# 그니까 지금 i는 김준태 - 학점 2.0인데
# 이거를 바꾼게 김준태 - 학점 4.5구나
# 그럼 g<rest>.+\s.\s는 김준태 - 이야
# 그래서 <rest>.+\s.\s

# %%
#5
#사용된 모든 태그 출력
