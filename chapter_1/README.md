### Run locally

```bash
export SPARK_LOCAL_HOSTNAME=localhost
spark-submit --packages io.delta:delta-spark_2.13:4.0.0 --properties-file chapter_1/spark-conf/spark-properties.conf chapter_1/hello_delta.py
```
