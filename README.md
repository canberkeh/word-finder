# Word Finder Backend Service

## General Info
This application works as a [Flask](https://flask.palletsprojects.com/en/2.0.x/) application deployed on [Heroku](https://www.heroku.com/) and is responsible for the returning query results that requested with parameters.
## Usage and Documentation Word Finder service can be used both from word-finder frontend and from swagger. For development and deployment
guidance check the related sections of this document. More information about usage can be found in [apidocs](https://word-finder-get-words.herokuapp.com/apidocs/)

### Requirements
Requirements are in requirements.txt file. Installs requeirements when docker is building. If you don't want to dockerize it, i higtly recommend using venv and then 
use command below.

    ```
    $ pip install -r requirements.txt
    ```

### Installation And Run
System is built on docker. If you want to dockerize it, just follow the command below.

    ```
    $ docker-compose up --build
    ```
Otherwise if you want to run locally, just run app.py

Go live on [Word-Finder](https://word-finder-tr.herokuapp.com/)

### Word-Finder Flow

[![](https://mermaid.ink/img/pako:eNpVz0GOwjAMBdCrRF4xErlAF0iUwgGA0SwIC0_zgQiadJwUCVHuTqoOEnhlfT1b9p3qYEEFHYXbk9pWxqtc891PEKtXzluIXknwCd7uldaz_jtC1Bp_HWLqVTl5lyXX5wz1BnJ1Nb7GbeUwpxYfOytO_MsR-5EsBlK-8X6N2AYf0c_HlKbUQBp2Nl97HzJD6YQGhorcWpazIeMf2XWt5YSldSkIFQe-REyJuxQ2N19TkaTDC1WO8-fNv3o8AUC-WDs)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNpVz0GOwjAMBdCrRF4xErlAF0iUwgGA0SwIC0_zgQiadJwUCVHuTqoOEnhlfT1b9p3qYEEFHYXbk9pWxqtc891PEKtXzluIXknwCd7uldaz_jtC1Bp_HWLqVTl5lyXX5wz1BnJ1Nb7GbeUwpxYfOytO_MsR-5EsBlK-8X6N2AYf0c_HlKbUQBp2Nl97HzJD6YQGhorcWpazIeMf2XWt5YSldSkIFQe-REyJuxQ2N19TkaTDC1WO8-fNv3o8AUC-WDs)
