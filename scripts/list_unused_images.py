#!/usr/bin/env python
# lists the images in image_dir that don't exist in doc files in doc_dir.

image_dir = 'images'
img_globs = ['*.png', '*.jpg', '*.gif']
img_list = []

doc_dir = '.'
doc_globs = ['*.xml', '*.rst', '*.md']
doc_list = []

# save the current working directory
pwd = Dir.getwd

# get the list of images
Dir.chdir(image_dir) { img_list = Dir.glob(img_globs) }

# do the same thing for the doc files
Dir.chdir(doc_dir) { doc_list = Dir.glob(doc_globs) }

# now, make a list of the images that exist in the docs.
found_images = []
doc_list.each do | doc_file |
  contents = File.read(doc_file)
  img_list.each do | img_file |
    found_images << img_file if contents.include?(img_file)
  end
end

# remove any duplicates
found_images.uniq!

# finally, print the list of images that are in img_list but that *don't* exist
# in found_images.
(img_list - found_images).each { |img| puts File.join(image_dir, img) }

