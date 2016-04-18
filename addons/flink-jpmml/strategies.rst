==========
Strategies
==========

Flink-JPMML's strategies are the mean the developer has to control the behaviour of a *Evaluation Operator*. When building a ``JPMMLEvaluationMapOperator`` or a ``JPMMLEvaluationFlatMapOperator`` you can specify many different strategies to customize parts of the evaluation process. Here are listed all the implemented strategies, grouped by their category. The developer is free to create their own strategies because they are intended as an entry point to manipulate *Evaluation Operators* in a safe and consistent way. 


Input preparation errors handling strategies
********************************************

These strategies let you handle exceptions raised during JPMML's preparation phase. They may be very different in nature and dependent on your PMML's file so there's no obvious way to deal with them.

.. container:: strategy 

	**Propagate Exception strategy**
	
	Rethrows the exception raised by JPMML.

	**Supported in:** 

	- **Java:** :code:`Strategies.propagateExceptionStrategy`
	- **Scala:** :code:`MissingValueStrategies.propagateExceptionStrategy`





Missing values strategies
*************************

JPMML and PMML standard allow for the specification of policies to deal with missing values. These are represented with a Java `null` in JPMML that except the possibility of `null` values during input preparation. At application level though, these missing values may be unexpected and if the developer is interested in handling them with a custom logic, he could implement its own missing value strategy.

.. container:: strategy 

	**Default Value strategy**
	
	Replace missing values with defaults. Requires a map of types to replace with their default values. If a type is not specified in the types' map, it will be left null.

	**Supported in:** 

	- **Java:** :code:`Strategies.defaultValueStrategy(Map<DataType, Object> m)`
	- **Scala:** :code:`MissingValueStrategies.createDefaultValueReplaceStrategy(defaults: Map[DataType, Any])`

.. container:: strategy 

	**Delegate to PMML strategy**
	
	Let the PMML policies handle the missing values.

	**Supported in:** 

	- **Java:** :code:`Strategies.delegateToPMMLStrategy()`
	- **Scala:** :code:`MissingValueStrategies.delegateToPMML`


Result extraction strategies
****************************

After the evaluation phase a raw result is produced by JPMML according to the specifications in the PMML file. This object may be parsed internally to the *Evaluation Operator* or forwarded to the following operator through the dedicated strategy.


.. container:: strategy 

	**Get Raw Result strategy**
	
	Forward JPMML's output without processing it.

	**Supported in:** 

	- **Java:** :code:`Strategies.getRawResultStrategy()`
	- **Scala:** :code:`ResultExtractionStrategies.getRawResult`

.. container:: strategy 

	**Target and Output field strategy**
	
	Extracts all the target fields and output fields.

	**Supported in:** 

	- **Java:** :code:`Strategies.extractTargetAndOutputFieldStrategy()`
	- **Scala:** :code:`ResultExtractionStrategies.extractTargetAndOutputField`

.. container:: strategy 

	**Extraction as case class**
	
	Extracts parts of the result object using a custom case class.

	**Supported in:** 

	- **Scala:** :code:`ResultExtractionStrategies.as[CustomClass]`


Operator-level error handling strategies
****************************************

This strategy process any exception raised during the evaluation process. It is used exclusively for flatMap operator and triggers only when an input fails to produce a result and is therefore discarded.

.. container:: strategy 

	**Log Exception strategy**
	
	Log the exception raised by the evaluation process.

	**Supported in:** 

	- **Java:** :code:`Strategies.logExceptionStrategy`
	- **Scala:** :code:`MissingValueStrategies.logExceptionStrategy`



