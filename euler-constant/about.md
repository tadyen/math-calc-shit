# Euler constant

This section is about the euler number `e ~ 2.71828`

This is NOT to be confused with the euler-*macceroni* constant and all other euler things because euler is the math GOAT with more than enough of his name to things.

## bruh this is like 200++ year old maths everyone knows about

yeah and?

## so why?

Because sandboxing why not? eg. School introduces **e** is some magic number where $\frac{d}{dx}e^x = e^x$ but we usually never really bat an eye more than that.

In uni level maths and beyond, e can be expressed as an infinite product, infinite sum, infinite fraction, etc.

eg.

Taylor-Maclauren series:

$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + ... = \sum^\infty_{n=0}\frac{x^n}{n!}$

amongst others

It's far from hands on and enters the realm of abstraction.

If asked for a *numerically computed* way of calculating e, it's usually via one of these infinite expressions which comes from an *analytical solution*.

It's never from first principals (for good reasons tbh).

However this also draws inspiration from how one can calculate $\pi$ numerically using an integral:

$\frac{\pi^2}{4} = \int^1_0 \sqrt{1 - x^2}{dx}$

which is simply the integral(area) of a unit circle in one quadrant. It's hard to obtain an analytical solution but easy to numerically compute.

This is actually a common exercise thrown at maths and cs students.

However the same treatment isn't exactly thought nor discussed with other common math constants so this is why I am sandboxxing this.

## Calculating e via derivative definition recursively

```txt
calculate Euler's number e via its derivative definition
e is approx 2.71828
The derivative definition is: d[e^x]/dx = e^x
in other words, if F(x) = f(x) then f(x) = e^x
we make a guess g, around x = 1, such that
  g = ae
and our psueudo-exp func,
  pexp(x) = (ae) ** x
since (ae)^x = e ^ (ln(a) * x)
thus d/dx {pexp}(x) = ln(a) * pexp(x)
in which
  pexp(x) = ae = g^x
  d = d/dx {pexp}(x) = ln(a) * g^x = ln(a) * pexp(x)
by definition, ln(a)
  < 0 if {a is complex}
  == 0 if {a == 1}
  == 1 if {a == e}
  > 1 if {a > e}
and knowing that e^x is a monotonic increasing function,
thus
  ln(a) between [0, 1] for a in [1, e]
  {ln(a) > 1} for {a > e}
thus
  if d > pexp(x), then ln(a) > 1, decrease g
  if d < pexp(x), then ln(a) < 1, increase g
  if d == pexp(x), then ln(a) == 1, and thus a == e
strategy:
  new_g = g * (pexp(x) / d)
using x = 1 gives pexp(x) = ae = g, which is computationally wayyyyyyy better
```
