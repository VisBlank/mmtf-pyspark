#!/user/bin/env python
'''
pythonRDDToDataset.py:

This class converts a PythonRDD<Row> to a Dataset<Row>. This method only
supports simple data types and all data need to be not null.

Authorship information:
    __author__ = "Mars Huang"
    __maintainer__ = "Mars Huang"
    __email__ = "marshuang80@gmai.com:
    __status__ = "debug"
'''
from pyspark.sql.types import *
from pyspark.sql import SparkSession

def getDataset(data, colNames):
    '''
    Converts a PythonRDD<Row> to a Dataset<Row>. This method only
	supports simple data types and all data need to be not null.

    Attributes:
        data (PythonRDD): PythonRDD of row objects
        colNames (list(str)): names of the columns in a row
    '''

    row = data.first()
    length = len(row)

    if length != len(colNames):
        raise Exception("colNames length does not match row length")

    sf = []

    for i in range(len(colNames)):
        o = row[i]
        if type(o) == str:
            sf.append(StructField(colNames[i], StringType(), False))
        elif type(o) == int:
            sf.append(StructField(colNames[i], IntegerType(), False))
        elif type(o) == float:
            sf.append(StructField(colNames[i], FloatType(), False))
        elif type(o) == long:
            sf.append(StructField(colNames[i], LongType(), False))
        else:
            print("Data type not implemented yet")

    schema = StructType(sf)
    spark = SparkSession.builder.getOrCreate()
    return spark.createDataFrame(data, schema)