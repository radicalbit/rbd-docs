*****************************************************
Write your first Evaluation Operator with Flink-JPMML
*****************************************************

This tutorial will explain how to create a minimal Flink Job that evaluates a PMML model against a DataStream.

The first concept you should learn about is what we call *Evaluation Operators*. These are regular Flink operators that are bound to a PMML model. They have a rigid signature and take as input a ``DataStream<Map<String,Object>>`` (in Java) or a ``DataStream[Map[String, Any]]`` (in Scala) and returns in output a ``DataStream<Map<String,Serializable>>`` (in Java) or a ``DataStream[Map[String, Serializable]]``. This may look weird at first but JPMML works primarily with `Map` and this way the user has transparency on the data structure received by the JPMML evaluator.

.. Note::
    Flink's Table API allow for the representation of tabular data but are still in development. The signatures of the Evaluation Operators will eventually move to a better format to support a proper representation of tabular data, using Flink's Table API or other means. The actual signatures are to be considered temporary and will evolve over time.


There are actually two kind of *Evaluation Operators*: ``JPMMLEvaluationMapOperator`` and ``JPMMLEvaluationFlatMapOperator``. These are to be used respectively with a map or a flatmap function. Their behaviour is similar but as you can expect, they handle errors differently. The first in fact doesn't allow for unhandled errors that would prevent the operator to produce a result. In such a case the operator would fail and the job would follow. It is more common though to let the job run even after a specific input generated an unexpected error so that the rest of the streaming could be evaluated. To do so you should use the flatmap operator that collect only valid results and handles the others without failing.

The *Evaluation Operator* wraps the evaluation process of JPMML that is composed of a pre-processing phase, a evaluation phase and a post-processing phase. This is entirely controlled by the content of the PMML document in use and Flink-JPMML does not interfere with these steps. It does however allow the developer to manipulate the data before passing them to JPMML and the results returned by JPMML.

These behaviours are customizable through a Strategy pattern that allow the developer to inject exclusively the desired logic without caring for the structural complexity intrinsical in the use of JPMML on a distributed processing framework. Flink-JPMML provides some generic strategies covering the most common patterns but the developer is supposed to create their own to achieve the best results. You can learn more about strategies :doc:`here<strategies>`.

Let's see it in action.

First we need to retrieve the PMML file. In this example we will read it from the local filesystem but in a real enviroment the location of this file could be any location accessible from the Flink Client.

.. literalinclude:: /rbd-examples/mvn/src/main/java/radicalbit/io/java/FlinkJPMMLQuickstart.java
    :language: java
    :caption: Java
    :lines: 36-42
    :name: java-jpmml-file

.. literalinclude:: /rbd-examples/mvn/src/main/scala/radicalbit/io/scala/FlinkJPMMLQuickstart.scala
    :caption: Scala
    :language: scala
    :lines: 30-32
    :name: scala-jpmml-file

Now we can build a ``JPMMLEvaluationMapOperator``. As you can see from the example, the API for Java and Scala diverge to follow an idiomatic approach for the specific language. Where Scala make use of default values for the constructor, Java uses a builder pattern to specify the desired strategies. In both cases it's not necessary to specify strategies exhaustively but only where the desired behaviour diverges from the default one.


.. literalinclude:: /rbd-examples/mvn/src/main/java/radicalbit/io/java/FlinkJPMMLQuickstart.java
    :language: java
    :caption: Java
    :lines: 43-51
    :name: java-jpmml-operator

.. literalinclude:: /rbd-examples/mvn/src/main/scala/radicalbit/io/scala/FlinkJPMMLQuickstart.scala
    :caption: Scala
    :lines: 33-37
    :language: scala
    :name: scala-jpmml-operator

The operator we just created can now be inserted in a Flink's pipeline through a ``.map()`` call.


.. literalinclude:: /rbd-examples/mvn/src/main/java/radicalbit/io/java/FlinkJPMMLQuickstart.java
    :language: java
    :caption: Java
    :lines: 53-54
    :name: java-jpmml-map

.. literalinclude:: /rbd-examples/mvn/src/main/scala/radicalbit/io/scala/FlinkJPMMLQuickstart.scala
    :caption: Scala
    :lines: 39-40
    :language: scala
    :name: scala-jpmml-map

Now you have a ``DataStream`` of the results and you can further process these data as your prefer. Following you can find the whole source of the Flink Job we worked with.

.. literalinclude:: /rbd-examples/mvn/src/main/java/radicalbit/io/java/FlinkJPMMLQuickstart.java
    :language: java
    :caption: Java
    :name: java-jpmml-complete

.. literalinclude:: /rbd-examples/mvn/src/main/scala/radicalbit/io/scala/FlinkJPMMLQuickstart.scala
    :caption: Scala
    :name: scala-jpmml-complete
    :language: scala
