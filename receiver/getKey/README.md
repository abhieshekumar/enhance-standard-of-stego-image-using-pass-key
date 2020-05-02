# receiver/getKey

* *driver.py* - Executes the scripts in a specific order to generate the key image.
* *final.py* -  It performs the last XOR operate in *driver.py*. But the XOR retrieves the key.
* *flat.py* - It is used to redistrubute the frequency value of image to flatten the histogram.
* *keyEncoder.py* - Converts the 2D matrix to a list of exception tuples.
* *keyTemplate.py* - Generates the template to write key.
* *path.py* - Helps importing files from other directories.
* *randomize.py* - Used to shuffle the image.
* *run.py* - The entry point used for execution.
* *withHash.py* - Performs cyclic XOR with the image.
