==========================================
How to contribute to the RBP documentation
==========================================

Steps required before working on the RBP documentation:

#. Install Sphinx and the required modules. (:doc:`ref <installation>`)
#. Clone `rbp-docs repository <https://github.com/radicalbit/rbp-docs>`_.
#. (Optional) Clone `rbp-docs-code repository <https://github.com/radicalbit/rbp-docs>`_.



How to build the documentation in HTML
______________________________________

Just execute the `make clean html` in the root directory of the project documentation. The result of the building process can be found in the :file:`_build/html` directory.


How to handle version numbers and frequently-changing references
________________________________________________________________

You should use the :file:`rbpsubstitutions.py` file for all the version references of the software used in RBP. Here are defined a list of global substitutions that replace placeholders everywhere in the documentation. Try to name the placeholders with care and try to avoid semantic replication. Create a new substitution only if really necessary. 

.. note::
	The way these substitutions work with directives make them usable excluvely inside content blocks.


How to include code
___________________

#. Commit your code to the `rbp-docs-code repository <http://github.com/radicalbit/rbp-docs-code>`_. Use the *snippets/* directory for scripts, short pieces of code and anything that doesn't require a proper verification and compilation. Use the *src/* directory for everything else.
#. Use the remote-code-block directive to include your code


.. literalinclude:: remote-code-block-example.txt

This custom directive takes 3 required parameter and a number of options. The 3 required parameter are:

- the language of the code block (for syntax highlighting purposes, *text* for no highlighting)
- the repository where the code block is hosted. These repositories are specified in the :file:`repos.py` file.
- the filename relative to the repository path.

The options supported as of now are:

- *caption*
- *lines*

Here a practical example:

.. literalinclude:: remote-code-block-example2.txt




