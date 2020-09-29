#!/bin/bash
if [ -z $SUDO_USER ]; then
    RUSER_UID=$(id -u ${USER})
    DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/${RUSER_UID}/bus" notify-send -i gtk-dialog-warning "Info" "Hello"
else    
    RUSER_UID=$(id -u ${SUDO_USER})
    sudo -u ${SUDO_USER} DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/${RUSER_UID}/bus" notify-send -i gtk-dialog-warning "Info" "Hello"
fi