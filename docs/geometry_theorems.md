# 📐 AMC 10 平面几何核心母定理与全套变式速查手册

> **学习原则**：不搞死记硬背，重在“**一眼看懂图形结构，举一反三秒杀考点**”。  
> 每个定理均配备**高清矢量几何图解**、**标准核心公式**、**实战变式拓展**与**AMC 10 真题秒杀技巧**。

---

## 目录索引
1. [角平分线双星体系（内角平分线 + 外角平分线推广 + 长度公式）](#1-角平分线双星体系)
2. [斯特瓦尔特定理与中线模型（阿波罗尼奥斯定理）](#2-斯特瓦尔特定理与中线模型)
3. [圆幂定理家族（相交弦、割线、切割线）](#3-圆幂定理家族全景)
4. [托勒密定理与正多边形拓展（黄金分割应用）](#4-托勒密定理与正多边形拓展)
5. [直角三角形射影定理与高线倒数平方和](#5-直角三角形射影定理与高线模型)
6. [塞瓦定理与梅涅劳斯定理（共点线与共线点的最高法则）](#6-塞瓦定理与梅涅劳斯定理)

---

## 1. 角平分线双星体系

### 【母定理】内角平分线定理 (Internal Angle Bisector)

![内角平分线定理](images/angle_bisector_internal.svg)

在 $\triangle ABC$ 中，$AD$ 为 $\angle A$ 的内角平分线，交 $BC$ 于点 $D$。则：

$$
\frac{BD}{DC} = \frac{AB}{AC} = \frac{c}{b}
$$

---

### 【拓展 1：外角平分线推广】(External Angle Bisector)

![外角平分线推广](images/angle_bisector_external.svg)

在 $\triangle ABC$ 中，延长 $BA$ 至 $A'$，作外角 $\angle A'AC$ 的平分线交 $BC$ 的延长线于点 $E$。则：

$$
\frac{EB}{EC} = \frac{AB}{AC} = \frac{c}{b}
$$

> 💡 **举一反三（极客洞察）**：  
> 比较内角式与外角式，发现 $D$ 点与 $E$ 点把线段 $BC$ 分别按内分与外分，得到完全相同的比例：
> $$ \frac{BD}{DC} = \frac{EB}{EC} = \frac{AB}{AC} $$
> 这在高等几何中称为**调和共轭点列（Harmonic Conjugate）**！以 $DE$ 为直径的圆，即为著名的**阿波罗尼斯圆（Apollonius Circle）**。

---

### 【拓展 2：角平分线自身长度公式】（AMC 10 极大杀器）

考场上经常给出三边长，要求算角平分线 $AD$ 的长度。不用做垂线，直接套用线段乘积差公式：

* **内角平分线长**：
$$
AD^2 = AB \cdot AC - BD \cdot DC = bc - mn
$$

* **外角平分线长**：
$$
AE^2 = EB \cdot EC - AB \cdot AC
$$

> **秒杀示例**：若 $\triangle ABC$ 中 $c=6, b=4$，底边被内角平分线分为 $m=3, n=2$：  
> 则 $AD^2 = 6 \times 4 - 3 \times 2 = 24 - 6 = 18 \implies AD = 3\sqrt{2}$，用时 10 秒！

---

## 2. 斯特瓦尔特定理与中线模型

### 【母定理】斯特瓦尔特定理 (Stewart's Theorem)

![斯特瓦尔特定理](images/stewart_and_median.svg)

在 $\triangle ABC$ 中，$D$ 为底边 $BC$ 上**任意一点**。设 $BC=a, AC=b, AB=c, AD=d, BD=m, CD=n$（满足 $a = m + n$），则恒有：

$$
b^2 m + c^2 n = a (d^2 + m n)
$$

* **英文记忆口诀**：*"A man and his dad put a bomb in the sink."* ($man + dad = bmb + cnc$)

---

### 【拓展 1：中线长公式与阿波罗尼奥斯定理】

当点 $D$ 恰好为 $BC$ 的**中点**时（即 $m = n = \frac{a}{2}$），斯特定理瞬间化简为**中线定理**：

$$
AB^2 + AC^2 = 2(AD^2 + BD^2) = 2 \left(m_a^2 + \frac{a^2}{4}\right)
$$

两边各乘以 2 移项，即得**中线长万能计算公式**：

$$
m_a = \frac{1}{2} \sqrt{2b^2 + 2c^2 - a^2}
$$

> 💡 **举一反三**：AMC 10 中若遇到“已知两边长与中线长，求第三边”或“求三条中线的平方和”，直接套用：
> $$ m_a^2 + m_b^2 + m_c^2 = \frac{3}{4} (a^2 + b^2 + c^2) $$

---

## 3. 圆幂定理家族全景

![圆幂定理三合一](images/power_of_a_point_family.svg)

圆幂定理（Power of a Point）描述的是：**过任意定点 $P$ 引与圆相交的直线，交点到点 $P$ 的距离乘积为恒定值**。根据点 $P$ 的位置分为三种经典形态：

### ① 圆内相交弦定理
两条弦 $AB, CD$ 交于圆内一点 $P$：
$$
PA \cdot PB = PC \cdot PD
$$

### ② 圆外两条割线定理
从圆外一点 $P$ 引两条割线 $PAB$ 和 $PCD$：
$$
PA \cdot PB = PC \cdot PD
$$

### ③ 切割线定理（切线是割线的极限形态）
从圆外一点 $P$ 引切线 $PT$（$T$ 为切点）与割线 $PAB$：
$$
PT^2 = PA \cdot PB = PC \cdot PD
$$

> 💡 **举一反三（根轴 Radical Axis）**：  
> 若平面上有两个圆，到两圆圆幂相等的点集是一条直线，称为**根轴**。如果两个圆相交，**两圆的公共弦所在直线就是根轴**！这是解决两圆相交求线段乘积最底层的几何背景。

---

## 4. 托勒密定理与正多边形拓展

### 【母定理】托勒密定理 (Ptolemy's Theorem)

![托勒密定理](images/ptolemy_and_pentagon.svg)

圆内接四边形 $ABCD$ 中，**两条对角线乘积 = 两组对边乘积之和**：

$$
AC \cdot BD = AB \cdot CD + BC \cdot AD
$$

---

### 【拓展 1：广义托勒密不等式】

对于平面上**任意**凸四边形 $ABCD$（不要求共圆），均恒有：

$$
AC \cdot BD \le AB \cdot CD + BC \cdot AD
$$

* **等号成立条件**：当且仅当 $A, B, C, D$ 四点共圆且按圆周顺序排列。

---

### 【拓展 2：正五边形与黄金分割（AMC 10 经典真题）】

在边长为 $1$ 的正五边形 $ABCDE$ 中，求对角线 $d$ 的长度：
1. 考虑圆内接四边形 $ABCD$（正多边形各顶点必共圆）；
2. 边长为 $AB=1, BC=1, CD=1$；对角线为 $AC=d, BD=d, AD=d$；
3. 代入托勒密定理：
$$
AC \cdot BD = AB \cdot CD + BC \cdot AD \implies d \cdot d = 1 \cdot 1 + 1 \cdot d
$$
$$
d^2 - d - 1 = 0 \implies d = \frac{1 + \sqrt{5}}{2} \approx 1.618 \quad \text{(黄金分割比！)}
$$

> 💡 **总结**：只要在正多边形中看到对角线相交，立刻构造圆内接四边形用托勒密定理列二次方程！

---

## 5. 直角三角形射影定理与高线模型

### 【母定理】射影定理 (Geometric Mean Theorem)

![射影定理与高线](images/right_triangle_project.svg)

在 Rt$\triangle ABC$ 中，$\angle C = 90^\circ$，$CD \perp AB$ 于 $D$（设 $CD=h, AD=p, BD=q, AB=c$）：

$$
h^2 = p \cdot q \quad \text{(斜边高是两底段的几何平均)}
$$
$$
AC^2 = p \cdot c, \quad BC^2 = q \cdot c \quad \text{(直角边是射影与斜边的几何平均)}
$$

---

### 【拓展 1：高线的倒数平方和（AMC 10 超高频模型）】

由于面积等式 $c \cdot h = a \cdot b \implies h = \frac{ab}{c}$，结合勾股定理 $c^2 = a^2 + b^2$：

$$
\frac{1}{h^2} = \frac{c^2}{a^2 b^2} = \frac{a^2 + b^2}{a^2 b^2} = \frac{1}{a^2} + \frac{1}{b^2}
$$

$$
\frac{1}{h^2} = \frac{1}{a^2} + \frac{1}{b^2}
$$

> 💡 **秒杀考点**：题目给出两直角边长为 $3$ 和 $4$，求斜边高：  
> $\frac{1}{h^2} = \frac{1}{9} + \frac{1}{16} = \frac{25}{144} \implies h = \frac{12}{5} = 2.4$。

---

### 【拓展 2：内切圆半径与外接圆半径公式】

* **直角三角形专属内切圆半径**：
$$
r = \frac{a + b - c}{2}
$$
* **任意三角形内切圆半径与面积（周长模型）**：
$$
\text{Area} = r \cdot s \quad \left(s = \frac{a + b + c}{2} \text{ 为半周长}\right)
$$
* **外接圆半径 $R$ 与正弦定理**：
$$
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R, \quad \text{Area} = \frac{abc}{4R}
$$

---

## 6. 塞瓦定理与梅涅劳斯定理

![塞瓦与梅涅劳斯](images/ceva_and_menelaus.svg)

这是处理三角形内**线段共点（Concurrency）**与**三点共线（Collinearity）**的最高理论工具：

### 【母定理 1】塞瓦定理 (Ceva's Theorem —— 判断三线共点)
在 $\triangle ABC$ 中，$D, E, F$ 分别是 $BC, CA, AB$ 上的点，三条塞瓦线 $AD, BE, CF$ **交于一点 $P$ 的充要条件是**：

$$
\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1
$$

* **经典验证**：三条中线（比例全为 1）、三条内角平分线（代入角平分线定理比值相消）必共点！

---

### 【母定理 2】梅涅劳斯定理 (Menelaus's Theorem —— 判断三点共线)
一条截线交 $\triangle ABC$ 的三边（或其延长线）于点 $D, E, F$，则**三点 $D, E, F$ 共线的充要条件是**：

$$
\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1
$$

> 💡 **记忆口诀**：“顶点到分点，分点到顶点，绕着三角形顺时针走一圈，三个比值乘积恒为 1”！

---

## 总结：考场几何“见条件反射图表”

| 题目给出的特征几何条件 | 脑海中第一反应调用的工具 |
| :--- | :--- |
| 看到 **内角平分线** / **外角平分线** | $\frac{BD}{DC} = \frac{c}{b}$ 或长度公式 $AD^2 = bc - mn$ |
| 看到 **圆 + 弦相交** 或 **圆外引切线割线** | 圆幂定理：相交两段乘积必相等 $PA \cdot PB = PC \cdot PD$ |
| 看到 **圆内接四边形** 或 **正五边形求对角线** | 托勒密定理：对角线积 = 对边积和 $AC \cdot BD = AB \cdot CD + BC \cdot AD$ |
| 看到 **三角形中线** 或 **求某边上线段中点长** | 阿波罗尼奥斯中线定理：$b^2 + c^2 = 2(m_a^2 + (a/2)^2)$ |
| 看到 **平面直角坐标系给多边形坐标** | 鞋带公式 Shoelace Formula 交叉相乘求面积 |
| 看到 **直角三角形斜边引垂线（高）** | 射影定理 $h^2 = pq$ 与高线倒数平方和 $\frac{1}{h^2} = \frac{1}{a^2} + \frac{1}{b^2}$ |
