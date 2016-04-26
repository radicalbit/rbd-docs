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

#. Correctly initialize the code submodule (:doc:`ref<installation>`).
#. Commit your code to the `rbp-docs-code repository <http://github.com/radicalbit/rbp-docs-code>`_ or to the internal submodule in the :file:`rbp-docs-code` directory. Use the *snippets/* directory for scripts, short pieces of code and anything that doesn't require a proper verification and compilation. Use the *src/* directory for everything else.
#. Use the `literalinclude` directive (`ref <http://www.sphinx-doc.org/en/stable/markup/code.html#directive-literalinclude>`_) to include your code.


.. literalinclude:: literalinclude-example.txt

.. Note::

    Always specify the :name: option when labeling the snippets with an already existing label. This will avoid warnings during the build process.


How code submodule works
________________________

The :file:`rbp-docs-code` directory contains a git submodule referencing a repositorying containing all the code snippets and examples. To better understand how git submodules, please refer to `Git Documentation<https://git-scm.com/docs/git-submodule>`_. Submodules are a powerful yet complex tool to handle dependencies between repositories. They are managed as indipendent entities by Git and their behaviour often differs to the expected behaviours of regular subdirectories. So take your time to learn how to work with both repositories at the same time. To contribute to this documentation a few predefined actions are provided as simple scripts to support your operativity.

Every branch of the parent repository is bound to a matching branch of the code repository. This is done through the ``branch =`` field of the :file:`.gitsubmodule` file. This can be configured using the :file:`bind_code_to_branch.sh`. Do this only for new branches. To work locally with different branches this is not necessary and regular git operativity is sufficient. 

To actually checkout the correct branch, you can do it manullay with a ``git checkout`` command inside the submodule directory or using :file:`checkout_code_branch.sh`. This will checkout the submodule branch according to the parent branch. You are expected not to break this alignment and to keep your cross-references consistent with this scheme.





