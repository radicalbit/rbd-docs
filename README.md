
How to setup your environment to work on the RBD documentation
==============================================================

First download and install Python then:

    sudo easy_install pip
    sudo pip install --upgrade pip
    sudo pip install -U Sphinx

On OSX, add these lines to your ~/.bash\_profile:

    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

To install the required modules:

    sudo pip install sphinx_rtd_theme
    sudo pip install rst2pdf
    sudo pip install requests

How to contribute to the RBD documentation
==========================================

Steps required before working on the RBD documentation:

1.  Install Sphinx and the required modules. (ref &lt;installation&gt;)
2.  Clone the repository with the --recursive option to initialize the code submodule:

<!-- -->

    git clone --recursive https://github.com/radicalbit/rbd-docs.git

If you forget the -recursive flag, you can always do

    cd rbd-docs/
    git submodule init rbd-examples
    git submodule update --remote

How to build the documentation in HTML
--------------------------------------

Just execute the make clean html in the root directory of the project documentation. The result of the building process can be found in the \_build/html directory.

How to handle version numbers and frequently-changing references
----------------------------------------------------------------

You should use the rbpsubstitutions.py file for all the version references of the software used in RBD. Here are defined a list ofglobal substitutions that replace placeholders everywhere in the documentation. Try to name the placeholders with care and try to avoidsemantic replication. Create a new substitution only if really necessary.

> **note**
>
> The way these substitutions work with directives make them usable exclusively inside content blocks.

How to include code
-------------------
1.  Correctly initialize the code submodule (ref&lt;installation&gt;).    
2.  Commit your code to the [rbd-examples repository] or to the internal submodule in the rbd-examples directory. Use the *snippets/* directory for scripts, short pieces of code and anything that doesn’t require a proper verification and compilation. Use the *src/* directory for everything else.
3.  Use the literalinclude directive ([ref]) to include your code.

> **note**
>
> Always specify the :name: option when labeling the snippets with an already existing label. This will avoid warnings during the build process.

How code submodule works
------------------------

The rbd-examples directory contains a git submodule referencing a repository containing all the code snippets and examples. To better understand how git submodules, please refer to [Git Documentation].

Submodules are a powerful yet complex tool to handle dependencies between repositories. They are managed as independent entities by Git and their behavior often differs to the expected behaviors of regular subdirectories. So take your time to learn how to work with both repositories at the same time.
To contribute to this documentation a few predefined actions are provided as simple scripts to support your operativity.

Every branch of the parent repository is bound to a matching branch of the code repository. This is done through the `-b branch-name` option of the `git submodule add` command. If you want to create a new branch in the parent directory and bind it to a related branch in the code repository, this procedure is strongly suggested:

    //First checkout the parent branch you want to bind
    git checkout recently-created-parent-branch

    //Then de-initialize the submodule
    git submodule deinit rbd-examples

    //Remove it from the index
    git rm rbd-examples

    //Re-add it with a new branch
    git submodule add --force -b new-code-branch-name https://github.com/radicalbit/rbd-examples.git

    //Update the submodule with remote changes from the correct branch
    git submodule update --remote

If the .gitmodules contains a reference to the correct branch, it worked correctly. Mind that these features require at least Git 1.8.2.

> **note**
>
> This procedure should be performed exclusively by the documentation maintainers. Regular contributors are not expected to do it in any circumstances.

If you make local modifications on the submodule and you want to go back to the original state, you can actually checkout the correct branch manually with a `git checkout` command inside the submodule directory or with `git submodule update`. This will checkout the submodule branch according to the parent branch. You are expected not to break this alignment and to keep your cross-references consistent with this scheme.

[rbd-examples repository]: %3Chttps://github.com/radicalbit/rbp-docs%3E
[ref]: http://www.sphinx-doc.org/en/stable/markup/code.html#directive-literalinclude
[Git Documentation]: https://git-scm.com/docs/git-submodule
