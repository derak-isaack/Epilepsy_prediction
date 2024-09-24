## <div style="padding: 35px;color:white;margin:10;font-size:200%;text-align:center;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://images.pexels.com/photos/7078619/pexels-photo-7078619.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)"><b><span style='color:black'><strong> Scalp EEG signals Epilepsy prediction </strong></span></b> </div> 

| <span style="color: grey;">*Epilepsy is a neurological brain disorder caused by abnormal chemical changes in our brains. It is often characterized by recurrent seizures which are brief episodes of involuntary movement that may involve a part/ entire body accompanied by loss of consciousness and control of bowel functioning.*</span>

| <span style="color: grey;">*50 million people have epilepsy globally with an estimated 5 million new diagnosis yearly.*</span>

| <span style="color: grey;">*80% of people with epilepsy live in low & middle income countries and only about 25% of them can get treatment.*</span>


![World Health Organization Badge](https://img.shields.io/badge/World%20Health%20Organization-0093D5?logo=worldhealthorganization&logoColor=fff&style=for-the-badge)
![DuckDB Badge](https://img.shields.io/badge/DuckDB-FFF000?logo=duckdb&logoColor=000&style=for-the-badge)
![TensorFlow Badge](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=fff&style=for-the-badge)
![Keras Badge](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=fff&style=for-the-badge)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)


### <div style="padding: 35px;color:white;margin:10;font-size:200%;text-align:center;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://images.pexels.com/photos/7078619/pexels-photo-7078619.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)"><b><span style='color:black'><strong>*Motivation*</strong></span></b> </div> 

Most individuals with epilepsy often suffer from stigma, discrimination, anxiety, and depression. This is largely due to the myths surrounding epilepsy, which can lead to isolation and discourage many from seeking treatment.

The suicide rate among people with epilepsy is `22% higher than that of the general population`, often compounded by high medication costs.

However, early detection and treatment can help mitigate seizures, ultimately improving quality of life and reducing global depression and suicide rates. For this reason, machine learning can be adopted to enhance the *data interpretation of EEG signals*, leading to more efficient classification of epileptic and non-epileptic individuals.



### <div style="padding: 35px;color:white;margin:10;font-size:200%;text-align:center;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://images.pexels.com/photos/7078619/pexels-photo-7078619.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)"><b><span style='color:black'><strong> Data description</strong></span></b> </div> 

Data was obtained from the open [CHB-MIT scalp database](https://physionet.org/content/chbmit/1.0.0/) data repository and contains several `EEG signals`. The `EEG` data has columns with the following annotations:

* F - Represents the `frontal`
* T - Represents the `temporal`
* C - Represents the `central`
* P - Represents the `parietal`
* O - Represents the `occipital`
* Z - Represents the `signals along the midline`

The `Temporal channels` are crucial because `temporal lobe` epilepsy is one of the most common epilepsy types. 

`T7-FT9` & `FT10-T8` will be used as the targets as they normally monitor the temporal region. 



