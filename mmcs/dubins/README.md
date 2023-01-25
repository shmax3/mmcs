# Dubins Car 

The Dubins model supposes that the plant is moving forward only on the plane with a constant speed and a constraint turning radius. The equations of motion for the model are the following:
$$
\dot{x} = v\cos\varphi, \\
\dot{y} = v\sin\varphi, \\
\dot{\varphi} = u.
$$
Here, $u(t) \in [-u_{\max}, +u_{\max}]$ is a control input, $v \in \mathbb{R}^+$ is a speed, and $u_{\max} \in \mathbb{R}^+$ is a maximal turning rate. If the control input is given than the state coordinates can be calculated by the following way:
$$
x(t) = x_0 + \int\limits_{t_0}^t v\cos\varphi(t)\mathrm{d}t, \\
y(t) = y_0 + \int\limits_{t_0}^t v\sin\varphi(t)\mathrm{d}t, \\
\varphi(t) = \varphi_0 + \int\limits_{t_0}^t u(t)\mathrm{d}t.
$$
$(x_0, y_0, \varphi_0) \in \mathbb{R}^2 \times \mathbb{S}$ and $t_0 \in \mathbb{R}$ present the initial state and the initial time moment. The minimal turning radius is $r_{\min} = v / u_{\max}$.

The canonical case of the Dubins model demands $x_0 = y_0 = t_0 = 0$, $\varphi_0 = \pi/2$, $v = 1$, and $u_{\max} = 1$.