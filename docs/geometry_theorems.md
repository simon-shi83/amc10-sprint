# 📐 平面几何 5 大必考公式与定理速查

AMC 10 的几何题几乎不要求复杂的辅助线推理，只要记住以下 5 个定理，90% 的几何中高档题可以直接代入秒杀：

---

### 1. 角平分线定理（Angle Bisector Theorem）
* **定理内容**：在 $\triangle ABC$ 中，$ 是 $\angle A$ 的内角平分线，交 $ 于 $。则：
  111731\frac{BD}{DC} = \frac{AB}{AC}111731
* **外角平分线推广**：若 $ 为外角平分线交 $ 延长线于 $，同样满足 $\frac{BE}{EC} = \frac{AB}{AC}$。

---

### 2. 圆幂定理（Power of a Point Theorem）
* **定理内容**：过圆外或圆内一点 $ 作相交割线或切线：
  * **相交弦定理（圆内）**：两条弦 , CD$ 相交于点 $ $\implies PA \cdot PB = PC \cdot PD$
  * **割线定理（圆外）**：割线 , PCD$ $\implies PA \cdot PB = PC \cdot PD$
  * **切割线定理**：$ 为切线，$ 为割线 $\implies PT^2 = PA \cdot PB$

---

### 3. 直角三角形射影定理（Geometric Mean Theorem）
* **定理内容**：在直角 $\triangle ABC$ 中，$\angle C = 90^\circ$， \perp AB$ 于 $：
  * ^2 = AD \cdot BD$（高线是两段射影的比例中项）
  * ^2 = AD \cdot AB$
  * ^2 = BD \cdot AB$

---

### 4. 鞋带公式（Shoelace Formula，坐标几何大杀器）
* **应用场景**：已知平面直角坐标系中多边形所有顶点的坐标，求面积。
* **公式**：按逆时针顺序排列顶点 , (x_2, y_2), \dots, (x_n, y_n)$：
  111731\text{Area} = \frac{1}{2} |(x_1 y_2 + x_2 y_3 + \dots + x_n y_1) - (y_1 x_2 + y_2 x_3 + \dots + y_n x_1)|111731

---

### 5. 托勒密定理（Ptolemy's Theorem，四边形压轴）
* **定理内容**：圆内接四边形 $ 中：
  111731AC \cdot BD = AB \cdot CD + BC \cdot AD111731
  *(对角线乘积 = 对边乘积之和)*
