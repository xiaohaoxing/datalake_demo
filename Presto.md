# PrestoDB Tutorial

## Intro

  After reading the whole [Deployment Instruction](https://prestodb.io/docs/current/installation/deployment.html#an-example-deployment-with-docker), the best way to deploy the prestodb is using docker, which is simple and fast.

## Instruction

1. Install docker

``` bash
sudo apt-get install docker 
```

2. Run a docker container

``` bash
sudo docker run -p 8100:8080 --name presto ahanaio/prestodb-sandbox
```

> 8080 is occupied by other web service in our case.

3. Start presto client

``` bash
sudo docker exec -it presto  presto-cli
```

4. Run test queries

``` sql
show catalogs;
```
<div align="center">
<img src="https://xiaohaoxing-1257815318.cos.ap-chengdu.myqcloud.com/image-20230201124530327.png" style="zoom:50%;align:center" />
</div>

```sql
show schemas in tpcds;
```

<div align="center">
<img src="https://xiaohaoxing-1257815318.cos.ap-chengdu.myqcloud.com/image-20230201124547714.png" style="zoom:50%" />
</div>

### Key conceptions

#### Catalog&Schema

Catalogs represent for **data sources** and schemas represent for **databases**, as indicated in [documentation](https://prestodb.io/docs/current/installation/deployment.html#catalog-properties):

> "Presto accesses data via connectors, which are mounted in catalogs.The connector provides all of the schemas and tables inside of the catalog. For example, the Hive connector maps each Hive database to a schema, so if the Hive connector is mounted as the `hive` catalog, and Hive contains a table `clicks` in database `web`, that table would be accessed in Presto as `hive.web.clicks`."

We can access data by specified the catalog and schema with `--catalog` and `--schema` parameters when start presto client:

``` bash
sudo docker exec -it presto  presto-cli --catalog tpcds --schema sf10
```

Or switch inside the client:

``` sql
use tpcds.sf10;
```


### References

[1] [Deploying Presto](https://prestodb.io/docs/current/installation/deployment.html)

[2] [ahanaio/prestodb-sandbox-Docker Image](https://hub.docker.com/r/ahanaio/prestodb-sandbox)

