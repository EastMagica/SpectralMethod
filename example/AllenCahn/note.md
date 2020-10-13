# Allen-Cahn Equations

----

## 1. Equations

$$
\partial_t \phi=-\lambda(-\varepsilon^2\Delta\phi + \phi^3 - \phi)\tag{1}
$$

using Fourier Transform $\phi=\sum_{k,l=-N/2}^{N/2}\exp(i(kx+ly))\widehat{\phi}_{kl}$, then

## 2. Pseudo-Spectral Method

### 2.1 Fourier Transform

$$\begin{aligned}
    \frac{\mathrm{d}\widehat{\phi}}{\mathrm{d}t} &=-\lambda(\varepsilon^2(k_x^2+k_y^2)\widehat{\phi} + \widehat{\phi^3} - \widehat{\phi}) \\
    &=-\lambda\left(\varepsilon^2(k_x^2+k_y^2)+1\right)\widehat{\phi} - \lambda\widehat{\phi^3} \\
    &=L(\widehat{\phi})+\widehat{N(\phi)}
\end{aligned} \tag{2}
$$

<!-- ### 2.2 Eliminate Stiffness

let $g(t)=\exp\left(\lambda(\varepsilon^2(k_x^2+k_y^2)+1)t\right)$, and $\widehat{v}=g(t)\widehat{\phi}$, then we have

$$\begin{aligned}
\frac{\mathrm{d}\widehat{v}}{\mathrm{d}t} &= -\lambda g(t)\widehat{\phi^3} \\
\widehat{\phi} &= g(t)^{-1}\widehat{v}
\end{aligned} \tag{3}
$$ -->

## 3. Initial Condition

### 3.1 Circle Condition

Let $\lambda=1, \varepsilon=1, L_x=256, L_y=256$,

$$
\phi(x, y, 0)=\begin{cases}
    1, & x^2+y^2<100^2 \\
    -1, & x^2+y^2 \geq 100^2
\end{cases} \tag{4}
$$

### 3.2 Random Conditon

$$
\phi(x, y, 0)=\begin{cases}
    1, &\text{random}<0.5 \\
    -1, &\text{random}\geq 0.5 \\
\end{cases} \tag{5}
$$
