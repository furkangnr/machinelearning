# Docker
This repo includes Docker Tutorials and useful links.

Very comprehensive Docker Tutorial on Youtube :
https://www.youtube.com/watch?v=PbiYll21Jxg&list=PLZdsdjcJ44WU_cY2Y1LFL

## Introduction 
Docker is a software platform that performs operating-system level virtualization also known as "containerization". Docker provides us flexibility, mobility and security. With the help of docker images, we can have different environments for different applications that do not interrupt each other.

## Installation 
Here is the links for Docker installation for different OS ( Windows, Linux, Mac ).

https://docs.docker.com/install/linux/docker-ce/ubuntu/

https://docs.docker.com/docker-for-windows/install/

https://docs.docker.com/docker-for-mac/install/#install-and-run-docker-for-mac

After installation, we can start with simple terminology.
# Docker Image 
A docker image is basically an environment ( we can even think them as files ) for different purposes. For example, we can have "Ubuntu" image which simply allows us to have Ubuntu in our computer without explicitly installation. Similarly, we can have "Tensorflow 1.12-gpu-py3" image which basically an environment which can run on GPU machines and Python3 installed with Tensorflow 1.12 and many other libraries. 

Where do we get the images ?
We can simply pull images from the public registries. The most known one is of course Docker Hub. A registry can have several repositories with several docker images.
** Public Registries : https://hub.docker.com , https://hub.docker.com/search?q=&type=image&image_filter=official

How to pull those docker images in our computer ? 

Go to terminal after you make sure that Docker is correctly installed and running. ( For Windows, I prefer Docker for Windows Desktop App)
Simply, type "docker pull image_name". Examples are :

      docker pull ubuntu 
      
      docker pull python 
      
      docker pull mysql 
      
Those pull commands will pull the "latest" version of the image by default. If you want to specify different version you should find tags of that images. For example, if you want to pull different Python versions. You should go "tags" in the hub.
https://hub.docker.com/_/python?tab=tags

Lets say we want to pull Python 3.6.7 

docker pull python:3.6.7

After pulling required / desired images for our purposes. We can go Command Line and see which images we have pulled :

"docker images" commmand will show us which images we have pulled.

To remove an image, we can use following command on terminal.

      docker rmi ubuntu

docker rmi python 

docker rmi mysql 

# Docker Container 
They are the trademarks of Docker. Since containers allows us to manupilate images, make changes in the images and then commiting those changes to another image, they are pretty useful. We can have multiple containers of the same image. Containers are places where we do manupilations in the images.

How to create a container out of a docker image ? 

      docker run -it "Image_ID1" /bin/bash 

It will create a container from "Image_ID1" and will go into bash. 

To see how many containers we created and from which images we created containers, use following command :

" docker ps -a"

To enter / start a container that is already created and to directly go into bash :

      docker ps -a 
 
      docker start "Container_ID"
 
      docker exec -it "Container_ID" bash 
 
 
To stop a container :

 docker stop "Container_ID"

How do we manupilate images and committing them to another image ? 

docker images 

docker run -it "IMAGE_ID" /bin/bash

#### we can do manupilations in the image such as : we can install different libraries, we can make file transfer etc. After those manupilations, we must commit that container to create a new image. To commit we must exit out of that container.

exit 

docker ps -a

      docker commit "Container_ID" new_image

Since we already committed those changes to create a new image,  we can now remove the container that we made changes in the image. New image will preserve manupilations.

How to rename a container ? 

docker rename "old_container_name" "new_container_name"

How to set a name when creating a container out of an image ? 

docker run -it --name container1 "Image_ID" bin/bash

#### docker -h will show some other useful docker commands that we can use.

For example, we can search for docker images that are in the public registry via this command :

  docker search ubuntu 
  
  docker search python 
  
  docker search tensorflow 


# How to copy files from local to docker container ? 

      docker cp SOURCE_OF_File "Container_ID":Destination

Example : 

      docker cp C:\Users\FURKANG\Desktop\Images  e7afc7fb7902:/Images

# How to copy files from docker container to local ? 
      
      docker cp "COntainer_ID":Container_File_Location Destination 
      docker cp "Container_ID":/foo.txt foo.txt

## A demo of how can one use default docker images to create desired image / application environment. Here, we will first make some data transfer and then we will install python3 and lastly we commit those changes to create another image which can be used on later.

      docker pull ubuntu 

      docker images 

      docker run -it --name container1 "Image_ID" bin/bash 

      ls 

      mkdir data

      exit

      docker ps -a 

      docker start "Container_ID"

      docker cp C:\Users\FURKANG\Desktop\Images  "Container_ID":/data

      docker exec -it "Container_ID" bin/bash  

      apt-get install python3

      ls 

      cd data 

      ls 

      exit

      docker ps -a 

      docker commit "Container_ID" New_Image

      docker images 

      docker ps -a 

      docker rm "Container_ID"      ( to remove containers use  " docker  rm " ) 

 







































