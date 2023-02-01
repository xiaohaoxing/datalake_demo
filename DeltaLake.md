# DeltaLake Tutorial

### Intro
After read some documents, the easiest way to get involved with Delta Lake is using Spark Interactive shell.

### Instruction

1. As the installation for java version spark is a little complex, we use pyspark. Install Pyspark with pip:

``` bash
pip install pyspark
```

2. Run PySpark with Delta Lake package:

``` bash
pyspark --packages io.delta:delta-core_2.12:2.1.0 \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```

3. Execute code in spark:

``` python
# write data
data = spark.range(0, 5)
data.write.format("delta").save("/tmp/delta-table")

# read data
df = spark.read.format("delta").load("/tmp/delta-table")
df.show()

# update data
data = spark.range(5, 10)
data.write.format("delta").mode("overwrite").save("/tmp/delta-table")
```

Result：

<img src="https://xiaohaoxing-1257815318.cos.ap-chengdu.myqcloud.com/image-20230201210507294.png" alt="image-20230201210507294" style="zoom:50%;" />



#### Additional
You can also put the codes in a source code file instead of running in interactive shell:

``` python
import pyspark
from delta import *

builder = pyspark.sql.SparkSession.builder.appName("MyApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# codes above in instruction step 3
```

### References

[1] [Getting Started with Delta Lake](https://delta.io/learn/getting-started)

[2] 
