---
layout: post
author: Rob Wheaton
tags: [cscc]
---

### Teachable Machine
The [Teachable Machine](https://teachablemachine.withgoogle.com/) project from Google is an example of the supervised learning method of training a machine learning model. The image projects use datasets of labeled images to solve a multiclass classification problem. More simply, given an arbitrary image, it will label that image with one of the classifications it was trained on, accompanied by a level of confidence. If it were human, it would say, "I am 75% confident that the image you showed me is a puppy."

The problem I chose to solve was recognizing a ski pass. I trained it on images with two classifications: ski pass and credit card. My thought was that they are similar enough in size and shape that telling them apart would be challenging. The use case I had in mind was a ski resort that wanted to allow guests to add credit and lift passes to an existing pass. This model could validate that the guest actually had the correct pass and, as a potential next iteration, use [Optical Character Recognition](https://aws.amazon.com/what-is/ocr/) to pull in the pass ID and/or guest name.

My model can be accessed [here](https://teachablemachine.withgoogle.com/models/YCzVnwzje/)
