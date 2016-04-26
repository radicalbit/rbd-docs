==========================================
How to contribute to the RBP documentation
==========================================

.. _rbp-docs-code repository: <https://github.com/radicalbit/rbp-docs>

Steps required before working on the RBP documentation:

#. Install Sphinx and the required modules. (:doc:`ref <installation>`)
#. Clone the repository with the `--recursive` option to initialize the code submodule:

::

	git clone --recursive https://github.com/radicalbit/rbp-docs.git
	


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

#. Correctly initialize the code submodule (:doc:`ref<installation>`).
#. Commit your code to the `rbp-docs-code repository`_ or to the internal submodule in the :file:`rbp-docs-code` directory. Use the *snippets/* directory for scripts, short pieces of code and anything that doesn't require a proper verification and compilation. Use the *src/* directory for everything else.
#. Use the `literalinclude` directive (`ref <http://www.sphinx-doc.org/en/stable/markup/code.html#directive-literalinclude>`_) to include your code.


.. literalinclude:: literalinclude-example.txt
    :caption: Example for literalinclude directive

.. Note::

    Always specify the :name: option when labeling the snippets with an already existing label. This will avoid warnings during the build process.


How code submodule works
________________________

The :file:`rbp-docs-code` directory contains a git submodule referencing a repositorying containing all the code snippets and examples. To better understand how git submodules, please refer to `Git Documentation <https://git-scm.com/docs/git-submodule>`_. Submodules are a powerful yet complex tool to handle dependencies between repositories. They are managed as indipendent entities by Git and their behaviour often differs to the expected behaviours of regular subdirectories. So take your time to learn how to work with both repositories at the same time. To contribute to this documentation a few predefined actions are provided as simple scripts to support your operativity.

Every branch of the parent repository is bound to a matching branch of the code repository. This is done through the ``-b branch-name`` option of the ``git submodule add`` command. If you want to create a new branch in the parent directory and bind it to a related branch in the code repository, this procedure is strongly suggested:

::

	//First checkout the parent branch you want to bind
	git checkout recently-created-parent-branch
	
	//Then de-initialize the submodule
	git submodule deinit rbp-docs-code
	
	//Remove it from the index
	git rm rbp-docs-code
	
	//Re-add it with a new branch
	git submodule add --force -b new-code-branch-name https://github.com/radicalbit/rbp-docs-code.git
	
	//Update the submodule with remote changes from the correct branch
	git submodule update --remote


If the :file:`.gitmodules` contains a reference to the correct branch, it worked correctly. Mind that these features require at least Git 1.8.2.

.. note:: This procedure should be performed exclusively by the documentation maintainers. Regular contributors are not expected to do it in any circumstances.

If you make local modifications on the submodule and you want to go back to the original state, you can actually checkout the correct branc manually with a ``git checkout`` command inside the submodule directory or with ``git submodule update``. This will checkout the submodule branch according to the parent branch. You are expected not to break this alignment and to keep your cross-references consistent with this scheme.




