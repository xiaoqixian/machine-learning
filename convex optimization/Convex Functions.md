# Convex Functions

### 1. Basic properties and examples

#### 1.1 Definitions

​	A function $f:\R^n\rarr\R$ is *convex* if $\mathrm{\textbf{dom}}\ f$ is a convex set and if for all $x,y\in\mathrm{\textbf{dom}}\ f$, and $\theta$ with $0\le\theta\le1$, we have
$$
f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)
$$
We say $f$ is *concave* if $-f$ is convex.

#### 1.2 Extended-value extensions

​	It is often convenient to extend a convex function to all of $\R^n$ by defining its value to be $\infin$ outside its domain. If $f$ is convex, define its *extended-value extension* $\tilde f: \R^n\rarr\R\cup\{\infin\}$  by
$$
\tilde f(x)=\left\{\begin{align}&f(x) &x\in\mathrm{\textbf{dom}}\ f\\
&\infin &x\notin\mathrm{\textbf{dom}}\ f
\end{align} \right.
$$
$\tilde f(x)$ is also convex. 

#### 1.3 First-order conditions

​	Suppose $f$ is differentiable (*i.e.*, its gradient $\nabla f$ exists at each point in $\mathrm{\textbf{dom}}\ f$, which is open). Then $f$ is convex if and only if $\mathrm{\textbf{dom}}\ f$ is convex and 
$$
f(y)\ge f(x)+\nabla f(x)^T(y-x)
$$
holds for all $x,y\in\mathrm{\textbf{dom}}\ f$. Similarly, $f$ is concave if and only if $\mathrm{\textbf{dom}}\ f$ is convex and
$$
f(y)\le f(x)+\nabla f(x)^T(y-x)
$$
for all $x,y\in\mathrm{\textbf{dom}}\ f$.

#### 1.4 Second-order conditions

​	We now assume $f$ is twice differentiable, that is, its *Hessian* or second derivative $\nabla^2f$ exists at each point of $\mathrm{\textbf{dom}}\ f$, which is open. Then $f$ is convex if and only if $\mathrm{\textbf{dom}}\ f$ is convex and its Hessian is positive semidefinite: for all $x\in\mathrm{\textbf{dom}}\ f$, 
$$
\nabla^2f(x)\succeq0
$$

> The Hessian matrix of function $f$ is defined by 
> $$
> H_f=
> \begin{bmatrix} 
> \displaystyle\frac{\part^2 f}{\part x_1^2} &
> \displaystyle\frac{\part^2 f}{\part x_1\part x_2} &
> \cdots &
> \displaystyle\frac{\part^2 f}{\part x_1\part x_n} \\
> \displaystyle\frac{\part^2 f}{\part x_2\part x_1} &
> \displaystyle\frac{\part^2 f}{\part x_2^2} &
> \cdots &
> \displaystyle\frac{\part^2 f}{\part x_2\part x_n} \\
> \vdots & \vdots & \ddots & \vdots\\
> \displaystyle\frac{\part^2 f}{\part x_n\part x_n} &
> \displaystyle\frac{\part^2 f}{\part x_n\part x_2} &
> \cdots &
> \displaystyle\frac{\part^2 f}{\part x_n^2}
> \end{bmatrix}
> $$

For a function on $\R$, this reduces to the simple condition $f''(x)\ge0$, which means that the derivative is nondecreasing. The condition $\nabla^2f(x)\succeq0$ can be interpreted geometrically as the requirement that the graph of the function have positive curvature at $x$.

#### 1.5 Examples

​	Omitted

#### 1.6 Sublevel sets

​	The *$\alpha$-sublevel set* of a function $f:\R^n\rarr\R$ is defined as
$$
C_\alpha =\{x\in\mathrm{\textbf{dom}}\ f |\ f(x)\le\alpha\}
$$
Sublevel sets of a convex function are convex, for any value of $\alpha$.

​	Similarly, if $f$ is concave, its *$\alpha$-superlevel set*, given by $\{x\in\mathrm{\textbf{dom}}\ f\ |\ f(x)\ge\alpha\}$, is a convex set.

#### 1.7 Epigraph

​	The graph of a function $f:\R^n\rarr\R$ is defined as 
$$
\{(x,f(x))\ |\ x\in \mathrm{\textbf{dom}}\ f\}
$$
which is a subset of $\R^{n+1}$. The *epigraph* of a function $f:\R^n\rarr\R$ is defiend as
$$
\mathrm{\textbf{epi}}\ f=\{(x,t)\ |\ x\in\mathrm{\textbf{dom}}\ f,f(x)\le t\}
$$
A function is convex if and only if its epigraph is a convex set. A function is concave if and only if its *hypograph*, defined as
$$
\mathrm{\textbf{hypo}}\ f=\{(x,t)\ |\ t\le f(t)\}
$$
is a convex set.

​	Many results for convex functions can be proved (or interpreted) geometrically using epigraphs, and applying results for convex sets. As an example, consider the first-order condition for convexity:
$$
f(y)\ge f(x)+\nabla f(x)^T(y-x)
$$
where $f$ is convex and $x,y\in\mathrm{\textbf{dom}}\ f$.  We can interpret this basi inequality geometrically in terms of $\mathrm{\textbf{epi}}\ f$. If $(y,t)\in \mathrm{\textbf{epi}}\ f$, then
$$
t\ge f(y)\ge f(x)+\nabla f(x)^T(y-x)
$$
We can express this as:
$$
(y,t)\in\mathrm{\textbf{epi}}\ f\Longrightarrow
\begin{bmatrix}
\nabla f(x)\\ -1
\end{bmatrix}^T
\left(
\begin{bmatrix}y\\t \end{bmatrix}-
\begin{bmatrix}x\\f(x) \end{bmatrix}
\right)\le 0
$$
This means that the hyperplane defined by $(\nabla f(x),-1)$ supports $\mathrm{\textbf{epi}}\ f$ at the boundary point $(x,f(x))$.

#### 1.8 Jensen's inequality and extensions

​	The basic inequality 
$$
f(\theta x+(1-\theta)y) \le\theta f(x)+(1-\theta)f(y)
$$
is sometimes called *Jensen's inequality*. 

​	As in the case of convex sets, the inequality extends to infinite sums, integrals, and expected values. For example, if $p(x)\ge0$ on $S\subseteq\mathrm{\textbf{dom}}\ f$, $\int_Sp(x)\mathrm dx=1$, then
$$
f\left(\int_Sp(x)x\mathrm dx \right)\le\int_Sf(x)p(x)\mathrm dx
$$
​	If $x$ is a random variable such that $x\in\mathrm{\textbf{dom}}\ f$ with probability one, and $f$ is convex, then we have
$$
f(\mathrm{\textbf{E}}x)\le \mathrm{\textbf{E}}f(x)
$$
​	All of these ineqaulities are now called *Jensen's inequality*.

### 2. Operations that preserve convexity

#### 2.1 Nonnegative weighted sums

​	If $f(x,y)$ is convex in $x$ for every $y\in\mathcal A$, and $w(y)\ge0$ for every $y\in\mathcal A$, then the function $g$ defined as
$$
g = \int_{\mathcal A}w(y)f(x,y)\mathrm dy
$$
is convex in $x$ (provided that the integral exists).

#### 2.2 Composition with an affine mapping

​	Suppose $f: \R^n\rarr\R,A\in\R^{n\times m},b\in\R^n$ Define $g:\R^m\rarr\R$ by
$$
g(x)=f(Ax+b)
$$
with $\mathrm{\textbf{dom}}\ g=\{x\ |\ Ax+b\in\mathrm{\textbf{dom}}\ f\}$. If $f$ is convex, then so is $g$.

#### 2.3 Pointwise maximum and supremum

​	If $f_1$ and $f_2$ are convex functions then their *pointwise maximum* $f$, defined by
$$
f(x) = \max\{f_1(x),f_2(x)\}
$$
with $\mathrm{\textbf{dom}}\ f=\mathrm{\textbf{dom}}\ f_1\cap\mathrm{\textbf{dom}}\ f_2$ is also convex.

#### 2.4 Composition

​	Suppose $h:\R^k\rarr\R,g:\R^n\rarr\R^k$ and they are convex, then we discuss the convexity of their composition $f=h\circ g:\R^n\rarr\R$, defined as
$$
f = h(g(x)),\quad \mathrm{\textbf{dom}}\ f=\{x\in\mathrm{\textbf{dom}}\ g\ |\ g(x)\in\mathrm{\textbf{dom}}\ h\}
$$
Omitted.

### 3. The conjugate function

#### 3.1 Definitions

> The *supermum* of a subset $S$ of a partially ordered set $P$ is the least element in $P$ that is greater than or equal to each element of $S$, if such an element exists.

​	Let $f:\R^n\rarr\R$. The function $f^*:\R^n\rarr\R$ defined as
$$
f^*(y)=\sup_{x\in\mathrm{\textbf{dom}}\ f}(y^Tx-f(x))
$$
is called the *conjugate* of the function $f$. The domain of the conjugate function consists of $y\in\R^n$ for which the supremum is finite, *i.e.*, for which the difference $y^Tx-f(x)$ is bounded above on $\mathrm{\textbf{dom}}\ f$. 

​	We see immediately that $f^*$ is convex, since it is the pointwise supermum of a family of convex functions of $y$. This is true whether or not $f$ is convex.

#### 3.2 Basic properties

##### Fenchel's inequality

$$
f^*(y)+f(x)\ge y^Tx
$$

This is quite obvious.

##### Conjugate of the conjugate

​	The conjugate of the conjugate of a convex function is the original function.

##### Differentiable functions ★

​	The conjugate of a differentiable function $f$ is also called the *Legendre transform* of $f$. 

​	Suppose $f$ is convex and differentiable, with $\mathrm{\textbf{dom}}\ f=\R^n$. Any maximizer $x^*$ of $y^Tx-f(x)$ satisfies $y=\nabla f(x^*)$, and conversely, if $x^*$ satisfies $y=\nabla f(x^*)$, then $x^*$ maximizes $y^Tx-f(x)$. Therefore, if $y=\nabla f(x^*)$, we have
$$
f^*(y)=x^{*T}\nabla f(x^*)-f(x^*)
$$
This allows us to determine $f^*(y)$ for any $f$ for which we can solve the gradient equation $y=\nabla f(z)$ for any $z$.

​	We can express this another way. Let $z\in\R^n$ be arbitrary and define $y=\nabla f(z)$. Then we have
$$
f^*(y)=z^T\nabla f(z)-f(z)
$$

##### Scaling and composition with affine transformation

​	Suppose $A\in\R^{n\times n}$ is nonsingular and $b\in\R^n$. Then the conjugate of $g(x)=f(Ax+b)$ is 
$$
g^*(y)=f^*(A^{-T}y)-b^TA^{-T}y
$$
with $\mathrm{\textbf{dom}}\ g^* = A^T\mathrm{\textbf{dom}}\ f^*$.

##### Sums of independent functions

​	If $f(u,v) = f_1(u)+f_2(v)$, where $f_1$ and $f_2$ are convex functions with conjugates $f_1^*$ and $f_2^*$, respectively, then
$$
f^*(w,z)=f_1^*(w)+f^*_2(z)
$$

### 4. Quasiconvex functions

#### 4.1 Definition

​	A function $f:\R^n\rarr\R$ is called *quasiconvex* if its domain and all its sublevel sets
$$
S_\alpha=\{x\in\mathrm{\textbf{dom}}\ f\ |\ f(x)\le\alpha\}
$$
for all $\alpha\in\R$, are convex. A function is *quasiconcave* if $-f$ is quasiconvex, *i.e.*, every superlevel set $\{x\ |\ f(x)\ge\alpha\}$ is convex.

​	A function that is both quasiconvex and quasiconcave is called *quasilinear*. If a function is quasilinear, then its domain, and every level set $\{x\ |\ f(x)=\alpha\}$ is convex. 

​	For a function on $\R$, quasiconvexity  requires that each sublevel set to be an interval. All convex functions are quasiconvex, but not all quasiconvex functions are convex, so quasiconvexity is a generalization of convexity.

#### 4.2 Basic properties

​	A function is quasiconvex if and only $\mathrm{\textbf{dom}}\ f$ is convex and for any $x,y\in\mathrm{\textbf{dom}}\ f$ and $0\le\theta\le1$,
$$
f(\theta x+(1-\theta y))\le\max\{f(x),f(y)\}
$$

##### Quasiconvex functions on $\R$

​	A continuous function $f:\R\rarr\R$ is quasiconvex if and only if at least one of the following conditions holds:

- $f$ is nondecreasing
- $f$ is nonincreasing
- there is a point $c\in\mathrm{\textbf{dom}}\ f$ such that for $t\le c$ (and $t\in\mathrm{\textbf{dom}}\ f$), $f$ is nonincreasing, and for $t\ge c$ (and $t\in\mathrm{\textbf{dom}}\ f$), $f$ is nondecreasing.

#### 4.3 Differentiable quasiconvex functions

##### First-order conditions

​	Suppose $f:\R^n\rarr\R$ is differentiable. Then $f$ is quaisconvex if and only if $\mathrm{\textbf{dom}}\ f$ is convex and for all $x,y\in\mathrm{\textbf{dom}}\ f$
$$
f(y)\le f(x)\Longrightarrow\nabla f(x)^T(y-x)\le 0\tag{4.1}
$$
​	**Proof**	It suffices to proove the result for a function on $\R$; the general result follows by restrication to an arbitrary line.

​	Suppose $f$ is differentiable function on $\R$ and satisfies
$$
f(y)\le f(x)\Longrightarrow f'(x)(y-x)\le 0
$$
Suppose $f(x_1)\ge f(x_2)$ where $x_1\ne x_2$. We assume $x_2>x_1$, and show that $f(z)\le f(x_1)$ for $z\in[x_1,x_2]$. Suppose there exists a $z\in[x_1,x_2]$ with $f(z)>f(x_1)$. Since $f$ is differentiable, we can choose a $z$ that also satisfies $f'(z)<0$. Because
$$
f(x_2)\le f(x_1)<f(z)\Longrightarrow f'(z)(x_2-z)\le 0
$$
However, $f(x_1)<f(z)\Longrightarrow f'(z)(x_1-z)\le0$ implies $f'(z)\ge0$, which contradicts $f'(z)<0$.

​	To prove suffciency, assume $f$ is quasiconvex. Suppose $f(x)\ge f(y)$. By the definition of quasiconvexity $f(x+t(y-x))\le f(x)$ for $0<t\le1$. Diving both sides by $t$, taking limit for $t\rarr0$, we obtain
$$
\lim_{t\rarr0}\frac{f(x+t(y-x))-f(x)}t=f'(x)(y-x)\le0
$$
​	The condition (4.1) has a simple geometric interpretation when $\nabla f(x)\ne0$. It states that $\nabla f(x)$ defines a supporting hyperplane to the sublevel set $\{y\ |\ f(y)\le f(x)\}$, at the point $x$.	

##### Second-order conditions

​	Now suppose $f$ is twice differentiable. If $f$ is quasiconvex, then for all $x\in\mathrm{\textbf{dom}}\ f$, and all $y\in\R^n$, we have
$$
y^T\nabla f(x)=0\Longrightarrow y^T\nabla^2f(x)y\ge0\tag{4.2}
$$
For a quasicconvex function on $\R$, this reduces a simple condition
$$
f'(x)=0\Longrightarrow f''(x)\ge0
$$
For a quasiconvex function on $\R^n$, when $\nabla f(x)\ne0$, the condition (4.2) means that $\nabla^2f(x)$ is positive semidefinite on the $(n-1)$-dimensional subspace $\nabla f(x)^{\perp}$. This implies that $\nabla^2f(x)$ can have at most one negative eigenvalue.

​	As a (partial) converse, if $f$ satisfies
$$
y^T\nabla f(x)=0\Longrightarrow y^T\nabla^2f(x)y\ge0
$$
for $x\in\mathrm{\textbf{dom}}\ f$ and all $y\in\R^n,y\ne0$, then $f$ is quasiconvex.

#### 4.4 Operatinos that preserve quasiconvexity

Omitted

#### 4.5 Representation via family of convex functions

​	In the sequel, it will be convenient to represent the sublevel sets of a quasiconvex function $f$ (which are convex) via inequalities of convex functions. We seek a family of convex functinos $\phi_t:\R^n\rarr\R$, indexed by $t\in\R$, with
$$
f(x)\le t\Longleftrightarrow\phi_t(x)\le0\tag{4.3}
$$
​	To see that such a representable always exists, we can take
$$
\phi_t(x)=\left\{\begin{align}&0&&f(x)\le t\\&\infin&&\mathrm{otherwise} \end{align}\right.
$$

### 5. Log-concave and log-convex functions

Omitted

### 6. Convexity with respect to generalized inequalities

#### 6.1 Monotonicity with respect to a generalized inequality

​	Suppose $K\subseteq\R^n$ is a proper cone with associated generalized inequality $\preceq_K$. A function $f:\R^n\rarr\R$ is called *K-nondecreasing* if
$$
x\preceq_K y\Longrightarrow f(x)\le f(y)
$$
and *K-increasing* if 
$$
x\prec_K y,x\ne y\Longrightarrow f(x)<f(y)
$$

##### Gradient conditions with monotonicity

​	A differentiable function $f$, with convex domain, is $K$-nondecreasing if and only if 
$$
\nabla f(x)\succeq_{K^*}0
$$
for all $x\in\mathrm{\textbf{dom}}\ f$. The converse is not true.

#### 6.2 Convexity with respect to a generalized inequality

​	Suppose $K\subseteq\R^m$ is a proper cone with associated generalized inequality $\preceq_K$. We say $f: \R^n\rarr\R^m$ is $K$*-convex* if for all $x,y$, and $0\le\theta\le1$,
$$
f(\theta x+(1-\theta)y)\preceq_K\theta f(x)+(1-\theta)f(y)
$$

##### Dual characterization of $K$-convexity

​	A function $f$ is $K$-convex if and only for every $w\succeq_{K^*}0$, the function $w^Tf$ is convex.

##### Differentiable $K$-convex functions

​	A differentiable function $f$ is  $K$-convex if and only if its domain is convex, and for all $x,y\in\mathrm{\textbf{dom}}\ f$,
$$
f(y)\succeq_Kf(x)+\mathrm Df(x)(y-x)
$$
(Here $\mathrm Df(x)\in\R^{m\times n}$ is the derivative or Jacobian matrix of $f$ at $x$).

> Suppose $f:\R^n\rarr\R^m$, the Jacobian matrix of $f$ is defined as
> $$
> J=
> \begin{bmatrix}
> \displaystyle\frac{\part f_1}{\part x_1}&
> \cdots&
> \displaystyle\frac{\part f_1}{\part x_n}\\
> \vdots & \ddots &\vdots\\
> \displaystyle\frac{\part f_m}{\part x_1}&
> \cdots&
> \displaystyle\frac{\part f_m}{\part x_n}
> \end{bmatrix}
> $$

##### Composition theorem

​	If $g:\R^n\rarr\R^p$ is  $K$-convex, $h:\R^p\rarr\R$ is convex, and $\tilde h$(the extended-value extensions of $h$) is $K$-nondecreasing, then $h\circ g$ is convex.