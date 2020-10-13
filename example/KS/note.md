# Kuramoto-Sivashinsky (KS) Equations

考虑 *KS* 方程

$$
\partial_t u = -\partial_x^4 u - \partial_x^2 u - u\partial_x u,\quad x\in(-\infty, \infty), t>0 \\
u(t, x) = u(t, x+2L\pi),\partial_x u(x, t)=\partial_x u(t, x+2L\pi),\quad t>0 \\
u(0, x) = u_0(x),\quad x\in(-\infty, \infty)
$$

其中, $u_0$ 是以 $2L\pi$ 为周期的函数.

$$
\frac{\mathrm{d}\widehat{u}}{\mathrm{d}t}=(-k^4+k^2)\widehat{u}-\widehat{u u_x}
$$

$\widehat{v}=\exp((k^4-k^2)t)\widehat{u}$

$$
\frac{\mathrm{d}\widehat{v}}{\mathrm{d}t}=-g\cdot\widehat{u u_x}
$$
