/*
  foilsim - Library for communicating with the foil
  simulator (running in your PC and connected with a
  USB to TTL adapter.

  Embedded Systems Design 2020.
*/

#ifndef foilsim_h
#define foissim_h

#include <Arduino.h>
#include <SoftwareSerial.h>


class foilsim
{
  public:
    foilsim(int rx_pin, int tx_pin);
    float get_height();
    float get_coord_x();
    float get_coord_y();
    float get_roll();
    float get_pitch();
    float get_speed();
    int set_motor_speed(float meters_second);
    int set_back_foil_angle(float angle);
    int set_front_right_foil_angle(float angle);
    int set_front_left_foil_angle(float angle);
  private:
    SoftwareSerial* foilserial;
    int max_communication_attempts = 100;
    int request_counter = 0;
    float send_get_command_robust(String command);
};


#endif
