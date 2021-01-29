f'{"formatVersion": "{self.formatversion}",
    "exportDate": 1568803440466,
    "actionSequence": {
        "name": "Create an incident (Registered Caller)",
        "description": "KI 11169\nVersion: 1.1\nDate: 18-09-2019\nAuthor: ChrisF / ChloEM\n\nStep 1: Create a new 1st line incident as a registered caller according to the details specified in the body of the step.\n\nTo add more fields in the body, please see:\n\nhttps://developers.topdesk.com/documentation/index.html#api-Incident-CreateIncident",
        "structureName": "incident1",
        "configuration": {
            "variables": [
                {
                    "name": "topdesk_user",
                    "value": "Enter the name of your API Operator account"
                },
                {
                    "name": "topdesk_applicationpassword",
                    "value": "Enter the application password"
                },
                {
                    "name": "topdesk_url",
                    "value": "Enter your TOPdesk URL here"
                }
            ],
            "mappingDefinitions": [],
            "steps": [
                {
                    "name": "step1",
                    "method": "POST",
                    "url": "${_variables.topdesk_url?no_esc}/tas/api/incidents",
                    "headers": [
                        {
                            "name": "Content-Type",
                            "value": "application/json"
                        },
                        {
                            "name": "Authorization",
                            "value": "Basic  ${_base64(_variables.topdesk_user + \":\" + _variables.topdesk_applicationpassword)}"
                        }
                    ],
                    "escapeBodyValues": true,
                    "body": "{\n\t\"status\": \"firstLine\",\n\t\"callerLookup\": {\n\t\t\"email\": \"${aanmelderemail}\"\n\t}\n}",
                    "executionCondition": "ONLY_WHEN_PREVIOUS_SUCCEEDED",
                    "customExecutionCondition": ""
                }
            ]
        }
    }
}'
