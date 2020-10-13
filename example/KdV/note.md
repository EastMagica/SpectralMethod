# Korteweg-de Vries (KdV) Equations

考虑 *Kdv* 方程

$$\begin{aligned}
    &\partial_t u + u\partial_x u + \partial_x^3 u=0,\quad x\in(-\infty, \infty), t>0 \\
    &u(0, x) = u_0(x),\quad x\in(-\infty, \infty)
\end{aligned} \tag{1}
$$

且已知其精确孤子解

$$
u(t, x)=12\mathcal{K}^2\mathrm{sech}^2(\mathcal{K}(x-x_0)-4\mathcal{K}^3 t) \tag{2}
$$

选取截断区间 $(-\pi L, \pi L)$, 其中 $L>0$, 则方程 $(1)$ 转变为

$$\begin{aligned}
    &\partial_t u + u\partial_x u + \partial_x^3 u=0,\quad x\in(-\pi L, \pi L) \\
    &u(0, x) = u_0(x),\quad x\in(-\pi L, \pi L)
\end{aligned} \tag{3}
$$

令 $u(t, x)=\sum^{\infty}_{|k|=0}\widehat{u}_k(t)e^{ikx}$, 代入 $(3)$ 可得

$$
\partial_t \widehat{u} + \widehat{u\partial_x u} -ik^3 \widehat{u}=0,\quad k=0, \pm 1, \cdots \tag{4}
$$

对方程 $(4)$ 方程两侧乘以积分因子 $\exp(-ik^3t)$ 可得

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left[e^{-ik^3t}\widehat{u}_k\right] = -e^{-ik^3t}\widehat{u\frac{\mathrm{d}u}{\mathrm{d}x}} \tag{5}
$$

令 $\widehat{v}_k = e^{-ik^3t}\widehat{u}_k, g=e^{-ik^3t}$, 则可以得到

$$\begin{aligned}
    \frac{\mathrm{d}\widehat{v}}{\mathrm{d}t}&=-g\cdot\mathcal{F}(\mathcal{F}^{-1}(g^{-1}\cdot\widehat{v})\mathcal{F}^{-1}(g^{-1}\cdot ik\widehat{v})) \\
    \widehat{u}_k &= g^{-1}\cdot\widehat{v}
\end{aligned} \tag{6}
$$
