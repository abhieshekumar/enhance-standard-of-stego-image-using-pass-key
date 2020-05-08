# Improved standard of stego image using the pass key

* README.md file inside each directory outlines the files and folders in that directory.
* Run the demo project using -

```bash
./automate.sh
```

* To view the state of images during the course of exexution add the *image* flag -

```bash
./automate.sh image
```

* You can also plot the histogram by adding the *histogram* flag -

```bash
./automate.sh histogram
```

* The algorithm designed here has the following parameters -
  * *seed* in *metadata/private.py*,
  * *privateImage* in *asset/*,
  * *tolerance* defined in *getTolerance()* in *metadata/private.py*,
  * *granularity* defined in *generateKey/randomize.py*, and
  * *nshuffle* define in *generateKey/randomize.py.
  * You can also decide to have different cover image and the image used for generatinf key image.

* All of the above defined parameters can be modified on the sender as well the receiver side to tune the algorithm.
