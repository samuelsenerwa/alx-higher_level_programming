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
  
 <li><b>5. Detect instance deletion</b></li>
 <ul>
   <li><a href = "">5-rectangle.py</a>: Python class that defines a rectangle. Builds on 4-rectangle.py with:</li>
   <ul>
     <li>Special method <code>__del__</code> that prints the message <code>Bye rectangle...</code> when a <code>Rectangle</code> is deleted.</li>
   </ul>
  </ul>
  <br>
  
   <li><b>6. How many instances</b></li>
 <ul>
   <li><a href = "">6-rectangle.py</a>: Python class that defines a rectangle. Builds on <a href = "">5-rectangle.py</a> with:</li>
   <ul>
     <li>Public class attribute <code>number_of_instances</code> that is initialized to <code>0</code>, incremented for each new instantiation, and decremened for each instance deletion.</li>
   </ul>
  </ul>
  <br>

   <li><b>7. Change representation</b></li>
 <ul>
   <li><a href = "">7-rectangle.py</a>: Python class that defines a rectangle. Builds on <a href="">6-rectangle.py</a> with:</li>
   <ul>
     <li>Public class attribute <code>class_symbol</code> that is initialized to <code>#</code> but can be any type - used as the symbol for string representation.</li>
   </ul>
  </ul>
  <br>
  
<li><b>8. Compare rectangles</b></li>
 <ul>
   <li><a href = "">8-rectangle.py</a>: Python class that defines a rectangle. Builds on <a>7-rectangle.py</a> with:</li>
   <ul>
     <li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the rectangle with the greater area (returns <code>rect_1</code> if both areas are equal).</li>
     <li>If either of <code>rect_1</code> or <code>rect_2</code> is not a Rectangle instance, a TypeError is raised with the message <code>rect_1</code> must be an instance of Rectangle or <code>rect_2</code> must be an instance of Rectangle.</li>
   </ul>
  </ul>
  <br>
  
<li><b>9. A square is a rectangle</b></li>
 <ul>
   <li><a href = "">9-rectangle.py</a>: Python class that defines a rectangle. Builds on <a href="">8-rectangle.py</a> with:</li>
   <ul>
     <li>Class method <code>def square(cls, size=0):</code> that returns a new <code>Rectangle</code> instance with <code>width == height == size</code>.
</li>
   </ul>
  </ul>
  <br>

<li><b>10. N Queens</b></li>
  
  ![readme3](https://user-images.githubusercontent.com/66512735/216452181-8327a2e9-f806-4076-b427-a42d301f04a1.jpeg)
  
 <ul>
   <li><a href = "">101-nqueens.py</a>: Python program that solves the <a href="">N queens puzzle</a>.</li>
   <ul>
     <li>Usage: <code>./101-nqueens.py N</code>.
       <li>Determines all possible solutions for placing N non-attacking queens on an NxN chessboard.</li>
     <li>Exactly two arguments must be provided. Otherwise, the program prints <code>Usage: nqueens N</code> and exits with the status <code>1</code>.</li>
     <li>If the provided <code>N</code> is not an integer, the program prints <code>N must be a number</code> and exits with the status <code>1</code>.</li>
      <li>If the provided <code>N</code> is less than <code>4</code>, the program prints <code>N</code> must be at least 4</code> and exits with the status <code>1</code>.</li>
     <li>Solutions are printed one per line in the format <code>[[r, c], [r, c], [r, c], [r, c]]</code> where <code>r</code> and <code>c</code> represent the row and column, respectively, where a queen must be placed.</li>
   </ul>
  </ul>
  <br>
  
  
