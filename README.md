# Mixpanel
An OMG service to access the Mixpanel APIs.

## Usage
```coffeescript
mixpanel track event: "Logged In" distinct_id: "john"
mixpanel track event: "Logged In" properties: {"Source": "Website"} distinct_id: "john"
mixpanel people_set properties: {"Fruit": "Mango"} distinct_id: "john"
```
