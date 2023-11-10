## Perceptron

### Perceptron Model

​	一种二分类的线性分类模型，输入空间是 $\mathcal{X}\subseteq\R^n$，输出空间是 $\mathcal Y\in\{-1,1\}$。感知机表示如下函数：
$$
f(x) = \mathrm{sign}(w\cdot x+b)
$$
​	感知机可以解释为：线性方程
$$
w\cdot x+b=0
$$
是特征空间 $\R^n$ 的一个超平面 (*hyperplane*)，$w$ 为该平面的一个法向量，$b$ 为截距。

### Learning Strategy

​	数据集的线性可分性 ：存在一个超平面可完全将两种实例点划分到平面两侧，则称线性可分。

​	假设数据集线性可分，可定义感知机学习策略为：定义损失函数并使损失函数最小化。感知机采用的损失函数是误分类点到超平面的总距离：
$$
\frac1{\|w\|}|w\cdot x_0+b|
$$
$\|w\|$: L2 范数，元素的平方和求平方根。

对误分类的数据：
$$
-y_i(w\cdot x_i+b) > 0
$$
正式定义损失函数: 
$$
L(w,b) = -\sum_{x_i\in M}y_i(w\cdot x_i+b)
$$

### Learning Algorithm

​	感知机学习算法是对以下最优化问题的算法，给定 $x_i\in\mathcal X = \R^n, y_i\in\mathcal Y =\{-1,1\}$，求参数 $w,b$，使损失函数最小化的解
$$
\min_{w,b}L(w,b) = -\sum_{x_i\in M}y_i(w\cdot x_i+b)
$$
​	随机选取一个超平面，然后采用**梯度下降算法**不断逼近最小损失函数。梯度定义为
$$
\nabla_wL(w,b) = -\sum_{x_i\in M}y_ix_i\\
\nabla_b L(w,b) = -\sum_{x_i\in M}y_i
$$

###### **Algorithm 1**

1. 选取初值 $w_0,b_0$

2. 在训练集中选择 $(x_i,y_i)$

3. 如果 $y_i(w\cdot x_i+b)\le0$
   $$
   w\leftarrow w+\eta y_ix_i\\
   b\leftarrow b + \eta y_i
   $$

4. 转至2，直至训练集中无误分类点

$\eta$ 称之为学习算法的学习率。

#### Convergence of the Algorithm

​	感知机算法收敛：经过有限次的迭代可以找到这样一个超平面达到完全正确划分。

​	记 $\hat w=(w^T,b)^T, \hat x=(x^T, 1)^T$，则 $\hat w\cdot\hat x = w\cdot x+b$。

##### Novikoff Theorem

1. 若训练集线性可分，则存在超平面将训练集完全正确分开（废话？），且存在 $\gamma>0$，使得
   $$
   y_i(\hat w_{opt}\cdot\hat x_i)\ge\gamma
   $$

2. 令 $R=\max_{1\le i\le M}\|\hat x_i\|$，则感知机在训练集上的误分类次数满足
   $$
   k\le\left(\frac R\gamma\right)^2
   $$

##### Dual Format

​	感知机参数 $w,b$ 均是线性增加的，关于 $(x_i,y_i)$ 的增量分别是 $\alpha_i y_ix_i$ 和 $\alpha_iy_i$，$\alpha_i = n_i\eta$，则参数可以表示为
$$
w = \sum_{i=1}^N\alpha_iy_ix_i\\
b = \sum_{i=1}^N\alpha_iy_i
$$

##### **Algorithm 2 (Dual Format of the Perceptron Algorithm)**

输出模型： $\displaystyle{f(x)=\mathrm{sign}\left(\sum_{j=1}^N\alpha_jy_jx_j\cdot x+ b\right)}$

1. $\alpha\leftarrow0,b\leftarrow 0$

2. 选择数据 $(x_i,y_i)$

3. 如果 $\displaystyle{y_i\left(\sum_{j=1}^N\alpha_jy_jx_j\cdot x_i+ b\right)}\le 0$
   $$
   \alpha_i\leftarrow\alpha_i+\eta\\
   b\leftarrow b + \eta y_i
   $$

4. 重复2直到没有误分类数据

#### Python Code of Perceptron

```python
import numpy as np
class Perceptron:
    def __init__(self):
        self.w = None
        self.b = None

    def train(self, X: np.ndarray, Y: np.ndarray, eta):
        # calculate Gram matrix
        assert X.shape[0] == Y.shape[0]
        w = np.zeros(X.shape[1])
        b = 0

        set_size = X.shape[0]

        complete = False
        while not complete:
            complete = True
            for i in range(set_size):
                if Y[i] * (w.dot(X[i]) + b) <= 0:
                    complete = False
                    w = w + eta * Y[i] * X[i]
                    b = b + eta * Y[i]

        self.w = w
        self.b = b

    def predict(self, x: np.ndarray):
        if not self.w or not self.b:
            return
        return self.w.dot(x) + self.b

    def show(self):
        print("w: ", self.w)
        print("b: ", self.b)
```

