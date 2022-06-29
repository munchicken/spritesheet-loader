# spritesheet-loader
*loads images from a spritesheet for use with my games*

>by Sarah Pierce


**spritesheet.py** - library with spritesheet-loader (use this file)

**spritesheet_loader.py** - test code for library (just for testing/demo)


**Object** - Spritesheet


**Properties**:

- image (spritesheet image)
- width (spritesheet width)
- height (spritesheet height)
- rows (number of image rows in spritesheet)
- cols (number of image columns in spritesheet)


**Methods**:

- **get_frame(row,col,scale,color)**  Method to get an individual frame at row/col in spritesheet, with scaling factor 'scale' & transparancy 'color'

- **get_frames(scale,color)**  Method to get all frames from spritesheet and return them as a list, with scaling factor 'scale' & transparancy 'color'

***Dependancies**: PyGame*
