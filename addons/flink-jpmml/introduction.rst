============
Introduction
============

Flink-JPMML is an API written both in Java and Scala designed to simplify the evaluation, in a Flink Job, of models serialized through the standard PMML format. This is accomplished using the JPMML libray and wrapping its functionalities. The goal is to offer to developers simple and composable abstractions to quickly evolve their workflows from serialized models to a streaming or batch Flink Job that ingests data and produces the results expected from the model.


Why Flink-JPMML?
----------------

The need for Flink-JPMML comes from the realization that many usage patterns are recurrent when dealing with ML engineering issues in a Distributed Processing Engine. This led us to consider the idea of implementing a library covering these patterns using Flink's data structures and abstractions to allow developers with no knowledge of PMML and JPMML to implement the desired behaviour without having to learn concepts and libraries outside their area of interest and expertise.

What is PMML?
-------------

What is JPMML?
--------------

Current features
----------------


