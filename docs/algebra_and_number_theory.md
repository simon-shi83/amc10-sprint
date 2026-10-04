# 🔢 数论与代数提速核心秘籍

---

### 1. 因数个数与因数和公式
若正整数 $ 的质因数分解为  = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}$：
* **正因数个数**：(N) = (a_1 + 1)(a_2 + 1)\dots(a_k + 1)$
* **正因数总和**：
  111731\sigma(N) = \left(\frac{p_1^{a_1+1}-1}{p_1-1}\right) \times \left(\frac{p_2^{a_2+1}-1}{p_2-1}\right) \dots \times \left(\frac{p_k^{a_k+1}-1}{p_k-1}\right)111731

---

### 2. 韦达定理多项式推广（Vieta's Formulas）
对于一元三次方程 ^3 + bx^2 + cx + d = 0$ 的三个根 , x_2, x_3$：
*  + x_2 + x_3 = -\frac{b}{a}$
*  x_2 + x_2 x_3 + x_3 x_1 = \frac{c}{a}$
*  x_2 x_3 = -\frac{d}{a}$

---

### 3. 同余模运算（Modular Arithmetic）与欧拉降幂
*  \pmod m = ((a \bmod m) + (b \bmod m)) \bmod m$
*  \pmod m = ((a \bmod m) \times (b \bmod m)) \bmod m$
* **求幂末位数字**：底数末尾数的幂次模 10 呈周期循环（周期通常为 1, 2 或 4）。

---

### 4. 隔板法（Stars and Bars）与容斥原理
* **正整数解个数**： + x_2 + \dots + x_k = n$（每个  \ge 1$）$\implies \binom{n-1}{k-1}$
* **非负整数解个数**： + x_2 + \dots + x_k = n$（每个  \ge 0$）$\implies \binom{n+k-1}{k-1}$
* **容斥原理（三集合）**：
  111731|A \cup B \cup C| = (|A|+|B|+|C|) - (|A \cap B| + |B \cap C| + |C \cap A|) + |A \cap B \cap C|111731
