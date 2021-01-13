# Image to ASCII Converter

## Table of Contents

* [ General ](#general)
* [ Technologies and Modules ](#tech)
* [ How to Use ](#howTo)
* [ TODO ](#todo)

<a name="general"></a>
## General

- Script can be used to convert .jpg files to ASCII txt file, with two different levels of gray scale.

<a name="tech"></a>
## Technologies and Modules

* Python >= 3.7
* Pillow >= 8.0.1
* numpy >= 1.19.4

<a name="howTo"></a>
## How to Use

- Clone the repository into your system, `cd` into the repository and run the program. By not passing any arguments, the program will run with default settings, and convert test image to ascii, in the output repository.

### Default Run

- Windows

```
cd <REPOSITORY_PATH>
python main.py
```

- Unix Based System

```
cd <REPOSITORY_PATH>
python3 main.py
```

### Optional Arguments

#### Convert your own image

- Windows

```
cd <REPOSITORY_PATH>
python main.py --file <IMAGE_PATH>
```

- Unix Based System

```
cd <REPOSITORY_PATH>
python3 main.py --file <IMAGE_PATH>
```

#### Save to specified directory:

- Windows

```
cd <REPOSITORY_PATH>
python main.py --output <OUTPUT_PATH>
```

- Unix Based System

```
cd <REPOSITORY_PATH>
python3 main.py --output <OUTPUT_PATH>
```

#### Scale the image to your desired dimensions

- Windows

```
cd <REPOSITORY_PATH>
python main.py --cols 150 --scale 0.8
```

- Unix Based System

```
cd <REPOSITORY_PATH>
python3 main.py ---cols 150 --scale 0.8
```