a = 5
rst = 100 if a>0 else 200
print(rst)
rst = [200, 100][False]
print(rst)
rst = {True:100, False:200}[a>0]
print(rst)

score = input("점수 입력:")
score = int(score)
result = "합격" if score >= 70 else "불합격"
result=["불합격", "합격"][score>=70]
print(result)
