# Simple Motions 

The simple motions model supposes that the plant is moving non-inertially on the plane with a constrained speed. The equations of motion for the model are the following:
$$\dot{x} = v\cos\varphi,$$
$$\dot{y} = v\sin\varphi.$$
Here, $v(t) \in [-v_{\max}, +v_{\max}]$, $\varphi(t) \in \mathbb{S}$ are control inputs ($v_{\max} \in \mathbb{R}^+$ is the maximal speed and $\mathbb{S}$ is a space of angels). If the control inputs are given than the state coordinates can be calculated by the following way:
$$x(t) = x_0 + \int\limits_{t_0}^t v(t)\cos\varphi(t)\mathrm{d}t,$$
$$y(t) = y_0 + \int\limits_{t_0}^t v(t)\sin\varphi(t)\mathrm{d}t.$$
$(x_0, y_0) \in \mathbb{R}^2$ and $t_0 \in \mathbb{R}$ present the initial state and the initial time moment.

The canonical case of the simple motions model demands $x_0 = y_0 = t_0 = 0$ and $v_{\max} = 1$.