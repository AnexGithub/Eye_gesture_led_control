#define RELAY_PIN 10

void setup() {
  Serial.begin(9600);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH);  // Relay OFF
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    if (command == "ON") {
      digitalWrite(RELAY_PIN, LOW);  // Relay ON
      Serial.println("Relay ON");
    } else if (command == "OFF") {
      digitalWrite(RELAY_PIN, HIGH);  // Relay OFF
      Serial.println("Relay OFF");
    }
  }
}
