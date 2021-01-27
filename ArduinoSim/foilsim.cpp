/*
  foilsim - Library for communicating with the foil
  simulator (running in your PC and connected with a
  USB to TTL adapter.

  Embedded Systems Design 2020.
*/

#include "foilsim.h"

foilsim::foilsim(int rx_pin, int tx_pin)
{
  foilserial = new SoftwareSerial(rx_pin, tx_pin);
  foilserial->setTimeout(10);
  foilserial->begin(57600);
}

float foilsim::get_height()
{
  return send_get_command_robust("HEIGHT");
}

float foilsim::get_coord_x()
{
  return send_get_command_robust("X");
}

float foilsim::get_coord_y()
{
  return send_get_command_robust("Y");
}

float foilsim::get_roll()
{
  return send_get_command_robust("ROLL");
}

float foilsim::get_pitch()
{
  return send_get_command_robust("PITCH");
}

float foilsim::get_speed()
{
  return send_get_command_robust("SPEED");
}

int foilsim::set_motor_speed(float meters_second)
{
  foilserial->println("MOTOR " + String(meters_second));
  return 0;
}

int foilsim::set_back_foil_angle(float angle)
{
  foilserial->println("FOIL_MID " + String(angle));
  return 0;
}

int foilsim::set_front_right_foil_angle(float angle)
{
  foilserial->println("FOIL_RIGHT " + String(angle));
  return 0;
}

int foilsim::set_front_left_foil_angle(float angle)
{
  foilserial->println("FOIL_LEFT " + String(angle));
  return 0;
}

float foilsim::send_get_command_robust(String command)
{
  request_counter++;
  float received_value = -1;
  bool received = false;

  int attempts = 0;

  while (!received && attempts < max_communication_attempts) {
    if (attempts % 10 == 0) {
      foilserial->println(command + " " + String(request_counter));
      if (attempts > 0) {
        delay(100);
      }
    }
    attempts += 1;
    String response = foilserial->readString();
    response.trim();
    //Serial.println("Received response: " + response);
    char * splitted_response;
    splitted_response = strtok(response.c_str(), " ");
    String trimmed_splitted_response = String(splitted_response);
    //trimmed_splitted_response.trim();
    if (splitted_response != NULL && trimmed_splitted_response.equals(command)) {
      splitted_response = strtok(NULL, " ");
      if (splitted_response != NULL && atoi(splitted_response) == request_counter) {
        if (splitted_response != NULL) {
          splitted_response = strtok(NULL, " ");
          received_value = atof(splitted_response);
          received = true;
        }
      }
    }
    delay(10);
  }
  return received_value;
}
