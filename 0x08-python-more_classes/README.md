<h1>Python More Classes</h1><br>
<p>In this project, I continued to practice object-oriented programming in Python. I learned about class methods, static methods, class vs instance attributes, andbhow to use the special <code>__str__</code> and <code>__repr__</code> methods.<br>
<h2> Tasks </h2>
<ul>
<li><b>0. Simple rectangle</b></li>
<ul>
<li><a href="">0-rectangle.py</a>: Empty Python class that defines a rectangle.</li>
</ul>
</ul>
<br>

<ul>
<li><b>1. Real definition of a rectangle</b></li>
<ul>
<li><a href="">1-rectangle.py</a>: Python class that defines a rectangle. Builds on <a href = "">0-rectangle.py</a> with:</li>
<ul>
<li>Private instance attribute <code>width</code>.</li>
<li>Property getter <code>def width(self):</code> to get width.</li>
<li>Property setter <code>def width(self, value):</code> to set width.</li>
<li>Private instance attribute <code>height</code>.</li>
<li>Property getter <code>def height(self):</code> to get height.</li>
<li>Property setter <code>def height(self, value):</code> to set height.</li>
<li>Instantiation with optional width and <code>height:</code> <code>def __init(self,   width=0, height=0):</code>.</li>
</ul>
</ul>
<ul>
<li>If either of width or height is not an integer, a TypeError is raised with the message width must be an integer or height must be an integer.</li>
<li>If either of <code>width</code> or <code>height</code> is less than 0, a <code>ValueError</code> is raised with the message width must be <code>>= 0</code> or height must be <code>>= 0</code>.</li>
</ul>
<br>

<li><b>2. Area and Perimeter</b></li>
<ul>
<li><a href = "">2-rectangle.py</a>: Python class that defines a rectangle. Builds on <a href="">1-rectangle.py</a> with:</li>
<ul>
<li>Public instance method <code>def area(self)</code>: that returns the area of the rectangle.</li>
<li>Public instance attribute <code>def perimeter(self)</code>: that returns the permiter of the rectangle (if either of <code>width</code> or <code>height</code> equals <code>0</code>, the perimeter is <code>0</code>).</li>
</ul>
</ul>
<br>

<li><b>3. String representation</b></li>
<ul>
<li><a href = "">3-rectangle.py</a>: Python class that defines a rectangle. Builds on 2-rectangle.py with:</li>
<ul>
<li>Special method <code>__str__</code> to print the rectangle with the <code>#</code> character (if either of <code>width</code> or <code>height</code> equals <code>0</code>, the method returns an empty string.).</li>
</ul>
</ul>
<br>

<li><b>4. Eval is magic</b></li>
<ul>
<li><a href = "">4-rectangle.py</a>: Python class that defines a rectangle. Builds on 3-rectangle.py with:</li>
<ul>
<li>Special method <code>__repr__</code> to return a string representation of the rectangle.</li>
</ul>
</ul>
<br>


