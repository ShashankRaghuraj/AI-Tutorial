# AI-Tutorial: Created for the Solon Hacks Hackathon

Hello! for starters, my name is Shashank and I gave a basic introduction over AI. I specifically covered vision AI in the introduction. In this repository, you will find a sample python script, a cascade classifer, and a testing folder. I encourage you all to play around with the different functionalities. This is just the beginning! Once you have the basics down, you can expand easily

As Kanye West said:
> We're living the future so the present is our past.

## What is AI?

Artificial Intelligence (AI) is a branch of computer science that focuses on building smart machines capable of performing human tasks. It is used in a variety of fields such as, but not limited to, Healthcare, Auto, and Education. Artificial Intelligence is used for faster, and more accurate results. Since AI is heavily data-driven, all data associated with the AI you want to create. This technology is used in every field, and almost every company so it is vital you learn the basics of AI.

## Types of AI

* Reactive Machines: This is the oldest form of AI systems and are very limited as these  machines cannot learn and grow. They solely rely on memory
* Limited Memory: These machines are like Reactive Machines, however, they have the ability to grow. All current AI are limited memory machines
* Theory of Mind: Next level AI that states that AI will be able to understand entities through emotions, beliefs, and thought process
* Self-aware: AI that has evolved to have developed self awareness
* Artificial Narrow Intelligence(ANI): AI that can perform human-like capabilities
* Artificial General Intelligence(AGI): Functions like a human and has multi-functional capabilities
* Artificial Superintelligence(ASI): Greater memory, faster data processing and analysis, and decision-making capabilities.

## Types of AI Systems

* Analytic AI: Analytic AI scans data for dependencies and patterns to produce recommendations and help users with insight
  - *Examples include sentiment analysis*
* Functional AI: Functional AI is similar to analytic AI but, instead of giving recommendations, it takes Action. Most Functional AI are part of the IOT(internet of things).
  - *Examples include Robots and self driving cars*
* Interactive AI: Interactive AI allows businesses to combine both communication and interactivity.
  - *Examples include Chatbots or Smart Personal Assistants*
* Text AI: Text AI includes anything related to text
  - *Examples include Text recognition, speech-to-text conversion, machine translation, and content generation*
* **Vision AI: Visual AI refers to analyzing images and determine complex aspects of the object**
  -  *Examples include computer vision*

#### In this tutorial, I specifically talked about Vision AI.

## The basics
As stated before, Vision AI refers to analyzing images and determining complex aspects of these images. It’s very hard to find a straight forwards response, so after years of trying I was able to come up with a foolproof method to get Vision AI to work each time. I find the best programming language for AI is python. I found this to be the best for a couple of reasons:
1) Easy for beginners
2) A lot of code snippets: If you need help getting started, virtually anything programming related has python code available	
3) Help for any problem imaginable: Stackoverflow

*I recommend using python when starting with AI, but once you understand in depth, then you can move onto other programming languages.*

## Prerequisites

Before doing anything, make sure you download a **virtual environment**.

Virtual environment: Virtual environments aid with installing the necessary packages, by avoiding the version that needs to be downloaded. This is important for both opencv and other packages you want to install in the future(for example speechrecognition, numpy, matplotlib, etc)

The virtual environment I use is virtualenv

Once you have downloaded the virtual environment, you need to download OpenCV(you can do so by writing *pip install opencv-python*)

## Steps
- Determine what objects you want to detect 
  - Get images of positive images meaning that they match what you want to detect
  - It would also be good to get testing images as well
- Next, annotate the images that are the object you want to detect
- After annotation of the images, save the model. 
- Next, use the sample code provided and put the file to the model where shown

*Now, you’re done!*

## Resources!
- OpenCV: https://docs.opencv.org/master/d9/df8/tutorial_root.html
  - OpenCV installation for python is very tough. If you need help. Feel free to message me as I have experienced a ton of different errors
- Custom Vision: https://www.customvision.ai/
  - Seamless transition between C# and Vision AI
- Haar Cascades trainer: https://amin-ahmadi.com/cascade-trainer-gui/
  - A haar cascade is an effective object detection approach in which positive and negative images will be trained to create a classifier
  - A classifier can be easily used for object detection when it comes to OpenCV
- Image dataset website: https://rb.gy/ufvhnn
- Image Annotation: https://www.makesense.ai/

### Hope this will help you get started with your own AI projects!!



