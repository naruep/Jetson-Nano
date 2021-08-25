## Controlling Servos with Jetson Nano using PCA9685

    <sudo apt-get install python3-pip>
    <sudo usermod -aG i2c jay>
    <sudo groupadd -f -r gpio>
    <sudo usermod -a -G gpio jay>
    <sudo cp /lib/udev/rules.d/99-systemd.rules /etc/udev/rules.d/>
    <sudo udevadm control --reload-rules && sudo udevadm trigger>
    <sudo reboot now>
    
    <sudo i2cdetect -y -r 1>
