# ***This is a Docker guide for me***
   
    1. sudo  docker run -it <image> bash
        - sudo docker run -it python:3.10.6 bash
        - sudo docker run -it --name <name container> <name image>
    2. sudo docker ps -a 
    3. sudo docker stop <docker id>
    4. sudo docker commit <docker id>  <name docker images>
    5. sudo docker start <container_id_or_name>
    6. sudo docker images
    7. sudo docker rmi <id images>
    8. useradd -m -s /bin/bash kirill
