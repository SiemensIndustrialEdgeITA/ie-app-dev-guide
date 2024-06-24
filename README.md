# INDUSTRIAL EDGE APP DEVELOPMENT GUIDES

- [INDUSTRIAL EDGE APP DEVELOPMENT GUIDES](#industrial-edge-app-development-guides)
  - [Introduction](#introduction)
  - [Covered topics](#covered-topics)
  - [Documentation](#documentation)
  - [Contribution](#contribution)
  - [Licence and Legal Information](#licence-and-legal-information)

## Introduction

The aim of this repository is to guide both experienced developers and new adopters of **Industrial Edge** and **Docker** in the development of industrial applications.

## Covered topics

- [Industrial Edge Development Environment Setup](./docs/development_environment_setup.md):
  - [Install Docker](./docs/development_environment_setup.md#install-docker): how to install Docker.
  - [Expose Docker socket on TCP port](./docs/development_environment_setup.md#expose-docker-socket-on-tcp-port): how to make Docker accessible for the IE App Publisher.
  - [Download the Industrial Edge App Publisher](./docs/development_environment_setup.md#download-the-industrial-edge-app-publisher): how to install the IE App Publisher.
  - [Set-up the Industrial Edge App Publisher](./docs/development_environment_setup.md#set-up-the-industrial-edge-app-publisher): how to configure the IE App Publisher.
- [Industrial Edge Apps Development Guide](./docs/how_to_develop_industrial_edge_apps.md):
  - [Dockerfile](./docs/how_to_develop_industrial_edge_apps.md#prepare-a-sample-application): how to use the `Dockerfile` and bring your application inside a Docker container.
  - [Docker Compose](./docs/how_to_develop_industrial_edge_apps.md#deployment-blueprint-docker-composeyaml): how to use the `docker-compose.yaml` file to manage your application structure and configurations.
  - [Industrial Edge Publisher](./docs/how_to_develop_industrial_edge_apps.md#packaging-the-application-for-industrial-edge): bring your application to Industrial Edge.
- [Industrial Edge Default Reverse Proxy](./docs/reverse_proxy.md): make your application accessible via the default `Nginx` reverse proxy.

## Documentation

You can find further documentation and help in the following links

* [Industrial Edge Platform Overview](https://docs.eu1.edge.siemens.cloud/develop_an_application/developer_guide/industrial_edge_platform/02_Introduction.html)
* [Industrial Edge Hub](https://docs.eu1.edge.siemens.cloud/get_started_and_operate/industrial_edge_hub/setup/ieh_index.html)
* [Industrial Edge Management](https://docs.eu1.edge.siemens.cloud/get_started_and_operate/industrial_edge_management/overview.html)
* [Industrial Edge Devices](https://docs.eu1.edge.siemens.cloud/get_started_and_operate/industrial_edge_device/setup_onboarding/sign_up/sign_up_with_configurated_email_server.html)
* [Industrial Edge Forum](https://www.siemens.com/industrial-edge-forum)
* [Industrial Edge landing page](https://new.siemens.com/global/en/products/automation/topic-areas/industrial-edge/simatic-edge.html)
* [Industrial Edge GitHub page](https://github.com/industrial-edge)
* [Industrial Edge Learning Path](https://siemens-learning-simaticedge.sabacloud.com)

## Contribution

Thank you for your interest in contributing. Anybody is free to report bugs, unclear documentation, and other problems regarding this repository in the Issues section.
Additionally everybody is free to propose any changes to this repository using Pull Requests.

## Licence and Legal Information

Please read the [Legal information](LICENSE.md).