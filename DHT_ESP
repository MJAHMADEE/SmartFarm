#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>
#include <SimpleDHT.h>

//DHT11
int pinDHT11 = 2;
SimpleDHT11 dht11;

int ledPin=5;

//LDR
int LDRpin = A0;
int LDRValue = 0;

//Ultrasonic
int trigPin = 12;
int echoPin = 13;
long duration = 0;
long double distance = 0.0;

//SoilM
int soilPin = 4;


void setup() {

  byte temperature = 0;
  byte humidity = 0;
  pinMode(ledPin, OUTPUT);

  //Ultrasonic
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);


  Serial.begin(115200);  //Serial connection
  WiFi.begin("SEYYYED", "12345678reza");   //WiFi connection

  while (WiFi.status() != WL_CONNECTED) {  //Wait for the WiFI connection completion

    delay(500);
    Serial.println("Waiting for connection");

  }

}
bool toggle=false;
void loop() {

  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status

    DynamicJsonBuffer JSONbuffer;
    JsonObject& JSONencoder = JSONbuffer.createObject(); 

    
    JSONencoder["sensorName"] = "nodeNo.1";
    JSONencoder["sensorType"] = "Temperature";

    JsonArray& values = JSONencoder.createNestedArray("values"); //JSON array
    JsonArray& timestamps = JSONencoder.createNestedArray("timestamps"); //JSON array

    //DHT11
    byte temperature;
    byte humidity;
    int err = SimpleDHTErrSuccess;
    if ((err = dht11.read(pinDHT11, &temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
        Serial.print("Read DHT11 failed, err="); Serial.println(err);delay(1000);
        return;
      }

    //LDR
    LDRValue = analogRead(LDRpin);

    //Ultrasonic
    digitalWrite(trigPin, LOW); // Clears the trigPin
    delayMicroseconds(2);
    
    digitalWrite(trigPin, HIGH); // Sets the trigPin on HIGH state for 10 micro seconds
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH); // Reads the echoPin, returns the sound wave travel time in microseconds
    Serial.println("duration = ");
    Serial.println(duration);
    
    distance = duration/29.0/2.0; // Calculating the distance

    //SoilM
    int soilMoisture = digitalRead(soilPin);

    values.add((int)temperature); //Add value to array
    timestamps.add(String(millis()+0)); //Add value to array

    values.add((int)humidity); //Add value to array
    timestamps.add(String(millis()+1)); //Add value to array

    values.add((int)LDRValue);//Add value to array
    timestamps.add(String(millis()+2)); //Add value to array

    values.add((int)soilMoisture);//Add value to array
    timestamps.add(String(millis()+3)); //Add value to array


    char JSONmessageBuffer[300];
    JSONencoder.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
    Serial.println(JSONmessageBuffer);

    HTTPClient http;    //Declare object of class HTTPClient

    http.begin("http://192.168.43.176:5050/postjson");      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header

    int httpCode = http.POST(JSONmessageBuffer);   //Send the request
    String payload = http.getString();                                        //Get the response payload

    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload

    http.end();  //Close connection

  } else {

    Serial.println("Error in WiFi connection");

  }

    delay(1000);  //Send a request every 1 second
    if(toggle)
        digitalWrite(ledPin, HIGH);
    else
        digitalWrite(ledPin, LOW);
    toggle=!toggle;
}
