# 🔢 数论与代数提速核心秘籍

---

### 1. 因数个数与因数和公式

若正整数 $N$ 的标准质因数分解为：

$$
N = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}
$$

* **正因数总个数 $d(N)$**：

$$
d(N) = (a_1 + 1)(a_2 + 1) \dots (a_k + 1)
$$

* **正因数总和 $\sigma(N)$**：

$$
\sigma(N) = \left(\frac{p_1^{a_1+1}-1}{p_1-1}\right) \left(\frac{p_2^{a_2+1}-1}{p_2-1}\right) \dots \left(\frac{p_k^{a_k+1}-1}{p_k-1}\right)
$$

* **OI 选手直觉**：正因数个数为奇数 $\iff N$ 是完全平方数！

---

### 2. 韦达定理多项式推广（Vieta's Formulas）

对于一元三次方程 $ax^3 + bx^2 + cx + d = 0$ 的三个根 $r_1, r_2, r_3$：

$$
r_1 + r_2 + r_3 = -\frac{b}{a}
$$

$$
r_1 r_2 + r_2 r_3 + r_3 r_1 = \frac{c}{a}
$$

$$
r_1 r_2 r_3 = -\frac{d}{a}
$$

* **高频变换技巧**：求平方和：

$$
r_1^2 + r_2^2 + r_3^2 = (r_1 + r_2 + r_3)^2 - 2(r_1 r_2 + r_2 r_3 + r_3 r_1)
$$

---

### 3. 同余模运算（Modular Arithmetic）与末位数循环

* 加法与乘法可直接按模运算展开：

$$
(a + b) \bmod m = ((a \bmod m) + (b \bmod m)) \bmod m
$$

$$
(a \times b) \bmod m = ((a \bmod m) \times (b \bmod m)) \bmod m
$$

* **求大数末位（模 10）**：任意正整数末位数字的幂次呈现以 1、2 或 4 为周期的循环特性。

---

### 4. 隔板法（Stars and Bars）与容斥原理

* **正整数解模型**：方程 $x_1 + x_2 + \dots + x_k = n$ 且每个 $x_i \ge 1$ 的整数解组数为：

$$
\binom{n-1}{k-1}
$$

* **非负整数解模型**：方程 $x_1 + x_2 + \dots + x_k = n$ 且每个 $x_i \ge 0$ 的整数解组数为：

$$
\binom{n+k-1}{k-1}
$$

* **三集合容斥原理（Inclusion-Exclusion Principle）**：

$$
|A \cup B \cup C| = (|A|+|B|+|C|) - (|A \cap B| + |B \cap C| + |C \cap A|) + |A \cap B \cap C|
$$

* **代码暴力验证**：此类计数题如果算完心里没底，在 `verify_scripts/` 中运行 4 行 Python 脚本立即验证！
