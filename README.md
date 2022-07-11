# Project Euler

## Problem 65 - Convergents of *e*

The square root of 2 can be written as an infinite continued fraction.

$\qquad\sqrt{2} = 1 + \displaystyle\cfrac{1}{\displaystyle 2+\cfrac{1}{\displaystyle 2+\cfrac{1}{\displaystyle 2+\cfrac{1}{\displaystyle 2+\dots}}}}$

The infinite continued fraction can be written, $\sqrt{2} = [1;(2)],\quad(2)$ indicates that 2 repeats *ad infinitum*.

In a similar way, $\sqrt{23} = [4;(1,3,1,8)]$.

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations.

Let us consider the convergents for $\sqrt{2}$.

$\qquad\displaystyle 1 + \cfrac{1}{2} = \cfrac{3}{2}$

$\qquad\displaystyle 1 + \cfrac{1}{\displaystyle 2+\cfrac{1}{2}} = \cfrac{7}{5}$

$\qquad\displaystyle 1 + \cfrac{1}{\displaystyle 2+\cfrac{1}{\displaystyle 2+\cfrac{1}{2}}} = \cfrac{17}{12}$

$\qquad\displaystyle 1 + \cfrac{1}{\displaystyle 2+\cfrac{1}{\displaystyle 2+\cfrac{1}{\displaystyle 2+\cfrac{1}{2}}}} = \cfrac{41}{29}$

Hence the sequence of the first ten convergents for $\sqrt{2}$ are:

$\qquad\displaystyle 1, \frac{3}{2}, \frac{7}{5}, \frac{17}{12}, \frac{41}{29}, \frac{99}{70}, \frac{239}{169}, \frac{577}{408}, \frac{1393}{985}, \frac{3363}{2378}, \dots$

What is most surprising is that the important mathematical constant,

$e = [2;1,2,1,1,4,1,1,6,1,\dots,1,2k,1,\dots]$.

The first ten terms in the sequence of convergents for *e* are:

$\qquad\displaystyle 2, 3, \frac{8}{3}, \frac{11}{4}, \frac{19}{7}, \frac{87}{32}, \frac{106}{39}, \frac{193}{71}, \frac{1264}{465}, \frac{1457}{536}, \dots$

The sum of digits in the numerator of the 10<sup>th</sup> convergent is 1 + 4 + 5 + 7 = 17.

Find the sum of digits in the numerator of the 100<sup>th</sup> convergent of the continued fraction for $e$.
