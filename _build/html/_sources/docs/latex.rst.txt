.. .. post:: Feb 07, 2025
   :category: Math
   :tags: Docs
   :author: Sam Khalilian

LaTex
=====

LaTex is the defacto markup language used for mathematical documentation and can be integrated into Sphinx. 

.. seealso::

   https://www.latex-project.org

=======
Install
=======

Install Sphinx extension https://pypi.org/project/sphinx-mathjax-offline/

.. code-block:: bash
    
   >> pip install -U sphinx-mathjax-offline


Set conf.py

.. code-block:: python

   extensions = [
      ...
      'sphinx.ext.mathjax',
   ]

============
Useful Links
============

* Latex syntax generator https://latex.codecogs.com/eqneditor/editor.php
* Example equations http://www.equationsheet.com/

========
Examples
========

.. list-table:: 
   :widths: 20 20
   :header-rows: 1
   :stub-columns: 0

   *  - Equation
      - Latex
   *  -
         .. math::

            x = \frac{{ - b \pm \sqrt {b^2  - 4ac} }}{{2a}} \texttt{ when } ax^2  + bx + c = 0
      - 
         .. code-block:: bash
         
            x = \frac{{ - b \pm \sqrt {b^2  - 4ac} }}{{2a}} 
            \texttt{ when } ax^2  + bx + c = 0
   *  -
         .. math::

            \log _b \left( {xy} \right) = \log _b \left( x \right) + \log _b \left( y \right)
      - 
         .. code-block:: bash
         
            \log _b \left( {xy} \right) = 
            \log _b \left( x \right) + \log _b \left( y \right)
   
   *  -
         .. math::

             \frac{d}{{dx}}x^n  = nx^{\left( {n - 1} \right)}
      - 
         .. code-block:: bash
            
             \frac{d}{{dx}}x^n  = nx^{\left( {n - 1} \right)}

   *  -
         .. math::

             \int {x^n } dx = \frac{{x^{n + 1} }}{{n + 1}},(n \ne  - 1)
      - 
         .. code-block:: bash
            
             \int {x^n } dx = \frac{{x^{n + 1} }}{{n + 1}},(n \ne  - 1)
   
   *  -
         .. math::

             \int {u\frac{{dv}}{{dx}}} dx = uv - \int {\frac{{du}}{{dx}}} vdx
      - 
         .. code-block:: bash
            
             \int {u\frac{{dv}}{{dx}}} dx = 
             uv - \int {\frac{{du}}{{dx}}} vdx

   *  -
         .. math::

             \mathop {\lim }\limits_{x \to \infty } \frac{1}{{x^n }} = 0
      - 
         .. code-block:: bash
            
             \mathop {\lim }\limits_{x \to \infty } \frac{1}{{x^n }} = 0

   *  -
         .. math::

            \begin{bmatrix}
               1 & 0 & 0 & 0 \\ 
               0 & 1 & 0 & 0 \\
               0 & 0 & 1 & 0 \\
               0 & 0 & 0 & 1
            \end{bmatrix}

      - 
         .. code-block:: bash

            \begin{bmatrix}
               1 & 0 & 0 & 0 \\ 
               0 & 1 & 0 & 0 \\
               0 & 0 & 1 & 0 \\
               0 & 0 & 0 & 1
            \end{bmatrix}
