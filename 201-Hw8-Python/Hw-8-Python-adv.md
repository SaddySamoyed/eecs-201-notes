# 8 Python Adv

## 8.1 Who needs MATLAB? (5)

You could probably replace MATLAB with Python + NumPy + SciPy + Matplotlib for general purpose use (unfortunately, MATLAB does have some really nifty tools in more focused areas that can be hard to replace).

For this exercise, we’re going to keep it simple since the SciPy stuff tends to be more domain specific. The only package dependencies you’ll need are NumPy (for data types) and Matplotlib (for plotting). 

Write a Python script that plots 
$$
y = x^3 − 7x + 2x + 2
$$
for 
$$
−4 ≤ x ≤ 4
$$
with the title `“Who needs MATLAB?”`
and saves the figure to a PNG file called `output.png` . The number of samples you use is up to you, but the figure should not look jagged from a low sample count. **This must be a Python script: no Jupyter notebooks and the like will be accepted.**

Hint:
• NumPy comes with its own version of MATLAB’s `linspace()` : `numpy.linspace()` . This can come in handy for generating your X coordinate samples.
• If you do this right, given that you have your X coordinate samples, you only need one line to calculate your Y coordinate samples. `numpy.ndarray` s are your friends!
• Matplotlib’s MATLAB-like plotting function is `pyplot.plot` . `pyplot` also has a mechanism to save figures.

## 8.2 Go Wild

The Python standard library is pretty darn big. I have no idea what sorts of problems that you all face in each of your classes or in your life, but chances are there’s some problem that you can solve with a Python script(s) and using the Python standard library. Or perhaps the standard library is missing some feature (*cough* YAML parsing *cough*) and you need to install some package.

The point of this particular exercise is to go wild and stretch out your wings with real problems you face: this is probably the best way to learn and get a feel for Python.

Minimum requirements are to use at least one of the more “advanced” modules/packages and have either some sort of file I/O or networking capability. Modules that provide fairly basic/fundamental things like os , math, string don’t count: feel free to ask if your choice in “advanced” module is appropriate. In addition, your script should do something reasonably useful: being a simple example of calling some functions from a module will not suffice (e.g. simply reading and printing things out from a CSV file: your script should do something with the data). Some examples of modules/packages that I find “advanced” enough from the standard library: `csv` , `argparse` , `curses` , `email` , `json` , `html` , `xml` (and friends), `http.client` , `sqlite3` , `tkinter`.
□ Submit your Python file(s) and any additional data files needed.
□ What packages did your script depend on?
□ What is your script for and what does it do?
