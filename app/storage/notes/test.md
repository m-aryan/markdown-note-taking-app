# Test File with HTML Elements

This Markdown file includes many **HTML elements** to show how they render inside `.md`.

---

## Basic HTML Elements

<p>This is a simple paragraph written in <strong>HTML</strong>.</p>

<b>Bold text using &lt;b&gt;</b>  
<br>
<i>Italic text using &lt;i&gt;</i>  
<br>
<u>Underlined text using &lt;u&gt;</u>

<hr>

### Links & Images

<a href="https://example.com">HTML Link</a>

<img src="https://via.placeholder.com/150" alt="Placeholder image">

---

## Lists

HTML **unordered list**:

<ul>
  <li>Item A</li>
  <li>Item B</li>
  <li>Item C</li>
</ul>

HTML **ordered list**:

<ol>
  <li>First</li>
  <li>Second</li>
  <li>Third</li>
</ol>

---

## Tables

<table>
  <tr>
    <th>Header 1</th>
    <th>Header 2</th>
  </tr>
  <tr>
    <td>Row 1, Col 1</td>
    <td>Row 1, Col 2</td>
  </tr>
  <tr>
    <td>Row 2, Col 1</td>
    <td>Row 2, Col 2</td>
  </tr>
</table>

---

## Divs, Spans & Styles

<div style="border:1px solid #ccc; padding:10px; background:#fafafa;">
  <h3>HTML Styled Box</h3>
  <p>This box is wrapped in a <code>&lt;div&gt;</code> with inline styling.</p>
</div>

<p>This sentence includes a <span style="color:red;">red span element</span>.</p>

---

## Buttons, Inputs & Forms

<form>
  <label for="name">Name:</label>
  <input id="name" type="text" placeholder="Enter your name">
  <button type="submit">Submit</button>
</form>

---

## Code Blocks Using HTML

<pre>
function hello() {
  console.log("Hello HTML inside Markdown!");
}
</pre>

---

## Blockquote Using HTML

<blockquote>
  This is an HTML blockquote inside Markdown.
</blockquote>

---

## Audio & Video

<audio controls>
  <source src="example.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<br>

<video width="300" controls>
  <source src="example.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Details/Collapse Element

<details>
  <summary>Click to expand</summary>
  <p>This is hidden content inside a &lt;details&gt; tag.</p>
</details>

---

## Final Note

<p>Markdown supports a large amount of raw HTML—this file includes headings, lists, tables, forms, media, inline styles, and widgets.</p>

