# FineGrainOCR: A Multimodal Fine-Grained Dataset for Grocery Product Recognition

FineGrainOCR is a multimodal dataset for grocery product recognition using image and OCR data. The dataset contains
products from the following categories: dairy, chocolate, milk/cream, meat, mushroom and toppings.
In the dataset, each class has one or more classes that it has a strong resemblance to.

Below are a few challenging cases where different grocery products have a similar appearance and are only differentiable 
by subtle details (ingredients side, meat packages), lactose and non-lactose product variant, and the same 
type of product with different weight.

<p float="left">
  <img src="assets/dataset_chocolate_back.jpg?raw=true" width="45%" />
  <img src="assets/dataset_meat_scaled.jpg?raw=true" width="45%" />
  <img src="assets/dataset_milk_lactose.jpg?raw=true" width="45%" />
  <img src="assets/dataset_milk_different_size.jpg?raw=true" width="45%" />
</p>

## Dataset

### Download
The dataset can be downloaded from the following Dropbox link: [FineGrainOCR](https://www.dropbox.com/scl/fi/jraqxgrg0z7carmj7anxs/FineGrainOCR.zip?rlkey=qq9p7orig0csxo7s1vq1htc5r&dl=0)

### Format/Structure
The image samples are RGB images with a resolution of 2592x1944. The OCR texts have the JSON format from 
Google Vision API. Each OCR reading is separated by "\n". An example of the JSON file can be seen below:

```json
[
  {
    "locale": "fr",
    "description": "ORIGINALE\nOCR_READING_2\nOCR_READING_3\n...\nOCR_READING_N\n",
    "bounding_poly": {
      "vertices": [
        {
          "x": 1510,
          "y": 275
        },
        {
          "x": 2210,
          "y": 275
        },
        {
          "x": 2210,
          "y": 1396
        },
        {
          "x": 1510,
          "y": 1396
        }
      ]
    }
  },
  {
    "description": "ORIGINALE",
    "bounding_poly": {
      "vertices": [
        {
          "x": 2130,
          "y": 1390
        },
        {
          "x": 1891,
          "y": 1397
        },
        {
          "x": 1890,
          "y": 1372
        },
        {
          "x": 2129,
          "y": 1365
        }
      ]
    }
  },
  {
    ...
  },
  ...
]
```

### Statistics

The dataset contains a total of 256 classes with 73378 images/texts for training and 18416 images/texts for validation.
The number of images/texts per class for the training set is shown in the histogram below.

<p align="center">
  <img src="assets/dataset_train_histogram.jpg?raw=true" width="50%" />
</p>


## Sample Images

Sample images and OCR texts are provided in the `samples` folder.

## Experiments

To run experiments with a subset of the training dataset in the same way as described in the paper, a new 
training dataset can be created using the following command:
```
python3 scripts/create_dataset_subset_symbolic_links.py --input-folder TRAIN_DATASET_FOLDER --output-folder TRAIN_SUBSET_DATASET_FOLDER --max-samples-class MAX_TRAIN_SAMPLES
```
where `TRAIN_DATASET_FOLDER` is the path to the training dataset, `TRAIN_SUBSET_DATASET_FOLDER` is the path to the
new training dataset, and `MAX_TRAIN_SAMPLES` is the maximum number of samples per class to be included in the new
training dataset. In the experiments, we MAX_TRAIN_SAMPLES has been set to 50, 100, 200, and 400. Symbolic links are
created to the original images/texts, so no significant storage space is required for subset of the dataset.

## Citation
If you use this dataset, please cite the following paper:
```
@article{,
  title={},
  author={},
  journal={},
  year={},
  publisher={}
}
```

<h2>Contact</h2>
<ul>
  <li>Email: <a href="mailto:tobias.pettersson@itab.com">tobias.pettersson[at]itab.com</a></li>
  <li>LinkedIn: <a href="https://www.linkedin.com/in/tobias-pettersson86">Tobias Pettersson</a></li>
</ul>