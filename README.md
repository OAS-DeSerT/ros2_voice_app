# xf_voice_app

A ROS2 voice application based on XFei SDK.

## Instructions

- Copy & install

  $ sudo cp libmsc.so /usr/lib/
  
  *Files are in libs.

  $ sudo apt install sox

  $ sudo apt install libsox-fmt-all

- Speech recognition demo

  $ ros2 run voice_app iat_publish

  $ ros2 topic pub -1 /voiceWakeup std_msgs/msg/String data:\ \'123\'\
  
  *It may not be worked to send the wakeup message for one time, try more. Or loop it without "-1".

- Speech synthesis demo

  $ ros2 run voice_app tts_subscribe

  $ ros2 topic pub -1 /voiceWords std_msgs/msg/String data:\ \'你好，我是小天才\'\
  
  *Need to press enter if there is a ">".

  $ ros2 topic pub /voiceWords std_msgs/msg/String data:\ \'haha\'\

- Voice repetition demo

  $ ros2 launch voice_app repeat_voice.launch.py

  $ ros2 topic pub -1 /voiceWakeup std_msgs/msg/String data:\ \'\'\

    or

  $ ros2 launch voice_app repeat_voice_launch.py

  $ ros2 topic pub /voiceWakeup std_msgs/msg/String data:\ \'\'\

- Voice assistant demo
  
  *The content of Q&A is written in the cpp file.
  
  *If the program does not capture keywords，it will repeat what it heard.

  $ ros2 launch voice_app voice_assistant.launch.py

  $ ros2 topic pub -1 /voiceWakeup std_msgs/msg/String data:\ \'\'\

    or

  $ ros2 launch voice_app voice_assistant_launch.py

  $ ros2 topic pub /voiceWakeup std_msgs/msg/String data:\ \'\'\

## Reference

- IFLYTEK open platform

**http://www.xfyun.cn/** 

