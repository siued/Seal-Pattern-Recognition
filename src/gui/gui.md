# The planning for a small GUI for the Seal-Pattern-Recognition project

# NOTE
This description was fed into ChatGPT to generate an initial skeleton for the GUI. With a few extra prompts asking it to generate 
some functions which it skipped over, the generated code was then taken and modified heavily to actually fulfill its task. 

## Usage
The app is primarily used to upload new pictures  to the wildbook database and run the  matching algorithm on them.

## Flow
- user opens the app
- they input the url to the wildbook server, there is a default one pre-set
- they upload one or more images
- the app uploads the images to the server using /api/upload/image
- the app runs the detection algorithm on the  new images using api/detect/cnn/yolo
- the app runs the matching algorithm on the new images using api/query/chip/dict/simple and gets the list of matches for each
- the app shows the user the best match for every new image and lets them choose whether it is amatch or not
- if no match, the user fills in a form with the seals' details, otherwise they get copied from the best match


