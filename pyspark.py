datafact =spark.read.format("csv").option("header","true").load("fact.csv")
datalookup=spark.read.format("csv").option("header","true").load("lookup.csv")

final = datafact.join(broadcast(datalookup),datafact.web_pageId=datalookup.web_pageid)
final.persist()
df_final=final.withColumn("row_number", row_number().over(Window.partitionBy("User_Id").orderBy("EventDate")))
df_final=df_final.withColumn("Date",to_date(unix_timestamp("Event_date","DD/MM/YYYY").cast("timestamp")))
df_final=df_final.withColumn("max_date",agg(max(event_date)))
# date of reference 12/10/2019
df_final=df_final.withColumn("duration",expr("datefiff('12/10/2019',date)"))
data_rf=df_final.groupBy("user_id")\
                .agg(min("duration")).alias("recency")\
                .count("web_pageid").alias("frequency")
data_rf= data_rf.withColumn("pageview_news_dur",lit(data_rf.filter(data_rf.pagetype=="news")))\
                .withColumn("pageview_news_fre_365",lit(data_rf.filter(data_rf.pagetype=="news" & data_rf.frequency==365)))\
                .withColumn("pageview_news_fre_730",lit(data_rf.filter(data_rf.pagetype=="news" & data_rf.frequency==730)))\






