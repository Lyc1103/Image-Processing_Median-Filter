# Average Filter

> Author : Ya Chen<br>
> Date : 2021 / 4 / 13

---

<br>
<div>

## Description

The median filter is a non-linear digital filtering technique, often used to remove noise from an image or signal. Such noise reduction is a typical pre-processing step to improve the results of later processing (for example, edge detection on an image). Median filtering is very widely used in digital image processing because, under certain conditions, it preserves edges while removing noise (but see the discussion below), also having applications in signal processing.<br>

### Algorithm description

The main idea of the median filter is to run through the signal entry by entry, replacing each entry with the median of neighboring entries. The pattern of neighbors is called the "window", which slides, entry by entry, over the entire signal. For one-dimensional signals, the most obvious window is just the first few preceding and following entries, whereas for two-dimensional (or higher-dimensional) data the window must include all entries within a given radius or ellipsoidal region (i.e. the median filter is not a separable filter).

<br>
We will divide the next implementation into three steps:

1. Select an experimental image
2. Apply a 3 by 3 Median Filter and to the image
3. Unsharp masking

</div>
<br>
<br>
<div>

## In-Output Example

### Input:

&emsp;&emsp; Original Image :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/2RAl6cv.jpg" width = "100">

### Output:

&emsp;&emsp; Gray Image :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/VMOW0jx.jpgg" width = "100">

&emsp;&emsp; Color Image Blured by Median Filter :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/YQ6tupk.jpg" width = "100">

&emsp;&emsp; Gray Image Blured by Median Filter:<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/pITn7ew.jpg" width = "100">

&emsp;&emsp; Unshape The Color Image Been Blered :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/Bm66qP6.jpg" width = "100">

&emsp;&emsp; Unshape The Gray Image Been Blered :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "https://i.imgur.com/duwdv35.jpg" width = "100">

</div>
