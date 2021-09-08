# правило пошуку імен в python-i:
# LEGB:   L=local, E=enclosing, G=global, B=builtins

def s():
    abs = 200
    def q():
        abs = 'hello'
        print(abs, "- from q()")
        return abs
    q()
    print(abs, "- from s()")   # перезатирає abs, що повертає ф-ія q()
    return abs

abs = [1,2,3,4,5]

print(s())   # 200
print(abs, " - from global abs")
# hello - q()
# 200 - s()
# 200
# [1, 2, 3, 4, 5]  - global abs

print()
def f():
    abs = 200
    def g():
        nonlocal abs   # цим ми кажемо, що abs=200 не є локальною відносно ф-ії g()
        abs = 'hello'
        print(abs, "- from g()")
        return abs
    g()
    print(abs, "- from f()")   # перезатирає abs, що повертає ф-ія g()
    return abs

abs = [1,2,3,4,5]

print(f())   # 200
print(abs, " - global abs")
