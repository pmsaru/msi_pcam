# msi_pcam
This project is about MSI and PCAM prediction
# To Run the code in docker use the following step 
Initially pull the docker using the docker ID `bioimaging/msimss` for MSI prediction and `bioimaging/lmp_meta` for lymph node metastatis prediction. Once downloaded, use the following steps to run the docker. 

*Note use the test images given here to check for the prediction*
# Usage in Windows 

*steps:*
1) open power shell
2) type the command below 

`docker run --rm -it -v <absolute path-to-test image>:/<your mnt name> bioimaging/msimss:latest /<your mnt name>/image file`

note: <your mnt name> can by any name. image file is the actual test image


# Usage in Linux

*steps:*

1) open terminal 
2) type the command below 

`sudo docker run --rm -it -v <absolute path-to-test image>:/<your mnt name> bioimaging/msimss:latest /<your mnt name>/image file`

note: <your mnt name> can by any name. image file is the actual test image
 
