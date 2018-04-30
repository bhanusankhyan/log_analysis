This project Log Analysis is created using python 3.6, flask,postgresql

1. Add these files of the project at approprite location. HTML file should be added under template folder.
2. Create User 'bhanu' with password 'bhanu' in postgresql database.
3. Now import the database file 'newsdata.sql' in your psql user 'bhanu'.
4. Create following Views in your database


 -- CREATE VIEW query1v1 AS
    SELECT log.path AS article_name,
    count(log.ip) AS visits
    FROM log
    WHERE log.path not like '/'
    GROUP BY log.path
    OREDER BY visits DESC;
  
 -- CREATE VIEW query1vf AS
    SELECT articles.slug,
    sum(query1v1.visits) as viewers,
    FROM query1v1 JOIN articles 
    ON query1v1.article_name like concat('%',articles.slug,'%')
    GROUP BY articles.slug
    ORDER BY viewers DESC;
  
 -- CREATE VIEW query2v1 AS
    SELECT articles.author AS id,
    sum(query1vf.viewers) AS views
    FROM articles JOIN query1vf 
    ON query1vf.slug = articles.slug
    GROUP BY articles.author;  
  
 -- CREATE VIEW query2vf AS
    SELECT authors.name, query2v1.views 
    FROM authors, query2v1
    WHERE authors.id = query2v1.id;
   
 -- CREATE VIEW query3v1 AS
    SELECT date(log.time) AS date,
    count(log.status) AS requests
    FROM log
    GROUP BY date(log.time)
    ORDER BY requests DESC;

 -- CREATE VIEW query3v2 AS
    SELECT date(log.time) AS date,
    count(log.status) as error
    FROM log
    WHERE log.status like '%404%'
    GROUP BY date(log.time)
    ORDER BY error DESC;
 
 -- CREATE VIEW query3vf AS
    SELECT query3v1.date, 
    cast((query3v2.error*100) as float) / query3v1.requests AS error
    FROM query3v1, query3v2
    WHERE query3v1.date = query3v2.date
    ORDER BY error DESC;


5. Export the flask app using command "export FLASK_APP = name_of_file" in command line.
6. Now run "python logs_analysis.py" command in command line.(It'll show Running on http://localhost:8000/ something message like this)
7. Now open any browser Chrome, Firefox etc.
8. Go to Adress "http://localhost:8000" and logs analysis tool will show some results in a web page.
