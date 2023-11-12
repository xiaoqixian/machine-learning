# Convex Sets

### 1. Affine and convex sets

#### 1.1 Affine sets

​	A set $C\in\R^n$ is *affine* if the line through any two distinct points in $C$ lies in $C$, which means $\forall x_1,x_2\in C,\theta\in\R$, we have $\theta x_1+(1-\theta)x_2\in C$.

​	An affine set $C$ can be expressed as
$$
C = V+x_0=\{v+x_0\ |\ v\in V\}
$$
*i.e.,* as a subspace plus an offset.

​	Every affine set can be expressed as the solution set of a system of linear equations.
$$
C = \{x\ |\ Ax=b \}, A\in\R^{m\times n},b\in \R^m
$$
​	The set of all affine combinations of points in some set $C\in\R^n$ is called the *affine hull* of $C$, and denoted $\mathrm{aff}\ C$:
$$
\mathrm{aff}\ C = \{\theta_1x_1+\cdots +\theta_kx_k\ |\ x_1,...,x_k\in C, \theta_1+\cdots+\theta_k=1\}
$$

>- The affine hull of the empty set is the empty set.
>- The affine hull of a singleton (a set made of one single element) is the singleton itself.
>- The affine hull of a set of two different points is the line through them.
>- The affine hull of a set of three different points not on one line is the plane going through them.
>- The affine hull of a set of four points not in a plane in $\R^3$ is the entire space $\R^3$.

#### 1.2 Affine dimension and relative interior

​	We define the *affine dimension* of a set $C$ as the dimension of its affine hull. 

​	If the affine dimension of a set $C\subseteq\R^n$ is less than $n$, then the set lies in the affine set $\mathrm{aff}\ C\ne \R^n$.

​	We define the *relative interior* of the set $C$, denoted $\mathrm{relint}\ C$, as its interior relative to $\mathrm{aff}\ C$:
$$
\mathrm{relint}\ C =\{x\in C\ |\ B(x,r)\cap\mathrm{aff}\ C\subseteq C\ \mathrm{for\ some}\ r>0 \}
$$
where $B(x,r) = \{y\ |\ \|y-x\|\le r\}$, the ball of radius $r$ and center $x$ in the norm $\|\cdot\|$.

> In mathematics, a **normed vector space** is a vector space over the real or complex numbers on which a norm is defined.
>
> A norm is a generalization of the intuitive motion of "length" in the physical world. If $V$ is a vector space over $K$, where $K$ is a field equal to $\C$ or $\R$, then a norm on $V$ is a map $V\rightarrow \R$, typically denoted as $\|\cdot\|$, satisfying the following four axioms: 
>
> 1. **Non-negativity**: for every $x\in V,\|x\|\ge0$
> 2. **Positive Definiteness**: for every $x\in V, \|x\|=0$ if and only if $x$ is the zero vector
> 3. **Absolute Homogeneity**: for every $\lambda\in K,x\in V$, $\|\lambda x\|=|\lambda|\ \|x\|$
> 4. **Triangle Inequality**: for every $x\in V, y\in V$, $\|x+y\|\le\|x\|+\|y\|$

The relative interior can be equivalently defined as
$$
\begin{align}
\mathrm{relint}\ C &:= \{x\in C\ |\ \forall\ y\in C, \exist\ \lambda>1,  \lambda x+(1-\lambda)y\in C
\}
\end{align}
$$

#### 1.3 Convex sets

​	A set $C$ is *convex* if the line segment between **any** two points in $C$ lies in $C$.

​	Obviously every affine set is convex, since it contains the entire line between any two distinct points in it.

​	A point of the form $\theta_1x_1+\cdots+\theta_kx_k$, where $\theta_1+\cdots+\theta_k=1$ and $\theta_i\ge0,i=1,...,k$, is a *convex combination* of point $x_1,...,x_k$.  A set is convex if and only if it contains every convex combination of its points.

​	 The *convex hull* of a set $C$, denoted $\mathrm{conv}\ C$, is the set of all convex combinations of points in $C$:
$$
\mathrm{conv}\ C = \{\theta_1x_1+\cdots+\theta_kx_k\ |\ x_i\in C,\theta_i\ge 0,i=1,...,k,\theta_1+\cdots+\theta_k=1\}
$$
​	$\theta_i\ge0$ is the key difference between convex hull and affine hull.

​	More generally, suppose $p:\R^n\rarr\R$ satisfies $p(x)\ge0$ for all $x\in C$ and $\displaystyle{\int_Cp(x)\mathrm d}x =1$, where $C\in \R^n$ is convex. Then
$$
\int_Cp(x)x\ \mathrm dx\in C
$$
if the integral exists.

#### 1.4 Cones

​	A set $C$ is called a *cone*, or *nonnegative homogeneous*, if for every $x\in C$ and $\theta\ge0$ we have $\theta x\in C$. A set $C$ is a *convex cone* if it is convex and a cone, which means that for any $x_1, x_1\in C$ and $\theta_1,\theta_2\ge 0$, we have
$$
\theta_1x_1+\theta_2x_2\in C
$$
​	*conic combination*: a point of the form $\theta_1x_1+\cdots+\theta_kx_k$ with $\theta_1,...,\theta_k\ge0$. 

​	Every conic combination of every point in a convex cone is also in the same convex cone.

​	The *conic hull* of a set $C$:
$$
\{\theta_1x_1 +\cdots +\theta_kx_k\ |\ x_i\in C,\theta_i\ge0,i=1,...,k \}
$$

#### 1.5 Some important examples

- The empty set $\empty$, any single point, and the whole space $\R^n$ are affine(hence, convex) subsets of $\R^n$
- Any line is affine. If it passes zero, it is a subspace, hence also a convex cone. 
- A line segment is convex, but not affine (unless it reduces to a point)
- A *ray*, which has the form $\{x_0+\theta v\ |\ \theta\ge0\}$, where $v\ne0$, is convex, but not affine. It is a convex cone if its base $x_0$ is 0.
- Any subspace is affine, and a convex cone (hence convex).

### 2. Hyperplanes and halfspaces

​	A *hyperplane* is a set of the form
$$
\{x\ |\ a^Tx=b\}
$$
where $a\in\R^n, a\ne 0, b\in \R$.  Analytically, it is the solution set of a nontrivial linear equation among the components of $x$. Geometrically, it is a hyperplane with *normal vector $a$*, the constant $b$ is the offset of the hyperplane from the origin.

​	It can also be expressed as 
$$
\{x\ |\ a^T(x-x_0)=0\} = x_0+a^\bot
$$
where $a^\bot$ denotes the orthogonal component of $a$:
$$
a^\bot = \{v\ |\ a^Tv=0 \}
$$
​	A hyperplane divides $\R^n$ into two *halfspaces*, which has the form of 
$$
\{x\ |\ a^Tx\le b \}
$$
A halfspace is convex but not affine.

#### 2.2 Euclidean balls and ellipsoids

​	A *Euclidean ball* in $\R^n$ has the form
$$
B(x_c, r) = \{x\ |\ \|x-x_c\|_2\le r\} = \{x\ |\ (x-x_c)^(x-x_c)\le r^2 \}
$$
where $r>0$.

​	A Euclidean ball is a convex set: if $\|x_1-x_c\|_2\le r,\|x_2-x_c\|_2\le r$, and $0\le\theta\le1$, then
$$
\begin{align}
\|\theta x_1+(1-\theta)x_2-x_c\| &= \|\theta(x-x_c)+(1-\theta)(x_2-x_c)\|_2\\
&\le\theta\|x-x_c\|_2+(1-\theta)\|x_2-x_c\|_2\\
&\le r
\end{align}
$$
​	A related family of convex sets is the *ellipsoids*, which have the form
$$
\varepsilon = \left\{x\ |\ (x-x_c)^TP^{-1}(x-x_c)\le1 \right\}
$$
where $P$ is symmetric and positive definite. The matrix $P$ determines how far the ellipsoid extends in every direction from the center $x_c$; the length of the semi-axes of $\varepsilon$ are give by $\sqrt{\lambda_i}$ where $\lambda_i$ are the **eigenvalues** of $P$.

#### 2.3 Norm balls and norm cones

​	The *norm cone* associated with the norm $\|\cdot\|$ is the set
$$
C = \left\{(x,t)\ |\ \|x\|\le t \right\}\subseteq\R^{n+1}
$$

#### 2.4 Polyhedra

​	A *polyhedra* is defined a solution set of a finite number of equalities and inequalities:
$$
\mathcal P = \left\{x\ |\ a_j^Tx\le b_j,j=1,...,m,\ c^T_jx=d_j,j=1,...,p \right\}
$$
A polyhedra is thus the intersection of a finite number of halfspaces and hyperplanes. Affine sets, rays, line segments, and halfspaces are all polyhedra.

​	The compact notation:
$$
\mathcal P = \left\{x\ |\ Ax\preceq b, Cx=d \right\}
$$
where
$$
A=\begin{bmatrix}a_1^T\\\vdots\\a_m^T \end{bmatrix},\quad 
C= \begin{bmatrix}c_1^T\\\vdots\\c_p^T \end{bmatrix}
$$

##### Simplexes

​	*Simplexes* are another important family of polyhedra. Suppose the $k+1$ points $v_0,...,v_k\in\R^n$ are *affinely independent*, which means that $v_1-v_0,...,v_k-v_0$ are linearly independent. The simplex determined by them is given by
$$
C = \mathrm{\textbf{conv}} \{v_1,...,v_k\} = \{\theta_0v_0+\cdots+\theta_kv_k\ |\ \theta\succeq 0, \textbf 1^T\theta=1 \}
$$
The affine dimension of this simplex is $k$, so it sometimes referred to as a $k$-dimensional simplex in $\R^n$.

> - A 1-dimensional simplex is a line segment.
> - A 2-dimensional simplex is a triangle includes it interior.
> - A 3-dimensional simplex is a tetrahedron.
> - The unit complex is the n-dimensional simplex determined by a zero-vector and the unit vectors.

​	To describe the simplex as a polyhedron, we define $y=(\theta_1,...,\theta_k)$ and 
$$
B=\left[v_1-v_0,\cdots,v_k-v_0\right] \in \R^{n\times n}
$$
we can say that $x\in C$ if and only if
$$
x = v_0+By
$$
Note that matrix $B$ has rank $k$, so there exists a nonsingular matrix $A=(A_1,A_2)\in\R^{n\times n}$ such that
$$
\begin{bmatrix}A_1\\A_2 \end{bmatrix}B=\begin{bmatrix}I\\0 \end{bmatrix}
$$
Multiplying on the left with $A$, we get
$$
A_1x=A_1v_0+y,\quad A_2x=A_2v_0
$$
As $y$ satisfies $y\succeq0$ and $\textbf 1^Tyt\le1$, in other words we have $x\in C$ if and only if 
$$
A_2x=A_2v_0,\quad A_1x\succeq A_1v_0,\quad 1^TA_1x\le1+\textbf1^TA_1v_0
$$
which is a set of linear equalities and inequalities in $x$, and so describes a polyhedron.

##### Convex hull description of polyhedra

​	The convex hull of polyhedron:
$$
\mathrm{\textbf{conv}}\left\{v_1,...,v_k\right\} = \left\{\theta_1v_1+\cdots+\theta_kv_k\ |\ \theta\succeq 0, \textbf1^T\theta=1 \right\}
$$
A generalization of this convex hull description:
$$
\left\{\theta_1v_1+\cdots+\theta_kv_k\ |\ \theta_1+\cdots+\theta_m=1,\theta_i\ge0,i=1,...,k \right\}
$$
where $m\le k$. We only require the first $m$ coefficients to sum to one.

#### 2.5 The positive semidefinite cone

​	Notation $S^n$ represents a symmetric $n\times n$ matrix
$$
S^n = \{X\in \R^{n\times n}\ |\ X = X^T \}
$$
which is a vector space with dimension $n(n+1)/2$. Also
$$
\begin{align}
&S^n_+ = \{X\in \R^{n\times n}\ |\ X\succeq 0 \}\\
&S^n_{++} = \{X\in \R^{n\times n}\ |\ X\succ 0 \}
\end{align}
$$

### 3. Operations that preserve convexity

#### 3.1 Intersection

​	Convexity is preserved under intersection: if $S_1$ and $S_2$ are convex, then $S_1\cap S_2$ is convex.

​	This property extends to the intersection of an infinite number of sets: if $S_\alpha$ is convex for every $\alpha\in\mathcal A$, then $\bigcap_{\alpha\in\mathcal A}S_\alpha$ is convex. The positive semidefinite cone can be expressed as 
$$
\bigcap_{z\ne0}\left\{X\in S^n\ |\ z^TXz\ge 0\right\}
$$
In fact, a closed convex set $S$ is the intersection of all halfspaces that contain it:
$$
S=\bigcap\ \left\{\mathcal H\ |\ \mathcal H\ \mathrm{halfspace}, S\subseteq\mathcal H\right\}
$$

#### 3.2 Affine functions

​	A function $f: \R^n\rarr\R^m$ is *affine* if it is a sum of a linear function and a constant, *i.e.,* if it has the form $f(x)=Ax+b$, where $A\in\R^{m\times n},b\in\R^m$. 

​	Suppose $S\subseteq\R^n$ is convex and $f:\R^n\rarr\R^m$ is an affine function, then the image of $S$ under $f$
$$
f(S) =\left\{f(x)\ |\ x\in S \right\}
$$
is convex. Similarly, if $f:\R^k\rarr\R^n$ is an affine function, the *inverse image* of $S$ under $f$
$$
f^{-1}(S) = \{x\ |\ f(x)\in S\}
$$
is convex.

#### 3.3 Linear-fractional and perspective functions

##### The perspective function

​	We define the *perspective function* $P: \R^{n+1}\rarr\R^n$, with domain $\mathrm{\textbf{dom}}\ P=\R^n\times\R_{++}$. The perspective function scales or normalizes vectors so the last component is one, and then drops the last component.

​	Suppose that $x=(\tilde x, x_{n+1}), y=(\tilde y, y_{n+1})\in\R^{n+1}$ with $x_{n+1}>0,y_{n+1}>0$. Then for $0<\theta<1$
$$
P(\theta x+(1-\theta)y) = \frac{\theta\tilde x+(1-\theta)\tilde y}{\theta x_{n+1}+(1-\theta)y_{n+1}}=\mu P(x) +(1-\mu)P(y)
$$
where
$$
\mu = \frac{\theta x_{n+1}}{\theta x_{n+1}+(1-\theta)y_{n+1}}\in[0,1]
$$
The correspondence between $\mu$ and $\theta$ is monotonic. 

​	The inverse image of a convex set under the perspective function is also convex: if $C\subseteq\R^n$ is convex, then
$$
P^{-1}(C) =\left\{(x,t)\ |\ x/t\in C, t>0 \right\}
$$
is convex. 

##### Linear-fractional functions

​	A *linear-fractional function* is formed by composing the perspective function with an affine function. Suppose $g:\R^n\rarr\R^{m+1}$ is affine, *i.e.*,
$$
g(x) =\begin{bmatrix}A\\c^T \end{bmatrix}x+\begin{bmatrix} b\\d\end{bmatrix}
$$
where $A\in\R^{m\times n}, b\in\R^m,c\in\R^n, d\in R$. The function $f:\R^n\rarr\R^m$ given by $f = P\circ g$, *i.e.*,
$$
f(x)=(Ax+b)/(c^Tx+d),\quad \mathrm{\textbf {dom}}\ f=\{x\ |\ c^Tx+d>0\}
$$
 is called a *linear-fractional* (or *projective*) function.

​	Like the perspective function, linear-fractional functions preserve convexity.  

### 4. Generalized inequalities

#### 4.1 Proper cones and generalized inequalities

​	A cone $K\subseteq\R^n$ is called a *proper cone* if it satisfies the following:

- $K$ is convex
- $K$ is closed
- $K$ is *solid*, which means it has nonempty interior
- $K$ is *pointed*, which means it contains no line (or equivalently, $x\in K, -x\in K\Longrightarrow x=0$)

​	We associate with the proper cone $K$ the partial ordering on $\R^n$ defined by
$$
x\preceq_Ky\Longleftrightarrow y-x\in K
$$
Similarly, we define an associated strict partial ordering by
$$
x\prec_Ky\Longleftrightarrow y-x\in\mathrm{\textbf{int}}\ K
$$
$\mathrm{\textbf{int}}\ K$ represents the interior of $K$. 

​	When $K=\R_+$, the partial ordering is $\le$ on $\R$.  

##### Properties of generalized inequalities

​	A generalized inequality $\preceq_K$ satisfies many properties, such as

- *preserved under addition*
- *transitive*
- *preserved under nonnegative scaling*
- *reflexive*: $x\preceq_K x$
- *antisymmetric*: if $x\preceq_Ky$ and $y\preceq_Kx$, then $x=y$
- *preserved under limits*: if $x_i\preceq_K y_i$, for $i=1,...,x_i\rarr x$ and $y_i\rarr y$ as $i\rarr\infin$, then $x\preceq_K y$

#### 4.2 Minimum and minimal elements

​	We say that $x\in S$ is the *minimum element* of $S$ if for every $y\in S$, $x\preceq_K y$.  We define the maximum element in a similar way. If a set has minimum element, the set is unique. 

​	We say that $x\in S$ is the *minimal element* of $S$ if $y\in S, y\preceq_K x$, then $y = x$. A set can have many different minimal (maximal) elements.

​	A point $x\in S$ is the minimum element of $S$ if and only if
$$
S\subseteq x+K
$$
​	A point $x\in S$ is the minimal element of $S$ if and only if
$$
(x-K)\cap S=\{x\}
$$

### 5. Separating and supporting hyperplanes

#### 5.1 Separating hyperplane theorem

​	*separating hyperplane theorem*: Suppose $C$ and $D$ are nonempty disjoint convex sets, and $C\cap D=\empty$, then there exists $a\ne0$ and $b$ such that for all $x\in C$, $ax\le b$, and for every $x\in D$, $ax\ge b$. 

##### Proof of separating hyperplane theorem

​	Here we consider a special case, we assume that the Euclidean distance between $C$ and $D$, defined as
$$
\mathrm{\textbf{dist}}(C,D)=\inf\{\|u-v\|_2\ |\ u\in C, v\in D\}
$$

>  $\inf S$ represents the greatest lower bound of set $S$.

is positive, and there exists $c\in C, d\in D$ that achieve the minimum distance. 

​	Define
$$
a=d-c,\quad b=\frac{\|d\|_2^2-\|c\|^2_2}2
$$
Now we need to prove that the affine function
$$
f(x)=a^Tx-b=(d-c)^T(x-(1/2)(d+c))
$$
is nonpositive on $C$, and nonnegative on $D$, *i.e.*, the hyperplane $\{x\ |\ a^Tx=b\}$ separates $C$ and $D$. This hyperplane is *perpendicular* to the line segment between $c$ and $d$. 

​	We first show that $f$ is nonnegative on $D$, suppose there is point $u\in D$ for which
$$
f(u) =(d-c)^T(u-d+(1/2)(d+c))=(d-c)^T(u-d)+\frac12\|d-c\|^2_2
$$
Obviously $(d-c)^T(u-d)<0$, now we observe that
$$
\left.\frac{\mathrm d}{\mathrm dt}\|d+t(u-d)-c\|^2_2\right|_{t=0} = 2(d-c)^T(u-d)<0
$$
so for some small $t>0$, with $t\le1$, we have
$$
\|d+t(u-d)-c\|_2 < \|d-c\|_2
$$
*i.e.*, the point $d+t(u-d)$ is a closer point to $c$ than $d$ is, which is contradictory to our assumption. So $f$ is nonnegative on $D$.

##### Strict separation

​	If the separating hyperplane we constructed above satisfies the stronger condition that $a^Tx<b$ for all $x\in C$ and $a^Tx>b$ for all $x\in D$. This is called *strict separation* of the sets $C$ and $D$. 

##### Converse separating hyperplane theorems

​	The converse of the separating hyperplane theorem (*i.e.*, existence of a separating  hyperplane implies that $C$ and $D$ do not intersect) is **not true**.

​	But by adding conditions on $C$ and $D$, we can have the following result: any two convex sets, at lease one of which is open, are disjoint if and only if exists a separating hyperplane.

#### 5.2 Supporting hyperplanes

​	Suppose $C\subseteq\R^n$, and $x_0$ is a point in its boundary $\mathrm{\textbf{bd}}\ C$.

If $a\ne0$ satisfies $a^Tx\le a^Tx_0$ for all $x\in C$, then the hyperplane $\{x\ |\ a^Tx=a^Tx_0\}$ is called a *supporting hyperplane* to $C$ at the point $x_0$. This is equivalent to saying that the set $C$ and the point $x_0$ are separated by the hyperplane $\{x\ |\ a^Tx=a^Tx_0\}$.  And $a$ is the normal vector of this hyperplane.

​	A basic result, called the *supporting hyperplane theorem*, states that for any point $x_0\in\mathrm{\textbf{bd}}\ C$, there exists a supporting hyperplane to $C$ at $x_0$. 

​	We distinguish two cases, if the interior of set $C$ is not empty, the result follows immediately by applying the separating hyperplane theorem to the sets $\{x_0\}$ and $\mathrm{\textbf{int}}\ C$. If the interior of $C$ is empty, then $C$ must lies in a affine set of dimension less than  $n$. and any hyperplane containing that affine set contains $C$ and $x_0$, and is a supporting hyperplane.

### 6. Dual cones and generalized inequalities

#### 6.1 Dual cones

​	Let $K$ be a cone. The set
$$
K^* = \{y\ |\ x^Ty\ge0\ \mathrm{for\ all\ }x\in K\}
$$
is called a *dual cone* of $K$. $K^*$ is a cone, and is always convex, even when the original cone $K$ is not.

​	Geometrically, $y\in K^*$ if and only if $-y$ is the normal of a hyperplane that supports $K$ at the origin. 

​	A cone whose dual cone is itself is called a *self-dual cone*.

​	Dual cones satisfy several properties, such as:

- closed and convex.
- $K_1\subseteq K_2$ implies $K_1^*\subseteq K_2^*$.
- If $K$ has nonempty interior, then $K^*$ is pointed.
- If the closure of $K$ is pointed then $K^*$ has nonempty interior.
- $K^{**}$ is the closure of convex hull of $K$. (Hence is $K$ is convex and closed, $K^{**}=K$.)

#### 6.2 Dual generalized and inequalities

​	Now suppose that the convex cone $K$ is proper, so it induces a generalized inequality $\preceq_K$. The its dual cone $K^*$ is also proper, and induces a generalized inequality $\preceq_{K^*}$. We refer it as the *dual* of the generalized inequality $\preceq_K$.

​	Some important proprtties relating a generalized inequality and its dual are:

- $x\preceq_Ky$ if and only if $\lambda^Tx\le\lambda^Ty$ for all $\lambda\succeq_{K^*}0$.
- $x\prec_Ky$ if and only if $\lambda^Tx<\lambda^Ty$ for all $\lambda\succeq_{K^*}0,\lambda\ne0$.

#### 6.3 Minimum and minimal elements via dual inequalities

##### Dual characterization of minimum element

​	$x$ is the minimum element of $S$, with respect to the generalized inequality $\preceq_K$, if and only if for all $\lambda\succ_{K^*}0$, $x$ is the unique minimizer of $\lambda^Tz$ over $z\in S$. Geometrically, this means that for any $\lambda\succ_{K^*}0$, the hyperplane
$$
\{z\ |\ \lambda^T(z-x)=0 \}
$$
is a strict supporting hyperplane to $S$ at $x$. 

##### Dual characterization of minimal element

​	If $\lambda\succ_{K^*}0$ and $x$ minimizes $\lambda^Tz$ over $z\in S$, then $x$ is minimal.

​	Convexity plays an important role in the converse, provided the set $S$ is convex, we can say that for any minimal element $x$ there exists a **nonzero** $\lambda\succeq_{K^*}0$ such that $x$ minimizes $\lambda^Tz$ over $z\in S$.

​	This converse theorem cannot be strengthened to $\lambda\succ_{K^*}0$.