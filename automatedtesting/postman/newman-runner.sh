#!/bin/bash

# Run Postman collection with a delay between requests
newman run automatedtesting/postman/DataValidationTestStarterAPIspostman_collection.json -e automatedtesting/postman/Test.environment.json --delay-request 2000 --reporters cli,junit --reporter-junit-export TEST-DataValidation.xml
