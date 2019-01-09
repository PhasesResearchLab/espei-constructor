# ESPEI Constructor

**Build and deploy native installers of Anaconda with ESPEI and pycalphad for Windows, macOS and Linux**

Build native graphical installation artifacts for Windows and macOS, and a shell installation script for Linux using [constructor](https://github.com/conda/constructor). Builds are automaticaly built on Travis-CI and Appveyor for each platform and uploaded to the cloud.

Artifacts are uploaded to this S3 bucket: https://espei-deploy.s3.amazonaws.com/index.html

## Updating the installer

When new versions of ESPEI and pycalphad are released on the `conda-forge` and/or `pycalphad` conda channels, or the frozen-in dependencies should be upgraded, new installers should be built in this repo.

To build a new installer:

1. Fork this project
2. Update the ESPEI and/or pycalphad version in `config.yaml`. If the versions of ESPEI or pycalphad do not change (only dependencies are updated), then increment the `build_number`.
3. Open a pull request. If the artifacts build correctly for all platforms, the pull request will be merged into the `master` branch, where the artifacts will be built again and uploaded to the S3 bucket.

