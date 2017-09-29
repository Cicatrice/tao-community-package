## How to test TAO Community packages

1. Download this repository locally, and set some variables
```bash
export TAO_VERSION=3.4.10
export PACKAGE_TARGET=rpm
#OR
export PACKAGE_TARGET=deb
```
2. Ensure you have `docker` and `docker-compose` installed, then
```bash
mkdir -p ./build ./releases
#Skip this if you prefer to run everything locally (you may need to install RPM and DEB tools)
docker build setup -t tao-community-build
```
3. Build the packages in `/releases` with `phing` using one of the following commands
```bash
#If you choose use Docker
docker run --rm -i -v $(pwd):/repo tao-community-build bash <<EOF
  chown -R root: /repo
  cd /repo
  phing -Drelease.version=${TAO_VERSION} build pack-${PACKAGE_TARGET} vendor-${PACKAGE_TARGET}
  chown -R $(id -u):$(id -g) /repo
EOF
#If you choose to not use Docker
phing -Drelease.version=${TAO_VERSION} build pack-${PACKAGE_TARGET} vendor-${PACKAGE_TARGET}
```
4. Copy the packages in the test environments, in order to have them available in test Docker containers
```bash
#Please check that you are not copying many versions of the same package
cd tests/${PACKAGE_TARGET} && cp ../../releases/*${PACKAGE_TARGET} .
```
5. Run docker-compose to kickstart the database and application containers
```bash
#The first start may take a while
docker-compose build && docker-compose up
```
6. Once done, you should be able to connect on your local machine to http://0.0.0.0:8740/tao-community

## Simple scenario

1. Log in TAO using `admin` username with `admin` password
2. On splash-screen, or in top menu, go in `Deliveries` section
3. Create a new `delivery`,
  * Select `QTI Example Test` (type three spaces characters in search field)
  * Click on `Publish`
  * On next page, enable `Guest Access`
  * Click on `Save`

4. Log out the application (click on the link on top right corner)
5. On the login page, click on `Guest Access`
6. Start the `Delivery of QTI Example Test`
7. If you can browse the items and see some MathJax formulae, it works!
