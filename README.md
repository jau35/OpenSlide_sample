# OpenSlide
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

# Setup
I used the following to install OpenSlide for python on MacOS High Sierra (Version 10.13.6).
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

