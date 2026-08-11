# EGT309_26S1_test


### Name: daniel
### Admin Number: 244469Q
### Github Link: https://github.com/Danielcyh/EGT_309_Test

#### Q2(a): Documenting Your Python Class:
the class is using the model name called dandelin/vilt-b32-finetuned-vqa, which is a Ai model that answer text questions
about input text.
First function __init__ is to setup the Vilt transformer when instance of the class is created
Second function _load_model is to get the image source
Third function ask is the main execution where it calls for the image, ensuring the image is ready for processing and do answer extraction
using logitsmax(-1) to look up for corresponding text label in the model


#### Q2(d) Suggest Improvements to the Code:

add in requests.get() to prevent it from hanging indefinitely if a url is slow
allow user to pass a device like cpu or cuda using if else instead of just auto detection
add comments on what each function does

#### Q4 Advanced Github features implemented:
implement github actions to automate task
add open source license to clarify how other developers can use modify the code