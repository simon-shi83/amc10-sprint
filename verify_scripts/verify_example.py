# verify_example.py
# 演示：信息学竞赛选手如何写 10 行 Python 代码暴力验证 AMC 10 数学题

"""
【经典题型示例】
求 1 到 1000 之间，既不能被 2 整除，也不能被 3 整除，但能被 5 整除的正整数有多少个？
"""

def math_formula_solution():
    # 纯数学方法：容斥原理
    # N(5) - N(10) - N(15) + N(30)
    c5 = 1000 // 5
    c10 = 1000 // 10
    c15 = 1000 // 15
    c30 = 1000 // 30
    ans = c5 - c10 - c15 + c30
    return ans

def brute_force_verify():
    # OI 选手暴力验证法
    count = 0
    for x in range(1, 1001):
        if x % 5 == 0 and x % 2 != 0 and x % 3 != 0:
            count += 1
    return count

if __name__ == '__main__':
    math_ans = math_formula_solution()
    code_ans = brute_force_verify()
    print(f'公式计算结果: {math_ans}')
    print(f'代码暴力结果: {code_ans}')
    assert math_ans == code_ans, '结果不一致！'
    print('✅ 验证完全一致！恭喜拿下 6 分！')
