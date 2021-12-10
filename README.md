# Conky-CountdownTimer-Python
Simple Python script to get a countdown in conky setup

### Usage 
Create a folder named ```.countdown``` in your home directory and put the script there.

Make the script executable using ```chmod +x countdown.py```

Run the script and use the function settime to set the desired countdown time in the format ```YYYY-MM-DD HH-MM```

Add the following line to conky:

```${execi 30 /bin/python3 ~/.countdown/countdown.py}```

the ```execi 30``` runs the command every 30 seconds to not waste resources

Feel free to edit this to your liking
