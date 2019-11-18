# _Mixpanel_ Open Microservice

> Allows interaction with MixPanel

[![Open Microservice Specification Version](https://img.shields.io/badge/Open%20Microservice-1.0-477bf3.svg)](https://openmicroservices.org)
[![Open Microservices Spectrum Chat](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/open-microservices)
[![Open Microservices Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md)
[![Open Microservices Commitzen](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

## Introduction

This project is an example implementation of the [Open Microservice Specification](https://openmicroservices.org), a standard
originally created at [Storyscript](https://storyscript.io) for building highly-portable "microservices" that expose the
events, actions, and APIs inside containerized software.

## Getting Started

The `oms` command-line interface allows you to interact with Open Microservices. If you're interested in creating an Open
Microservice the CLI also helps validate, test, and debug your `oms.yml` implementation!

See the [oms-cli](https://github.com/microservices/oms) project to learn more!

### Installation

```
npm install -g @microservices/oms
```

## Usage

### Open Microservices CLI Usage

Once you have the [oms-cli](https://github.com/microservices/oms) installed, you can run any of the following commands from
within this project's root directory:

#### Actions

##### track

> Record an event

##### Action Arguments

| Argument Name | Type     | Required | Default | Description                 |
| :------------ | :------- | :------- | :------ | :-------------------------- |
| event         | `string` | `true`   | None    | No description provided.    |
| properties    | `map`    | `false`  | None    | No description provided.    |
| distinct_id   | `string` | `true`   | None    | No description provided.    |
| PROJECT_TOKEN | `string` | `true`   | None    | Your Mixpanel project token |

```shell
oms run track \
    -a event='*****' \
    -a properties='*****' \
    -a distinct_id='*****' \
    -e PROJECT_TOKEN=$PROJECT_TOKEN
```

##### people_set

> Set properties of a people record

##### Action Arguments

| Argument Name | Type     | Required | Default | Description                 |
| :------------ | :------- | :------- | :------ | :-------------------------- |
| properties    | `map`    | `true`   | None    | No description provided.    |
| distinct_id   | `string` | `true`   | None    | No description provided.    |
| PROJECT_TOKEN | `string` | `true`   | None    | Your Mixpanel project token |

```shell
oms run people_set \
    -a properties='*****' \
    -a distinct_id='*****' \
    -e PROJECT_TOKEN=$PROJECT_TOKEN
```

## Contributing

All suggestions in how to improve the specification and this guide are very welcome. Feel free share your thoughts in the
Issue tracker, or even better, fork the repository to implement your own ideas and submit a pull request.

[![Edit mixpanel on CodeSandbox](https://codesandbox.io/static/img/play-codesandbox.svg)](https://codesandbox.io/s/github/oms-services/mixpanel)

This project is guided by [Contributor Covenant](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md).
Please read out full [Contribution Guidelines](https://github.com/oms-services/.github/blob/master/CONTRIBUTING.md).

## Additional Resources

- [Install the CLI](https://github.com/microservices/oms) - The OMS CLI helps developers create, test, validate, and build
  microservices.
- [Example OMS Services](https://github.com/oms-services) - Examples of OMS-compliant services written in a variety of
  languages.
- [Example Language Implementations](https://github.com/microservices) - Find tooling & language implementations in Node,
  Python, Scala, Java, Clojure.
- [Storyscript Hub](https://hub.storyscript.io) - A public registry of OMS services.
- [Community Chat](https://spectrum.chat/open-microservices) - Have ideas? Questions? Join us on Spectrum.
