# Airflow-Demo-Automation


Airflow is an open-source platform to programmatically author, schedule and monitor workflows. Airflow was started in 2014 at Airbnb 
The project joined the Apache Software Foundation’s Incubator program in 2016. It is one fo the most intuitive way to automate and track repeatable tasks in the Analytics ecosystem.

## Use Case

Here you have a data provider, who has flat files which when uploaded into database will be used for analysis. After the files has been uploaded, Data Engineer, will process those files and make sure it’s available with data scientist to either run some models or perform basic aggregations. The summarized data will then be used by a business analyst to create a report or dashboard in excel or tableau for manager.

As of today, there are number of pain points associated with each stakeholder in this scenario:
1. Waiting time due to dependency on data provider and manual effort to start the process of report generation.
2. There is cumbersome monitoring for Data scientist or Business Analyst, in case there is an error in code and lot of time is spent in debugging and identifying errors in code. 
3. There is lack of transparency throughout process for manager and lot of back and forth to communicate the status of report.

![1574100207862](https://github.com/guptapiyush340/Airflow-Demo-Automation/blob/master/2.png)

## Airflow Implementation

With airflow, we can overcome all these pain points.
1. Airflow include automatic or conditional trigger which can run a code on it own and handle dependencies gracefully by executing code of existing files and wait for new files. This is turn help in faster time to market and reduce the overall time taken for report generation.
2. It has nice Ui which can be used to not only monitor but also debug the code using log files. It handles errors efficiently by trying to run the codes again an easily reprocess the historical jobs
3. There is inbuilt system for notification which can be triggered for important events like uploading data files or completion of report generation process. Real time status of each task can also be tracked using the UI. It also creates gantt chart for business users that help in tracking the overall timeline of process.

![1574100207862](https://github.com/guptapiyush340/Airflow-Demo-Automation/blob/master/1.png)

## DAGs Overview

![1574100207862](https://github.com/guptapiyush340/Airflow-Demo-Automation/blob/master/4.png)

## How to get Started

![1574100207862](https://github.com/guptapiyush340/Airflow-Demo-Automation/blob/master/3.png)
