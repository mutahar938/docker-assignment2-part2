Create the Web Application Container

web/requirements.txt: List the dependencies (Flask and psycopg2-binary to connect to PostgreSQL).
web/app.py: A simple Flask application that displays a "Hello, World!" message and connects to the database to verify health.
web/Dockerfile: Instructions to build the web application container.

------------------------------------------------------------------------------------------------------------


Create the Database Container

Create a custom Dockerfile for the PostgreSQL database container incorporating necessary runtime dependencies.   db/Dockerfile


------------------------------------------------------------------------------------------------------------

Write the docker-compose.yml

Create the orchestrator file that defines both services (web and database), linking them using Docker Compose's default internal bridge network.   docker-compose.yml

------------------------------------------------------------------------------------------------------------


Build and Run the Application

Open your terminal inside the part2-docker-compose folder
Build and run the containers in detached mode

 Command : docker-compose up -d --build
Result :
ill be ignored, please remove it to avoid potential confusion
[+] Building 3.3s (20/20) FINISHED
 => [internal] load local bake definitions                                                                                      0.0s
 => => reading from stdin 1.09kB                                                                                                0.0s
 => [database internal] load build definition from Dockerfile                                                                   0.0s
 => => transferring dockerfile: 73B                                                                                             0.0s
 => [web internal] load build definition from Dockerfile                                                                        0.1s
 => => transferring dockerfile: 200B                                                                                            0.0s
 => [database internal] load metadata for docker.io/library/postgres:15-alpine                                                  1.8s
 => [web internal] load metadata for docker.io/library/python:3.11-slim                                                         1.7s
 => [auth] library/postgres:pull token for registry-1.docker.io                                                                 0.0s
 => [auth] library/python:pull token for registry-1.docker.io                                                                   0.0s
 => [web internal] load .dockerignore                                                                                           0.0s
 => => transferring context: 2B                                                                                                 0.0s
 => [web 1/5] FROM docker.io/library/python:3.11-slim@sha256:e88e9763f943ec1834f992a4b51e0f24500486803e8bc534e5767af9ea65f6ce   0.1s
 => => resolve docker.io/library/python:3.11-slim@sha256:e88e9763f943ec1834f992a4b51e0f24500486803e8bc534e5767af9ea65f6ce       0.1s
 => [web internal] load build context                                                                                           0.0s
 => => transferring context: 93B                                                                                                0.0s
 => [database internal] load .dockerignore                                                                                      0.0s
 => => transferring context: 2B                                                                                                 0.0s
 => CACHED [web 2/5] WORKDIR /app                                                                                               0.0s
 => CACHED [web 3/5] COPY requirements.txt .                                                                                    0.0s
 => CACHED [web 4/5] RUN pip install --no-cache-dir -r requirements.txt                                                         0.0s
 => CACHED [web 5/5] COPY . .                                                                                                   0.0s
 => [web] exporting to image                                                                                                    0.2s
 => => exporting layers                                                                                                         0.0s
 => => exporting manifest sha256:8356142adb83eb6c07cebaa1372b4a7937c01b5b55fa63a1609069000695c68f                               0.0s
 => => exporting config sha256:ff3343a56c80b8cd95e27f21a7553077df16c91b560601392543bd2b0c5208c6                                 0.0s
 => => exporting attestation manifest sha256:7b8fb0927e51aa805a3beffacd34daca44da6e2dd35fbc9972042ae13d184548                   0.0s
 => => exporting manifest list sha256:76b6c2a744f4b057de9fef3b81742e27b3cc0109102edd06e00e90404fc65932                          0.0s
 => => naming to docker.io/library/part2-web:latest                                                                             0.0s
 => => unpacking to docker.io/library/part2-web:latest                                                                          0.0s
 => CACHED [database 1/1] FROM docker.io/library/postgres:15-alpine@sha256:f7d23353e1b15400d22ebe31189f4d314b87a4c129cc400c8c2  0.1s
 => => resolve docker.io/library/postgres:15-alpine@sha256:f7d23353e1b15400d22ebe31189f4d314b87a4c129cc400c8c2d8d4ca127bf81     0.1s
 => [database] exporting to image                                                                                               0.3s
 => => exporting layers                                                                                                         0.0s
 => => exporting manifest sha256:96fe461e5675c96885fa3f5cab4ba6836a899bef23c668ae606057cc54e38f8d                               0.0s
 => => exporting config sha256:1a696a7989ab2182db336cea3157041e7fa34e4428a5071ee41458a97ab94d5a                                 0.0s
 => => exporting attestation manifest sha256:e98da0fa2126c3b4af8c51a6e8f79551bd35621a2162794ca5e01109399c7d14                   0.1s
 => => exporting manifest list sha256:4e88542e43d89e4132aafc166502f942b425e61afa0a62a0b7489405d6eea349                          0.0s
 => => naming to docker.io/library/part2-database:latest                                                                        0.0s
 => => unpacking to docker.io/library/part2-database:latest                                                                     0.0s
 => [web] resolving provenance for metadata file                                                                                0.0s
 => [database] resolving provenance for metadata file                                                                           0.0s
[+] up 5/5
 ✔ Image part2-web           Built                                                                                               3.7s
 ✔ Image part2-database      Built                                                                                               3.6s
 ✔ Network part2_app-network Created                                                                                             0.0s
 ✔ Container postgres_db     Healthy                                                                                             6.0s
 ✔ Container part2-web-1     Started                  


------------------------------------------------------------------------------------------------------------


Modify and Redeploy the Web Application
Modify web/app.py to introduce a new feature or message ( adding a new route or updating the greeting message)

------------------------------------------------------------------------------------------------------------

Implement a Scaling Strategy
Scale the web application service horizontally to run multiple instances concurrently:
docker-compose up -d --scale web=3

------------------------------------------------------------------------------------------------------------


Implement a Monitoring Strategy
Create a monitoring/prometheus.yml configuration file:

------------------------------------------------------------------------------------------------------------
