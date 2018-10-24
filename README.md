# MATLAB scripts

I wrote a couple MATLAB functions to decompose an SVS file into individual JPGs. This could be used to create an image hierarchy of the slide. See the example below to get started.

```
% required parameters
params.filename =  'path/to/file.svs';  % path to SVS file
params.n = 5;                           % take n samples per dimension (5x5 = 25 images)
params.d = 1000;                        % sub-sample size (reads in 1000 x 1000 pixels)

% optional parameters
params.out_dir = 'img/';                % change the output directory
params.resize = [256, 256];             % resize the images
params.r_begin = 20000;                 % change the starting y-pixel
params.c_begin = 30000;                 % change the starting x-pixel

decompose_file(params);
```

# What is OpenSlide
[OpenSlide](https://openslide.org/) provides a simple interface to read whole-slide images.
The Python binding includes a [Deep Zoom](https://docs.microsoft.com/en-us/previous-versions/windows/silverlight/dotnet-windows-silverlight/cc645050(v=vs.95)) generator and a simple web-based viewer.

The library can read virtual slides in the following formats:
- Aperio (.svs, .tif)
- Hamamatsu (.vms, .vmu, .ndpi)
- Leica (.scn)
- MIRAX (.mrxs)
- Philips (.tiff)
- Sakura (.svslide)
- Trestle (.tif)
- Ventana (.bif, .tif)
- Generic tiled TIFF (.tif)

# Installing OpenSlide
I used the following steps to install OpenSlide for python on MacOS High Sierra (Version 10.13.6).
See the [OpenSlide download page](https://openslide.org/download/) for other options.

## Install virtualenv
```
python3 -m pip install --user virtualenv
```

## Create virtualenv
```
python3 -m virtualenv openslide-env
```

## Activate virtualenv
```
source openslide-env/bin/activate
```

## Install openslide with python bindings
```
brew install openslide		 # install openslide 
pip install openslide-python  # install python bindings
```

## To deactivate virtualenv when finished
```
deactivate
```
