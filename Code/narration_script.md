# Narration Script – Derivatives and Rate of Change
### M3 Internal Assessment | Synchronized to 5-Minute (300s) Animation

---

> **Recording note:** Speak naturally and clearly at ~130–145 words per minute—like explaining to a fellow first-year engineering student. Total target duration: **5 minutes (300 seconds)**.

---

## SCENE 1 — Opening Hook (0:00 – 0:30 | 30s)

*(Opening question appears on screen)*

"Here is a question that lies at the heart of calculus and engineering: **How can we calculate the exact rate at which something changes at one particular instant?**"

*(Car and live speedometer appear)*

"Imagine a car driving down a highway. Its speed is constantly changing—accelerating, cruising, slowing down. Look at the speedometer: it jumps from twenty to forty-five, seventy-two, ninety-five, sixty kilometers per hour."

*(Average Speed vs. Instantaneous Speed cards appear)*

"Now notice the difference between two ideas. **Average speed** takes the total distance divided by the total time over an interval. **Instantaneous speed** is what the speedometer reads at one exact moment, like t equals three seconds."

*(Parabola f(x) = x² and title card appear)*

"To measure instantaneous change mathematically, we use **derivatives**. Welcome to **Derivatives and Rate of Change: From Average Rate to Instantaneous Rate.**"

---

## SCENE 2 — Concept Introduction (0:30 – 1:10 | 40s)

*(Axes and parabola f(x) = x² draw in; points (1,1), (2,4), (3,9) appear)*

"Let's work with a clean, familiar function: f of x equals x squared. Every input x maps to one output y: one maps to one, two maps to four, and three maps to nine."

*(Points A=(1,1) and B=(3,9), secant line, and rise/run triangle appear)*

"What does rate of change mean geometrically? It means **slope**—how fast y increases for each unit increase in x."

"If we pick two points on the curve, A and B, and connect them with a straight line, that line is called a **secant line**. The horizontal distance between them is the **run**, b minus a. The vertical change is the **rise**, f of b minus f of a."

*(Average rate formula and numerical example appear)*

"So the **average rate of change** is simply rise over run: f of b minus f of a, divided by b minus a—the slope of the secant line. For example, from a equals one to b equals three, we get nine minus one over three minus one, which equals eight over two, or **four**."

---

## SCENE 3 — Secant to Tangent Animation (1:10 – 2:15 | 65s)

*(Points A=(2,4) and B=(4,16) appear; initial calculation shows 6)*

"Now let's watch what happens on y equals x squared when we bring the two points closer together. Fix point A at two comma four, and start point B at four comma sixteen. The initial secant slope is sixteen minus four over four minus two—twelve over two—which equals **six**."

*(Live Slope and Gap h readouts appear; B slides through 3.5, 3.0, 2.5, 2.2, 2.1, 2.05, 2.01, 2.001)*

"Let's call the horizontal gap between them h. Right now, h is two. Watch what happens as B slides toward A and h shrinks toward zero: at three point five, the slope is five point five; at three, it's five; at two point five, four point five; then four point two, four point one, four point zero five, four point zero one."

*(Gold tangent line and +1 / +4 slope triangle appear)*

"Notice how the secant line rotates smoothly and settles into a single limiting position. That limiting line is the **tangent line**—it touches the curve at just one point, two comma four, and has a slope of **four**."

*(Average vs. Instantaneous comparison appears)*

"Remember the distinction: **average rate** comes from a secant across two points with h greater than zero; **instantaneous rate** comes from the tangent at one point as h approaches zero. At x equals two, f prime of two equals **four**."

---

## SCENE 4 — First Principles Derivation (2:15 – 3:30 | 75s)

*(Setup: points (x, f(x)) and (x+h, f(x+h)) and secant slope)*

"Let's now derive this exact formula using **first principles**. Place point A at x comma f of x, and point B a small distance h away at x plus h comma f of x plus h. The run is h, and the rise is f of x plus h minus f of x, so the secant slope is their ratio. Taking the limit as h approaches zero gives the derivative f prime of x."

*(0/0 warning appears)*

"Before we compute, ask yourself: why can't we just plug in h equals zero right away? Because that gives f of x minus f of x over zero, which is **zero over zero**—completely undefined! Instead, we must simplify algebraically while h is still non-zero."

*(Steps 1–5 transform smoothly)*

"Here is the definition: f prime of x equals the limit as h approaches zero of f of x plus h minus f of x, all over h."

"Step 1: Substitute f of x equals x squared, giving x plus h squared minus x squared over h."

"Step 2: Expand x plus h squared into x squared plus two x h plus h squared."

"Step 3: Notice that x squared and minus x squared cancel out cleanly, leaving two x h plus h squared over h."

"Step 4: Factor out the common h in the numerator: h times two x plus h, over h."

"Step 5: Because h approaches zero without being zero yet, we can divide h by h to get one, leaving the limit as h approaches zero of two x plus h."

*(Final boxed f'(x) = 2x and slope examples)*

"Now there is no division by zero! Letting h equal zero gives **f prime of x equals two x**. This single formula tells us the tangent slope at any point on the parabola: two at x equals one, four at x equals two, and six at x equals three."

---

## SCENE 5 — Interpretation and Worked Example (3:30 – 4:25 | 55s)

*(Parabola returns; point (2,4) highlighted; f'(2) = 4 computed)*

"Let's interpret this result back on our graph y equals x squared. At the point two comma four, we substitute x equals two into f prime of x equals two x, giving **f prime of two equals four**."

*(Tangent line and +1 / +4 triangle draw in; y = 4x - 4 derived)*

"Geometrically, the tangent line at two comma four has slope four—for every step of one unit to the right, the line rises by four units. Using the point-slope formula, y minus y one equals m times x minus x one, we get y minus four equals four times x minus two, which simplifies to **y equals four x minus four**."

*(Car connection)*

"Connecting back to our opening car example, if position follows x squared, then at x equals two the instantaneous speed is exactly four units per unit of x."

*(Point (3,9) and tangent y = 6x - 9 appear)*

"Let's check one more point: x equals three, at three comma nine. Here, f prime of three equals two times three, or **six**, giving the tangent line y equals six x minus nine. Because six is greater than four, the tangent is visibly steeper—showing that the parabola grows faster as x increases."

---

## SCENE 6 — Summary and Credits (4:25 – 5:00 | 35s)

*(Three takeaways and key formulas appear)*

"Let's wrap up the three core ideas from today's lesson."

"First, the **average rate of change** between two points is the slope of the secant line connecting them."

"Second, the **instantaneous rate of change** at a single point is the slope of the tangent line."

"Third, the **derivative** f prime of x gives us that exact instantaneous rate at any point x. For f of x equals x squared, f prime of x equals two x, so f prime of two is four and f prime of three is six."

*(Credits and Thank-You screen)*

"Thank you for watching this presentation on Derivatives and Rate of Change."
