============
Introduction
============

Flink-JPMML is an API written both in Java and Scala designed to simplify the evaluation, in a Flink Job, of models serialized through the standard PMML format. This is accomplished using the JPMML libray and wrapping its functionalities. The goal is to offer to developers simple and composable abstractions to quickly evolve their workflows from serialized models to a streaming or batch Flink Job that ingests data and produces the results expected from the model.


Why Flink-JPMML?
----------------

The need for Flink-JPMML comes from the realization that many usage patterns are recurrent when dealing with ML engineering issues in a Distributed Processing Engine. This led us to consider the idea of implementing a library covering these patterns using Flink's data structures and abstractions to allow developers with no knowledge of PMML and JPMML to implement the desired behaviour without having to learn concepts and libraries outside their area of interest and expertise.

What is PMML?
-------------

PMML is the de-facto standard for ML and statistical model serialization. It is supported by many modeling software both in the enterprise world (SPSS, SAS, RapidMiner) and academic world (Weka). Many processing softwares (SparkML, OpenScoring) and languages (Java, R, Python) have integrations and libraries that allow you to work easily with JPMML.

As of now this is the default choice to import and export models across different systems and to store them in a clear and portable format. It uses XML to represent the models and there's a dedicated schema for every class of models supported. For more information about PMML, please refer to the `DMG's website <http://dmg.org/pmml/v4-2-1/GeneralStructure.html>`_.

What is JPMML?
--------------

JPMML is a suite of libraries, written mostly in Java, dedicated to the serialization and deserialization, evaluation, storage and transformation of PMML models. The core components are the Model API, used to map PMML specifications to equivalent Java classes, and the Evaluator API, a reference implementation of the PMML specification that supports preprocessing of the input data, evaluation of one or more models and post-processing of the models' output.

For more information about JPMML, please refer to the `JPMML repository <https://github.com/jpmml>`_.

Current features
----------------


