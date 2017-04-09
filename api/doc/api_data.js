define({ "api": [
  {
    "type": "get",
    "url": "data/all",
    "title": "Read all data",
    "name": "GetAll",
    "group": "Data",
    "version": "0.0.1",
    "description": "<p>Return entries from the database.</p>",
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://localhost:5000/data/all",
        "type": "curl"
      }
    ],
    "filename": "./myproject.py",
    "groupTitle": "Data"
  },
  {
    "type": "get",
    "url": "data/:id",
    "title": "Read data",
    "name": "GetData",
    "group": "Data",
    "version": "0.0.1",
    "description": "<p>Return last data in JSON, or a specific one with optionnal ID.</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "id",
            "description": "<p>Data unique ID (optionnal)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "id",
            "description": "<p>ID of the entry in the database</p>"
          },
          {
            "group": "Success 200",
            "type": "date",
            "optional": false,
            "field": "date_enr",
            "description": "<p>Creation date of the entry, format : YYYY-MM-DD</p>"
          },
          {
            "group": "Success 200",
            "type": "time",
            "optional": false,
            "field": "heure_enr",
            "description": "<p>Creation hour of the entry, format : HH:MM:SS (UTC+2)</p>"
          },
          {
            "group": "Success 200",
            "type": "decimal",
            "optional": false,
            "field": "temp",
            "description": "<p>Temperature, unit : °C</p>"
          },
          {
            "group": "Success 200",
            "type": "decimal",
            "optional": false,
            "field": "hum",
            "description": "<p>Humidity, unit : %</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"date_enr\": \"2017-04-06\",\n    \"heure_enr\": \"21:17:24\",\n    \"hum\": 35,\n    \"id\": 42,\n    \"temp\": 25\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./myproject.py",
    "groupTitle": "Data"
  },
  {
    "type": "get",
    "url": "data/:start_date/:end_date",
    "title": "Read data (days)",
    "name": "GetDates",
    "group": "Data",
    "version": "0.0.1",
    "description": "<p>Return data from date 1 to date 2 in JSON format.</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "start_date",
            "description": "<p>Format YYYY-MM-DD</p>"
          },
          {
            "group": "Parameter",
            "type": "date",
            "optional": false,
            "field": "end_date",
            "description": "<p>Format YYYY-MM-DD</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage - Return data from 2017-04-06 to 2017-04-09 :",
        "content": "curl -i http://localhost:5000/data/2017-04-06/2017-04-09",
        "type": "curl"
      }
    ],
    "filename": "./myproject.py",
    "groupTitle": "Data"
  },
  {
    "type": "get",
    "url": "data/first/:num",
    "title": "Read first data",
    "name": "GetFirst",
    "group": "Data",
    "version": "0.0.1",
    "description": "<p>Return n first data in JSON format.</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "num",
            "description": "<p>Number of entries wanted</p>"
          }
        ]
      }
    },
    "filename": "./myproject.py",
    "groupTitle": "Data"
  },
  {
    "type": "get",
    "url": "data/:start_hour/:end_hour",
    "title": "Read data (hours)",
    "name": "GetHours",
    "group": "Data",
    "version": "0.0.1",
    "description": "<p>Return data from hour 1 to hour 2 in JSON format.</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "time",
            "optional": false,
            "field": "start_hour",
            "description": "<p>Format HH:MM:SS</p>"
          },
          {
            "group": "Parameter",
            "type": "time",
            "optional": false,
            "field": "end_hour",
            "description": "<p>Format HH:MM:SS</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage - Return every morning data :",
        "content": "curl -i http://localhost:5000/data/08:00:00/12:00:00",
        "type": "curl"
      }
    ],
    "filename": "./myproject.py",
    "groupTitle": "Data"
  },
  {
    "type": "get",
    "url": "data/hum",
    "title": "Read humidity",
    "name": "GetHum",
    "group": "Data",
    "version": "0.0.1",
    "description": "<p>Return every humidity with its timestamp.</p>",
    "filename": "./myproject.py",
    "groupTitle": "Data"
  },
  {
    "type": "get",
    "url": "data/last/:num",
    "title": "Read last data",
    "name": "GetLast",
    "group": "Data",
    "version": "0.0.1",
    "description": "<p>Return n last data in JSON format.</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "num",
            "description": "<p>Number of entries wanted</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "Example usage - Return the 10 last data :",
        "content": "curl -i http://localhost:5000/data/last/10",
        "type": "curl"
      }
    ],
    "filename": "./myproject.py",
    "groupTitle": "Data"
  },
  {
    "type": "get",
    "url": "data/temp",
    "title": "Read temperatures",
    "name": "GetTemp",
    "group": "Data",
    "version": "0.0.1",
    "description": "<p>Return every temperature with its timestamp.</p>",
    "filename": "./myproject.py",
    "groupTitle": "Data"
  },
  {
    "type": "get",
    "url": "data/temp-hum",
    "title": "Read temperature and humidity",
    "name": "GetTempHum",
    "group": "Data",
    "version": "0.0.1",
    "description": "<p>Return every temperature and humidity with their timestamp.</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "decimal",
            "optional": false,
            "field": "hum",
            "description": "<p>Humidity, unit : %</p>"
          },
          {
            "group": "Success 200",
            "type": "decimal",
            "optional": false,
            "field": "temp",
            "description": "<p>Temperature, unit : °C</p>"
          },
          {
            "group": "Success 200",
            "type": "datetime",
            "optional": false,
            "field": "timestamp",
            "description": "<p>Timestamp from the database record</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"hum\": 35,\n    \"temp\": 25,\n    \"timestamp\": \"2017-04-06 21:17:24\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./myproject.py",
    "groupTitle": "Data"
  },
  {
    "type": "post",
    "url": "data/",
    "title": "Record data",
    "name": "PostData",
    "group": "Data",
    "version": "0.0.1",
    "description": "<p>Data sent from NodeMCU to a Raspberry Pi web server.</p>",
    "filename": "./myproject.py",
    "groupTitle": "Data"
  }
] });
