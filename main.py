from PIL import Image, ImageDraw, ImageChops
import random

def random_colour():
    return(random.randint(0,255), random.randint(0,255),random.randint(0,255)) #three channels

def interpolate(start_colour, end_colour, factor: float):      # factor between 0 and 1, if 0.5 half way between
    reciprocal = 1 - factor #always add to one

    # need to convert back to integer from float
    return (int(start_colour[0] * reciprocal + end_colour[0] * factor), int(start_colour[1] * reciprocal + end_colour[1] * factor), int(start_colour[2] * reciprocal + end_colour[2] * factor))

def add_image(path: str):
    print("Adding Images")
    image_size = 128                                                                # square (128 pixels by 128 pixels)
    image_background_colour = (3,3,3)
    start_colour = random_colour()
    end_colour = random_colour()
    image_padding = 15
    image = Image.new("RGB", size=(image_size, image_size), color=(image_background_colour));   # create base image

    draw = ImageDraw.Draw(image)
    points = []

    # draw 20 random lines
    for i in range(7):
        random_points = (random.randint(image_padding, image_size - image_padding), random.randint(image_padding, image_size - image_padding))
        points.append(random_points)

    line_thinkness = 1
    num_points = len(points) -1

    # draw out the points from start to end
    for i, point in enumerate(points):

        # overlay the image
        overlay_image = Image.new("RGB", size=(image_size, image_size), color=(0,0,0));
        overlaydraw = ImageDraw.Draw(overlay_image)

        point_start = point

        # check if at end, if it is loop
        if i == num_points:
            # otherwise it is the very first point
            point_next = points[0]
        else:
            # otherwise it is next point
            point_next = points[i+1]


        line_coordinates = (point_start, point_next)

        factor = i / num_points
        line_fill = interpolate(start_colour, end_colour, factor)

        line_thinkness += 1
        overlaydraw.line(line_coordinates, fill=line_fill, width = line_thinkness)
        image = ImageChops.add(image, overlay_image)

    image.save(path)                                                    # save a base image

if __name__ == "__main__":
    for i in range(10):
        add_image(f"test_image{i}.png")