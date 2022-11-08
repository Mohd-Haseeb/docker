## Commands

![](./images/img_2.png)

- docker pull postgres
> To pull an image from the internet itnto our docker machine
![](./images/img_4.png)
![](./images/img_5.png)

- docker image ls   
> to list all the images present

- docker ps
> to list all containers 
![](./images/img_6.png)

- docker run -e POSTGRES_PASSWORD=mypassword postgres
> to run a container

- docker run -e POSTGRES_PASSWORD=mypassword -d postgres
![](./images/img_7.png)
![](./images/img_8.png)

- docker run --name my-postres-container -e POSTGRES_PASSWORD=mypassword -d postgres
![](./images/img_9.png)
![](./images/img_10.png)



Note : we cannot reuse the name again for other container

- docker stop [container_name or container_id]

### NOW, SPINNING TWO POSTGRES MACHINES WITH DIFFERENT VERSION

If no version is mentioned, by default it goes with __latest__

- docker run --name my-postres-latest -e POSTGRES_PASSWORD=mypassword -d postgres

- docker run --name my-postres-old-version -e POSTGRES_PASSWORD=mypassword -d postgres:13

![](./images/img_15.png)
![](./images/img_16.png)
![](./images/img_18.png)

> if run two services on same port, it will call for conflicts. To avoid this we assign different ports using __PORT MAPPING__

![](./images/img_21.png)

- docker container prune
> to remove all stoppped containers 
![](./images/img_23.png)

- docker volume ls

- docker container ls -a 
> to list all containers, even the stopped one 


- docker image ls

## LETS MOVE TO MONGO

- docker pull mongo
![](./images/img_25.png)

- docker image ls
![](./images/img_26.png)

- docker run --name my-mongo -d mongo
![](./images/img_27.png)

- docker container ls
![](./images/img_28.png)

- docker stop my-mongo
![](./images/img_28.png)

> By default, mongo runs on port 27010. So, how to interact with this port ??

> Here comes __PORT MAPPING__

- docker run --name my-mongodb -p 4000:27017 -d mongo
> Here -p is for port, 4000 is where we want to map this container and 27017 is default port for mongo
![](./images/img_32.png)

> The advantage of this is, we can use another mongo of same version but on differet port

- docker logs [options]
![](./images/img_34.png)


- docker stop [container_name]

- docker container prune

![](./images/img_35.png)


## Lets go to mongo-express image


- docker run --name [container_name] -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=oot -e  MONGO_INITDB_ROOT_PASSWORD=example --net mongo-network -d mongo 
> here we are creating mongo container


- docker network ls
> to get list of all networks


- docker run -d \
  -p 8081:8081 \
  -e ME_CONFIG_MONGODB_ADMINUSERNAME=root \
  -e ME_CONFIG_MONGODB_ADMINPASSWORD=example \
  -e ME_CONFIG_MONGODB_SERVER=[mongo_container_name_we_want_to_connect] \
  --net mongo-network \
  --name mongo-express-container \
  mongo-express

  ## DOCKER COMPOSE

![](./images/img_37.png)
![](./images/img_38.png)
![](./images/img_39.png)
![](./images/img_41.png)
![](./images/img_42.png)
![](./images/img_46.png)
![](./images/img_50.png)

  












## NOTES

- What are Images ?

    - They are just like CDs with an opsrating systems which needs to be run on system to install the operating systrm 

- What are containers ?

    - Images run on containers. Just like how cds are played in the DVDs(containers)

- Docker isn't composed of only one image. It comes with a variety of layers with it

- The moment we install an image on our computer, that is an __conatiner__

- Docker runs on a specific port

- __DOCKER__ VS __VM__


- __DATA PERSISTENCE__



