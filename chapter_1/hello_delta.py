import os
from pathlib import Path
from pyspark.sql import SparkSession

from delta import *

if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()

    delta_path = os.path.join(os.getcwd(), "chapter_1/data/salary_table")

    print(delta_path)

    salary_df = DeltaTable.forPath(spark, delta_path).toDF()
    salary_df.show()

    spark.stop()