# ReduxAL

Currently only works with 1080p displays


Recoil             |  Recoil Reduced
:-------------------------:|:-------------------------:
![](https://github.com/josephp27/ApexLegendsGunRecoilReducer/blob/master/examples/recoil.gif)  |  ![](https://github.com/josephp27/ApexLegendsGunRecoilReducer/blob/master/examples/no-recoil.gif)


## How it works
ReduxAL takes a small screenshot whenever a gun swap is signaled (scroll wheel event) or whenever a gun is picked up (e pressed). This image is compared against a database of images using mean squared error. If a gun is detected, and the gun is fired using the mouse left click, the corresponding recoil reduction settings from [gun_settings.py](https://github.com/josephp27/ApexLegendsGunRecoilReducer/blob/master/guns/gun_settings/gun_settings.py) will be used to reduce recoil.

## Adding your own custom recoil reduction settings
These can be added into the gun_settings.py, listed above, and loaded into [pulldown.py](https://github.com/josephp27/ApexLegendsGunRecoilReducer/blob/master/mouse_events/pull_down.py) 

## Running the application
Install python 3.x from [python.org](https://www.python.org/)


Install requirements:
```
pip install -r requirements.txt
```
Run with:
```
python predicter.py
```

## TODO:
Add requirements file and a lot of other guns

## Disclaimer
This program does not inject any code into the game and therefore should be hard to detect. Use at your own risk. I did this project for fun to get better with python and do not use this in game. I am not responsible if this results in you getting banned
