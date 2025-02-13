const int soundSensorPin = A0; // Analog pin for sound sensor
const int noiseThreshold = 650; // Adjust based on your sound sensor sensitivity

void setup() {
  Serial.begin(9600);
  pinMode(soundSensorPin, INPUT);
}

void loop() {
  int soundLevel = analogRead(soundSensorPin);
  Serial.println(soundLevel); // Print sound level for debugging
  if (soundLevel > noiseThreshold) {
    Serial.println("NOISE_DETECTED");
    delay(3000); // Delay to avoid multiple triggers
  }
  delay(100); // Short delay to avoid constant reading
}c:\Users\markb\OneDrive\Documents\Arduino\soundsensor\soundsensor.ino