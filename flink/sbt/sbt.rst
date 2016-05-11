===============================
Using SBT to create a Flink job
===============================

Motivation
----------

Maven is a widely accepted build tool for projects that target the Java platform. The Radicalbit Fast Data Distribution provides an archetype to kickstart your development projects using Maven, but Scala developers may find more compelling to use the Maven alternative of choice for the Scala ecosystem, SBT (Simple Build Tool).

Basic 'archetype'
-----------------

Currently, SBT does not provide built-in capabilities to scaffold a project like Maven archetypes do.
As such, some manual work is required to initialize the build definition properly.
The following steps describe how to create the initial scaffolding for the project.
All the steps involve the usage of a terminal emulator and require a basic understanding of how to use one.

First of all, let's create a directory for our Flink project::

    mkdir my-flink-project

Then, move into the directory and create a project directory::

    cd my-flink-project
    mkdir project

To package our application, we'll use the ``sbt-assembly`` plugin. To add it to our build, create and open in your favorite text editor the ``project/assembly.sbt`` file and fill it in with this single line:

.. literalinclude:: /rbp-docs-code/sbt/project/assembly.sbt
    :caption: assembly.sbt
    :language: scala

Now it's time to actually create the build definition. Open your favorite text editor and type in the following text:

.. literalinclude:: /rbp-docs-code/sbt/build.sbt
    :caption: build.sbt
    :language: scala

Once the build definition is ready, create the standard directory structure for SBT project (including a directory hierarchy that mirrors the package structure)::

    mkdir -p src/main/scala/org/example/

Now you can create and open src/main/scala/org/example/Job.scala in your favorite text editor and create a simple app to test your build definition:

.. literalinclude:: /rbp-docs-code/sbt/src/main/scala/io/radicalbit/flink/batch/BatchJob.scala
    :caption: BatchJob.scala
    :language: scala

You can now run your project by simply typing the following command::

    sbt run

To package a deployable artifact you just have to type::

    sbt assembly

You will find the packaged artifact under the ``target`` directory.
