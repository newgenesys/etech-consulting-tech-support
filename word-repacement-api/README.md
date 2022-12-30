# Introduction

In this project, we have developed a python API that allows a user to enter a text, and
the application will search for keywords and replace them with suitable words. The API
was built using FastAPI.



# Usage

- A user enters the search text, the application searches for word occurrences and then
replace them with their respective replacements. If there are no replacements the exact
text is returned.

- The docker image can be built using


- $:> docker build -t word-replacement-api .

Then the following command can be used to run the image

- $:> docker run -p 8000:8000 word-replacement-api

In order to access the API documentation in Swagger open API standard and test,
access the following address on the web browser

- http://172.17.0.1:8000
