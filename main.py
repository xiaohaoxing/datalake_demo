# start pyspark:
# pyspark --packages io.delta:delta-core_2.12:2.1.0 \
#   --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
#   --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"


# run in spark command line:

# write data
data = spark.range(0, 5)
data.write.format("delta").save("/tmp/delta-table")

# read data
df = spark.read.format("delta").load("/tmp/delta-table")
df.show()

# update data
data = spark.range(5, 10)
data.write.format("delta").mode("overwrite").save("/tmp/delta-table")
