<h1>Python- Everything is Object</h1>
<br>

![readme1](https://user-images.githubusercontent.com/66512735/215960335-af0b1178-c7c6-49a3-82ad-d50967db7c40.jpg)

<br>

<p> In this project, I studied object instantiation in Python, delving into variable aliasing and object identifiers, types, and mutability. The project involved a series of quiz-like questions the answers to which I provided in single-line <code>.txt</code> files.</p>
<br>

![giphy](https://user-images.githubusercontent.com/66512735/215962838-4b40c87e-bac0-4152-81a2-6202a3173492.gif)

<br>

<h2> Tasks </h2>
<ul>
<li><b>0. Who am I?</b></li>
<ul>
<li> <a href = "">0-answer.txt</a>: What function would you use to print the type of an object?</li>
</ul> <br>
<li><b>1. Where are you?</b></li>
<ul>
<li><a href= "">1-answer.txt</a>: How do you get a variable's identifier (which is the memory address in the CPython implementation)?</li>
</ul>
<br>
<li><b>2. Right count</b></li>
<ul>
<li><a href = "">2-answer.txt</a>: In the following code, do a and b point to the same object?</li>
</ul>
<pre><code>>>> a = 89
>>> b = 100 </code></pre>
<li><b>3. Right count =</b></li>
<ul>
<li><a href = "">3-answer.txt</a>: In the following code, do a and b point to the same object?</li>
</ul>
<pre> <code> >>> a = 89
  >>> b = 89 </code></pre>
<li><b>5. Right count =+</b></li>
<ul>
<li><a href = "">5-answer.txt</a>: In the following code, do a and b point to the same object?</a></li>
</ul>
<pre> <code> >>> a = 89
  >>> b = a + 1 </code> </pre>
<li><b>6. Is equal</b></li>
<ul>
<li> <a href = ""> 6-answer.txt</a>: What do these 3 lines print?</li>
</ul>
<pre><code>>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)</code></pre>
<li><b>7. Is the same</b></li>
<ul>
<li><a href ="">7-answer.txt</a>: What do these 3 lines print?</li>
</ul>
<pre><code>>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)</code></pre>
<li><b>8. Is really equal</b></li>
<ul>
<li><a href = "">8-answer.txt</a>: What do these 3 lines print?</li>
</ul>
<pre><code>>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)</pre></code>
<li><b>9. Is really the same</b></li>
<ul>
<li><a href = "">9-answer.txt</a>: What do these 3 lines print?</a></li>
</ul>
<pre><code>>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)</code></pre>
<li><b>10. And with a list, is it equal</b></li>
<ul>
<li><a href = "">10-answer.txt</a>: What do these 3 lines print?</li>
</ul>
<pre><code>>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)</pre></code>

<li><b>11. And with a list, is it the same</b></li>
<ul>
<li><a href = "">11-answer.txt</a>: What do these 3 lines print?</li>
</ul>
<pre><code>>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)</pre></code>

<li><b>12. And with a list, is it really equal</b></li>
<ul>
<li><a href = "">12-answer.txt</a>: What do these 3 lines print?</li>
</ul>
<pre><code>>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)</pre></code>

<li><b>13. And with a list, is it really the same</b></li>
<ul>
<li><a href = "">13-answer.txt</a>: What do these 3 lines print?</li>
</ul>
<pre><code>>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)</pre></code>

<li><b>14. List append</b></li>
<ul>
<li><a href = "">14-answer.txt: What does this script print?</li>
</ul>
<pre><code>l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)</pre></code>

<li><b>15. List add</b></li>
<ul>
<li><a href = "">15-answer.txt</a>: What does this script print?</li>
</ul>
<pre><code>l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)</pre></code>

<li><b>16. Integer incrementation</b></li>
<ul>
<li><a href = "">16-answer.txt</a>: What does this script print?</li>
</ul>
<pre><code>def increment(n):
    n += 1

a = 1
increment(a)
print(a)</pre></code>


<li><b>17. List incrementation</b></li>
<ul>
<li><a href = "">17-answer.txt: What does this script print?</li>
</ul>
<pre><code>def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)</pre></code>

<li><b>18. List assignation</b></li>
<ul>
<li><a href = "">18-answer.txt: What does this script print?</li>
</ul>
<pre><code>def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)</pre></code>

<li><b>19. Copy a list object</b></li>
<ul>
<li><a href = "">19-copy_list.py</a>: Python function <code>def copy_list(l):</code> that returns a copy of a list.</li>
</ul>


<li><b>20. Tuple or not?</b></li>
<ul>
<li><a href = "">20-answer.txt: Is a a tuple?</li>
</ul>
<pre><code>a = ()</pre></code>

<li><b>21. Tuple or not?</b></li>
<ul>
<li><a href = "">21-answer.txt: Is a a tuple?</li>
</ul>
<pre><code>a = (1, 2)</pre></code>








